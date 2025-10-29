-- =============================================================
-- 付加価値計算（valueadded_note.md の方針に基づく改訂版）
-- =============================================================
--
-- 【計算方針】
-- 付加価値 = 売価 - 原価
--
-- 【受注データ取得方針】
-- 1. 過去～当月: SHIPORDER から取得
-- 2. 翌月以降: M_TRANSACTOR.A_EDIF=1 なら SHIPORDER、それ以外は MPS から取得
--
-- 【原価の細分化】
-- 1. 有償支給費: M_ITEM.A_FPTYPE = 'Y'
-- 2. 自給素材費: M_ITEM.A_FPTYPE != 'Y' AND M_ITEM.IMTYP = '1' AND M_ITEM.PROCESS IN ('GEN','SOZ')
-- 3. 購入費: M_ITEM.A_FPTYPE != 'Y' AND M_ITEM.IMTYP = '1' AND M_ITEM.PROCESS NOT IN ('GEN','SOZ')
-- 4. 外注費: M_ITEM.A_FPTYPE != 'Y' AND M_ITEM.IMTYP = '2'
-- 5. 原材料費: PROCESS = 'GEN'の品目については、M_BOM2から材料費を取得
--              (COST_TREEのRECORD_ID-1の品目をHPROCESS,HITEMとし、GEN品目をLPROCESS,LITEMとして参照)
--
-- =============================================================

WITH
-- ① 基準月（当月1日）と翌月1日
this_month AS (SELECT :THIS_MONTH_START AS dt FROM dual),
next_month AS (SELECT ADD_MONTHS(:THIS_MONTH_START, 1) AS dt FROM dual),

-- ② orders : 受注取得
orders AS (
    /* 過去～当月（翌月1日未満）は常に SHIPORDER 起点 */
    SELECT
        so.RCORDERNO AS order_no,
        so.PROCESS   AS process,
        so.ITEM      AS item,
        so.VENDOR    AS vendor,
        so.CUSTOM    AS custom,
        so.DELIDATE  AS base_date,
        so.ORDERQTY  AS qty
    FROM   SHIPORDER so
    WHERE  so.DELIDATE BETWEEN :FROM_DATE AND :TO_DATE
      AND  so.DELIDATE < (SELECT dt FROM next_month)

    UNION ALL

    /* 翌月以降：A_EDIF=1 は SHIPORDER 起点 */
    SELECT
        so.RCORDERNO AS order_no,
        so.PROCESS,
        so.ITEM,
        so.VENDOR,
        so.CUSTOM,
        so.DELIDATE  AS base_date,
        so.ORDERQTY  AS qty
    FROM   SHIPORDER so
    JOIN   M_TRANSACTOR mt
           ON mt.TRANSACTOR = so.CUSTOM
    WHERE  so.DELIDATE BETWEEN :FROM_DATE AND :TO_DATE
      AND  so.DELIDATE >= (SELECT dt FROM next_month)
      AND  NVL(mt.A_EDIF, 0) = 1

    UNION ALL

    /* 翌月以降：A_EDIF≠1（またはNULL）は MPS 起点 */
    /* 注: MPSでは同じRCORDERNOが複数の日付に分割されることがあるため、
         RCORDERNO + PLANDATE の組み合わせを一意のorder_noとして使用 */
    SELECT
        mp.RCORDERNO || '_' || TO_CHAR(mp.PLANDATE, 'YYYYMMDD') AS order_no,
        mp.PROCESS,
        mp.ITEM,
        mp.VENDOR,
        mp.CUSTOM,
        mp.PLANDATE  AS base_date,
        mp.ORDERQTY  AS qty
    FROM   MPS mp
    JOIN   M_TRANSACTOR mt
           ON mt.TRANSACTOR = mp.CUSTOM
    WHERE  mp.PLANDATE BETWEEN :FROM_DATE AND :TO_DATE
      AND  mp.PLANDATE >= (SELECT dt FROM next_month)
      AND  NVL(mt.A_EDIF, 0) <> 1
),

-- ③ price_interval : applydate ～ next_applydate-1 で有効区間を生成
--    売価(S)はPRICE
--    買価(P)は:
--      - A_FPTYPE='Y' (有償支給): ACT_PRICE
--      - SOZ工程: ACT_PROC_CHARGE（GEN材料費を除いた加工費のみ）
--      - その他: ACT_PRICE（GAI=外注費、KOB=購入費）
price_interval AS (
    SELECT /*+ MATERIALIZE */
           mp.item,
           mp.process,
           mp.spflag,
           CASE
               WHEN mp.spflag = 'S' THEN mp.price
               WHEN mp.spflag = 'P' THEN
                   CASE
                       WHEN mi.A_FPTYPE = 'Y' THEN mp.act_price
                       WHEN mp.process = 'SOZ' THEN mp.act_proc_charge
                       ELSE mp.act_price
                   END
               ELSE mp.price
           END AS price,
           mp.applydate AS eff_from,
           NVL( LEAD(mp.applydate) OVER (PARTITION BY mp.item,mp.process,mp.spflag
                                       ORDER BY mp.applydate) - 1,
                DATE '9999-12-31') AS eff_to
    FROM   M_PRICE mp
    LEFT   JOIN M_ITEM mi
           ON mi.ITEM = mp.ITEM AND mi.PROCESS = mp.PROCESS
    WHERE  mp.applydate <= :TO_DATE
),

-- ④ orders_price : 売価をインターバル JOIN
orders_price AS (
    SELECT o.*, pi.price AS sales_price
    FROM   orders o
    LEFT   JOIN price_interval pi
           ON pi.item     = o.item
          AND pi.process  = o.process
          AND pi.spflag   = 'S'
          AND o.base_date BETWEEN pi.eff_from AND pi.eff_to
),

-- ⑤ child_cost_raw : 子部品×買単価（インターバル JOIN）
child_cost_raw AS (
    SELECT
        o.order_no,
        o.item         AS parent_item,
        o.base_date    AS base_date,
        ct.RECORD_ID   AS record_id,
        ct.ITEM        AS child_item,
        ct.PHUNIT      AS qty_per,
        mi.A_FPTYPE,
        mi.IMTYP,
        mi.PROCESS     AS child_process,
        pi.price       AS buy_price
    FROM   orders o
    JOIN   COST_TREE ct
           ON ct.PRDCT_ITEM    = o.item
          AND ct.PRDCT_PROCESS = o.process
    JOIN   M_ITEM mi
           ON mi.ITEM    = ct.ITEM
          AND mi.PROCESS = ct.PROCESS
          AND mi.A_ITMSTATUS <= 7
    LEFT   JOIN price_interval pi
           ON pi.item     = ct.ITEM
          AND pi.process  = ct.PROCESS
          AND pi.spflag   = 'P'
          AND o.base_date BETWEEN pi.eff_from AND pi.eff_to
),

-- ⑥ child_cost : 子部品キーで重複排除
child_cost AS (
    SELECT DISTINCT
           order_no,
           parent_item,
           base_date,
           record_id,
           child_item,
           qty_per,
           A_FPTYPE,
           IMTYP,
           child_process,
           buy_price
    FROM   child_cost_raw
),

-- ⑦ gen_material_cost : PROCESS='GEN'の場合の原材料費（M_BOM2から取得）
--    重要: GEN材料費を加算するのはSOZ品目の子GENのみ
--    - SOZ品目: ACT_PROC_CHARGEにはGEN材料費が含まれていないため、別途加算
--    - KOB品目: ACT_PRICEに既にGEN材料費が含まれているため、加算不要
--    計算式: (PRICE × ACT_PHUNIT) - (SCR_PRICE × ACT_SCR_PHUNIT)
--           = 正味材料費 - スクラップ回収額
gen_material_cost AS (
    SELECT
        cc.order_no,
        cc.parent_item,
        cc.child_item,
        (bom.PRICE * bom.ACT_PHUNIT) - (bom.SCR_PRICE * bom.ACT_SCR_PHUNIT) AS gen_mat_cost
    FROM   child_cost cc
    JOIN   COST_TREE ct_prev
           ON ct_prev.RECORD_ID = cc.record_id - 1
    JOIN   (
        SELECT
            HPROCESS,
            HITEM,
            LPROCESS,
            LITEM,
            PRICE,
            ACT_PHUNIT,
            SCR_PRICE,
            ACT_SCR_PHUNIT,
            APPLYDATE,
            ROW_NUMBER() OVER (PARTITION BY HPROCESS, HITEM, LPROCESS, LITEM
                               ORDER BY APPLYDATE DESC) AS rn
        FROM   M_BOM2
    ) bom
           ON bom.HPROCESS = ct_prev.PROCESS
          AND bom.HITEM    = ct_prev.ITEM
          AND bom.LPROCESS = cc.child_process
          AND bom.LITEM    = cc.child_item
          AND bom.APPLYDATE <= cc.base_date
          AND bom.rn = 1
    WHERE  cc.child_process = 'GEN'
      AND  ct_prev.PROCESS = 'SOZ'  -- SOZ品目の子GENのみ対象
),

-- ⑧ bom_cost : 外注費と仕入材料費の2区分＋合計（オーダー単位）
--    仕入材料費 = GEN材料費(M_BOM2) + SOZ加工費(ACT_PROC_CHARGE) + KOB購入費
bom_cost_base AS (
    SELECT
        cc.order_no,
        cc.parent_item AS item,
        -- 外注費: IMTYP='2' (GAI品目)
        NVL(SUM(CASE WHEN NVL(cc.A_FPTYPE, 'N') <> 'Y' AND cc.IMTYP = '2'
                     THEN cc.qty_per * cc.buy_price END), 0) AS cost_gaichuu,
        -- 仕入材料費(購入): IMTYP='1' (SOZ+KOB品目)、GEN除く
        -- SOZ品目はACT_PROC_CHARGEを使用（GEN材料費除く）
        NVL(SUM(CASE WHEN NVL(cc.A_FPTYPE, 'N') <> 'Y' AND cc.IMTYP = '1'
                      AND cc.child_process <> 'GEN'
                     THEN cc.qty_per * cc.buy_price END), 0) AS cost_shiire_kounyu,
        -- 有償支給費: A_FPTYPE='Y'
        NVL(SUM(CASE WHEN cc.A_FPTYPE = 'Y'
                     THEN cc.qty_per * cc.buy_price END), 0) AS cost_yushou
    FROM   child_cost cc
    GROUP BY cc.order_no, cc.parent_item
),
gen_material_cost_total AS (
    SELECT
        order_no,
        parent_item,
        SUM(gen_mat_cost) AS cost_gen
    FROM   gen_material_cost
    GROUP BY order_no, parent_item
),
bom_cost AS (
    SELECT
        bc.order_no,
        bc.item,
        -- 外注費
        bc.cost_gaichuu AS cost_gaichuu,
        -- 仕入材料費 = GEN材料費 + SOZ+KOB購入費（有償支給費を除く）
        NVL(gmc.cost_gen, 0) + bc.cost_shiire_kounyu AS cost_shiire,
        -- 有償支給費（独立して表示）
        bc.cost_yushou AS cost_yushou,
        -- 原価合計 = 外注費 + 仕入材料費 + 有償支給費
        bc.cost_gaichuu + NVL(gmc.cost_gen, 0) + bc.cost_shiire_kounyu + bc.cost_yushou AS bom_cost_total
    FROM   bom_cost_base bc
    LEFT   JOIN gen_material_cost_total gmc
           ON gmc.order_no    = bc.order_no
          AND gmc.parent_item = bc.item
)

-- ⑨ 最終集計（日本語列名）
--    外部コストは「外注費」「仕入材料費」「有償支給費」の3区分
SELECT /*+ MONITOR */
    op.order_no      AS オーダーNo,
    op.item          AS 品目,
    op.process       AS 工程,
    op.base_date     AS 納期,
    op.qty           AS 数量,
    op.sales_price   AS 売価,
    bc.cost_gaichuu  AS 外注費,
    bc.cost_shiire   AS 仕入材料費,
    bc.cost_yushou   AS 有償支給費,
    bc.bom_cost_total AS 原価合計,
    (op.sales_price - NVL(bc.bom_cost_total,0)) * op.qty AS 付加価値,
    vend.TRANSACTORNM AS 取引先,
    cust.TRANSACTORNM AS 顧客
FROM   orders_price op
LEFT   JOIN bom_cost bc
       ON bc.order_no = op.order_no
      AND bc.item     = op.item
LEFT   JOIN M_TRANSACTOR vend
       ON vend.TRANSACTOR = op.vendor
LEFT   JOIN M_TRANSACTOR cust
       ON cust.TRANSACTOR = op.custom
ORDER BY 品目, 納期;
