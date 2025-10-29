from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import pandas as pd

class DatabaseManager:
    def __init__(self):
        # 環境変数の読み込み
        load_dotenv()
        user = os.getenv('ORACLE_USER')
        password = os.getenv('ORACLE_PASSWORD')
        host = os.getenv('ORACLE_HOST')
        port = os.getenv('ORACLE_PORT')
        service_name = os.getenv('ORACLE_SERVICE')

        # データベース接続設定
        self.DATABASE_URL = f"oracle+oracledb://{user}:{password}@{host}:{port}/?service_name={service_name}"
        self.engine = create_engine(self.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)

    def execute_query(self, query):
        """クエリを実行してデータフレームを返す"""
        with self.engine.connect() as conn:
            return pd.read_sql(text(query), conn)

class ValueAddedDataManager(DatabaseManager):
    def fetch_value_added_summary(self, start_date, end_date):
        """月次集計（顧客別）のデータを取得"""
        query = f"""
        SELECT
            TO_CHAR(s.DELIDATE, 'YYYY-MM') AS 取引月,
            s.CUSTOM AS 顧客CD,
            SUM(COALESCE(ct.ACT_PS1, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 素材,
            SUM(COALESCE(ct.ACT_PS6, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 支給,
            SUM(COALESCE(ct.ACT_PS2, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 購買,
            SUM(COALESCE(ct.ACT_PS3, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 外注,
            SUM(p.PRICE * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 受注合計,
            SUM(
                (p.PRICE
                - COALESCE(ct.ACT_PS1, 0)
                - COALESCE(ct.ACT_PS2, 0)
                - COALESCE(ct.ACT_PS3, 0)
                - COALESCE(ct.ACT_PS6, 0)
                ) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END
            ) AS 付加価値高
        FROM
            SHIPORDER s
        CROSS APPLY (
            SELECT *
            FROM M_PRICE mp
            WHERE
                mp.PROCESS = s.PROCESS
                AND mp.ITEM = s.ITEM
                AND mp.APPLYDATE <= s.DELIDATE
                AND mp.SPFLAG = 'S'
            ORDER BY mp.APPLYDATE DESC
            FETCH FIRST 1 ROW ONLY
        ) p
        LEFT JOIN COST_TREE ct
            ON s.PROCESS = ct.PRDCT_PROCESS
            AND s.ITEM = ct.PRDCT_ITEM
            AND ct.LEVELD = 'o1'
        WHERE
            s.DELIDATE BETWEEN TO_DATE('{start_date}', 'YYYY-MM-DD') AND TO_DATE('{end_date}', 'YYYY-MM-DD')
        GROUP BY
            TO_CHAR(s.DELIDATE, 'YYYY-MM'),
            s.CUSTOM
        ORDER BY
            顧客CD,
            取引月
        """
        return self.execute_query(query)

    def fetch_value_added_summary_total(self, start_date, end_date):
        """月次集計（全体）のデータを取得"""
        query = f"""
        SELECT
            TO_CHAR(s.DELIDATE, 'YYYY-MM') AS 取引月,
            SUM(COALESCE(ct.ACT_PS1, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 素材,
            SUM(COALESCE(ct.ACT_PS6, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 支給,
            SUM(COALESCE(ct.ACT_PS2, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 購買,
            SUM(COALESCE(ct.ACT_PS3, 0) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 外注,
            SUM(p.PRICE * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END) AS 受注合計,
            SUM(
                (p.PRICE
                - COALESCE(ct.ACT_PS1, 0)
                - COALESCE(ct.ACT_PS2, 0)
                - COALESCE(ct.ACT_PS3, 0)
                - COALESCE(ct.ACT_PS6, 0)
                ) * CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END
            ) AS 付加価値高
        FROM
            SHIPORDER s
        CROSS APPLY (
            SELECT *
            FROM M_PRICE mp
            WHERE
                mp.PROCESS = s.PROCESS
                AND mp.ITEM = s.ITEM
                AND mp.APPLYDATE <= s.DELIDATE
                AND mp.SPFLAG = 'S'
            ORDER BY mp.APPLYDATE DESC
            FETCH FIRST 1 ROW ONLY
        ) p
        LEFT JOIN COST_TREE ct
            ON s.PROCESS = ct.PRDCT_PROCESS
            AND s.ITEM = ct.PRDCT_ITEM
            AND ct.LEVELD = 'o1'
        WHERE
            s.DELIDATE BETWEEN TO_DATE('{start_date}', 'YYYY-MM-DD') AND TO_DATE('{end_date}', 'YYYY-MM-DD')
        GROUP BY
            TO_CHAR(s.DELIDATE, 'YYYY-MM')
        ORDER BY
            取引月
        """
        return self.execute_query(query)

    def fetch_value_added_orders(self, start_date, end_date):
        """オーダー単位のデータを取得"""
        # SQLファイルのパスを決定
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sql_file_path = os.path.join(os.path.dirname(current_dir), 'sql', 'value_added.sql')

        try:
            # SQLファイルを読み込み
            with open(sql_file_path, 'r', encoding='utf-8') as file:
                query = file.read()

            # 余分な空白やセミコロンを削除
            query = query.strip()
            if query.endswith(';'):
                query = query[:-1]

            # 当月1日を計算
            today = pd.to_datetime("today")
            this_month_start = today.replace(day=1).strftime('%Y-%m-%d')

            # パラメータ置換
            query = query.replace(':FROM_DATE', f"TO_DATE('{start_date}', 'YYYY-MM-DD')")
            query = query.replace(':TO_DATE', f"TO_DATE('{end_date}', 'YYYY-MM-DD')")
            query = query.replace(':THIS_MONTH_START', f"TO_DATE('{this_month_start}', 'YYYY-MM-DD')")

            # クエリを実行
            return self.execute_query(query)

        except FileNotFoundError:
            raise FileNotFoundError(f"SQLファイルが見つかりません: {sql_file_path}")
        except Exception as e:
            # エラー時にSQLの一部を表示して診断しやすくする
            query_preview = query[:200] + '...' if 'query' in locals() and len(query) > 200 else query
            raise Exception(f"クエリ実行中にエラーが発生しました: {str(e)}\nクエリプレビュー: {query_preview}")

    def fetch_value_added_orders_v2(self, start_date, end_date):
        """オーダー単位のデータを取得（v2: valueadded_note.mdの方針に基づく改訂版）"""
        # SQLファイルのパスを決定
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sql_file_path = os.path.join(os.path.dirname(current_dir), 'sql', 'value_added.sql')

        try:
            # SQLファイルを読み込み
            with open(sql_file_path, 'r', encoding='utf-8') as file:
                query = file.read()

            # 余分な空白やセミコロンを削除
            query = query.strip()
            if query.endswith(';'):
                query = query[:-1]

            # 当月1日を計算
            today = pd.to_datetime("today")
            this_month_start = today.replace(day=1).strftime('%Y-%m-%d')

            # パラメータ置換
            query = query.replace(':FROM_DATE', f"TO_DATE('{start_date}', 'YYYY-MM-DD')")
            query = query.replace(':TO_DATE', f"TO_DATE('{end_date}', 'YYYY-MM-DD')")
            query = query.replace(':THIS_MONTH_START', f"TO_DATE('{this_month_start}', 'YYYY-MM-DD')")

            # クエリを実行
            return self.execute_query(query)

        except FileNotFoundError:
            raise FileNotFoundError(f"SQLファイルが見つかりません: {sql_file_path}")
        except Exception as e:
            # エラー時にSQLの一部を表示して診断しやすくする
            query_preview = query[:200] + '...' if 'query' in locals() and len(query) > 200 else query
            raise Exception(f"クエリ実行中にエラーが発生しました: {str(e)}\nクエリプレビュー: {query_preview}")

    def fetch_latest_sales_price(self):
        query = """
        SELECT *
        FROM (
            SELECT mp.*,
                   ROW_NUMBER() OVER (PARTITION BY mp.ITEM, mp.PROCESS ORDER BY mp.APPLYDATE DESC) as rn
            FROM M_PRICE mp
            WHERE
                mp.APPLYDATE <= SYSDATE
                AND mp.SPFLAG = 'S'
                AND mp.PROCESS IN ('KEN','KUM','KOB')
                --AND mp.TRANSACTOR = 'YMC'
        )
        WHERE rn = 1
        ORDER BY ITEM, PROCESS
        """
        return self.execute_query(query)

    def fetch_latest_purchase_price(self):
        query = """
        SELECT *
        FROM (
            SELECT mp.*,
                   ROW_NUMBER() OVER (PARTITION BY mp.ITEM, mp.PROCESS ORDER BY mp.APPLYDATE DESC) as rn
            FROM M_PRICE mp
            WHERE
                mp.APPLYDATE <= SYSDATE
                AND mp.SPFLAG = 'P'
        )
        WHERE rn = 1
        ORDER BY ITEM, PROCESS
        """
        return self.execute_query(query)

    def fetch_latest_cost(self):
        query = """
        SELECT *
        FROM (
            SELECT mc.*,
                ROW_NUMBER() OVER (PARTITION BY mc.ITEM, mc.PROCESS, mc.VENDOR ORDER BY mc.APPLYDATE DESC) as rn
            FROM M_COST mc
            WHERE
                mc.APPLYDATE <= SYSDATE
            )
            WHERE rn = 1
        ORDER BY ITEM, PROCESS, VENDOR
        """
        return self.execute_query(query)

    def fetch_cost_tree(self):
        query = """
        SELECT *
        FROM COST_TREE
        ORDER BY RECORD_ID
        """
        return self.execute_query(query)

    def fetch_value_added_debug(self, start_date, end_date):
        """
        value_added.sql の各CTE（中間段階）を個別のDataFrameとして返す。
        戻り値: dict[str, pd.DataFrame]
        keys: orders, price_interval, orders_price, child_cost_raw, child_cost, bom_cost, final
        """
        # 文字列整形（YYYY-MM-DD 前提）
        start_str = pd.to_datetime(start_date).strftime('%Y-%m-%d')
        end_str   = pd.to_datetime(end_date).strftime('%Y-%m-%d')
        this_month_start = pd.to_datetime("today").replace(day=1).strftime('%Y-%m-%d')

        ymc_list_sql = "('7536','YEJP','YHSJ','YMC','YMEC','YMPC')"

        from_date_sql = f"TO_DATE('{start_str}', 'YYYY-MM-DD')"
        to_date_sql   = f"TO_DATE('{end_str}', 'YYYY-MM-DD')"
        tms_sql       = f"TO_DATE('{this_month_start}', 'YYYY-MM-DD')"

        # --- orders（SRC列を追加して“どこから来たか”を可視化） ---
        orders_sql = f"""
        SELECT 'SHIPORDER_BEFORE' AS SRC,
               so.RCORDERNO AS ORDER_NO,
               so.PROCESS,
               so.ITEM,
               so.VENDOR,
               so.DELIDATE AS BASE_DATE,
               so.ORDERQTY AS QTY
        FROM   SHIPORDER so
        WHERE  so.DELIDATE BETWEEN {from_date_sql} AND {to_date_sql}
          AND  so.DELIDATE < {tms_sql}

        UNION ALL

        SELECT 'SHIPORDER_YMC' AS SRC,
               so.RCORDERNO,
               so.PROCESS,
               so.ITEM,
               so.VENDOR,
               so.DELIDATE,
               so.ORDERQTY
        FROM   SHIPORDER so
        WHERE  so.DELIDATE BETWEEN {from_date_sql} AND {to_date_sql}
          AND  so.DELIDATE >= {tms_sql}
          AND  so.VENDOR IN {ymc_list_sql}

        UNION ALL

        SELECT 'MPS_NON_YMC' AS SRC,
               mp.RCORDERNO,
               mp.PROCESS,
               mp.ITEM,
               mp.VENDOR,
               mp.PLANDATE  AS BASE_DATE,
               mp.ORDERQTY  AS QTY
        FROM   MPS mp
        WHERE  mp.PLANDATE BETWEEN {from_date_sql} AND {to_date_sql}
          AND  mp.PLANDATE >= {tms_sql}
          AND  mp.VENDOR NOT IN {ymc_list_sql}
        """

        # --- price_interval ---
        price_interval_sql = f"""
        SELECT item,
               process,
               spflag,
               price,
               applydate AS eff_from,
               NVL( LEAD(applydate) OVER (PARTITION BY item,process,spflag ORDER BY applydate) - 1,
                    DATE '9999-12-31') AS eff_to
        FROM   M_PRICE
        WHERE  applydate <= {to_date_sql}
        """

        # --- orders_price ---
        orders_price_sql = f"""
        SELECT o.*,
               pi.price AS SALES_PRICE
        FROM   ({orders_sql}) o
        LEFT   JOIN ({price_interval_sql}) pi
               ON pi.item    = o.item
              AND pi.process = o.process
              AND pi.spflag  = 'S'
              AND o.base_date BETWEEN pi.eff_from AND pi.eff_to
        """

        # --- child_cost_raw ---
        child_cost_raw_sql = f"""
        SELECT
            o.order_no,
            o.item       AS parent_item,
            ct.ITEM      AS child_item,
            ct.PHUNIT    AS qty_per,
            mi.A_FPTYPE,
            mi.IMTYP,
            mi.PROCESS,
            pi.price     AS buy_price
        FROM   ({orders_sql}) o
        JOIN   COST_TREE ct
               ON ct.PRDCT_ITEM = o.item
        JOIN   M_ITEM mi
               ON mi.ITEM    = ct.ITEM
              AND mi.PROCESS = ct.PROCESS
              AND mi.A_ITMSTATUS <= 7
        LEFT   JOIN ({price_interval_sql}) pi
               ON pi.item    = ct.ITEM
              AND pi.process = ct.PROCESS
              AND pi.spflag  = 'P'
              AND o.base_date BETWEEN pi.eff_from AND pi.eff_to
        """

        # --- child_cost（重複排除） ---
        child_cost_sql = f"""
        SELECT DISTINCT
               order_no,
               parent_item,
               child_item,
               qty_per,
               A_FPTYPE,
               IMTYP,
               PROCESS,
               buy_price
        FROM   ({child_cost_raw_sql})
        """

        # --- bom_cost（4区分＋合計） ---
        bom_cost_sql = f"""
        SELECT order_no,
               parent_item AS item,
               SUM(CASE WHEN A_FPTYPE = 'Y'
                        THEN qty_per * buy_price END) AS cost_yushou,
               SUM(CASE WHEN A_FPTYPE <> 'Y' AND IMTYP = '1' AND PROCESS IN ('GEN','SOZ')
                        THEN qty_per * buy_price END) AS cost_jikyu,
               SUM(CASE WHEN A_FPTYPE <> 'Y' AND IMTYP = '1' AND PROCESS NOT IN ('GEN','SOZ')
                        THEN qty_per * buy_price END) AS cost_kounyu,
               SUM(CASE WHEN A_FPTYPE <> 'Y' AND IMTYP = '2'
                        THEN qty_per * buy_price END) AS cost_gaichuu,
               SUM(qty_per * buy_price)              AS bom_cost_total
        FROM   ({child_cost_sql})
        GROUP BY order_no, parent_item
        """

        # --- final（最終集計） ---
        final_sql = f"""
        SELECT
            op.order_no   AS オーダーNo,
            op.item       AS 品目,
            op.base_date  AS 納期,
            op.qty        AS 数量,
            op.sales_price AS 売価,
            bc.cost_yushou AS 有支材単価,
            bc.cost_jikyu  AS 自給材単価,
            bc.cost_kounyu AS 購入単価,
            bc.cost_gaichuu AS 外注単価,
            bc.bom_cost_total AS 単価計,
            (op.sales_price - NVL(bc.bom_cost_total,0)) * op.qty AS 付加価値
        FROM   ({orders_price_sql}) op
        LEFT   JOIN ({bom_cost_sql}) bc
               ON bc.order_no = op.order_no
              AND bc.item     = op.item
        ORDER BY 品目, 納期
        """

        # 実行＆返却
        return {
            "orders":           self.execute_query(orders_sql),
            "price_interval":   self.execute_query(price_interval_sql),
            "orders_price":     self.execute_query(orders_price_sql),
            "child_cost_raw":   self.execute_query(child_cost_raw_sql),
            "child_cost":       self.execute_query(child_cost_sql),
            "bom_cost":         self.execute_query(bom_cost_sql),
            "final":            self.execute_query(final_sql),
        }