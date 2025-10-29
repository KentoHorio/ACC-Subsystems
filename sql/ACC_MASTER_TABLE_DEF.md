# データベース テーブル定義書（整理版・全件保持）

以下は主要な項目（テーブル名, 列ID, 列名, 備考）をテーブルごとに分割したものです。備考が空欄の場合は出力しません。

## テーブル: A_BOM

| テーブル名   | 列ID      | 列名        | 備考                        |
|:-------------|:----------|:------------|:----------------------------|
| A_BOM        | A_FSEQNO  | 出力順序    | （なし）                    |
| A_BOM        | CHK       | チェック    | （なし）                    |
| A_BOM        | HIMQTY    | 親基準数    | （なし）                    |
| A_BOM        | HITEM     | 親品目      | （なし）                    |
| A_BOM        | HPROCESS  | 親工程      | （なし）                    |
| A_BOM        | HVENDOR   | 親仕入先    | （なし）                    |
| A_BOM        | ISSUEQTY  | 出庫数      | （なし）                    |
| A_BOM        | LIMQTY    | 子基準数    | （なし）                    |
| A_BOM        | LITEM     | 子品目      | （なし）                    |
| A_BOM        | LOCT      | 入出庫場所  | （なし）                    |
| A_BOM        | LPROCESS  | 子工程      | （なし）                    |
| A_BOM        | LVENDOR   | 子仕入先    | （なし）                    |
| A_BOM        | ODEDDATE  | 失効日      | （なし）                    |
| A_BOM        | ODSTDATE  | 発効日      | （なし）                    |
| A_BOM        | PHUNIT    | 員数        | （なし）                    |
| A_BOM        | RGSTD     | 登録日      | （なし）                    |
| A_BOM        | SHARERTIO | 共用比率(%) | （なし）                    |
| A_BOM        | SHARETYP  | 共用区分    | （なし）                    |
| A_BOM        | STDPHUNIT | 基準員数    | （なし）                    |
| A_BOM        | SWEDDATE  | 切替失効日  | （なし）                    |
| A_BOM        | SWSTDATE  | 切替発効日  | （なし）                    |
| A_BOM        | UNITTYP   | 員数区分    | 0;基準員数優先;1;基準数優先 |
| A_BOM        | UPDTD     | 更新日      | （なし）                    |
| A_BOM        | UPDTWKCD  | 更新担当者  | （なし）                    |
| A_BOM        | YIELD     | 歩留(%)     | （なし）                    |

## テーブル: BOM_CHK_LST

| テーブル名   | 列ID      | 列名       | 備考                                                                 |
|:-------------|:----------|:-----------|:---------------------------------------------------------------------|
| BOM_CHK_LST  | INFLOOP   | 無限ループ | 製品構成マスタの登録に誤りがあります。                               |
| BOM_CHK_LST  | ITEM      | 品目       | （なし）                                                             |
| BOM_CHK_LST  | PRDCTCTRL | 製番管理Ｆ | 工程条件マスタ、または品目マスタの製番管理Ｆの設定に誤りがあります。 |
| BOM_CHK_LST  | PROCESS   | 工程       | （なし）                                                             |
| BOM_CHK_LST  | VENDOR    | 仕入先     | （なし）                                                             |

## テーブル: BOM_CH_ACT_TMP

| テーブル名     | 列ID        | 列名       | 備考     |
|:---------------|:------------|:-----------|:---------|
| BOM_CH_ACT_TMP | ACTSTOCK    | 現在在庫数 | （なし） |
| BOM_CH_ACT_TMP | ID          | ID         | （なし） |
| BOM_CH_ACT_TMP | ITEM        | 品目       | （なし） |
| BOM_CH_ACT_TMP | LOCT        | 場所       | （なし） |
| BOM_CH_ACT_TMP | PROCESS     | 工程       | （なし） |
| BOM_CH_ACT_TMP | PRODUCTITEM | 最終品目   | （なし） |
| BOM_CH_ACT_TMP | VENDOR      | 仕入先     | （なし） |

## テーブル: BOM_LST

| テーブル名   | 列ID        | 列名           | 備考                   |
|:-------------|:------------|:---------------|:-----------------------|
| BOM_LST      | A_FMCUS     | 代表得意先     | （なし）               |
| BOM_LST      | A_VENDOR    | 発注先         | 購入品、外注品の発注先 |
| BOM_LST      | ACTSTOCK    | 実際在庫数     | （なし）               |
| BOM_LST      | ID          | ID             | （なし）               |
| BOM_LST      | ITEM        | 品目           | （なし）               |
| BOM_LST      | LEVELD      | レベル         | （なし）               |
| BOM_LST      | LINED       | ライン         | （なし）               |
| BOM_LST      | ODEDDATE    | 失効日         | （なし）               |
| BOM_LST      | ODSTDATE    | 発効日         | （なし）               |
| BOM_LST      | OPERABLEF   | 使用F          | （なし）               |
| BOM_LST      | PHUNIT      | 員数           | （なし）               |
| BOM_LST      | PRDCTQTY    | 指示残数       | （なし）               |
| BOM_LST      | PROCESS     | 工程           | （なし）               |
| BOM_LST      | PRODUCTITEM | 最終品目       | （なし）               |
| BOM_LST      | RGSTD       | 登録日         | （なし）               |
| BOM_LST      | SHARERTIO   | 共用比率（％） | （なし）               |
| BOM_LST      | SHARETYP    | 共用区分       | （なし）               |
| BOM_LST      | SWEDDATE    | 切替失効日     | （なし）               |
| BOM_LST      | SWSTDATE    | 切替発行日     | （なし）               |
| BOM_LST      | VENDOR      | 仕入先         | （なし）               |

## テーブル: BOM_LST2

| テーブル名   | 列ID        | 列名           | 備考     |
|:-------------|:------------|:---------------|:---------|
| BOM_LST2     | ACTSTOCK    | 実際在庫数     | （なし） |
| BOM_LST2     | ID          | ID             | （なし） |
| BOM_LST2     | ITEM        | 品目           | （なし） |
| BOM_LST2     | LEVELD      | レベル         | （なし） |
| BOM_LST2     | ODEDDATE    | 失効日         | （なし） |
| BOM_LST2     | ODSTDATE    | 発効日         | （なし） |
| BOM_LST2     | OPERABLEF   | 使用F          | （なし） |
| BOM_LST2     | PHUNIT      | 員数           | （なし） |
| BOM_LST2     | PRDCTQTY    | 指示残数       | （なし） |
| BOM_LST2     | PROCESS     | 工程           | （なし） |
| BOM_LST2     | PRODUCTITEM | 最終品目       | （なし） |
| BOM_LST2     | RGSTD       | 登録日         | （なし） |
| BOM_LST2     | SHARERTIO   | 共用比率（％） | （なし） |
| BOM_LST2     | SHARETYP    | 共用区分       | （なし） |
| BOM_LST2     | SWEDDATE    | 切替失効日     | （なし） |
| BOM_LST2     | SWSTDATE    | 切替発行日     | （なし） |
| BOM_LST2     | VENDOR      | 仕入先         | （なし） |

## テーブル: BOM_TMP

| テーブル名   | 列ID     | 列名     | 備考     |
|:-------------|:---------|:---------|:---------|
| BOM_TMP      | BOM2_F   | BOM2FLG  | （なし） |
| BOM_TMP      | HITEM    | 親品目   | （なし） |
| BOM_TMP      | HPROCESS | 親工程   | （なし） |
| BOM_TMP      | HVENDOR  | 親仕入先 | （なし） |
| BOM_TMP      | LITEM    | 子品目   | （なし） |
| BOM_TMP      | LPROCESS | 子工程   | （なし） |
| BOM_TMP      | LVENDOR  | 子仕入先 | （なし） |
| BOM_TMP      | PHUNIT   | 員数     | （なし） |

## テーブル: CHK_M_BANK

| テーブル名   | 列ID    | 列名               | 備考     |
|:-------------|:--------|:-------------------|:---------|
| CHK_M_BANK   | BANKCD  | 銀行コード         | （なし） |
| CHK_M_BANK   | CMMSTYP | 手数料種別0〜3以外 | （なし） |

## テーブル: CHK_M_BOM

| テーブル名   | 列ID      | 列名                           | 備考     |
|:-------------|:----------|:-------------------------------|:---------|
| CHK_M_BOM    | CHITEM    | 親品目無                       | YES/NO   |
| CHK_M_BOM    | CLITEM    | 子品目無                       | YES/NO   |
| CHK_M_BOM    | HIMQTY    | 親基準数                       | YES/NO   |
| CHK_M_BOM    | HITEM     | 親品目                         | （なし） |
| CHK_M_BOM    | HPROCESS  | 親工程                         | （なし） |
| CHK_M_BOM    | HVENDOR   | 親仕入先                       | （なし） |
| CHK_M_BOM    | IMTYP     | 親品目が購入品                 | YES/NO   |
| CHK_M_BOM    | IMTYP2    | 親品目が外注品で子品目が製造品 | YES/NO   |
| CHK_M_BOM    | LITEM     | 子品目                         | （なし） |
| CHK_M_BOM    | LPROCESS  | 子工程                         | （なし） |
| CHK_M_BOM    | LVENDOR   | 子仕入先                       | （なし） |
| CHK_M_BOM    | ODSTDATE  | 発効日>=失効日                 | YES/NO   |
| CHK_M_BOM    | PHUNIT    | 員数＝０                       | YES/NO   |
| CHK_M_BOM    | SHARERTIO | 警告：共用比率が１００％でない | YES/NO   |
| CHK_M_BOM    | SWSTDATE  | 切替発効日>=切替失効日         | YES/NO   |
| CHK_M_BOM    | UNIT      | 子品目単位エラー               | YES/NO   |
| CHK_M_BOM    | UNITTYP   | 員数区分　０，１以外           | YES/NO   |

## テーブル: CHK_M_BOM2

| テーブル名   | 列ID       | 列名             | 備考     |
|:-------------|:-----------|:-----------------|:---------|
| CHK_M_BOM2   | APPLYDATE  | 適用日           | （なし） |
| CHK_M_BOM2   | CAPPLYDATE | 適用日           | （なし） |
| CHK_M_BOM2   | CHITEM     | 親品目無         | YES/NO   |
| CHK_M_BOM2   | CHITEM2    | 親品目購入区分≠R | YES/NO   |
| CHK_M_BOM2   | CLITEM     | 子品目無         | YES/NO   |
| CHK_M_BOM2   | CLITEM2    | 子品目購入区分≠G | YES/NO   |
| CHK_M_BOM2   | HITEM      | 親品目           | （なし） |
| CHK_M_BOM2   | HPROCESS   | 親工程           | （なし） |
| CHK_M_BOM2   | HVENDOR    | 親仕入先         | （なし） |
| CHK_M_BOM2   | LITEM      | 子品目           | （なし） |
| CHK_M_BOM2   | LPROCESS   | 子工程           | （なし） |
| CHK_M_BOM2   | LVENDOR    | 子仕入先         | （なし） |
| CHK_M_BOM2   | ODSTDATE   | 発効日>=失効日   | YES/NO   |
| CHK_M_BOM2   | PHUNIT     | 投入重量         | （なし） |
| CHK_M_BOM2   | PRICE      | 投入単価         | （なし） |

## テーブル: CHK_M_BOM2_LST

| テーブル名     | 列ID    | 列名       | 備考     |
|:---------------|:--------|:-----------|:---------|
| CHK_M_BOM2_LST | INFLOOP | 無限ループ | YES/NO   |
| CHK_M_BOM2_LST | ITEM    | 品目       | （なし） |
| CHK_M_BOM2_LST | PROCESS | 工程       | （なし） |
| CHK_M_BOM2_LST | VENDOR  | 仕入先     | （なし） |

## テーブル: CHK_M_BOM_LST

| テーブル名    | 列ID      | 列名       | 備考     |
|:--------------|:----------|:-----------|:---------|
| CHK_M_BOM_LST | INFLOOP   | 無限ループ | YES/NO   |
| CHK_M_BOM_LST | ITEM      | 品目       | （なし） |
| CHK_M_BOM_LST | PRDCTCTRL | 製番管理Ｆ | YES/NO   |
| CHK_M_BOM_LST | PROCESS   | 工程       | （なし） |
| CHK_M_BOM_LST | VENDOR    | 仕入先     | （なし） |

## テーブル: CHK_M_BUCKET

| テーブル名   | 列ID     | 列名                                             | 備考     |
|:-------------|:---------|:-------------------------------------------------|:---------|
| CHK_M_BUCKET | BKTEDD   | ﾊﾞｹｯﾄ終了日                                      | （なし） |
| CHK_M_BUCKET | BKTNO    | ﾊﾞｹｯﾄＮｏ                                        | （なし） |
| CHK_M_BUCKET | BKTSTD   | ﾊﾞｹｯﾄ開始日                                      | （なし） |
| CHK_M_BUCKET | BKTTIME  | バケット開始日〜スケジュール最終日＞一年間       | YES/NO   |
| CHK_M_BUCKET | BKTYEAR  | ﾊﾞｹｯﾄ年                                          | （なし） |
| CHK_M_BUCKET | CBKTSTD  | ﾊﾞｹｯﾄ開始日>ﾊﾞｹｯﾄ最終日                          | YES/NO   |
| CHK_M_BUCKET | CBKTSTD2 | バケット期間連続性エラー                         | YES/NO   |
| CHK_M_BUCKET | MRPTIME  | バケット開始日〜所要量計算最終日＞一年間         | YES/NO   |
| CHK_M_BUCKET | ODRDEDD  | ｽｹｼﾞｭｰﾙ最終日＞受注取込最終日                    | YES/NO   |
| CHK_M_BUCKET | ODRDTIME | バケット開始日〜受注取込最終日＞一年間           | YES/NO   |
| CHK_M_BUCKET | ODTIME   | バケット開始日〜所要量計算受注取込最終日＞一年間 | YES/NO   |
| CHK_M_BUCKET | PODTIME  | バケット開始日〜購入品確定最終日＞一年間         | YES/NO   |
| CHK_M_BUCKET | SCHEDD   | ﾊﾞｹｯﾄ最終日＞ｽｹｼﾞｭｰﾙ最終日                       | YES/NO   |

## テーブル: CHK_M_CNCTEQP

| テーブル名    | 列ID      | 列名         | 備考     |
|:--------------|:----------|:-------------|:---------|
| CHK_M_CNCTEQP | CFRITEM   | 出力品目無   | YES/NO   |
| CHK_M_CNCTEQP | CFRLINED  | 出力ライン無 | YES/NO   |
| CHK_M_CNCTEQP | CTOITEM   | 入力品目無   | YES/NO   |
| CHK_M_CNCTEQP | CTOLINED  | 入力ライン無 | YES/NO   |
| CHK_M_CNCTEQP | FRITEM    | 出力品目     | （なし） |
| CHK_M_CNCTEQP | FRLINED   | 出力ライン   | （なし） |
| CHK_M_CNCTEQP | FRPROCESS | 出力工程     | （なし） |
| CHK_M_CNCTEQP | FRVENDOR  | nil          | （なし） |
| CHK_M_CNCTEQP | TOITEM    | 入力品目     | （なし） |
| CHK_M_CNCTEQP | TOLINED   | 入力ライン   | （なし） |
| CHK_M_CNCTEQP | TOPROCESS | 入力工程     | （なし） |
| CHK_M_CNCTEQP | TOVENDOR  | nil          | （なし） |

## テーブル: CHK_M_CODE

| テーブル名   | 列ID   | 列名     | 備考     |
|:-------------|:-------|:---------|:---------|
| CHK_M_CODE   | CFCDTY | タイプ無 | （なし） |
| CHK_M_CODE   | FCDTY  | タイプ   | （なし） |
| CHK_M_CODE   | FCODE  | コード   | （なし） |

## テーブル: CHK_M_CONSUMPTTAX

| テーブル名        | 列ID    | 列名     | 備考     |
|:------------------|:--------|:---------|:---------|
| CHK_M_CONSUMPTTAX | NO_DATA | データ無 | （なし） |

## テーブル: CHK_M_COST

| テーブル名   | 列ID      | 列名            | 備考     |
|:-------------|:----------|:----------------|:---------|
| CHK_M_COST   | ACTCOST1  | 実際加工費      | （なし） |
| CHK_M_COST   | APPLYDATE | 適用日          | （なし） |
| CHK_M_COST   | CITEM     | 品目無          | （なし） |
| CHK_M_COST   | COSTF     | 原価区分0,1以外 | （なし） |
| CHK_M_COST   | ITEM      | 品目            | （なし） |
| CHK_M_COST   | PROCESS   | 工程            | （なし） |
| CHK_M_COST   | STDCOST1  | 標準加工費      | （なし） |
| CHK_M_COST   | VENDOR    | 仕入先          | （なし） |

## テーブル: CHK_M_CUSTOM

| テーブル名   | 列ID     | 列名                   | 備考     |
|:-------------|:---------|:-----------------------|:---------|
| CHK_M_CUSTOM | CLND     | 顧客ｶﾚﾝﾀﾞｰ無           | YES/NO   |
| CHK_M_CUSTOM | CUSTOM   | 顧客                   | （なし） |
| CHK_M_CUSTOM | LOTCTRLF | ロット管理F ０，１以外 | YES/NO   |
| CHK_M_CUSTOM | TRNSCLND | 配送便ｶﾚﾝﾀﾞｰ無         | YES/NO   |

## テーブル: CHK_M_ITEM

| テーブル名   | 列ID          | 列名                             | 備考     |
|:-------------|:--------------|:---------------------------------|:---------|
| CHK_M_ITEM   | A_CARD        | 現品票区分0,1以外                | （なし） |
| CHK_M_ITEM   | A_FGROUP      | 商品分類無                       | （なし） |
| CHK_M_ITEM   | A_FMCUS       | 代表得意先無                     | （なし） |
| CHK_M_ITEM   | A_FMCUS_NL    | 代表得意先未設定                 | （なし） |
| CHK_M_ITEM   | A_FPCLASS     | クラス1無                        | （なし） |
| CHK_M_ITEM   | A_FPCLASS_NL  | クラス1未設定                    | （なし） |
| CHK_M_ITEM   | A_FPCLASS2    | クラス2無                        | （なし） |
| CHK_M_ITEM   | A_FPLACE1     | 場所1無                          | （なし） |
| CHK_M_ITEM   | A_FPLACE1_NL  | 場所1未設定                      | （なし） |
| CHK_M_ITEM   | A_FPLACE2     | 場所2無                          | （なし） |
| CHK_M_ITEM   | A_FPLACE3     | 場所3無                          | （なし） |
| CHK_M_ITEM   | A_FPLACE4     | 場所4無                          | （なし） |
| CHK_M_ITEM   | A_FPLACE5     | 場所5無                          | （なし） |
| CHK_M_ITEM   | A_FPTYPE      | 購入区分無                       | （なし） |
| CHK_M_ITEM   | A_FPTYPE_NL   | 購入区分未設定                   | （なし） |
| CHK_M_ITEM   | A_FRELEASE    | オーダ発行区分0,1以外            | （なし） |
| CHK_M_ITEM   | A_FRELEASE2   | オーダ発行区分不適合             | （なし） |
| CHK_M_ITEM   | A_ISOCARD     | ISO移動票区分0,1以外             | （なし） |
| CHK_M_ITEM   | A_ITMSTATUS   | ステータス無効                   | （なし） |
| CHK_M_ITEM   | A_PROCURE     | 調達区分0,1以外                  | （なし） |
| CHK_M_ITEM   | A_QLTYREP     | 成績表添付区分0,1以外            | （なし） |
| CHK_M_ITEM   | A_RCVTEST     | 受入検査区分0,1以外              | （なし） |
| CHK_M_ITEM   | A_SHIPSECT    | 出荷担当部門無                   | （なし） |
| CHK_M_ITEM   | A_SHIPSECT_NL | 出荷担当部門未設定               | （なし） |
| CHK_M_ITEM   | A_VENDOR      | 発注先無                         | （なし） |
| CHK_M_ITEM   | A_VENDOR_NL   | 発注先未設定                     | （なし） |
| CHK_M_ITEM   | A_WBIN        | ダブルビン区分0,1以外            | （なし） |
| CHK_M_ITEM   | ABNM          | 略称無                           | （なし） |
| CHK_M_ITEM   | ACCEPTLOC     | 納入場所無                       | YES/NO   |
| CHK_M_ITEM   | BOM           | 製品構成無                       | YES/NO   |
| CHK_M_ITEM   | CASECD        | 容器無                           | （なし） |
| CHK_M_ITEM   | COST_NL       | 原価マスタ登録無                 | （なし） |
| CHK_M_ITEM   | CPROCESS      | 工程無                           | YES/NO   |
| CHK_M_ITEM   | CSTTYP        | 単価区分　０，１以外             | YES/NO   |
| CHK_M_ITEM   | CVENDOR       | 仕入先無                         | YES/NO   |
| CHK_M_ITEM   | IMTYP         | 製品区分　０，１，２以外         | YES/NO   |
| CHK_M_ITEM   | INDP          | 独立需要Ｆ　０，１以外           | YES/NO   |
| CHK_M_ITEM   | ITEM          | 品目                             | （なし） |
| CHK_M_ITEM   | LOTCTRLF      | ロット管理F ０，１以外           | YES/NO   |
| CHK_M_ITEM   | MRPF          | 所要量計算LV　０，１以外         | YES/NO   |
| CHK_M_ITEM   | MRPF2         | 所要量計算LV=1　且つ　購納F=1    | YES/NO   |
| CHK_M_ITEM   | ODPLCY        | 発注LV　０，１以外               | YES/NO   |
| CHK_M_ITEM   | OFCLTRM       | 購入品確定期間>３６６            | YES/NO   |
| CHK_M_ITEM   | PACKAGECD     | 荷姿無                           | （なし） |
| CHK_M_ITEM   | PACKQTY       | 入数=0                           | （なし） |
| CHK_M_ITEM   | PRDCTCAPA     | 能力無                           | YES/NO   |
| CHK_M_ITEM   | PRDCTCTRL     | 製番管理Ｆ　０，１，２以外       | YES/NO   |
| CHK_M_ITEM   | PRDCTCTRL2    | 製番管理Ｆ=２ 且つ 独立需要Ｆ<>1 | YES/NO   |
| CHK_M_ITEM   | PRICE_NL      | 単価マスタ登録無                 | （なし） |
| CHK_M_ITEM   | PRMRYF        | 主材区分　０，１，２以外         | YES/NO   |
| CHK_M_ITEM   | PROCESS       | 工程                             | （なし） |
| CHK_M_ITEM   | PURCHSF       | 購納F　０，１以外                | YES/NO   |
| CHK_M_ITEM   | SBJCT         | 科目無                           | YES/NO   |
| CHK_M_ITEM   | SECT          | 担当部門無                       | YES/NO   |
| CHK_M_ITEM   | STCKF         | 在庫引落区分　０，１以外         | YES/NO   |
| CHK_M_ITEM   | STDATE        | 発効日>=失効日                   | YES/NO   |
| CHK_M_ITEM   | STGSECT       | 保管部門無                       | YES/NO   |
| CHK_M_ITEM   | STGTYP        | 保管Ｆ　０，１以外               | YES/NO   |
| CHK_M_ITEM   | STLOC         | 保管場所無                       | YES/NO   |
| CHK_M_ITEM   | TRLT          | 搬送L/T(分)>使用期限(分)         | YES/NO   |
| CHK_M_ITEM   | USEUPF        | 半製品使切F　０，１以外          | YES/NO   |
| CHK_M_ITEM   | VENDOR        | 仕入先                           | （なし） |
| CHK_M_ITEM   | WRHOUSEF      | 倉庫工程                         | YES/NO   |

## テーブル: CHK_M_ITEM_V

| テーブル名   | 列ID   | 列名   | 備考     |
|:-------------|:-------|:-------|:---------|
| CHK_M_ITEM_V | COUNT  | 重複数 | （なし） |
| CHK_M_ITEM_V | ITEM   | 品目   | （なし） |

## テーブル: CHK_M_JIG

| テーブル名   | 列ID      | 列名                  | 備考     |
|:-------------|:----------|:----------------------|:---------|
| CHK_M_JIG    | CLOCATION | 場所無                | YES/NO   |
| CHK_M_JIG    | JIG       | 治具                  | （なし） |
| CHK_M_JIG    | NUMJIG    | 治具数＝0             | YES/NO   |
| CHK_M_JIG    | NUMRPR    | 修理数>治具数         | YES/NO   |
| CHK_M_JIG    | STRPR     | 修理開始日>修理完了日 | YES/NO   |

## テーブル: CHK_M_LINED

| テーブル名   | 列ID         | 列名                              | 備考     |
|:-------------|:-------------|:----------------------------------|:---------|
| CHK_M_LINED  | BATCH        | バッチ処理F　０，１以外           | YES/NO   |
| CHK_M_LINED  | CLNDNO       | ｶﾚﾝﾀﾞｰ番号無                      | YES/NO   |
| CHK_M_LINED  | CNCTFLG      | 連結F　０、１以外                 | YES/NO   |
| CHK_M_LINED  | CNCTLINED    | 連結ライン無                      | YES/NO   |
| CHK_M_LINED  | CNCTLINED2   | 工程・ライン＝連結工程・ライン    | YES/NO   |
| CHK_M_LINED  | CPROCESS     | 工程無                            | YES/NO   |
| CHK_M_LINED  | ENTMAJ       | 終業時切上F　０、１、２以外       | YES/NO   |
| CHK_M_LINED  | EQPF         | ストレージF　０、１以外           | YES/NO   |
| CHK_M_LINED  | FIFO         | 先入先出Ｆ　０，１以外            | YES/NO   |
| CHK_M_LINED  | GNTDSPF      | ガントチャート非表示F　０、１以外 | YES/NO   |
| CHK_M_LINED  | ISLOCTDEF    | 出庫場所規定値無                  | YES/NO   |
| CHK_M_LINED  | LINED        | ライン                            | （なし） |
| CHK_M_LINED  | LOADLV       | 平均負荷割F　０、１以外           | YES/NO   |
| CHK_M_LINED  | LOTGRNT      | ロットサイズ保証Ｆ　０，１以外    | YES/NO   |
| CHK_M_LINED  | ODTPY        | 指示発行区分　０、１、２以外      | YES/NO   |
| CHK_M_LINED  | OFFTMTBL     | 休出稼働時間帯無                  | YES/NO   |
| CHK_M_LINED  | OPRTRATIO    | 計画稼働率=0                      | YES/NO   |
| CHK_M_LINED  | OVLAPF       | ｵｰﾊﾞｰﾗｯﾌﾟF　０、１以外            | YES/NO   |
| CHK_M_LINED  | PRDCTCTRL_F1 | ロットサイズ保証Ｆの警告          | YES/NO   |
| CHK_M_LINED  | PRDCTCTRL_F2 | 先入先出Ｆの警告                  | YES/NO   |
| CHK_M_LINED  | PRDCTCTRL_F3 | 端数処理数の警告                  | YES/NO   |
| CHK_M_LINED  | PROCESS      | 工程                              | （なし） |
| CHK_M_LINED  | PRODSETUPF   | 定期段取区分　０、１、２以外      | YES/NO   |
| CHK_M_LINED  | PRODWKGRP    | 定期段取人員G無                   | YES/NO   |
| CHK_M_LINED  | RCLOCTDEF    | 入庫場所規定値無                  | YES/NO   |
| CHK_M_LINED  | SBCNTCD      | 外注コード無                      | YES/NO   |
| CHK_M_LINED  | SBCNTF       | 外注F　０、１以外                 | YES/NO   |
| CHK_M_LINED  | SECT         | 担当部門無                        | YES/NO   |
| CHK_M_LINED  | STDTMTBL     | 標準稼働時間帯無                  | YES/NO   |
| CHK_M_LINED  | STGF         | ストレージ区分　０、１以外        | YES/NO   |
| CHK_M_LINED  | WGTCNVF      | 比重変換F　０、１以外             | YES/NO   |

## テーブル: CHK_M_LOCATION

| テーブル名     | 列ID       | 列名               | 備考     |
|:---------------|:-----------|:-------------------|:---------|
| CHK_M_LOCATION | A_CLND     | 納入先カレンダーNo | （なし） |
| CHK_M_LOCATION | A_FACCFLG  | 集荷区分           | （なし） |
| CHK_M_LOCATION | A_LOCTF    | 場所区分           | （なし） |
| CHK_M_LOCATION | CLLCTYPE   | 集荷タイプ         | （なし） |
| CHK_M_LOCATION | CLLCTYPE2  | 集荷タイプ2        | （なし） |
| CHK_M_LOCATION | LOCT       | 場所               | （なし） |
| CHK_M_LOCATION | PARTSF     | パーツ区分         | （なし） |
| CHK_M_LOCATION | TRANSACTOR | 取引先             | （なし） |

## テーブル: CHK_M_MAXMININVT

| テーブル名       | 列ID      | 列名               | 備考     |
|:-----------------|:----------|:-------------------|:---------|
| CHK_M_MAXMININVT | CITEM     | 品目無             | YES/NO   |
| CHK_M_MAXMININVT | CMAXINVNT | 最小在庫＞最大在庫 | YES/NO   |
| CHK_M_MAXMININVT | CSTDATE   | 開始日＞終了日     | YES/NO   |
| CHK_M_MAXMININVT | CSTDATE2  | 在庫期間重複       | YES/NO   |
| CHK_M_MAXMININVT | EDDATE    | 終了日             | （なし） |
| CHK_M_MAXMININVT | ITEM      | 品目               | （なし） |
| CHK_M_MAXMININVT | PROCESS   | 工程               | （なし） |
| CHK_M_MAXMININVT | STDATE    | 開始日             | （なし） |
| CHK_M_MAXMININVT | VENDOR    | 仕入先             | （なし） |

## テーブル: CHK_M_OVSPROCURE

| テーブル名       | 列ID          | 列名                  | 備考     |
|:-----------------|:--------------|:----------------------|:---------|
| CHK_M_OVSPROCURE | DT1           | 到着予定日≦出荷予定日 | （なし） |
| CHK_M_OVSPROCURE | DT2           | 引当期限日≦出荷予定日 | （なし） |
| CHK_M_OVSPROCURE | DT3           | 引当期限日≦到着予定日 | （なし） |
| CHK_M_OVSPROCURE | DT4           | 到着予定日二重登録    | （なし） |
| CHK_M_OVSPROCURE | PROCURE_BKTNO | 調達BKTNo             | （なし） |
| CHK_M_OVSPROCURE | PROCURE_YM    | 調達年月              | （なし） |
| CHK_M_OVSPROCURE | TRANSACTOR    | 発注先                | （なし） |

## テーブル: CHK_M_PRDCTCAPA

| テーブル名      | 列ID       | 列名                             | 備考     |
|:----------------|:-----------|:---------------------------------|:---------|
| CHK_M_PRDCTCAPA | AMANG      | 後段取人員G 無                   | YES/NO   |
| CHK_M_PRDCTCAPA | AMANG1     | 後段取人員G 人員数オーバー       | YES/NO   |
| CHK_M_PRDCTCAPA | CAPA       | 生産能力＝０                     | YES/NO   |
| CHK_M_PRDCTCAPA | CDSTUP1    | 段取Ｇ１特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CDSTUP2    | 段取Ｇ２特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CDSTUP3    | 段取Ｇ３特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CDSTUP4    | 段取Ｇ４特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CDSTUP5    | 段取Ｇ５特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CDSTUP6    | 段取Ｇ6特性値無                  | YES/NO   |
| CHK_M_PRDCTCAPA | CDSTUP7    | 段取Ｇ7特性値無                  | YES/NO   |
| CHK_M_PRDCTCAPA | CITEM      | 品目無                           | YES/NO   |
| CHK_M_PRDCTCAPA | CLINED     | ライン無                         | YES/NO   |
| CHK_M_PRDCTCAPA | CNCTFLG    | 連結F　０、１以外                | YES/NO   |
| CHK_M_PRDCTCAPA | CNCTLINED  | 連結ライン無                     | YES/NO   |
| CHK_M_PRDCTCAPA | CNCTLINED2 | 工程・ライン＝連結工程・ライン   | YES/NO   |
| CHK_M_PRDCTCAPA | CQLTY1     | 品質Ｇ１特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CQLTY2     | 品質Ｇ２特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CQLTY3     | 品質Ｇ３特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CQLTY4     | 品質Ｇ４特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CQLTY5     | 品質Ｇ５特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CQLTY6     | 品質Ｇ６特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | CQLTY7     | 品質Ｇ７特性値無                 | YES/NO   |
| CHK_M_PRDCTCAPA | DSTUP1     | 段取Ｇ１特性値                   | （なし） |
| CHK_M_PRDCTCAPA | DSTUP2     | 段取Ｇ２特性値                   | （なし） |
| CHK_M_PRDCTCAPA | DSTUP3     | 段取Ｇ３特性値                   | （なし） |
| CHK_M_PRDCTCAPA | DSTUP4     | 段取Ｇ４特性値                   | （なし） |
| CHK_M_PRDCTCAPA | DSTUP5     | 段取Ｇ５特性値                   | （なし） |
| CHK_M_PRDCTCAPA | DSTUP6     | 段取Ｇ６特性値                   | （なし） |
| CHK_M_PRDCTCAPA | DSTUP7     | 段取Ｇ７特性値                   | （なし） |
| CHK_M_PRDCTCAPA | DUM1       | DUM1                             | （なし） |
| CHK_M_PRDCTCAPA | DUM2       | DUM2                             | （なし） |
| CHK_M_PRDCTCAPA | DUM3       | DUM3                             | （なし） |
| CHK_M_PRDCTCAPA | DUM4       | DUM4                             | （なし） |
| CHK_M_PRDCTCAPA | DUM5       | DUM5                             | （なし） |
| CHK_M_PRDCTCAPA | DUM6       | DUM6                             | （なし） |
| CHK_M_PRDCTCAPA | DUM7       | DUM7                             | （なし） |
| CHK_M_PRDCTCAPA | FMANG      | 段取人員Ｇ無                     | YES/NO   |
| CHK_M_PRDCTCAPA | FMANG1     | 段取人員Ｇ 人員数オーバー        | YES/NO   |
| CHK_M_PRDCTCAPA | INVLF      | 無効F　０、１以外                | YES/NO   |
| CHK_M_PRDCTCAPA | ITEM       | 品目                             | （なし） |
| CHK_M_PRDCTCAPA | JIG1       | 使用治具１－治具番号無           | YES/NO   |
| CHK_M_PRDCTCAPA | JIG2       | 使用治具２－治具番号無           | YES/NO   |
| CHK_M_PRDCTCAPA | JIG3       | 使用治具３－治具番号無           | YES/NO   |
| CHK_M_PRDCTCAPA | JIG4       | 使用治具４－治具番号無           | YES/NO   |
| CHK_M_PRDCTCAPA | JIG5       | 使用治具５－治具番号無           | YES/NO   |
| CHK_M_PRDCTCAPA | LINED      | ライン                           | （なし） |
| CHK_M_PRDCTCAPA | PREFER     | 優先順位 １〜99以外              | YES/NO   |
| CHK_M_PRDCTCAPA | PROCESS    | 工程                             | （なし） |
| CHK_M_PRDCTCAPA | QLTY1      | 品質Ｇ１特性値                   | （なし） |
| CHK_M_PRDCTCAPA | QLTY2      | 品質Ｇ２特性値                   | （なし） |
| CHK_M_PRDCTCAPA | QLTY3      | 品質Ｇ３特性値                   | （なし） |
| CHK_M_PRDCTCAPA | QLTY4      | 品質Ｇ４特性値                   | （なし） |
| CHK_M_PRDCTCAPA | QLTY5      | 品質Ｇ５特性値                   | （なし） |
| CHK_M_PRDCTCAPA | QLTY6      | 品質Ｇ６特性値                   | （なし） |
| CHK_M_PRDCTCAPA | QLTY7      | 品質Ｇ７特性値                   | （なし） |
| CHK_M_PRDCTCAPA | SBCNTCSTF  | 単価区分　０．１以外             | YES/NO   |
| CHK_M_PRDCTCAPA | SCHMETH    | 立案方法　１〜３以外             | YES/NO   |
| CHK_M_PRDCTCAPA | SMIMSETUPF | 同一品目固定段取F ０，１，２以外 | YES/NO   |
| CHK_M_PRDCTCAPA | STDATE     | 発効日>失効日                    | YES/NO   |
| CHK_M_PRDCTCAPA | STDLOT     | ロットサイズエラー１             | YES/NO   |
| CHK_M_PRDCTCAPA | STDLOT2    | ロットサイズエラー２             | YES/NO   |
| CHK_M_PRDCTCAPA | STDLOT3    | ロットサイズエラー３             | YES/NO   |
| CHK_M_PRDCTCAPA | VENDOR     | 仕入先                           | （なし） |
| CHK_M_PRDCTCAPA | WKGRP1     | 人員Ｇ１無                       | YES/NO   |
| CHK_M_PRDCTCAPA | WKGRP11    | 人員Ｇ１ 人員数オーバー          | YES/NO   |
| CHK_M_PRDCTCAPA | WKGRP2     | 人員Ｇ２無                       | YES/NO   |
| CHK_M_PRDCTCAPA | WKGRP21    | 人員Ｇ２ 人員数オーバー          | YES/NO   |
| CHK_M_PRDCTCAPA | WKGRP3     | 人員Ｇ３無                       | YES/NO   |
| CHK_M_PRDCTCAPA | WKGRP31    | 人員Ｇ３ 人員数オーバー          | YES/NO   |

## テーブル: CHK_M_PRDCTGRP

| テーブル名     | 列ID     | 列名               | 備考     |
|:---------------|:---------|:-------------------|:---------|
| CHK_M_PRDCTGRP | COMF     | 共通Ｆ　０，１以外 | YES/NO   |
| CHK_M_PRDCTGRP | PRDCTGRP | 製品群             | （なし） |

## テーブル: CHK_M_PRICE

| テーブル名   | 列ID         | 列名                       | 備考                   |
|:-------------|:-------------|:---------------------------|:-----------------------|
| CHK_M_PRICE  | ACT_PRICE    | 実際単価=0                 | （なし）               |
| CHK_M_PRICE  | APPLYDATE    | 適用日                     | （なし）               |
| CHK_M_PRICE  | APPLYDATE_CH | 対象適用日無               | （なし）               |
| CHK_M_PRICE  | CITEM        | 品目無                     | （なし）               |
| CHK_M_PRICE  | CSPFLAG      | 売買区分S,P以外            | （なし）               |
| CHK_M_PRICE  | CTRANSACTOR  | 取引先無                   | （なし）               |
| CHK_M_PRICE  | ITEM         | 品目                       | （なし）               |
| CHK_M_PRICE  | PR_PRICE     | 売上情報・仕入情報の単価無 | （なし）               |
| CHK_M_PRICE  | PRICE        | 標準単価=0                 | （なし）               |
| CHK_M_PRICE  | PRICEF       | 単価区分0,1以外            | （なし）               |
| CHK_M_PRICE  | PROCESS      | 工程                       | （なし）               |
| CHK_M_PRICE  | SPFLAG       | 売買区分                   | S;売上単価;P; 仕入単価 |
| CHK_M_PRICE  | TRANSACTOR   | 取引先                     | （なし）               |
| CHK_M_PRICE  | VENDOR       | 仕入先                     | （なし）               |

## テーブル: CHK_M_PROCESS

| テーブル名    | 列ID        | 列名                        | 備考                    |
|:--------------|:------------|:----------------------------|:------------------------|
| CHK_M_PROCESS | CLND        | カレンダー番号無            | YES/NO                  |
| CHK_M_PROCESS | CSTF        | 原価計算Ｆ　０，１以外      | YES/NO                  |
| CHK_M_PROCESS | DUEDOPT     | 納期最適化Ｆ　０，１以外    | YES/NO                  |
| CHK_M_PROCESS | EVAL_F      | 評価区分                    | （なし）                |
| CHK_M_PROCESS | PAYSAL_F    | 売買作成F　０，１以外       | 0;作成する;1;作成しない |
| CHK_M_PROCESS | PRDCTCTRL   | 製番管理Ｆ　０，１，２以外  | YES/NO                  |
| CHK_M_PROCESS | PRDCTGRP    | 製品群無                    | YES/NO                  |
| CHK_M_PROCESS | PRDCTINST_F | 指示書区分０，１以外        | YES/NO                  |
| CHK_M_PROCESS | PRICE_F     | 単価登録F０，１，２、３以外 | （なし）                |
| CHK_M_PROCESS | PROCESS     | 工程                        | （なし）                |
| CHK_M_PROCESS | QLTYOPT     | 品質最適化Ｆ　０，１以外    | YES/NO                  |
| CHK_M_PROCESS | SETUPOPT    | 段取最適化Ｆ　０，１以外    | YES/NO                  |
| CHK_M_PROCESS | WRKROPT     | 人員最適化Ｆ　０，１以外    | YES/NO                  |

## テーブル: CHK_M_PRVDCST

| テーブル名    | 列ID    | 列名         | 備考     |
|:--------------|:--------|:-------------|:---------|
| CHK_M_PRVDCST | ACTCST  | 現在単価＝０ | YES/NO   |
| CHK_M_PRVDCST | CITEM   | 品目無       | YES/NO   |
| CHK_M_PRVDCST | CPRVD   | 支給先無     | YES/NO   |
| CHK_M_PRVDCST | ITEM    | 品目         | （なし） |
| CHK_M_PRVDCST | PROCESS | 工程         | （なし） |
| CHK_M_PRVDCST | PRVD    | 支給先       | （なし） |
| CHK_M_PRVDCST | VENDOR  | 仕入先       | （なし） |

## テーブル: CHK_M_QLTY

| テーブル名   | 列ID      | 列名           | 備考     |
|:-------------|:----------|:---------------|:---------|
| CHK_M_QLTY   | CLINED    | ライン無       | YES/NO   |
| CHK_M_QLTY   | CQLTYATR1 | 品質特性値１無 | YES/NO   |
| CHK_M_QLTY   | CQLTYATR2 | 品質特性値２無 | YES/NO   |
| CHK_M_QLTY   | LINED     | ライン         | （なし） |
| CHK_M_QLTY   | PROCESS   | 工程           | （なし） |
| CHK_M_QLTY   | QLTYATR1  | 品質特性値１   | （なし） |
| CHK_M_QLTY   | QLTYATR2  | 品質特性値２   | （なし） |
| CHK_M_QLTY   | QLTYG     | 品質Ｇ         | （なし） |

## テーブル: CHK_M_QLTYATR

| テーブル名    | 列ID    | 列名              | 備考     |
|:--------------|:--------|:------------------|:---------|
| CHK_M_QLTYATR | CLINED  | ライン無          | YES/NO   |
| CHK_M_QLTYATR | CQLTYG  | 品質Ｇ １〜７以外 | YES/NO   |
| CHK_M_QLTYATR | LINED   | ライン            | （なし） |
| CHK_M_QLTYATR | PROCESS | 工程              | （なし） |
| CHK_M_QLTYATR | QLTYA   | 品質特性値        | （なし） |
| CHK_M_QLTYATR | QLTYG   | 品質Ｇ            | （なし） |

## テーブル: CHK_M_RCISMST

| テーブル名    | 列ID    | 列名                         | 備考     |
|:--------------|:--------|:-----------------------------|:---------|
| CHK_M_RCISMST | CSTF    | 原価管理区分　０，１以外     | YES/NO   |
| CHK_M_RCISMST | MNYF    | 金額計上F0,1以外             | （なし） |
| CHK_M_RCISMST | PRVDF   | 支給区分　０，１，２以外     | YES/NO   |
| CHK_M_RCISMST | RCISCD  | 入出庫区分                   | （なし） |
| CHK_M_RCISMST | RCISF   | 入庫・出庫区分　０，１以外   | YES/NO   |
| CHK_M_RCISMST | RETURNF | 返品区分　０，１以外         | YES/NO   |
| CHK_M_RCISMST | STCKF   | 在庫計上区分　０，１，２以外 | YES/NO   |

## テーブル: CHK_M_RMPRDCT

| テーブル名    | 列ID       | 列名       | 備考     |
|:--------------|:-----------|:-----------|:---------|
| CHK_M_RMPRDCT | BKTNO      | ﾊﾞｹｯﾄＮｏ  | （なし） |
| CHK_M_RMPRDCT | BKTYEAR    | ﾊﾞｹｯﾄ年    | （なし） |
| CHK_M_RMPRDCT | CBUCKET    | バケット無 | YES/NO   |
| CHK_M_RMPRDCT | CITEM      | 品目無     | YES/NO   |
| CHK_M_RMPRDCT | CLINED     | ライン無   | YES/NO   |
| CHK_M_RMPRDCT | CPRDCTCAPA | 生産能力無 | YES/NO   |
| CHK_M_RMPRDCT | CPROCESS   | 工程無     | YES/NO   |
| CHK_M_RMPRDCT | LINED      | ライン     | （なし） |
| CHK_M_RMPRDCT | PROCESS    | 工程       | （なし） |

## テーブル: CHK_M_SETUP

| テーブル名   | 列ID     | 列名           | 備考     |
|:-------------|:---------|:---------------|:---------|
| CHK_M_SETUP  | CLINED   | ライン無       | YES/NO   |
| CHK_M_SETUP  | CSETUPA1 | 段取特性値１無 | YES/NO   |
| CHK_M_SETUP  | CSETUPA2 | 段取特性値２無 | YES/NO   |
| CHK_M_SETUP  | LINED    | ライン         | （なし） |
| CHK_M_SETUP  | MANGRP   | 段取人員Ｇ無   | YES/NO   |
| CHK_M_SETUP  | PROCESS  | 工程           | （なし） |
| CHK_M_SETUP  | SETUPA1  | 段取特性値１   | （なし） |
| CHK_M_SETUP  | SETUPA2  | 段取特性値２   | （なし） |
| CHK_M_SETUP  | SETUPG   | 段取Ｇ         | （なし） |

## テーブル: CHK_M_SETUPATR

| テーブル名     | 列ID    | 列名              | 備考     |
|:---------------|:--------|:------------------|:---------|
| CHK_M_SETUPATR | CLINED  | ライン無          | YES/NO   |
| CHK_M_SETUPATR | CSETUPG | 段取Ｇ １〜７以外 | YES/NO   |
| CHK_M_SETUPATR | LINED   | ライン            | （なし） |
| CHK_M_SETUPATR | PROCESS | 工程              | （なし） |
| CHK_M_SETUPATR | SETUPA  | 段取特性値        | （なし） |
| CHK_M_SETUPATR | SETUPG  | 段取Ｇ            | （なし） |

## テーブル: CHK_M_SMPRDCT

| テーブル名    | 列ID           | 列名                     | 備考     |
|:--------------|:---------------|:-------------------------|:---------|
| CHK_M_SMPRDCT | CITEM          | 品目無                   | YES/NO   |
| CHK_M_SMPRDCT | CSMPRDCTIM     | 同時品目無               | YES/NO   |
| CHK_M_SMPRDCT | DUPLICATE_DATA | 品目＝同時生産品目       | YES/NO   |
| CHK_M_SMPRDCT | ITEM           | 品目                     | （なし） |
| CHK_M_SMPRDCT | PROCESS        | 工程                     | （なし） |
| CHK_M_SMPRDCT | SMPRDCTF       | 同時生産区分　０，１以外 | YES/NO   |
| CHK_M_SMPRDCT | SMPRDCTIM      | 同時生産品目             | （なし） |
| CHK_M_SMPRDCT | VENDOR         | 仕入先                   | （なし） |

## テーブル: CHK_M_SYSMANAGE

| テーブル名      | 列ID   | 列名       | 備考     |
|:----------------|:-------|:-----------|:---------|
| CHK_M_SYSMANAGE | BANKCD | 銀行コード | （なし） |
| CHK_M_SYSMANAGE | KEY_M  | KEY        | （なし） |

## テーブル: CHK_M_TMTBL

| テーブル名   | 列ID   | 列名             | 備考     |
|:-------------|:-------|:-----------------|:---------|
| CHK_M_TMTBL  | S_HOUR | 稼働期間＞24時間 | YES/NO   |
| CHK_M_TMTBL  | TMTBL  | 稼働時間帯       | （なし） |

## テーブル: CHK_M_TMTBLD

| テーブル名   | 列ID   | 列名               | 備考     |
|:-------------|:-------|:-------------------|:---------|
| CHK_M_TMTBLD | CTMTBL | 稼働時間帯　無     | YES/NO   |
| CHK_M_TMTBLD | OPFLG  | 稼働F　０、１以外  | YES/NO   |
| CHK_M_TMTBLD | SQNO   | 稼働番号           | （なし） |
| CHK_M_TMTBLD | STHR   | 開始時間＞終了時間 | YES/NO   |
| CHK_M_TMTBLD | TMTBL  | 稼働時間帯         | （なし） |

## テーブル: CHK_M_TRANSACTOR

| テーブル名       | 列ID          | 列名                    | 備考     |
|:-----------------|:--------------|:------------------------|:---------|
| CHK_M_TRANSACTOR | A_EDIF        | EDI取込F0,1,2,3以外     | （なし） |
| CHK_M_TRANSACTOR | ACCTYP        | 口座種別0,1,2以外       | （なし） |
| CHK_M_TRANSACTOR | BANKCD        | 銀行コード無            | （なし） |
| CHK_M_TRANSACTOR | CLMCD         | 請求先無                | （なし） |
| CHK_M_TRANSACTOR | CLMCD_NL      | 請求先未設定            | （なし） |
| CHK_M_TRANSACTOR | CMMSF         | 手数料区分0,1以外       | （なし） |
| CHK_M_TRANSACTOR | FORCASTF      | 受注タイプ0,1以外       | （なし） |
| CHK_M_TRANSACTOR | FRACT         | 金額端数区分0,1,2以外   | （なし） |
| CHK_M_TRANSACTOR | MCLLDNF       | メイン金種区分0〜3以外  | （なし） |
| CHK_M_TRANSACTOR | PCLLCTCY      | 支払予定月0,1,2以外     | （なし） |
| CHK_M_TRANSACTOR | PR_AP_F       | 売上計上区分0,1以外     | （なし） |
| CHK_M_TRANSACTOR | PYECD         | 支払先無                | （なし） |
| CHK_M_TRANSACTOR | PYECD_NL      | 支払先未設定            | （なし） |
| CHK_M_TRANSACTOR | TAXCLCF       | 消費税計算区分0,1以外   | （なし） |
| CHK_M_TRANSACTOR | TAXF          | 消費税区分0,1,9以外     | （なし） |
| CHK_M_TRANSACTOR | TAXFRF        | 消費税端数区分0,1,2以外 | （なし） |
| CHK_M_TRANSACTOR | TRANSACTOR    | 取引先                  | （なし） |
| CHK_M_TRANSACTOR | TRANSACTORFLG | 取引区分0,1,2以外       | （なし） |

## テーブル: CHK_M_VENDOR

| テーブル名   | 列ID     | 列名                   | 備考     |
|:-------------|:---------|:-----------------------|:---------|
| CHK_M_VENDOR | LOTCTRLF | ロット管理F ０，１以外 | YES/NO   |
| CHK_M_VENDOR | VENDOR   | 仕入先                 | （なし） |

## テーブル: CHK_M_WORKER

| テーブル名   | 列ID     | 列名             | 備考     |
|:-------------|:---------|:-----------------|:---------|
| CHK_M_WORKER | CLND     | ｶﾚﾝﾀﾞｰ番号無     | YES/NO   |
| CHK_M_WORKER | OFFTMTBL | 休出稼働時間帯無 | YES/NO   |
| CHK_M_WORKER | STDTMTBL | 標準稼働時間帯無 | YES/NO   |
| CHK_M_WORKER | WKGRP    | 生産人員Ｇ       | （なし） |

## テーブル: CHK_M_WORKERCD

| テーブル名     | 列ID   | 列名           | 備考     |
|:---------------|:-------|:---------------|:---------|
| CHK_M_WORKERCD | SECT   | 部門無         | （なし） |
| CHK_M_WORKERCD | USERID | グループＩＤ無 | （なし） |
| CHK_M_WORKERCD | WKCD   | 担当者         | （なし） |

## テーブル: CHK_S_PRDCTNOSTOCK

| テーブル名         | 列ID     | 列名                               | 備考     |
|:-------------------|:---------|:-----------------------------------|:---------|
| CHK_S_PRDCTNOSTOCK | BKTNO    | ﾊﾞｹｯﾄＮｏ                          | （なし） |
| CHK_S_PRDCTNOSTOCK | BKTYEAR  | ﾊﾞｹｯﾄ年                            | （なし） |
| CHK_S_PRDCTNOSTOCK | CBKT     | バケット無                         | YES/NO   |
| CHK_S_PRDCTNOSTOCK | CITEM    | 品目無                             | YES/NO   |
| CHK_S_PRDCTNOSTOCK | CLINED   | ライン無                           | YES/NO   |
| CHK_S_PRDCTNOSTOCK | CMPFLG   | 完了Ｆ　－２，－１，０，１，２以外 | YES/NO   |
| CHK_S_PRDCTNOSTOCK | ITEM     | 品目                               | （なし） |
| CHK_S_PRDCTNOSTOCK | PRDCTBNO | 枝番                               | （なし） |
| CHK_S_PRDCTNOSTOCK | PRDCTNO  | 製番                               | （なし） |
| CHK_S_PRDCTNOSTOCK | PROCESS  | 工程                               | （なし） |

## テーブル: CHK_S_SUSPENDSTOCK

| テーブル名         | 列ID        | 列名       | 備考     |
|:-------------------|:------------|:-----------|:---------|
| CHK_S_SUSPENDSTOCK | BKTNO       | ﾊﾞｹｯﾄＮｏ  | （なし） |
| CHK_S_SUSPENDSTOCK | BKTYEAR     | ﾊﾞｹｯﾄ年    | （なし） |
| CHK_S_SUSPENDSTOCK | CBKT        | バケット無 | YES/NO   |
| CHK_S_SUSPENDSTOCK | CITEM       | 品目無     | YES/NO   |
| CHK_S_SUSPENDSTOCK | ITEM        | 品目       | （なし） |
| CHK_S_SUSPENDSTOCK | PROCESS     | 工程       | （なし） |
| CHK_S_SUSPENDSTOCK | SUSPENDDATE | 保留解除日 | （なし） |

## テーブル: CONSUMP_TMP

| テーブル名   | 列ID      | 列名       | 備考                       |
|:-------------|:----------|:-----------|:---------------------------|
| CONSUMP_TMP  | A_FPLACE1 | 場所1      | （なし）                   |
| CONSUMP_TMP  | A_FPLACE2 | 場所2      | （なし）                   |
| CONSUMP_TMP  | A_FPLACE3 | 場所3      | （なし）                   |
| CONSUMP_TMP  | A_FPLACE4 | 場所4      | （なし）                   |
| CONSUMP_TMP  | A_FPLACE5 | 場所5      | （なし）                   |
| CONSUMP_TMP  | DRWNO     | 部品番号   | （なし）                   |
| CONSUMP_TMP  | IMNM      | 品名       | （なし）                   |
| CONSUMP_TMP  | IMTYP     | 製品区分   | 0;製造品､1;購入品､2;外注品 |
| CONSUMP_TMP  | ISSUEQTY  | 出庫数     | （なし）                   |
| CONSUMP_TMP  | ITEM      | 品目       | （なし）                   |
| CONSUMP_TMP  | LOCT      | 入出庫場所 | （なし）                   |
| CONSUMP_TMP  | PHUNIT    | 員数       | （なし）                   |
| CONSUMP_TMP  | PROCESS   | 工程       | （なし）                   |
| CONSUMP_TMP  | PRORDERNO | オーダNo   | （なし）                   |
| CONSUMP_TMP  | RCISCD    | 入出庫区分 | （なし）                   |
| CONSUMP_TMP  | UNIT      | 単位       | （なし）                   |
| CONSUMP_TMP  | VENDOR    | 仕入先     | （なし）                   |

## テーブル: COST_SUMM_D

| テーブル名   | 列ID       | 列名               | 備考     |
|:-------------|:-----------|:-------------------|:---------|
| COST_SUMM_D  | ACT_P1     | 実際素材費         | （なし） |
| COST_SUMM_D  | ACT_P10    | 実際予備4          | （なし） |
| COST_SUMM_D  | ACT_P2     | 実際購入費         | （なし） |
| COST_SUMM_D  | ACT_P3     | 実際外注加工費     | （なし） |
| COST_SUMM_D  | ACT_P4     | 実際社内加工費     | （なし） |
| COST_SUMM_D  | ACT_P5     | 実際管理費         | （なし） |
| COST_SUMM_D  | ACT_P6     | 実際支給費         | （なし） |
| COST_SUMM_D  | ACT_P7     | 実際予備1          | （なし） |
| COST_SUMM_D  | ACT_P8     | 実際予備2          | （なし） |
| COST_SUMM_D  | ACT_P9     | 実際予備3          | （なし） |
| COST_SUMM_D  | ACT_PS_TTL | 実際積上合計       | （なし） |
| COST_SUMM_D  | ACT_PS1    | 実際積上素材費     | （なし） |
| COST_SUMM_D  | ACT_PS10   | 実際積上予備4      | （なし） |
| COST_SUMM_D  | ACT_PS2    | 実際積上購入費     | （なし） |
| COST_SUMM_D  | ACT_PS3    | 実際積上外注加工費 | （なし） |
| COST_SUMM_D  | ACT_PS4    | 実際積上社内加工費 | （なし） |
| COST_SUMM_D  | ACT_PS5    | 実際積上管理費     | （なし） |
| COST_SUMM_D  | ACT_PS6    | 実際積上支給費     | （なし） |
| COST_SUMM_D  | ACT_PS7    | 実際積上予備1      | （なし） |
| COST_SUMM_D  | ACT_PS8    | 実際積上予備2      | （なし） |
| COST_SUMM_D  | ACT_PS9    | 実際積上予備3      | （なし） |
| COST_SUMM_D  | CALDATE    | 指定日             | （なし） |
| COST_SUMM_D  | ITEM       | 品目               | （なし） |
| COST_SUMM_D  | PROCESS    | 工程               | （なし） |
| COST_SUMM_D  | STD_P1     | 標準素材費         | （なし） |
| COST_SUMM_D  | STD_P10    | 標準予備4          | （なし） |
| COST_SUMM_D  | STD_P2     | 標準購入費         | （なし） |
| COST_SUMM_D  | STD_P3     | 標準外注加工費     | （なし） |
| COST_SUMM_D  | STD_P4     | 標準社内加工費     | （なし） |
| COST_SUMM_D  | STD_P5     | 標準管理費         | （なし） |
| COST_SUMM_D  | STD_P6     | 標準支給費         | （なし） |
| COST_SUMM_D  | STD_P7     | 標準予備1          | （なし） |
| COST_SUMM_D  | STD_P8     | 標準予備2          | （なし） |
| COST_SUMM_D  | STD_P9     | 標準予備3          | （なし） |
| COST_SUMM_D  | STD_PS_TTL | 標準積上合計       | （なし） |
| COST_SUMM_D  | STD_PS1    | 標準積上素材費     | （なし） |
| COST_SUMM_D  | STD_PS10   | 標準積上予備4      | （なし） |
| COST_SUMM_D  | STD_PS2    | 標準積上購入費     | （なし） |
| COST_SUMM_D  | STD_PS3    | 標準積上外注加工費 | （なし） |
| COST_SUMM_D  | STD_PS4    | 標準積上社内加工費 | （なし） |
| COST_SUMM_D  | STD_PS5    | 標準積上管理費     | （なし） |
| COST_SUMM_D  | STD_PS6    | 標準積上支給費     | （なし） |
| COST_SUMM_D  | STD_PS7    | 標準積上予備1      | （なし） |
| COST_SUMM_D  | STD_PS8    | 標準積上予備2      | （なし） |
| COST_SUMM_D  | STD_PS9    | 標準積上予備3      | （なし） |
| COST_SUMM_D  | VENDOR     | 仕入先             | （なし） |

## テーブル: COST_TREE

| テーブル名   | 列ID          | 列名               | 備考                                        |
|:-------------|:--------------|:-------------------|:--------------------------------------------|
| COST_TREE    | A_FMCUS       | 代表得意先         | （なし）                                    |
| COST_TREE    | A_FPTYPE      | 購入区分           | R;固定自給;Y;有償支給;N;無償支給;G;変動自給 |
| COST_TREE    | A_SUPPLIER    | 供給者             | 有償支給の供給者                            |
| COST_TREE    | A_VENDOR      | 発注先             | 購入品、外注品の発注先                      |
| COST_TREE    | ACT_P1        | 実際素材費         | （なし）                                    |
| COST_TREE    | ACT_P10       | 実際予備4          | （なし）                                    |
| COST_TREE    | ACT_P2        | 実際購入費         | （なし）                                    |
| COST_TREE    | ACT_P3        | 実際外注加工費     | （なし）                                    |
| COST_TREE    | ACT_P4        | 実際社内加工費     | （なし）                                    |
| COST_TREE    | ACT_P5        | 実際管理費         | （なし）                                    |
| COST_TREE    | ACT_P6        | 実際支給費         | （なし）                                    |
| COST_TREE    | ACT_P7        | 実際予備1          | （なし）                                    |
| COST_TREE    | ACT_P8        | 実際予備2          | （なし）                                    |
| COST_TREE    | ACT_P9        | 実際予備3          | （なし）                                    |
| COST_TREE    | ACT_PS_TTL    | 実際積上合計       | （なし）                                    |
| COST_TREE    | ACT_PS1       | 実際積上素材費     | （なし）                                    |
| COST_TREE    | ACT_PS10      | 実際積上予備4      | （なし）                                    |
| COST_TREE    | ACT_PS2       | 実際積上購入費     | （なし）                                    |
| COST_TREE    | ACT_PS3       | 実際積上外注加工費 | （なし）                                    |
| COST_TREE    | ACT_PS4       | 実際積上社内加工費 | （なし）                                    |
| COST_TREE    | ACT_PS5       | 実際積上管理費     | （なし）                                    |
| COST_TREE    | ACT_PS6       | 実際積上支給費     | （なし）                                    |
| COST_TREE    | ACT_PS7       | 実際積上予備1      | （なし）                                    |
| COST_TREE    | ACT_PS8       | 実際積上予備2      | （なし）                                    |
| COST_TREE    | ACT_PS9       | 実際積上予備3      | （なし）                                    |
| COST_TREE    | CALDATE       | 指定日             | （なし）                                    |
| COST_TREE    | ITEM          | 品目               | （なし）                                    |
| COST_TREE    | LEVELD        | 展開レベル         | （なし）                                    |
| COST_TREE    | LINED         | ライン             | （なし）                                    |
| COST_TREE    | PHUNIT        | 構成数             | （なし）                                    |
| COST_TREE    | PRDCT_ITEM    | 対象品目           | （なし）                                    |
| COST_TREE    | PRDCT_PROCESS | 対象品目工程       | （なし）                                    |
| COST_TREE    | PROCESS       | 工程               | （なし）                                    |
| COST_TREE    | RECORD_ID     | レコードID         | （なし）                                    |
| COST_TREE    | SALE_PRICE    | 売単価             | （なし）                                    |
| COST_TREE    | STD_P1        | 標準素材費         | （なし）                                    |
| COST_TREE    | STD_P10       | 標準予備4          | （なし）                                    |
| COST_TREE    | STD_P2        | 標準購入費         | （なし）                                    |
| COST_TREE    | STD_P3        | 標準外注加工費     | （なし）                                    |
| COST_TREE    | STD_P4        | 標準社内加工費     | （なし）                                    |
| COST_TREE    | STD_P5        | 標準管理費         | （なし）                                    |
| COST_TREE    | STD_P6        | 標準支給費         | （なし）                                    |
| COST_TREE    | STD_P7        | 標準予備1          | （なし）                                    |
| COST_TREE    | STD_P8        | 標準予備2          | （なし）                                    |
| COST_TREE    | STD_P9        | 標準予備3          | （なし）                                    |
| COST_TREE    | STD_PS_TTL    | 標準積上合計       | （なし）                                    |
| COST_TREE    | STD_PS1       | 標準積上素材費     | （なし）                                    |
| COST_TREE    | STD_PS10      | 標準積上予備4      | （なし）                                    |
| COST_TREE    | STD_PS2       | 標準積上購入費     | （なし）                                    |
| COST_TREE    | STD_PS3       | 標準積上外注加工費 | （なし）                                    |
| COST_TREE    | STD_PS4       | 標準積上社内加工費 | （なし）                                    |
| COST_TREE    | STD_PS5       | 標準積上管理費     | （なし）                                    |
| COST_TREE    | STD_PS6       | 標準積上支給費     | （なし）                                    |
| COST_TREE    | STD_PS7       | 標準積上予備1      | （なし）                                    |
| COST_TREE    | STD_PS8       | 標準積上予備2      | （なし）                                    |
| COST_TREE    | STD_PS9       | 標準積上予備3      | （なし）                                    |
| COST_TREE    | TRANSACTOR    | 取引先             | （なし）                                    |
| COST_TREE    | VENDOR        | 仕入先             | （なし）                                    |

## テーブル: COST_TREE_MAIN

| テーブル名     | 列ID       | 列名     | 備考                   |
|:---------------|:-----------|:---------|:-----------------------|
| COST_TREE_MAIN | APPLYDATE  | 適用日   | （なし）               |
| COST_TREE_MAIN | ITEM       | 品目     | （なし）               |
| COST_TREE_MAIN | PROCESS    | 工程     | （なし）               |
| COST_TREE_MAIN | SPFLAG     | 売買区分 | S;売上単価;P; 仕入単価 |
| COST_TREE_MAIN | TRANSACTOR | 取引先   | （なし）               |
| COST_TREE_MAIN | VENDOR     | 仕入先   | （なし）               |

## テーブル: CSTM_CSTOD

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| CSTM_CSTOD   | CUSTOM   | 顧客コード   | （なし） |
| CSTM_CSTOD   | CUSTOMNM | 顧客名       | （なし） |
| CSTM_CSTOD   | ODFILE   | 受注ファイル | （なし） |

## テーブル: CSTM_CSTOD_ADD

| テーブル名     | 列ID      | 列名             | 備考     |
|:---------------|:----------|:-----------------|:---------|
| CSTM_CSTOD_ADD | ADDODFILE | 追加受注ファイル | （なし） |
| CSTM_CSTOD_ADD | CUSTOM    | 顧客コード       | （なし） |
| CSTM_CSTOD_ADD | CUSTOMNM  | 顧客名           | （なし） |

## テーブル: CUSTOMORDER

| テーブル名   | 列ID         | 列名                 | 備考                                  |
|:-------------|:-------------|:---------------------|:--------------------------------------|
| CUSTOMORDER  | A_CARD_FLG   | カード区分           | （なし）                              |
| CUSTOMORDER  | A_COLOR      | 色指示コード         | （なし）                              |
| CUSTOMORDER  | A_EDI_F      | EDI取込F             | 0;EDI以外;1;YMC20L;2;MORIC;3;YMC01    |
| CUSTOMORDER  | A_ODRCD      | 発注方針コード       | （なし）                              |
| CUSTOMORDER  | A_PACKCD     | 荷姿コード           | （なし）                              |
| CUSTOMORDER  | A_PACKNM     | 荷姿名称             | （なし）                              |
| CUSTOMORDER  | A_PACKQTY    | 荷姿収容数           | （なし）                              |
| CUSTOMORDER  | A_PROCESS    | 工程番号             | （なし）                              |
| CUSTOMORDER  | A_STATUS     | 生試区分             | （なし）                              |
| CUSTOMORDER  | A_SUPPLIER   | 供給者               | （なし）                              |
| CUSTOMORDER  | A_SUPPLIERNM | 供給者名称           | （なし）                              |
| CUSTOMORDER  | A_USER       | 使用者               | （なし）                              |
| CUSTOMORDER  | A_USERNM     | 使用者名称           | （なし）                              |
| CUSTOMORDER  | ADDFLG       | 追加Ｆ               | 0;通常;1;追加                         |
| CUSTOMORDER  | ALLOCNO      | 引当受注No           | （なし）                              |
| CUSTOMORDER  | AMOUNT       | 受注金額             | （なし）                              |
| CUSTOMORDER  | ASTARTDATE   | 先行着手可能日       | （なし）                              |
| CUSTOMORDER  | BKTNO        | 受注読込バケット年No | （なし）                              |
| CUSTOMORDER  | BKTYEAR      | 受注読込バケット年   | （なし）                              |
| CUSTOMORDER  | CMPFLG       | 出荷完了             | 0;未完了;1;完了                       |
| CUSTOMORDER  | CUSTOM       | 顧客                 | （なし）                              |
| CUSTOMORDER  | CUSTOMIMNM   | 顧客品名             | （なし）                              |
| CUSTOMORDER  | CUSTOMITEM   | 顧客品目             | （なし）                              |
| CUSTOMORDER  | CUSTOMNO     | 顧客注番             | （なし）                              |
| CUSTOMORDER  | DELIDATE     | 顧客納期             | （なし）                              |
| CUSTOMORDER  | DELILT       | 顧客納入L/T（日）    | （なし）                              |
| CUSTOMORDER  | DELITIME     | 納入時間(時)         | （なし）                              |
| CUSTOMORDER  | DEMANDNO     | 社内注番             | （なし）                              |
| CUSTOMORDER  | INVOICENO    | 納品書番号           | （なし）                              |
| CUSTOMORDER  | ITEM         | 品目                 | （なし）                              |
| CUSTOMORDER  | LATE_F       | 遅延F                | 0;遅延ではない;1;遅延                 |
| CUSTOMORDER  | LOCT         | 納入プラットフォーム | （なし）                              |
| CUSTOMORDER  | OFFCLF       | 確定/内示Ｆ          | 0;内示;1;確定                         |
| CUSTOMORDER  | ORDERCL      | 受注区分             | 0;新規;-1;受注取消                    |
| CUSTOMORDER  | ORDERQTY     | 受注数               | （なし）                              |
| CUSTOMORDER  | PER_F        | パー割F              | （なし）                              |
| CUSTOMORDER  | PRDCTQTY     | 生産指示数           | （なし）                              |
| CUSTOMORDER  | PRNFLG       | 出荷指示書印刷F      | 0;印刷未完了;1;印刷完了               |
| CUSTOMORDER  | PROCESS      | 工程                 | （なし）                              |
| CUSTOMORDER  | RCORDERNO    | 受注No               | （なし）                              |
| CUSTOMORDER  | REMARK       | 備考                 | （なし）                              |
| CUSTOMORDER  | REPDELIDATE  | 回答納期             | （なし）                              |
| CUSTOMORDER  | RORDERDATE   | 受注日               | （なし）                              |
| CUSTOMORDER  | SCHCOMPDATE  | 出荷予定日           | 納期を顧客納入L/Tでオフセットした日付 |
| CUSTOMORDER  | SHIPDATE     | 最終出荷日           | （なし）                              |
| CUSTOMORDER  | SHIPQTY      | 出荷数               | （なし）                              |
| CUSTOMORDER  | STARTDATE    | 着手可能日           | （なし）                              |
| CUSTOMORDER  | STOCKALLOC   | 在庫引当数           | （なし）                              |
| CUSTOMORDER  | UNITPRICE    | 受注単価             | （なし）                              |
| CUSTOMORDER  | UPDTD        | 更新日               | （なし）                              |
| CUSTOMORDER  | UPDTWKCD     | 更新担当者           | （なし）                              |
| CUSTOMORDER  | URGENCYFLG   | 山積用特急F          | 0;通常;1;特急;2;超特急                |
| CUSTOMORDER  | VENDOR       | 仕入先               | （なし）                              |

## テーブル: CUSTOMORDER_NEW

| テーブル名      | 列ID       | 列名                 | 備考                                                                                                                       |
|:----------------|:-----------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------|
| CUSTOMORDER_NEW | ASTARTDATE | 先行着手可能日       | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | CUSTOM     | 顧客                 | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | CUSTOMIMNM | 顧客品名             | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | CUSTOMITEM | 顧客品目             | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | CUSTOMNO   | 顧客注番             | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | DELIDATE   | 顧客納期             | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | DELITIME   | 納入時間(時)         | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | DEMANDNO   | 社内注番             | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | ITEM       | 品目                 | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | LOCT       | 納入プラットフォーム | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | MOVELV     | 移動LV               | 0;前後倒し;1;前倒し第２優先;2;前倒し第１優先;10;先行ありで前後倒し;11;先行ありで前倒し第２優先;12;先行ありで前倒し第１優先 |
| CUSTOMORDER_NEW | OFFCLF     | 確定/内示Ｆ          | 0;内示;1;確定                                                                                                              |
| CUSTOMORDER_NEW | ORDERQTY   | 受注数               | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | PRDCTBNO   | 枝番                 | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | PRDCTNO    | 製番                 | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | PROCESS    | 工程                 | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | RGSTD      | 登録日               | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | RORDERDATE | 受注日               | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | SNO        | 連番                 | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | SORT1      | 山積用ソート１       | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | SORT2      | 山積用ソート２       | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | SORT3      | 山積用ソート３       | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | STARTDATE  | 着手可能日           | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | TMPWRITEF  | 書込みF（TMP）       | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | UNITPRICE  | 受注単価             | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | UPDTD      | 更新日               | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | UPDTWKCD   | 更新担当者           | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | URGENCYFLG | 山積用特急F          | 0;通常;1;特急;2;超特急                                                                                                     |
| CUSTOMORDER_NEW | VENDOR     | 仕入先               | （なし）                                                                                                                   |
| CUSTOMORDER_NEW | YMC_F      | ヤマハデータF        | （なし）                                                                                                                   |

## テーブル: CUSTOMORDER_TXT

| テーブル名      | 列ID       | 列名           | 備考                                                                                                                       |
|:----------------|:-----------|:---------------|:---------------------------------------------------------------------------------------------------------------------------|
| CUSTOMORDER_TXT | ASTARTDATE | 先行着手可能日 | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | CUSTOMIMNM | 顧客品名       | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | CUSTOMITEM | 顧客品目       | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | CUSTOMNO   | 顧客注番       | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | DELIDATE   | 顧客納期       | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | DELITIME   | 納入時間(時)   | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | DEMANDNO   | 社内注番       | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | ITEM       | 品目           | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | MOVELV     | 移動LV         | 0;前後倒し;1;前倒し第２優先;2;前倒し第１優先;10;先行ありで前後倒し;11;先行ありで前倒し第２優先;12;先行ありで前倒し第１優先 |
| CUSTOMORDER_TXT | OFFCLF     | 確定/内示Ｆ    | 0;内示;1;確定                                                                                                              |
| CUSTOMORDER_TXT | ORDERCL    | 受注区分       | 0;新規;-1;受注取消                                                                                                         |
| CUSTOMORDER_TXT | ORDERQTY   | 受注数         | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | PRDCTBNO   | 枝番           | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | PRDCTNO    | 製番           | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | RORDERDATE | 受注日         | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | SORT1      | 山積用ソート１ | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | SORT2      | 山積用ソート２ | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | SORT3      | 山積用ソート３ | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | STARTDATE  | 着手可能日     | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | UNITPRICE  | 受注単価       | （なし）                                                                                                                   |
| CUSTOMORDER_TXT | URGENCYFLG | 山積用特急F    | 0;"通常";1;"特急";2;"超特急"                                                                                               |

## テーブル: D_ADDERR

| テーブル名   | 列ID        | 列名                         | 備考               |
|:-------------|:------------|:-----------------------------|:-------------------|
| D_ADDERR     | CANCELERR   | 受注情報にない削除情報       | （なし）           |
| D_ADDERR     | DELIDATEERR | 納期未入力                   | （なし）           |
| D_ADDERR     | DEMANDNO    | 社内注番                     | （なし）           |
| D_ADDERR     | DEPERR      | 既に、登録されている受注情報 | （なし）           |
| D_ADDERR     | ITEM        | 品目                         | （なし）           |
| D_ADDERR     | ITEMERR     | 品目無                       | （なし）           |
| D_ADDERR     | K_NO        | キー項目                     | （なし）           |
| D_ADDERR     | ORDERCL     | 受注区分                     | 0;新規;-1;受注取消 |
| D_ADDERR     | ORDERCLERR  | 受注区分　０・－１以外       | （なし）           |
| D_ADDERR     | ORDERQTYERR | 受注数<=0                    | （なし）           |
| D_ADDERR     | PRDCTERR    | 生産確定済受注               | （なし）           |
| D_ADDERR     | PRDCTNOERR  | 製番無・枝番有               | （なし）           |

## テーブル: D_ADDERR2

| テーブル名   | 列ID     | 列名     | 備考     |
|:-------------|:---------|:---------|:---------|
| D_ADDERR2    | DEMANDNO | 社内注番 | （なし） |
| D_ADDERR2    | ITEM     | 品目     | （なし） |
| D_ADDERR2    | K_NO     | キー項目 | （なし） |

## テーブル: D_ADDERR3

| テーブル名   | 列ID     | 列名     | 備考     |
|:-------------|:---------|:---------|:---------|
| D_ADDERR3    | DEMANDNO | 社内注番 | （なし） |
| D_ADDERR3    | ITEM     | 品目     | （なし） |
| D_ADDERR3    | K_NO     | キー項目 | （なし） |
| D_ADDERR3    | PRDCTBNO | 枝番     | （なし） |
| D_ADDERR3    | PRDCTNO  | 製番     | （なし） |

## テーブル: D_ADDPRDCT

| テーブル名   | 列ID      | 列名                       | 備考                                                                                                                                 |
|:-------------|:----------|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| D_ADDPRDCT   | ACTFNDATE | 完了日                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | ACTFNTIME | 完了時間(時分)             | （なし）                                                                                                                             |
| D_ADDPRDCT   | ACTSTDATE | 開始日                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | ACTSTTIME | 開始時間(時分)             | （なし）                                                                                                                             |
| D_ADDPRDCT   | BKTNO     | バケットNo                 | （なし）                                                                                                                             |
| D_ADDPRDCT   | BKTYEAR   | バケット年                 | （なし）                                                                                                                             |
| D_ADDPRDCT   | CMPFLG    | 完了Ｆ                     | 0;未完了;1;完了                                                                                                                      |
| D_ADDPRDCT   | CMPQTY    | 完成数                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | CYCLETIME | サイクルタイム(秒)         | （なし）                                                                                                                             |
| D_ADDPRDCT   | FNDATE    | 完了予定日                 | （なし）                                                                                                                             |
| D_ADDPRDCT   | FNTIME    | 完了予定時間(時分)         | （なし）                                                                                                                             |
| D_ADDPRDCT   | ITEM      | 品目                       | （なし）                                                                                                                             |
| D_ADDPRDCT   | LEVELD    | ﾚﾍﾞﾙ                       | （なし）                                                                                                                             |
| D_ADDPRDCT   | LINED     | 指示ライン                 | （なし）                                                                                                                             |
| D_ADDPRDCT   | MRPLOSS   | 展開ロス量                 | （なし）                                                                                                                             |
| D_ADDPRDCT   | OFFCLF    | 確定/内示Ｆ                | 0;内示;1;確定                                                                                                                        |
| D_ADDPRDCT   | PERMFLG   | 追加許可F                  | 0;指示追加しない;-1;指示追加する                                                                                                     |
| D_ADDPRDCT   | PLANDATE  | 指示日                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | PRDCTBNO  | 枝番                       | （なし）                                                                                                                             |
| D_ADDPRDCT   | PRDCTCTRL | 製番管理Ｆ                 | 0;オーダ管理(すべての受注に対して作業指示作成);1;製番管理(確定受注に対して作業指示作成);2;製番管理(すべての受注に対して作業指示作成) |
| D_ADDPRDCT   | PRDCTMANH | 人稼働時間（人時）         | （なし）                                                                                                                             |
| D_ADDPRDCT   | PRDCTNO   | 製番                       | （なし）                                                                                                                             |
| D_ADDPRDCT   | PRDCTQTY  | 指示数                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | PRDCTSQ   | 順序                       | （なし）                                                                                                                             |
| D_ADDPRDCT   | PRDCTTIME | 稼働時間(分)               | （なし）                                                                                                                             |
| D_ADDPRDCT   | PROCESS   | 工程                       | （なし）                                                                                                                             |
| D_ADDPRDCT   | REQQTY    | 必要数                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | SCHLOSS   | 指示ロス量                 | （なし）                                                                                                                             |
| D_ADDPRDCT   | SCRPQTY   | 不良数                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | SETUPMANH | 人段取時間（人時）         | （なし）                                                                                                                             |
| D_ADDPRDCT   | SETUPTIME | 段取時間(分)               | （なし）                                                                                                                             |
| D_ADDPRDCT   | SQNO      | 連番                       | （なし）                                                                                                                             |
| D_ADDPRDCT   | STTM      | 開始予定時間(分)           | （なし）                                                                                                                             |
| D_ADDPRDCT   | STTMA     | 開始予定時間(相対時間(分)) | （なし）                                                                                                                             |
| D_ADDPRDCT   | UPDTD     | 更新日                     | （なし）                                                                                                                             |
| D_ADDPRDCT   | UPDTWKCD  | 更新担当者                 | （なし）                                                                                                                             |
| D_ADDPRDCT   | VENDOR    | 仕入先                     | （なし）                                                                                                                             |

## テーブル: D_BUCKET

| テーブル名   | 列ID   | 列名           | 備考     |
|:-------------|:-------|:---------------|:---------|
| D_BUCKET     | BEAF_F | 期間指定F      | （なし） |
| D_BUCKET     | BKTSTD | バケット開始日 | （なし） |

## テーブル: D_CUSTOMORDER

| テーブル名    | 列ID        | 列名              | 備考                                  |
|:--------------|:------------|:------------------|:--------------------------------------|
| D_CUSTOMORDER | ADDFLG      | 追加Ｆ            | 0;通常;1;追加                         |
| D_CUSTOMORDER | ALLOCNO     | 引当受注No        | （なし）                              |
| D_CUSTOMORDER | AMOUNT      | 受注金額          | （なし）                              |
| D_CUSTOMORDER | ASTARTDATE  | 先行着手可能日    | （なし）                              |
| D_CUSTOMORDER | BLOCKREGFLG | 一括登録F         | 0;しない;1;する                       |
| D_CUSTOMORDER | CMPFLG      | 出荷完了          | 0;未完了;1;完了                       |
| D_CUSTOMORDER | CUSTOM      | 顧客              | （なし）                              |
| D_CUSTOMORDER | CUSTOMIMNM  | 顧客品名          | （なし）                              |
| D_CUSTOMORDER | CUSTOMITEM  | 顧客品目          | （なし）                              |
| D_CUSTOMORDER | CUSTOMNO    | 顧客注番          | （なし）                              |
| D_CUSTOMORDER | DELIDATE    | 顧客納期          | （なし）                              |
| D_CUSTOMORDER | DELILT      | 顧客納入L/T（日） | （なし）                              |
| D_CUSTOMORDER | DELITIME    | 納入時間(時)      | （なし）                              |
| D_CUSTOMORDER | DEMANDNO    | 社内注番          | （なし）                              |
| D_CUSTOMORDER | ITEM        | 品目              | （なし）                              |
| D_CUSTOMORDER | OFFCLF      | 確定/内示Ｆ       | 0;内示;1;確定                         |
| D_CUSTOMORDER | ORDERCL     | 受注区分          | 0;新規;-1;受注取消                    |
| D_CUSTOMORDER | ORDERQTY    | 受注数            | （なし）                              |
| D_CUSTOMORDER | PRDCTQTY    | 生産指示数        | （なし）                              |
| D_CUSTOMORDER | PRNFLG      | 出荷指示書印刷F   | 0;印刷未完了;1;印刷完了               |
| D_CUSTOMORDER | PROCESS     | 工程              | （なし）                              |
| D_CUSTOMORDER | RCORDERNO   | 受注No            | （なし）                              |
| D_CUSTOMORDER | REPDELIDATE | 回答納期          | （なし）                              |
| D_CUSTOMORDER | RORDERDATE  | 受注日            | （なし）                              |
| D_CUSTOMORDER | SCHCOMPDATE | 出荷予定日        | 納期を顧客納入L/Tでオフセットした日付 |
| D_CUSTOMORDER | SHIPDATE    | 最終出荷日        | （なし）                              |
| D_CUSTOMORDER | SHIPQTY     | 出荷数            | （なし）                              |
| D_CUSTOMORDER | STARTDATE   | 着手可能日        | （なし）                              |
| D_CUSTOMORDER | STOCKALLOC  | 在庫引当数        | （なし）                              |
| D_CUSTOMORDER | TMPSHIPDATE | 分納日(TMP)       | （なし）                              |
| D_CUSTOMORDER | TMPSHIPQTY  | 分納数(TMP)       | （なし）                              |
| D_CUSTOMORDER | TMPSHIPTIME | 分納時間(TMP)     | （なし）                              |
| D_CUSTOMORDER | TMPWOKERCD  | 担当者(TMP)       | （なし）                              |
| D_CUSTOMORDER | UNITPRICE   | 受注単価          | （なし）                              |
| D_CUSTOMORDER | UPDTD       | 更新日            | （なし）                              |
| D_CUSTOMORDER | UPDTWKCD    | 更新担当者        | （なし）                              |
| D_CUSTOMORDER | URGENCYFLG  | 山積用特急F       | 0;通常;1;特急;2;超特急                |
| D_CUSTOMORDER | VENDOR      | 仕入先            | （なし）                              |

## テーブル: D_ERR

| テーブル名   | 列ID        | 列名                         | 備考               |
|:-------------|:------------|:-----------------------------|:-------------------|
| D_ERR        | CANCELERR   | 受注情報にない削除情報       | （なし）           |
| D_ERR        | DELIDATEERR | 納期未入力                   | （なし）           |
| D_ERR        | DEMANDNO    | 社内注番                     | （なし）           |
| D_ERR        | DEPERR      | 既に、登録されている受注情報 | （なし）           |
| D_ERR        | ITEM        | 品目                         | （なし）           |
| D_ERR        | ITEMERR     | 品目無                       | （なし）           |
| D_ERR        | K_NO        | キー項目                     | （なし）           |
| D_ERR        | ORDERCL     | 受注区分                     | 0;新規;-1;受注取消 |
| D_ERR        | ORDERCLERR  | 受注区分　０・－１以外       | （なし）           |
| D_ERR        | ORDERQTYERR | 受注数<=0                    | （なし）           |
| D_ERR        | PRDCTERR    | 生産確定済受注               | （なし）           |
| D_ERR        | PRDCTNOERR  | 製番無・枝番有               | （なし）           |

## テーブル: D_ERR2

| テーブル名   | 列ID     | 列名     | 備考     |
|:-------------|:---------|:---------|:---------|
| D_ERR2       | DEMANDNO | 社内注番 | （なし） |
| D_ERR2       | ITEM     | 品目     | （なし） |
| D_ERR2       | K_NO     | キー項目 | （なし） |

## テーブル: D_ERR3

| テーブル名   | 列ID     | 列名     | 備考     |
|:-------------|:---------|:---------|:---------|
| D_ERR3       | DEMANDNO | 社内注番 | （なし） |
| D_ERR3       | ITEM     | 品目     | （なし） |
| D_ERR3       | K_NO     | キー項目 | （なし） |
| D_ERR3       | PRDCTBNO | 枝番     | （なし） |
| D_ERR3       | PRDCTNO  | 製番     | （なし） |

## テーブル: D_MPS

| テーブル名   | 列ID         | 列名               | 備考                                                                                                                       |
|:-------------|:-------------|:-------------------|:---------------------------------------------------------------------------------------------------------------------------|
| D_MPS        | ADDFLG       | 追加Ｆ             | 0;通常;1;追加                                                                                                              |
| D_MPS        | ASTARTDATE   | 先行着手可能日     | （なし）                                                                                                                   |
| D_MPS        | BKTNO        | 受注読込バケットNo | （なし）                                                                                                                   |
| D_MPS        | BKTYEAR      | 受注読込バケット年 | （なし）                                                                                                                   |
| D_MPS        | CHANGEDATE   | 変更納期           | （なし）                                                                                                                   |
| D_MPS        | CUSTOM       | 顧客               | （なし）                                                                                                                   |
| D_MPS        | DELAYPROCESS | 遅れ工程           | （なし）                                                                                                                   |
| D_MPS        | ITEM         | 品目               | （なし）                                                                                                                   |
| D_MPS        | MOVELV       | 移動LV             | 0;前後倒し;1;前倒し第２優先;2;前倒し第１優先;10;先行ありで前後倒し;11;先行ありで前倒し第２優先;12;先行ありで前倒し第１優先 |
| D_MPS        | MPSORDERNO   | オーダNo           | （なし）                                                                                                                   |
| D_MPS        | OFFCLF       | 確定/内示Ｆ        | 0;内示;1;確定                                                                                                              |
| D_MPS        | ORDERCL      | 受注区分           | 0;新規;-1;受注取消                                                                                                         |
| D_MPS        | ORDERQTY     | 受注数             | （なし）                                                                                                                   |
| D_MPS        | PBKTNO       | 生産確定バケットNo | （なし）                                                                                                                   |
| D_MPS        | PBKTYEAR     | 生産確定バケット年 | （なし）                                                                                                                   |
| D_MPS        | PLANDATE     | 計画納期           | （なし）                                                                                                                   |
| D_MPS        | PRDCTBNO     | 枝番               | （なし）                                                                                                                   |
| D_MPS        | PRDCTFLG     | 生産確定F          | 0;未確定;1;仕掛中;2;確定                                                                                                   |
| D_MPS        | PRDCTNO      | 製番               | （なし）                                                                                                                   |
| D_MPS        | PROCESS      | 工程               | （なし）                                                                                                                   |
| D_MPS        | PROGDATE     | 進捗日付           | 実績入力時、完了日をセット                                                                                                 |
| D_MPS        | PROGPROCESS  | 仕掛工程           | （なし）                                                                                                                   |
| D_MPS        | PROGTIME     | 進捗時刻           | 実績入力時、完了時間をセット                                                                                               |
| D_MPS        | RCORDERNO    | 受注No             | （なし）                                                                                                                   |
| D_MPS        | SORT1        | 山積用ソート１     | （なし）                                                                                                                   |
| D_MPS        | SORT2        | 山積用ソート２     | （なし）                                                                                                                   |
| D_MPS        | SORT3        | 山積用ソート３     | （なし）                                                                                                                   |
| D_MPS        | STARTDATE    | 着手可能日         | （なし）                                                                                                                   |
| D_MPS        | STATUS       | ステータス         | 0;未着手;1;着手;2;完了                                                                                                     |
| D_MPS        | UPDTD        | 更新日             | （なし）                                                                                                                   |
| D_MPS        | UPDTWKCD     | 更新担当者         | （なし）                                                                                                                   |
| D_MPS        | URGENCYFLG   | 山積用特急F        | 0;通常;1;特急;2;超特急                                                                                                     |
| D_MPS        | VENDOR       | 仕入先             | （なし）                                                                                                                   |

## テーブル: D_NEWERR

| テーブル名   | 列ID        | 列名                         | 備考               |
|:-------------|:------------|:-----------------------------|:-------------------|
| D_NEWERR     | CANCELERR   | 受注情報にない削除情報       | （なし）           |
| D_NEWERR     | DELIDATEERR | 納期未入力                   | （なし）           |
| D_NEWERR     | DEMANDNO    | 社内注番                     | （なし）           |
| D_NEWERR     | DEPERR      | 既に、登録されている受注情報 | （なし）           |
| D_NEWERR     | ITEM        | 品目                         | （なし）           |
| D_NEWERR     | ITEMERR     | 品目無                       | （なし）           |
| D_NEWERR     | K_NO        | キー項目                     | （なし）           |
| D_NEWERR     | ORDERCL     | 受注区分                     | 0;新規;-1;受注取消 |
| D_NEWERR     | ORDERCLERR  | 受注区分　０・－１以外       | （なし）           |
| D_NEWERR     | ORDERQTYERR | 受注数<=0                    | （なし）           |
| D_NEWERR     | PRDCTERR    | 生産確定済受注               | （なし）           |
| D_NEWERR     | PRDCTNOERR  | 製番無・枝番有               | （なし）           |

## テーブル: D_NEWERR2

| テーブル名   | 列ID     | 列名     | 備考     |
|:-------------|:---------|:---------|:---------|
| D_NEWERR2    | DEMANDNO | 社内注番 | （なし） |
| D_NEWERR2    | ITEM     | 品目     | （なし） |
| D_NEWERR2    | K_NO     | キー項目 | （なし） |

## テーブル: D_NEWERR3

| テーブル名   | 列ID     | 列名     | 備考     |
|:-------------|:---------|:---------|:---------|
| D_NEWERR3    | DEMANDNO | 社内注番 | （なし） |
| D_NEWERR3    | ITEM     | 品目     | （なし） |
| D_NEWERR3    | K_NO     | キー項目 | （なし） |
| D_NEWERR3    | PRDCTBNO | 枝番     | （なし） |
| D_NEWERR3    | PRDCTNO  | 製番     | （なし） |

## テーブル: D_ORDERNO

| テーブル名   | 列ID     | 列名             | 備考     |
|:-------------|:---------|:-----------------|:---------|
| D_ORDERNO    | ALPHNO   | 採番アルファ     | （なし） |
| D_ORDERNO    | K_NO     | キー項目         | （なし） |
| D_ORDERNO    | LAST_OD1 | 最終オーダNo     | （なし） |
| D_ORDERNO    | NEXT_OD1 | 次回オーダNo     | （なし） |
| D_ORDERNO    | NEXT_OD2 | 次回内示オーダNo | （なし） |

## テーブル: EDI_ADDERROR

| テーブル名   | 列ID        | 列名           | 備考                     |
|:-------------|:------------|:---------------|:-------------------------|
| EDI_ADDERROR | A_SUPPLIER  | 供給者         | 0;受注;1;支給            |
| EDI_ADDERROR | A_USER      | 使用者         | 0;受注;1;支給            |
| EDI_ADDERROR | CUSTOMITEM  | 品目           | 0;受注;1;支給            |
| EDI_ADDERROR | CUSTOMNO    | オーダーNo     | 0;受注;1;支給            |
| EDI_ADDERROR | DATA_KUBUN  | データ区分     | 0;受注;1;支給            |
| EDI_ADDERROR | DELIDATE    | 納期           | 0;受注;1;支給            |
| EDI_ADDERROR | DELITIME    | 納入時刻       | 0;受注;1;支給            |
| EDI_ADDERROR | IHARA       | メーカー       | イハラ自社の取引先コード |
| EDI_ADDERROR | ITEM        | 旧部品番号     | 0;受注;1;支給            |
| EDI_ADDERROR | ITEM_STATUS | 品目ステータス | 0;受注;1;支給            |
| EDI_ADDERROR | K_NO        | キー項目       | （なし）                 |
| EDI_ADDERROR | LOCT        | 納入先         | 0;受注;1;支給            |
| EDI_ADDERROR | ODFILE      | EDIファイル    | （なし）                 |
| EDI_ADDERROR | OFFCLF      | 確定/内示Ｆ    | 0;受注;1;支給            |
| EDI_ADDERROR | ORDERQTY    | 数量           | 0;受注;1;支給            |
| EDI_ADDERROR | PROCESS     | 工程           | 0;受注;1;支給            |
| EDI_ADDERROR | REMARK      | 備考           | 0;受注;1;支給            |
| EDI_ADDERROR | STATUS      | 生試区分       | 0;受注;1;支給            |
| EDI_ADDERROR | TRANSACTOR  | 顧客           | （なし）                 |

## テーブル: EDI_ERROR

| テーブル名   | 列ID        | 列名           | 備考                     |
|:-------------|:------------|:---------------|:-------------------------|
| EDI_ERROR    | A_SUPPLIER  | 供給者         | 0;受注;1;支給            |
| EDI_ERROR    | A_USER      | 使用者         | 0;受注;1;支給            |
| EDI_ERROR    | CUSTOMITEM  | 品目           | 0;受注;1;支給            |
| EDI_ERROR    | CUSTOMNO    | オーダーNo     | 0;受注;1;支給            |
| EDI_ERROR    | DATA_KUBUN  | データ区分     | 0;受注;1;支給            |
| EDI_ERROR    | DELIDATE    | 納期           | 0;受注;1;支給            |
| EDI_ERROR    | DELITIME    | 納入時刻       | 0;受注;1;支給            |
| EDI_ERROR    | IHARA       | メーカー       | イハラ自社の取引先コード |
| EDI_ERROR    | ITEM        | 旧部品番号     | 0;受注;1;支給            |
| EDI_ERROR    | ITEM_STATUS | 品目ステータス | 0;受注;1;支給            |
| EDI_ERROR    | K_NO        | キー項目       | （なし）                 |
| EDI_ERROR    | LOCT        | 納入先         | 0;受注;1;支給            |
| EDI_ERROR    | ODFILE      | EDIファイル    | （なし）                 |
| EDI_ERROR    | OFFCLF      | 確定/内示Ｆ    | 0;受注;1;支給            |
| EDI_ERROR    | ORDERQTY    | 数量           | 0;受注;1;支給            |
| EDI_ERROR    | PROCESS     | 工程           | 0;受注;1;支給            |
| EDI_ERROR    | REMARK      | 備考           | 0;受注;1;支給            |
| EDI_ERROR    | STATUS      | 生試区分       | 0;受注;1;支給            |
| EDI_ERROR    | TRANSACTOR  | 顧客           | （なし）                 |

## テーブル: EXERECORD

| テーブル名   | 列ID     | 列名             | 備考     |
|:-------------|:---------|:-----------------|:---------|
| EXERECORD    | ERRORMSG | エラーメッセージ | （なし） |
| EXERECORD    | EXENAME  | 実行処理名       | （なし） |
| EXERECORD    | PATHD    | フルパス         | （なし） |
| EXERECORD    | REMARKD  | 備考             | （なし） |
| EXERECORD    | RGSTD    | 登録日           | （なし） |
| EXERECORD    | TERMINAL | 端末情報         | （なし） |
| EXERECORD    | VER_NO   | バージョンNO     | （なし） |
| EXERECORD    | VERSIOND | バージョン情報   | （なし） |
| EXERECORD    | WKCD     | 担当者           | （なし） |

## テーブル: IMPLOSION_TXT

| テーブル名    | 列ID     | 列名        | 備考     |
|:--------------|:---------|:------------|:---------|
| IMPLOSION_TXT | A_VENDOR | 発注先      | （なし） |
| IMPLOSION_TXT | DRWNO    | 部品番号    | （なし） |
| IMPLOSION_TXT | EDDATE   | 失効日      | （なし） |
| IMPLOSION_TXT | ITEM     | 品目        | （なし） |
| IMPLOSION_TXT | LEVELD   | 展開レベル  | （なし） |
| IMPLOSION_TXT | LINED    | ライン      | （なし） |
| IMPLOSION_TXT | NO       | レコードNo. | （なし） |
| IMPLOSION_TXT | PHUNIT   | 数          | （なし） |
| IMPLOSION_TXT | PROCESS  | 工程        | （なし） |
| IMPLOSION_TXT | STDATE   | 発効日      | （なし） |
| IMPLOSION_TXT | VENDOR   | 仕入先      | （なし） |

## テーブル: INI_ISSUE_RECEIVE

| テーブル名        | 列ID                   | 列名                   | 備考     |
|:------------------|:-----------------------|:-----------------------|:---------|
| INI_ISSUE_RECEIVE | AO_CODE                | 入庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | AO_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | AO_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | CO_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | CO_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | CO_HCODE               | 親品目入庫区分初期値   | （なし） |
| INI_ISSUE_RECEIVE | CO_LCODE               | 子品目出庫区分初期値   | （なし） |
| INI_ISSUE_RECEIVE | IO_CODE                | 出庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | IO_CODE_TAB            | 出庫区分               | （なし） |
| INI_ISSUE_RECEIVE | IO_COST_TAB            | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | IO_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | IO_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | IO_DATE_TAB            | 出庫日                 | （なし） |
| INI_ISSUE_RECEIVE | IO_LOCT                | 出庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | IO_LOCT_TAB            | 出庫場所               | （なし） |
| INI_ISSUE_RECEIVE | IO_REMARKS_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | IO_TERMINALID          | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | IO_TERMINALID_TAB      | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | IO_WORKERID_TAB        | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | IP_CHEKINGREGISTRATION | 登録時メッセージ設定   | （なし） |
| INI_ISSUE_RECEIVE | IP_CODE                | 出庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | IP_CODE_TAB            | 出庫区分               | （なし） |
| INI_ISSUE_RECEIVE | IP_COST_TAB            | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | IP_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | IP_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | IP_DATE_TAB            | 出庫日                 | （なし） |
| INI_ISSUE_RECEIVE | IP_LOCT                | 出庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | IP_LOCT_TAB            | 出庫場所               | （なし） |
| INI_ISSUE_RECEIVE | IP_ONORDERINPUT        | オーダNo選択時の設定   | （なし） |
| INI_ISSUE_RECEIVE | IP_QUANTITY_TAB        | 出庫数                 | （なし） |
| INI_ISSUE_RECEIVE | IP_REMARKS_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | IP_TERMINALID          | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | IP_TERMINALID_TAB      | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | IP_WORKERID_TAB        | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | IPS_CODE               | 出庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | IPS_CODE_TAB           | 出庫区分               | （なし） |
| INI_ISSUE_RECEIVE | IPS_COST_TAB           | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | IPS_DATE_ED            | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | IPS_DATE_ST            | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | IPS_DATE_TAB           | 出庫日                 | （なし） |
| INI_ISSUE_RECEIVE | IPS_LOCT               | 出庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | IPS_LOCT_TAB           | 出庫場所               | （なし） |
| INI_ISSUE_RECEIVE | IPS_REMARKS_TAB        | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | IPS_TERMINALID         | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | IPS_TERMINALID_TAB     | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | IPS_WORKERID_TAB       | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | IS_CHEKINGREGISTRATION | 登録時メッセージ設定   | （なし） |
| INI_ISSUE_RECEIVE | IS_CODE                | 出庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | IS_CODE_TAB            | 出庫区分               | （なし） |
| INI_ISSUE_RECEIVE | IS_COST_TAB            | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | IS_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | IS_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | IS_DATE_TAB            | 出庫日                 | （なし） |
| INI_ISSUE_RECEIVE | IS_LOCT                | 出庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | IS_LOCT_TAB            | 出庫場所               | （なし） |
| INI_ISSUE_RECEIVE | IS_ONORDERINPUT        | オーダNo選択時の設定   | （なし） |
| INI_ISSUE_RECEIVE | IS_QUANTITY_TAB        | 出庫数                 | （なし） |
| INI_ISSUE_RECEIVE | IS_REMARKS_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | IS_TERMINALID          | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | IS_TERMINALID_TAB      | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | IS_WORKERID_TAB        | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | K_NO                   | キー項目               | （なし） |
| INI_ISSUE_RECEIVE | MV_RCISCD              | 移動元出庫区分初期値   | （なし） |
| INI_ISSUE_RECEIVE | MV_RCISCD2             | 移動先入庫区分初期値   | （なし） |
| INI_ISSUE_RECEIVE | PMV_DATE_ED            | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | PMV_DATE_ST            | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | PMV_ISSUEQTY_TAB       | 支給数                 | （なし） |
| INI_ISSUE_RECEIVE | PMV_LOCT_TAB           | 支給元（自社）タブ     | （なし） |
| INI_ISSUE_RECEIVE | PMV_LOCT2_TAB          | 支給先（外注）タブ     | （なし） |
| INI_ISSUE_RECEIVE | PMV_RCISCD             | 移動先入庫区分初期値   | （なし） |
| INI_ISSUE_RECEIVE | PMV_RCISCD_TAB         | 入出庫区分タブ         | （なし） |
| INI_ISSUE_RECEIVE | PMV_RCISCD2            | 移動元出庫区分初期値   | （なし） |
| INI_ISSUE_RECEIVE | PMV_RCISCD2_TAB        | 入庫区分（外注）タブ   | （なし） |
| INI_ISSUE_RECEIVE | PMV_RCISDATE_TAB       | 支給日                 | （なし） |
| INI_ISSUE_RECEIVE | PMV_REMARK_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | PMV_WORKERCD_TAB       | 担当者タブ             | （なし） |
| INI_ISSUE_RECEIVE | PP_CHEKINGREGISTRATION | 登録時メッセージ設定   | （なし） |
| INI_ISSUE_RECEIVE | PP_CODE                | 入庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | PP_CODE_TAB            | 入庫区分               | （なし） |
| INI_ISSUE_RECEIVE | PP_COST_TAB            | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | PP_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | PP_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | PP_DATE_TAB            | 入庫日                 | （なし） |
| INI_ISSUE_RECEIVE | PP_FINISHEDORDERALARM  | 入庫数＞発注数の警告   | （なし） |
| INI_ISSUE_RECEIVE | PP_LOCT                | 入庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | PP_LOCT_TAB            | 入庫場所               | （なし） |
| INI_ISSUE_RECEIVE | PP_ONORDERINPUT        | オーダNo選択時の設定   | （なし） |
| INI_ISSUE_RECEIVE | PP_QUANTITY            | 入庫数                 | （なし） |
| INI_ISSUE_RECEIVE | PP_QUANTITY_TAB        | 入庫数                 | （なし） |
| INI_ISSUE_RECEIVE | PP_REMARKS_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | PP_STARTDATE           | 支給品納入開始日       | （なし） |
| INI_ISSUE_RECEIVE | PP_TERMINALID          | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | PP_TERMINALID_TAB      | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | PP_WORKERID_TAB        | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | RO_CODE                | 入庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | RO_CODE_TAB            | 入庫区分               | （なし） |
| INI_ISSUE_RECEIVE | RO_COST_TAB            | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | RO_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | RO_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | RO_DATE_TAB            | 入庫日                 | （なし） |
| INI_ISSUE_RECEIVE | RO_LOCT                | 入庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | RO_LOCT_TAB            | 入庫場所               | （なし） |
| INI_ISSUE_RECEIVE | RO_REMARKS_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | RO_TERMINALID          | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | RO_TERMINALID_TAB      | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | RO_WORKERID_TAB        | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | RP_CHEKINGREGISTRATION | 登録時メッセージ設定   | （なし） |
| INI_ISSUE_RECEIVE | RP_CODE                | 入庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | RP_CODE_TAB            | 入庫区分               | （なし） |
| INI_ISSUE_RECEIVE | RP_COST_TAB            | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | RP_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | RP_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | RP_DATE_TAB            | 入庫日                 | （なし） |
| INI_ISSUE_RECEIVE | RP_FINISHEDORDERALARM  | 入庫数＞発注数の警告   | （なし） |
| INI_ISSUE_RECEIVE | RP_LOCT                | 入庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | RP_LOCT_TAB            | 入庫場所               | （なし） |
| INI_ISSUE_RECEIVE | RP_ONORDERINPUT        | オーダNo選択時の設定   | （なし） |
| INI_ISSUE_RECEIVE | RP_QUANTITY            | 入庫数                 | （なし） |
| INI_ISSUE_RECEIVE | RP_QUANTITY_TAB        | 入庫数                 | （なし） |
| INI_ISSUE_RECEIVE | RP_REMARKS_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | RP_STARTDATE           | 購入品納入開始日       | （なし） |
| INI_ISSUE_RECEIVE | RP_TERMINALID          | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | RP_TERMINALID_TAB      | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | RP_WORKERID_TAB        | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | RS_CHEKINGREGISTRATION | 登録時メッセージ設定   | （なし） |
| INI_ISSUE_RECEIVE | RS_CODE                | 入庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | RS_CODE_TAB            | 入庫区分               | （なし） |
| INI_ISSUE_RECEIVE | RS_COST_TAB            | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | RS_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | RS_DATE_ST             | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | RS_DATE_TAB            | 入庫日                 | （なし） |
| INI_ISSUE_RECEIVE | RS_FINISHEDORDERALARM  | 入庫数＞発注数の警告   | （なし） |
| INI_ISSUE_RECEIVE | RS_LCODE               | 消費品目出庫区分初期値 | （なし） |
| INI_ISSUE_RECEIVE | RS_LOCT                | 入庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | RS_LOCT_TAB            | 入庫場所               | （なし） |
| INI_ISSUE_RECEIVE | RS_ONORDERINPUT        | オーダNo選択時の設定   | （なし） |
| INI_ISSUE_RECEIVE | RS_QUANTITY            | 入庫数                 | （なし） |
| INI_ISSUE_RECEIVE | RS_QUANTITY_TAB        | 入庫数                 | （なし） |
| INI_ISSUE_RECEIVE | RS_REMARKS_TAB         | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | RS_STARTDATE           | 外注品納入開始日       | （なし） |
| INI_ISSUE_RECEIVE | RS_TERMINALID          | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | RS_TERMINALID_TAB      | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | RS_WORKERID_TAB        | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | RSR_CODE               | 入庫区分初期値         | （なし） |
| INI_ISSUE_RECEIVE | RSR_CODE_TAB           | 入庫区分               | （なし） |
| INI_ISSUE_RECEIVE | RSR_COST_TAB           | 単価                   | （なし） |
| INI_ISSUE_RECEIVE | RSR_DATE_ED            | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | RSR_DATE_ST            | 実績日入力制限開始期間 | （なし） |
| INI_ISSUE_RECEIVE | RSR_DATE_TAB           | 入庫日                 | （なし） |
| INI_ISSUE_RECEIVE | RSR_LOCT               | 入庫場所初期値         | （なし） |
| INI_ISSUE_RECEIVE | RSR_LOCT_TAB           | 入庫場所               | （なし） |
| INI_ISSUE_RECEIVE | RSR_REMARKS_TAB        | 備考                   | （なし） |
| INI_ISSUE_RECEIVE | RSR_TERMINALID         | 端末ＩＤ初期値         | （なし） |
| INI_ISSUE_RECEIVE | RSR_TERMINALID_TAB     | 端末ＩＤ               | （なし） |
| INI_ISSUE_RECEIVE | RSR_WORKERID_TAB       | 担当者                 | （なし） |
| INI_ISSUE_RECEIVE | SH_CODE                | 計画外出庫区分初期値   | （なし） |
| INI_ISSUE_RECEIVE | SH_DATE_ED             | 実績日入力制限終了期間 | （なし） |
| INI_ISSUE_RECEIVE | SH_DATE_ST             | 実績日入力制限開始期間 | （なし） |

## テーブル: INI_PRODUCTRESULT_ENTRY

| テーブル名              | 列ID                    | 列名                   | 備考     |
|:------------------------|:------------------------|:-----------------------|:---------|
| INI_PRODUCTRESULT_ENTRY | DR_ACTUALLINE           | 実績ライン初期値       | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_ACTUALLINE_TAB       | 実績ライン             | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_CHEKINGREGISTRATION  | 登録時確認             | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_CODE                 | 入庫区分初期値         | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_CODE_TAB             | 入出庫区分             | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_COMPLETEQUANTITY     | 完成数初期値           | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_COMPLETEQUANTITY_TAB | 完成数                 | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_DATE_TAB             | 生産開始日             | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_DEFECTQUANTITY_TAB   | 不良数                 | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_ENDTIME              | 生産終了時間入力       | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_ENDTIME_TAB          | 終了開始時間           | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_FINISHEDORDERALARM   | 生産数＞必要数の警告   | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_LCODE                | 消費品目出庫区分       | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_LOCT_TAB             | 入庫場所               | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_ONORDERINPUT         | オーダNo選択時の設定   | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_STARTDATE            | 生産開始日             | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_STARTDATE_ED         | 実績日入力制限終了期間 | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_STARTDATE_ST         | 実績日入力制限開始期間 | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_STARTTIME            | 生産開始時間入力       | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_STARTTIME_TAB        | 生産開始時間           | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_WORKERID_TAB         | 担当者                 | （なし） |
| INI_PRODUCTRESULT_ENTRY | DR_WORKERQUANTITY_TAB   | 生産人員数             | （なし） |
| INI_PRODUCTRESULT_ENTRY | K_NO                    | キー項目               | （なし） |

## テーブル: INI_SHIPPINGRESULT

| テーブル名         | 列ID                    | 列名                   | 備考     |
|:-------------------|:------------------------|:-----------------------|:---------|
| INI_SHIPPINGRESULT | K_NO                    | キー項目               | （なし） |
| INI_SHIPPINGRESULT | RE_CHEKINGREGISTRATION  | 登録時メッセージ設定   | （なし） |
| INI_SHIPPINGRESULT | RE_CODE                 | 入庫区分初期値         | （なし） |
| INI_SHIPPINGRESULT | RE_CODE_TAB             | 入庫区分               | （なし） |
| INI_SHIPPINGRESULT | RE_ONORDERINPUT         | オーダNo入力時設定     | （なし） |
| INI_SHIPPINGRESULT | RE_RECEIVEDATE_ED       | 実績日入力制限終了期間 | （なし） |
| INI_SHIPPINGRESULT | RE_RECEIVEDATE_ST       | 実績日入力制限開始期間 | （なし） |
| INI_SHIPPINGRESULT | RE_RECEIVEDATE_TAB      | 返品日                 | （なし） |
| INI_SHIPPINGRESULT | RE_RECEIVEQUANTITY_TAB  | 返品数                 | （なし） |
| INI_SHIPPINGRESULT | RE_RECEIVETIME_TAB      | 返品時間               | （なし） |
| INI_SHIPPINGRESULT | RE_WORKERID_TAB         | 担当者                 | （なし） |
| INI_SHIPPINGRESULT | SH_CHEKINGREGISTRATION  | 登録時メッセージ設定   | （なし） |
| INI_SHIPPINGRESULT | SH_CODE                 | 出庫区分初期値         | （なし） |
| INI_SHIPPINGRESULT | SH_CODE_TAB             | 出庫区分               | （なし） |
| INI_SHIPPINGRESULT | SH_FINISHEDORDERALARM   | 出荷数＞受注数の警告   | （なし） |
| INI_SHIPPINGRESULT | SH_LOCT                 | 出庫場所               | （なし） |
| INI_SHIPPINGRESULT | SH_LOCT_TAB             | 出庫場所               | （なし） |
| INI_SHIPPINGRESULT | SH_ONORDERINPUT         | オーダNo入力時設定     | （なし） |
| INI_SHIPPINGRESULT | SH_SHIPPINGDATE         | 分納日                 | （なし） |
| INI_SHIPPINGRESULT | SH_SHIPPINGDATE_ED      | 実績日入力制限終了期間 | （なし） |
| INI_SHIPPINGRESULT | SH_SHIPPINGDATE_ST      | 実績日入力制限開始期間 | （なし） |
| INI_SHIPPINGRESULT | SH_SHIPPINGDATE_TAB     | 分納日                 | （なし） |
| INI_SHIPPINGRESULT | SH_SHIPPINGQUANTITY     | 分納数初期値           | （なし） |
| INI_SHIPPINGRESULT | SH_SHIPPINGQUANTITY_TAB | 分納数                 | （なし） |
| INI_SHIPPINGRESULT | SH_SHIPPINGTIME_TAB     | 分納時間               | （なし） |
| INI_SHIPPINGRESULT | SH_WORKERID_TAB         | 担当者                 | （なし） |

## テーブル: INI_YMC20L

| テーブル名   | 列ID          | 列名              | 備考     |
|:-------------|:--------------|:------------------|:---------|
| INI_YMC20L   | K_NO          | キー              | （なし） |
| INI_YMC20L   | YMEC_READ_FLG | YMC-YMEC同時読込F | （なし） |

## テーブル: INVSTOCKNO_TREE

| テーブル名      | 列ID      | 列名   | 備考     |
|:----------------|:----------|:-------|:---------|
| INVSTOCKNO_TREE | INVDATE   | 棚卸日 | （なし） |
| INVSTOCKNO_TREE | INVNO1    | 棚番   | （なし） |
| INVSTOCKNO_TREE | INVNO2    | 棚番2  | （なし） |
| INVSTOCKNO_TREE | INVNO3    | 棚番3  | （なし） |
| INVSTOCKNO_TREE | INVNO4    | 棚番4  | （なし） |
| INVSTOCKNO_TREE | INVNO5    | 棚番5  | （なし） |
| INVSTOCKNO_TREE | ITEM      | 品目   | （なし） |
| INVSTOCKNO_TREE | LEVELD    | レベル | （なし） |
| INVSTOCKNO_TREE | OPERABLEF | 使用F  | （なし） |
| INVSTOCKNO_TREE | PLACE1    | 場所   | （なし） |
| INVSTOCKNO_TREE | PLACE2    | 場所2  | （なし） |
| INVSTOCKNO_TREE | PLACE3    | 場所3  | （なし） |
| INVSTOCKNO_TREE | PLACE4    | 場所4  | （なし） |
| INVSTOCKNO_TREE | PLACE5    | 場所5  | （なし） |
| INVSTOCKNO_TREE | PROCESS   | 工程   | （なし） |
| INVSTOCKNO_TREE | VENDOR    | 仕入先 | （なし） |

## テーブル: INVSTOCKTMP_TREE

| テーブル名       | 列ID       | 列名       | 備考     |
|:-----------------|:-----------|:-----------|:---------|
| INVSTOCKTMP_TREE | BOOKSTOCK  | 帳簿在庫   | （なし） |
| INVSTOCKTMP_TREE | DIFFERENCE | 在庫差異   | （なし） |
| INVSTOCKTMP_TREE | GROSQTY    | グロス在庫 | （なし） |
| INVSTOCKTMP_TREE | INVNO1     | 棚番1      | （なし） |
| INVSTOCKTMP_TREE | INVNO2     | 棚番2      | （なし） |
| INVSTOCKTMP_TREE | INVNO3     | 棚番3      | （なし） |
| INVSTOCKTMP_TREE | INVNO4     | 棚番4      | （なし） |
| INVSTOCKTMP_TREE | INVNO5     | 棚番5      | （なし） |
| INVSTOCKTMP_TREE | INVQTY     | 棚卸在庫数 | （なし） |
| INVSTOCKTMP_TREE | ITEM       | 品目       | （なし） |
| INVSTOCKTMP_TREE | LEVELD     | レベル     | （なし） |
| INVSTOCKTMP_TREE | OPERABLEF  | 使用F      | （なし） |
| INVSTOCKTMP_TREE | PHUNIT     | 員数       | （なし） |
| INVSTOCKTMP_TREE | PLACE1     | 場所1      | （なし） |
| INVSTOCKTMP_TREE | PLACE2     | 場所2      | （なし） |
| INVSTOCKTMP_TREE | PLACE3     | 場所3      | （なし） |
| INVSTOCKTMP_TREE | PLACE4     | 場所4      | （なし） |
| INVSTOCKTMP_TREE | PLACE5     | 場所5      | （なし） |
| INVSTOCKTMP_TREE | PROCESS    | 工程       | （なし） |
| INVSTOCKTMP_TREE | VENDOR     | 仕入先     | （なし） |

## テーブル: KOUSEI_CHK_LST

| テーブル名     | 列ID    | 列名       | 備考                                                                 |
|:---------------|:--------|:-----------|:---------------------------------------------------------------------|
| KOUSEI_CHK_LST | HINMOKU | 品目       | （なし）                                                             |
| KOUSEI_CHK_LST | KOUTEI  | 工程       | （なし）                                                             |
| KOUSEI_CHK_LST | MLOOP   | 無限ループ | 製品構成マスタの登録に誤りがあります。                               |
| KOUSEI_CHK_LST | SEIBAN  | 製番管理Ｆ | 工程条件マスタ、または品目マスタの製番管理Ｆの設定に誤りがあります。 |
| KOUSEI_CHK_LST | VENDOR  | 仕入先     | （なし）                                                             |

## テーブル: LAST_EDI_INFO

| テーブル名    | 列ID      | 列名        | 備考               |
|:--------------|:----------|:------------|:-------------------|
| LAST_EDI_INFO | CUSTOM    | 顧客        | （なし）           |
| LAST_EDI_INFO | DELIDATE  | 顧客納期    | （なし）           |
| LAST_EDI_INFO | ITEM      | 品目        | （なし）           |
| LAST_EDI_INFO | OFFCLF    | 確定/内示Ｆ | 0;内示;1;確定      |
| LAST_EDI_INFO | ORDERCL   | 受注区分    | 0;新規;-1;受注取消 |
| LAST_EDI_INFO | ORDERQTY  | 受注数      | （なし）           |
| LAST_EDI_INFO | PROCESS   | 工程        | （なし）           |
| LAST_EDI_INFO | RCORDERNO | 受注No      | （なし）           |
| LAST_EDI_INFO | RGSTD     | 登録日      | （なし）           |
| LAST_EDI_INFO | VENDOR    | 仕入先      | （なし）           |

## テーブル: LOGIX_J_BUNNOU

| テーブル名     | 列ID       | 列名       | 備考     |
|:---------------|:-----------|:-----------|:---------|
| LOGIX_J_BUNNOU | BUNNOUDAY  | 分納日     | （なし） |
| LOGIX_J_BUNNOU | BUNNOUSU   | 分納数     | （なし） |
| LOGIX_J_BUNNOU | BUNNOUTIME | 分納時間   | （なし） |
| LOGIX_J_BUNNOU | ORDERNO    | オーダＮｏ | （なし） |
| LOGIX_J_BUNNOU | TANID      | 担当者     | （なし） |

## テーブル: LOGIX_J_JUCYU

| テーブル名    | 列ID            | 列名                      | 備考                                                                                                                       |
|:--------------|:----------------|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| LOGIX_J_JUCYU | CHAKUSHU_DATE   | 着手可能日                | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | DMTYP           | 需要区分                  | 0;独立需要;1;従属需要                                                                                                      |
| LOGIX_J_JUCYU | EDABAN          | 枝番                      | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | HENNOUKI        | 変更納期                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | HINMOKU         | 品目                      | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | IDOU            | 移動LV                    | 0;前後倒し;1;前倒し第２優先;2;前倒し第１優先;10;先行ありで前後倒し;11;先行ありで前倒し第２優先;12;先行ありで前倒し第１優先 |
| LOGIX_J_JUCYU | JBKTNO          | 受注読込バケットNo        | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | JBKTYEAR        | 受注読込バケット年        | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | JKUBUN          | 受注区分                  | 0;"新規";1;"更新"(使用しない);-1;"受注取消"                                                                                |
| LOGIX_J_JUCYU | JUCYUDAY        | 受注日                    | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | JUCYUSU         | 受注数                    | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KAITONOUKI      | 回答納期                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KAN_F           | 出荷完了F                 | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KBUNNOUDAY      | 分納日(TMP)               | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KBUNNOUSU       | 分納数(TMP)               | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KBUNNOUTIME     | 分納時間(TMP)             | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KOCYUBAN        | 顧客注番                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KOHINBAN        | 顧客品目                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KOHINMEI        | 顧客品名                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KOKYAKU         | 顧客                      | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KOUTEI          | 工程                      | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | KTANID          | 担当者(TMP)               | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | NAI_F           | 確定/内示Ｆ               | 0;"内示";1;"確定"                                                                                                          |
| LOGIX_J_JUCYU | NOUKI           | 顧客納期                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | NOUNYULT        | 顧客納入L/T（日）(未使用) | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | NOUNYUTIME      | 納入時間(時)              | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | OKURE           | 遅れ工程                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | ORDERNO         | オーダNo                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | PLANNOUKI       | 計画納期                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | S_CHAKUSHU_DATE | 先行着手可能日            | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SBKTNO          | 生産確定バケットNo        | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SBKTYEAR        | 生産確定バケット年        | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SEIBAN          | 製番                      | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SEIKAKU         | 生産確定F                 | 0;"未確定";1;"仕掛中";2;"確定"                                                                                             |
| LOGIX_J_JUCYU | SHACYUBAN       | 社内注番                  | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SHUKKADAY       | 出荷日                    | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SHUKKASU        | 出荷数                    | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SORT1           | 山積用ソート１            | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SORT2           | 山積用ソート２            | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | SORT3           | 山積用ソート３            | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | TMP_F           | (TMP)                     | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | TOKKYU_F        | 山積用特急F               | 0;"通常";1;"特急";2;"超特急"                                                                                               |
| LOGIX_J_JUCYU | VENDOR          | 仕入先                    | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | Z_HIKIATE_F     | Z_HIKIATE_F               | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | Z_HINMOKU       | Z_HINMOKU                 | （なし）                                                                                                                   |
| LOGIX_J_JUCYU | Z_KOUTEI        | Z_KOUTEI                  | （なし）                                                                                                                   |

## テーブル: LOGIX_KOUSEI_LST

| テーブル名       | 列ID         | 列名           | 備考     |
|:-----------------|:-------------|:---------------|:---------|
| LOGIX_KOUSEI_LST | ENDHINMOKU   | 最終品目       | （なし） |
| LOGIX_KOUSEI_LST | HINMOKU      | 品目           | （なし） |
| LOGIX_KOUSEI_LST | ID           | ID             | （なし） |
| LOGIX_KOUSEI_LST | INSUU        | 員数           | （なし） |
| LOGIX_KOUSEI_LST | KOU_ENDDAY   | 切替失効日     | （なし） |
| LOGIX_KOUSEI_LST | KOU_ENTRY    | 発注登録日     | （なし） |
| LOGIX_KOUSEI_LST | KOU_HIRITU   | 共用比率（％） | （なし） |
| LOGIX_KOUSEI_LST | KOU_KUBUN    | 共用区分       | （なし） |
| LOGIX_KOUSEI_LST | KOU_STARTDAY | 切替発行日     | （なし） |
| LOGIX_KOUSEI_LST | KOUTEI       | 工程           | （なし） |
| LOGIX_KOUSEI_LST | LEVELD       | レベル         | （なし） |
| LOGIX_KOUSEI_LST | VENDOR       | 仕入先         | （なし） |

## テーブル: LOGIX_KOU_ORDER

| テーブル名      | 列ID      | 列名       | 備考     |
|:----------------|:----------|:-----------|:---------|
| LOGIX_KOU_ORDER | BKTNO     | バケットNo | （なし） |
| LOGIX_KOU_ORDER | BKTYEAR   | バケット年 | （なし） |
| LOGIX_KOU_ORDER | HINMOKU   | 品目       | （なし） |
| LOGIX_KOU_ORDER | KAI_NOUKI | 回答納期   | （なし） |
| LOGIX_KOU_ORDER | KOUTEI    | 工程       | （なし） |
| LOGIX_KOU_ORDER | NOUKI     | 納期       | （なし） |
| LOGIX_KOU_ORDER | ORDERSUU  | オーダ数   | （なし） |
| LOGIX_KOU_ORDER | VENDOR    | 仕入先     | （なし） |

## テーブル: LOGIX_MC_HENKOUNOUKI

| テーブル名           | 列ID         | 列名       | 備考                        |
|:---------------------|:-------------|:-----------|:----------------------------|
| LOGIX_MC_HENKOUNOUKI | BKTNO        | バケットNo | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | BKTYEAR      | バケット年 | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | EDABAN       | 枝番       | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | HEN_NOUKI    | 変更納期   | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | HINMOKU      | 品目       | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | KOUTEI       | 工程       | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | OKURE        | 変更日数   | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | OKURE_KOUTEI | 遅れ工程   | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | ORDERNO      | オーダNo   | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | PLAN_NOUKI   | 計画納期   | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | SEIBAN       | 製番       | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | SENKOU_F     | 先行Ｆ     | 0;"納期後倒し";1;"先行する" |
| LOGIX_MC_HENKOUNOUKI | SIJISUU      | 受注数     | （なし）                    |
| LOGIX_MC_HENKOUNOUKI | VENDOR       | 仕入先     | （なし）                    |

## テーブル: LOGIX_MC_KOUTEIFUKA

| テーブル名          | 列ID         | 列名                             | 備考     |
|:--------------------|:-------------|:---------------------------------|:---------|
| LOGIX_MC_KOUTEIFUKA | B_SEISANSU   | バケット期間生産数               | （なし） |
| LOGIX_MC_KOUTEIFUKA | B_SEISANTIME | バケット期間生産時間（時間）     | （なし） |
| LOGIX_MC_KOUTEIFUKA | BKTNO        | バケットNo                       | （なし） |
| LOGIX_MC_KOUTEIFUKA | BKTYEAR      | バケット年                       | （なし） |
| LOGIX_MC_KOUTEIFUKA | KOUTEI       | 工程                             | （なし） |
| LOGIX_MC_KOUTEIFUKA | S_SEISANSU   | スケジュール期間生産数           | （なし） |
| LOGIX_MC_KOUTEIFUKA | S_SEISANTIME | スケジュール期間生産時間（時間） | （なし） |

## テーブル: LOGIX_MC_MBKTFUKA

| テーブル名        | 列ID          | 列名                             | 備考     |
|:------------------|:--------------|:---------------------------------|:---------|
| LOGIX_MC_MBKTFUKA | B_HYOUJUNTIME | バケット期間総負荷時間(時間)     | （なし） |
| LOGIX_MC_MBKTFUKA | B_KADOUTIME   | バケット期間稼働時間(時間)       | （なし） |
| LOGIX_MC_MBKTFUKA | B_LOSSTIME    | バケット期間ロス時間(時間)       | （なし） |
| LOGIX_MC_MBKTFUKA | B_SETUPTIME   | バケット期間段取時間(時間)       | （なし） |
| LOGIX_MC_MBKTFUKA | BKTNO         | バケットNo                       | （なし） |
| LOGIX_MC_MBKTFUKA | BKTYEAR       | バケット年                       | （なし） |
| LOGIX_MC_MBKTFUKA | KOUTEI        | 工程                             | （なし） |
| LOGIX_MC_MBKTFUKA | LINED         | ライン                           | （なし） |
| LOGIX_MC_MBKTFUKA | S_HYOUJUNTIME | スケジュール期間総負荷時間(時間) | （なし） |
| LOGIX_MC_MBKTFUKA | S_KADOUTIME   | スケジュール期間稼働時間(時間)   | （なし） |
| LOGIX_MC_MBKTFUKA | S_LOSSTIME    | スケジュール期間ロス時間(時間)   | （なし） |
| LOGIX_MC_MBKTFUKA | S_SETUPTIME   | スケジュール期間段取時間(時間)   | （なし） |
| LOGIX_MC_MBKTFUKA | SNO           | 出力番号                         | （なし） |

## テーブル: LOGIX_MC_MDFUKA

| テーブル名      | 列ID        | 列名           | 備考     |
|:----------------|:------------|:---------------|:---------|
| LOGIX_MC_MDFUKA | BKTNO       | バケットNo     | （なし） |
| LOGIX_MC_MDFUKA | BKTYEAR     | バケット年     | （なし） |
| LOGIX_MC_MDFUKA | DATED       | 日付           | （なし） |
| LOGIX_MC_MDFUKA | HYOUJUNTIME | 負荷時間(時間) | （なし） |
| LOGIX_MC_MDFUKA | KADOUTIME   | 稼働時間(時間) | （なし） |
| LOGIX_MC_MDFUKA | KOUTEI      | 工程           | （なし） |
| LOGIX_MC_MDFUKA | LINED       | ライン         | （なし） |
| LOGIX_MC_MDFUKA | LOSSTIME    | ロス時間(時間) | （なし） |
| LOGIX_MC_MDFUKA | SETUPTIME   | 段取時間(時間) | （なし） |

## テーブル: LOGIX_MC_TBKTFUKA

| テーブル名        | 列ID          | 列名                             | 備考     |
|:------------------|:--------------|:---------------------------------|:---------|
| LOGIX_MC_TBKTFUKA | B_HYOUJUNTIME | バケット期間総負荷時間(時間)     | （なし） |
| LOGIX_MC_TBKTFUKA | B_KADOUTIME   | バケット期間稼働時間(時間)       | （なし） |
| LOGIX_MC_TBKTFUKA | B_LOSSTIME    | バケット期間ロス時間(時間)       | （なし） |
| LOGIX_MC_TBKTFUKA | B_SETUPTIME   | バケット期間段取時間(時間)       | （なし） |
| LOGIX_MC_TBKTFUKA | BKTNO         | バケットNo                       | （なし） |
| LOGIX_MC_TBKTFUKA | BKTYEAR       | バケット年                       | （なし） |
| LOGIX_MC_TBKTFUKA | KOUTEI        | 工程                             | （なし） |
| LOGIX_MC_TBKTFUKA | LINED         | ライン                           | （なし） |
| LOGIX_MC_TBKTFUKA | S_HYOUJUNTIME | スケジュール期間総負荷時間(時間) | （なし） |
| LOGIX_MC_TBKTFUKA | S_KADOUTIME   | スケジュール期間稼働時間(時間)   | （なし） |
| LOGIX_MC_TBKTFUKA | S_LOSSTIME    | スケジュール期間ロス時間(時間)   | （なし） |
| LOGIX_MC_TBKTFUKA | S_SETUPTIME   | スケジュール期間段取時間(時間)   | （なし） |
| LOGIX_MC_TBKTFUKA | SNO           | 出力番号                         | （なし） |

## テーブル: LOGIX_MC_TDFUKA

| テーブル名      | 列ID        | 列名           | 備考     |
|:----------------|:------------|:---------------|:---------|
| LOGIX_MC_TDFUKA | BKTNO       | バケットNo     | （なし） |
| LOGIX_MC_TDFUKA | BKTYEAR     | バケット年     | （なし） |
| LOGIX_MC_TDFUKA | DATED       | 日付           | （なし） |
| LOGIX_MC_TDFUKA | HYOUJUNTIME | 負荷時間(時間) | （なし） |
| LOGIX_MC_TDFUKA | KADOUTIME   | 稼働時間(時間) | （なし） |
| LOGIX_MC_TDFUKA | KOUTEI      | 工程           | （なし） |
| LOGIX_MC_TDFUKA | LINED       | ライン         | （なし） |
| LOGIX_MC_TDFUKA | LOSSTIME    | ロス時間(時間) | （なし） |
| LOGIX_MC_TDFUKA | SETUPTIME   | 段取時間(時間) | （なし） |

## テーブル: LOGIX_M_BUCKET

| テーブル名     | 列ID     | 列名               | 備考            |
|:---------------|:---------|:-------------------|:----------------|
| LOGIX_M_BUCKET | BKTNO    | バケットNo         | （なし）        |
| LOGIX_M_BUCKET | BKTYEAR  | バケット年         | （なし）        |
| LOGIX_M_BUCKET | ENDDAY   | ﾊﾞｹｯﾄ最終日        | （なし）        |
| LOGIX_M_BUCKET | ENTRY    | 登録日             | （なし）        |
| LOGIX_M_BUCKET | RADISH   | 受注取込最終日     | （なし）        |
| LOGIX_M_BUCKET | SCHEDULE | スケジュール最終日 | （なし）        |
| LOGIX_M_BUCKET | SEIORDER | 作業指示確定F      | 0;未完了;1;完了 |
| LOGIX_M_BUCKET | STARTDAY | バケット開始日     | （なし）        |

## テーブル: LOGIX_M_CALEND

| テーブル名     | 列ID     | 列名           | 備考                       |
|:---------------|:---------|:---------------|:---------------------------|
| LOGIX_M_CALEND | CALEND   | カレンダー番号 | （なし）                   |
| LOGIX_M_CALEND | DATED    | 年月日         | （なし）                   |
| LOGIX_M_CALEND | KADOUBI  | 稼働日         | FALSE;非稼働;TRUE;稼働     |
| LOGIX_M_CALEND | ZANGYOKA | 残業可         | FALSE;残業不可;TRUE;残業可 |

## テーブル: LOGIX_M_CLNNO

| テーブル名    | 列ID   | 列名           | 備考     |
|:--------------|:-------|:---------------|:---------|
| LOGIX_M_CLNNO | CLNMEI | カレンダー名   | （なし） |
| LOGIX_M_CLNNO | CLNNO  | カレンダー番号 | （なし） |

## テーブル: LOGIX_M_DOUJI

| テーブル名    | 列ID          | 列名             | 備考                      |
|:--------------|:--------------|:-----------------|:--------------------------|
| LOGIX_M_DOUJI | DOUJI_HINMOKU | 同時生産品目     | （なし）                  |
| LOGIX_M_DOUJI | DOUJI_KUBUN   | 同時生産区分     | 0;同時に生産;1;事前に生産 |
| LOGIX_M_DOUJI | DOUJI_TORISU  | 同時生産品目取数 | （なし）                  |
| LOGIX_M_DOUJI | ENTRY         | 登録日           | （なし）                  |
| LOGIX_M_DOUJI | HINMOKU       | 品目             | （なし）                  |
| LOGIX_M_DOUJI | KOUTEI        | 工程             | （なし）                  |
| LOGIX_M_DOUJI | TORISU        | 品目取数         | （なし）                  |
| LOGIX_M_DOUJI | VENDOR        | 仕入先           | （なし）                  |

## テーブル: LOGIX_M_HINMOKU

| テーブル名      | 列ID      | 列名           | 備考                                                                                                                                       |
|:----------------|:----------|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| LOGIX_M_HINMOKU | DOKURITU  | 独立需要F      | 0;従属需要;1;独立需要                                                                                                                      |
| LOGIX_M_HINMOKU | ENDDAY    | 失効日         | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | ENTRY     | 登録日         | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | HANSOULT  | 搬送L/T(分)    | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | HIJUU     | 比重           | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | HINMEI    | 品名           | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | HINMOKU   | 品目           | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | HOKANLT   | 保管F          | 0;"休日を加味しない";1;"休日を加味する"                                                                                                    |
| LOGIX_M_HINMOKU | HTANKA    | 標準単価       | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | JIGU      | 治具数         | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | JIKOULT   | 自工程L/T(日)  | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | KOUTEI    | 工程           | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | KUBUN     | 製品区分       | 0;製造品;1;購入品                                                                                                                          |
| LOGIX_M_HINMOKU | MARUME    | 所要量丸め     | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | MATOME    | 指示まとめ日数 | 未使用                                                                                                                                     |
| LOGIX_M_HINMOKU | MAXZAIKO  | 最大在庫       | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | MINZAIKO  | 最小在庫       | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | NG        | 仕損率(％)     | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | RUIKEILT  | 累計L/T(日)    | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | SEIBAN    | 製番管理F      | 0;"オーダ管理(すべての受注に対して作業指示作成)";1;"製番管理(確定受注に対して作業指示作成)";2;"製番管理(すべての受注に対して作業指示作成)" |
| LOGIX_M_HINMOKU | SENDOLT   | 使用期限(分)   | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | SETUPDAY  | 最適化日数(日) | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | SIZE1     | SIZE1          | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | SIZE2     | SIZE2          | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | SIZE3     | SIZE3          | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | STARTDAY  | 発効日         | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | SYUZAIK   | 主材区分       | 0;部品;1;主材;2;副材                                                                                                                       |
| LOGIX_M_HINMOKU | TANI      | 単位           | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | TUKAIKIRI | 半製品使切F    | 0;使切らない;1;使切る                                                                                                                      |
| LOGIX_M_HINMOKU | VENDOR    | 仕入先         | （なし）                                                                                                                                   |
| LOGIX_M_HINMOKU | ZUBAN     | 部品番号       | （なし）                                                                                                                                   |

## テーブル: LOGIX_M_JIGU

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| LOGIX_M_JIGU | ENTRY    | 登録日     | （なし） |
| LOGIX_M_JIGU | ESYURI   | 修理完了日 | （なし） |
| LOGIX_M_JIGU | JIGUMEI  | 治具名     | （なし） |
| LOGIX_M_JIGU | JIGUNO   | 治具番号   | （なし） |
| LOGIX_M_JIGU | JIGUSUU  | 治具数     | （なし） |
| LOGIX_M_JIGU | SSYURI   | 修理開始日 | （なし） |
| LOGIX_M_JIGU | SYURISUU | 修理数     | （なし） |

## テーブル: LOGIX_M_KJIKAN

| テーブル名     | 列ID     | 列名           | 備考     |
|:---------------|:---------|:---------------|:---------|
| LOGIX_M_KJIKAN | ENTRY    | 登録日         | （なし） |
| LOGIX_M_KJIKAN | HYOJUN   | 定時時間(時間) | （なし） |
| LOGIX_M_KJIKAN | KADOU_CD | 稼働時間帯     | （なし） |
| LOGIX_M_KJIKAN | KADOUMEI | 稼働時間帯名   | （なし） |
| LOGIX_M_KJIKAN | ZANGYO   | 残業時間(時間) | （なし） |

## テーブル: LOGIX_M_KJIKANM

| テーブル名      | 列ID     | 列名       | 備考          |
|:----------------|:---------|:-----------|:--------------|
| LOGIX_M_KJIKANM | E_HOUR   | 終了時     | （なし）      |
| LOGIX_M_KJIKANM | E_MIN    | 終了分     | （なし）      |
| LOGIX_M_KJIKANM | ENTRY    | 登録日     | （なし）      |
| LOGIX_M_KJIKANM | KADOU_CD | 稼働時間帯 | （なし）      |
| LOGIX_M_KJIKANM | KADOU_F  | 稼働F      | 0;定時;1;残業 |
| LOGIX_M_KJIKANM | KADOU_NO | 稼働番号   | （なし）      |
| LOGIX_M_KJIKANM | S_HOUR   | 開始時     | （なし）      |
| LOGIX_M_KJIKANM | S_MIN    | 開始分     | （なし）      |

## テーブル: LOGIX_M_KOUSEI

| テーブル名     | 列ID       | 列名        | 備考                    |
|:---------------|:-----------|:------------|:------------------------|
| LOGIX_M_KOUSEI | BUDOMARI   | 歩留(%)     | （なし）                |
| LOGIX_M_KOUSEI | ENDDAY     | 失効日      | （なし）                |
| LOGIX_M_KOUSEI | ENTRY      | 登録日      | （なし）                |
| LOGIX_M_KOUSEI | HIRITU     | 共用比率(%) | （なし）                |
| LOGIX_M_KOUSEI | INSUU      | 員数        | （なし）                |
| LOGIX_M_KOUSEI | INSUUKUBUN | 員数区分    | 0;員数優先;1;基準数優先 |
| LOGIX_M_KOUSEI | KINSUU     | 基準員数    | （なし）                |
| LOGIX_M_KOUSEI | KOHINMOKU  | 子品目      | （なし）                |
| LOGIX_M_KOUSEI | KOKIJUNSU  | 子基準数    | （なし）                |
| LOGIX_M_KOUSEI | KOKOUTEI   | 子工程      | （なし）                |
| LOGIX_M_KOUSEI | KOVENDOR   | 子仕入先    | （なし）                |
| LOGIX_M_KOUSEI | KUBUN      | 共用区分    | （なし）                |
| LOGIX_M_KOUSEI | OYAHINMOKU | 親品目      | （なし）                |
| LOGIX_M_KOUSEI | OYAKIJUNSU | 親基準数    | （なし）                |
| LOGIX_M_KOUSEI | OYAKOUTEI  | 親工程      | （なし）                |
| LOGIX_M_KOUSEI | OYAVENDOR  | 親仕入先    | （なし）                |
| LOGIX_M_KOUSEI | STARTDAY   | 発効日      | （なし）                |

## テーブル: LOGIX_M_KOUTEI

| テーブル名     | 列ID      | 列名             | 備考                                                                                                                                       |
|:---------------|:----------|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| LOGIX_M_KOUTEI | CLNNO     | ｶﾚﾝﾀﾞｰ番号       | （なし）                                                                                                                                   |
| LOGIX_M_KOUTEI | ENTRY     | 登録日           | （なし）                                                                                                                                   |
| LOGIX_M_KOUTEI | KOUTEI    | 工程             | （なし）                                                                                                                                   |
| LOGIX_M_KOUTEI | KOUTEIMEI | 工程名           | （なし）                                                                                                                                   |
| LOGIX_M_KOUTEI | MANOP     | 人員最適化F      | 0;"しない";1;"する"                                                                                                                        |
| LOGIX_M_KOUTEI | MAXZAIKO  | 最大在庫         | （なし）                                                                                                                                   |
| LOGIX_M_KOUTEI | NOUKIOP   | 納期最適化F      | 0;"しない";1;"する"                                                                                                                        |
| LOGIX_M_KOUTEI | PASS      | スケジュールPASS | 未使用                                                                                                                                     |
| LOGIX_M_KOUTEI | QLTYOP    | 品質最適化F      | 0;"しない";1;"する"                                                                                                                        |
| LOGIX_M_KOUTEI | SEIBAN    | 製番管理F        | 0;"オーダ管理(すべての受注に対して作業指示作成)";1;"製番管理(確定受注に対して作業指示作成)";2;"製番管理(すべての受注に対して作業指示作成)" |
| LOGIX_M_KOUTEI | SEIHIN    | 製品群           | （なし）                                                                                                                                   |
| LOGIX_M_KOUTEI | SETUPOP   | 段取最適化F      | 0;"しない";1;"する"                                                                                                                        |
| LOGIX_M_KOUTEI | SORT      | ソート条件       | （なし）                                                                                                                                   |

## テーブル: LOGIX_M_LINE

| テーブル名   | 列ID       | 列名                  | 備考                                                                         |
|:-------------|:-----------|:----------------------|:-----------------------------------------------------------------------------|
| LOGIX_M_LINE | BAT_F      | バッチ処理F           | YES/NO(未使用)                                                               |
| LOGIX_M_LINE | CLNNO      | ｶﾚﾝﾀﾞｰ番号            | （なし）                                                                     |
| LOGIX_M_LINE | DAISHASU   | 供給台車数            | （なし）                                                                     |
| LOGIX_M_LINE | ENTRY      | 登録日                | （なし）                                                                     |
| LOGIX_M_LINE | FUKARITU   | 計画稼働率(%)         | （なし）                                                                     |
| LOGIX_M_LINE | GAICHU_F   | 外注F                 | 0;"内作";1;"外作"                                                            |
| LOGIX_M_LINE | GANTDISP_F | ガントチャート非表示F | 0;表示する;1;表示しない                                                      |
| LOGIX_M_LINE | HASUU      | 端数処理数            | （なし）                                                                     |
| LOGIX_M_LINE | HEIKIN_F   | 平均負荷割F           | 0;"しない";1;"する"                                                          |
| LOGIX_M_LINE | HIJUU_F    | 比重変換F             | 0;なし;1;あり                                                                |
| LOGIX_M_LINE | KADOU_CD   | 標準稼働時間帯        | （なし）                                                                     |
| LOGIX_M_LINE | KADOU_CD2  | 休出稼働時間帯        | （なし）                                                                     |
| LOGIX_M_LINE | KIRIAGE    | 終業時刻調整F         | 0;"終業時刻短縮";1;"終業時刻延長";2;"翌日に作業がまたがらない"               |
| LOGIX_M_LINE | KOURITU    | ｽｹｼﾞｭｰﾗ効率(%)        | （なし）                                                                     |
| LOGIX_M_LINE | KOUTEI     | 工程                  | （なし）                                                                     |
| LOGIX_M_LINE | LINED      | ライン                | （なし）                                                                     |
| LOGIX_M_LINE | LINEMEI    | ライン名              | （なし）                                                                     |
| LOGIX_M_LINE | LOT        | ﾛｯﾄｻｲｽﾞ保証Ｆ         | 0;"しない";1;"する"                                                          |
| LOGIX_M_LINE | LOT_SIJI   | 指示発行区分          | 0;指示まとめをする;1;翌日にまたがる指示を分ける;2;ロット単位の指示を発行する |
| LOGIX_M_LINE | M_KOURITU  | マクロ効率(%)         | （なし）                                                                     |
| LOGIX_M_LINE | MANGROUPT  | 定期段取人員G         | （なし）                                                                     |
| LOGIX_M_LINE | MAXZ       | ストレージ最大在庫    | （なし）                                                                     |
| LOGIX_M_LINE | MINZ       | ストレージ最小在庫    | （なし）                                                                     |
| LOGIX_M_LINE | NINZUUT    | 定期段取人数          | （なし）                                                                     |
| LOGIX_M_LINE | OVERLAP    | オーバラップF         | 0;"しない";1;"する"                                                          |
| LOGIX_M_LINE | R_KOUTEI   | 連結工程              | （なし）                                                                     |
| LOGIX_M_LINE | R_LINED    | 連結ライン            | （なし）                                                                     |
| LOGIX_M_LINE | RENK_F     | 連結F                 | 0;"連結無し";1;"連結有り"                                                    |
| LOGIX_M_LINE | SAKI       | 先入先出F             | 0;"しない";1;"する"                                                          |
| LOGIX_M_LINE | SETUPDAY   | 最適化日数(日)        | （なし）                                                                     |
| LOGIX_M_LINE | SETUPTIMET | 定期段取時間(分)      | （なし）                                                                     |
| LOGIX_M_LINE | SORT       | ソート条件            | （なし）                                                                     |
| LOGIX_M_LINE | STRAGE_F   | ストレージF           | 0;設備;1;ストレージ装置                                                      |
| LOGIX_M_LINE | STRAGE_K   | ストレージ区分        | 0;タンク;1;供給台車                                                          |
| LOGIX_M_LINE | TDAN_BATCH | 定期段取バッチ数      | （なし）                                                                     |
| LOGIX_M_LINE | TDAN_KIKAN | 定期段取期間(日)      | （なし）                                                                     |
| LOGIX_M_LINE | TDAN_KUBUN | 定期段取区分          | 0;なし;1;バッチ数により発生;2;期間により発生                                 |
| LOGIX_M_LINE | ZANGYOHI   | 残業比率（％）        | （なし）                                                                     |

## テーブル: LOGIX_M_MAN

| テーブル名   | 列ID      | 列名           | 備考     |
|:-------------|:----------|:---------------|:---------|
| LOGIX_M_MAN  | CLNNO     | ｶﾚﾝﾀﾞｰ番号     | （なし） |
| LOGIX_M_MAN  | ENTRY     | 登録日         | （なし） |
| LOGIX_M_MAN  | KADOU_CD  | 標準稼働時間帯 | （なし） |
| LOGIX_M_MAN  | KADOU_CD2 | 休出稼働時間帯 | （なし） |
| LOGIX_M_MAN  | KOURITU   | 効率(%)        | （なし） |
| LOGIX_M_MAN  | MAN       | 生産人員G      | （なし） |
| LOGIX_M_MAN  | MANMEI    | 生産人員名     | （なし） |
| LOGIX_M_MAN  | MANSUU    | 人員数         | （なし） |

## テーブル: LOGIX_M_MAX_MIN_ZAIKO

| テーブル名            | 列ID     | 列名     | 備考     |
|:----------------------|:---------|:---------|:---------|
| LOGIX_M_MAX_MIN_ZAIKO | ENDDAY   | 終了日   | （なし） |
| LOGIX_M_MAX_MIN_ZAIKO | ENTRY    | 登録日   | （なし） |
| LOGIX_M_MAX_MIN_ZAIKO | HINMOKU  | 品目     | （なし） |
| LOGIX_M_MAX_MIN_ZAIKO | KOUTEI   | 工程     | （なし） |
| LOGIX_M_MAX_MIN_ZAIKO | MAXZAIKO | 最大在庫 | （なし） |
| LOGIX_M_MAX_MIN_ZAIKO | MINZAIKO | 最小在庫 | （なし） |
| LOGIX_M_MAX_MIN_ZAIKO | STARTDAY | 開始日   | （なし） |
| LOGIX_M_MAX_MIN_ZAIKO | VENDOR   | 仕入先   | （なし） |

## テーブル: LOGIX_M_NOURYOKU

| テーブル名       | 列ID         | 列名                         | 備考                                                                   |
|:-----------------|:-------------|:-----------------------------|:-----------------------------------------------------------------------|
| LOGIX_M_NOURYOKU | AMANGROUP    | 後段取人員G                  | （なし）                                                               |
| LOGIX_M_NOURYOKU | ANINZUU      | 後段取人数                   | （なし）                                                               |
| LOGIX_M_NOURYOKU | ASETUPTIME   | 後段取時間(分)               | （なし）                                                               |
| LOGIX_M_NOURYOKU | BATCHMAX     | 最大可能バッチ数             | （なし）                                                               |
| LOGIX_M_NOURYOKU | BATCHMIN     | 最小生産バッチ数             | （なし）                                                               |
| LOGIX_M_NOURYOKU | ENDDAY       | 失効日                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | ENTRY        | 登録日                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | GAI_JIKOULT  | 外注自工程L/T（日）          | （なし）                                                               |
| LOGIX_M_NOURYOKU | GAI_RUIKEILT | 外注累計L/T（日）            | （なし）                                                               |
| LOGIX_M_NOURYOKU | HINMOKU      | 品目                         | （なし）                                                               |
| LOGIX_M_NOURYOKU | JIGU1        | 治具１                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | JIGU2        | 治具２                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | JIGU3        | 治具３                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | JIGU4        | 治具４                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | JIGU5        | 治具５                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | JUNJO        | 順序Ｇ                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | KOUTEI       | 工程                         | （なし）                                                               |
| LOGIX_M_NOURYOKU | LINED        | ライン                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | LOSS         | 固定ロス量                   | （なし）                                                               |
| LOGIX_M_NOURYOKU | MAN          | 標準人員（人）               | （なし）                                                               |
| LOGIX_M_NOURYOKU | MANG1        | 人員Ｇ１                     | （なし）                                                               |
| LOGIX_M_NOURYOKU | MANG2        | 人員Ｇ２                     | （なし）                                                               |
| LOGIX_M_NOURYOKU | MANG3        | 人員Ｇ３                     | （なし）                                                               |
| LOGIX_M_NOURYOKU | MANGROUP     | 段取人員G                    | （なし）                                                               |
| LOGIX_M_NOURYOKU | MANKOURITU   | 人員減効率（％）             | （なし）                                                               |
| LOGIX_M_NOURYOKU | MAXLOT       | ロットサイズ                 | （なし）                                                               |
| LOGIX_M_NOURYOKU | MINMAN       | 最少人員（人）               | （なし）                                                               |
| LOGIX_M_NOURYOKU | MUKOU_F      | 無効Ｆ                       | 0;有効;1;無効                                                          |
| LOGIX_M_NOURYOKU | NINZUU       | 段取人数                     | （なし）                                                               |
| LOGIX_M_NOURYOKU | NOURYOKU     | 時間当生産能力(生産数／時間) | （なし）                                                               |
| LOGIX_M_NOURYOKU | QUALTY1      | 品質Ｇ１特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | QUALTY2      | 品質Ｇ２特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | QUALTY3      | 品質Ｇ３特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | QUALTY4      | 品質Ｇ４特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | QUALTY5      | 品質Ｇ５特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | QUALTY6      | 品質Ｇ６特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | QUALTY7      | 品質Ｇ７特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | R_KOUTEI     | 連結工程                     | （なし）                                                               |
| LOGIX_M_NOURYOKU | R_LINED      | 連結ライン                   | （なし）                                                               |
| LOGIX_M_NOURYOKU | RENK_F       | 連結F                        | 0;"連結無し";1;"連結有り"                                              |
| LOGIX_M_NOURYOKU | RITUAN       | 立案方法                     | 1;"稼働率優先";2;"同期化優先";3;"最適化日数内稼働率優先"               |
| LOGIX_M_NOURYOKU | SETUP1       | 段取Ｇ１特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | SETUP2       | 段取Ｇ２特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | SETUP3       | 段取Ｇ３特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | SETUP4       | 段取Ｇ４特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | SETUP5       | 段取Ｇ５特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | SETUP6       | 段取Ｇ６特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | SETUP7       | 段取Ｇ７特性値               | （なし）                                                               |
| LOGIX_M_NOURYOKU | SETUPF       | 同一品目固定段取F            | 0;固定段取しない;1;固定段取する;2;最大可能バッチ数以上で固定段取りする |
| LOGIX_M_NOURYOKU | SETUPTIME    | 固定段取時間(分)             | （なし）                                                               |
| LOGIX_M_NOURYOKU | STARTDAY     | 発効日                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | VENDOR       | 仕入先                       | （なし）                                                               |
| LOGIX_M_NOURYOKU | YUSEN        | 優先順位                     | 第１優先〜第99優先                                                     |

## テーブル: LOGIX_M_QUALITY

| テーブル名      | 列ID         | 列名        | 備考     |
|:----------------|:-------------|:------------|:---------|
| LOGIX_M_QUALITY | ENTRY        | 登録日      | （なし） |
| LOGIX_M_QUALITY | KOUTEI       | 工程        | （なし） |
| LOGIX_M_QUALITY | LINED        | ライン      | （なし） |
| LOGIX_M_QUALITY | OMOMI        | 品質重み    | （なし） |
| LOGIX_M_QUALITY | QUALITY1     | 品質特性値1 | （なし） |
| LOGIX_M_QUALITY | QUALITY2     | 品質特性値2 | （なし） |
| LOGIX_M_QUALITY | QUALITYGROUP | 品質G       | （なし） |

## テーブル: LOGIX_M_QUALITYMEI

| テーブル名         | 列ID         | 列名       | 備考     |
|:-------------------|:-------------|:-----------|:---------|
| LOGIX_M_QUALITYMEI | ENTRY        | 登録日     | （なし） |
| LOGIX_M_QUALITYMEI | KOUTEI       | 工程       | （なし） |
| LOGIX_M_QUALITYMEI | LINED        | ライン     | （なし） |
| LOGIX_M_QUALITYMEI | QUALITY      | 品質特性値 | （なし） |
| LOGIX_M_QUALITYMEI | QUALITYGROUP | 品質G      | （なし） |
| LOGIX_M_QUALITYMEI | QUALITYMEI   | 品質特性名 | （なし） |

## テーブル: LOGIX_M_RENKETU

| テーブル名      | 列ID      | 列名       | 備考     |
|:----------------|:----------|:-----------|:---------|
| LOGIX_M_RENKETU | ENTRY     | 登録日     | （なし） |
| LOGIX_M_RENKETU | I_HINMOKU | 入力品目   | （なし） |
| LOGIX_M_RENKETU | I_KOUTEI  | 入力工程   | （なし） |
| LOGIX_M_RENKETU | I_LINED   | 入力ライン | （なし） |
| LOGIX_M_RENKETU | I_VENDOR  | 入力仕入先 | （なし） |
| LOGIX_M_RENKETU | O_HINMOKU | 出力品目   | （なし） |
| LOGIX_M_RENKETU | O_KOUTEI  | 出力工程   | （なし） |
| LOGIX_M_RENKETU | O_LINED   | 出力ライン | （なし） |
| LOGIX_M_RENKETU | O_VENDOR  | 出力仕入先 | （なし） |

## テーブル: LOGIX_M_SETUP

| テーブル名    | 列ID       | 列名         | 備考     |
|:--------------|:-----------|:-------------|:---------|
| LOGIX_M_SETUP | ENTRY      | 登録日       | （なし） |
| LOGIX_M_SETUP | KOUTEI     | 工程         | （なし） |
| LOGIX_M_SETUP | LINED      | ライン       | （なし） |
| LOGIX_M_SETUP | MANGROUP   | 人員G        | （なし） |
| LOGIX_M_SETUP | NINZUU     | 人数         | （なし） |
| LOGIX_M_SETUP | SETUP1     | 段取特性値1  | （なし） |
| LOGIX_M_SETUP | SETUP2     | 段取特性値2  | （なし） |
| LOGIX_M_SETUP | SETUPGROUP | 段取G        | （なし） |
| LOGIX_M_SETUP | SETUPTIME  | 段取時間(分) | （なし） |

## テーブル: LOGIX_M_SETUPMEI

| テーブル名       | 列ID       | 列名       | 備考     |
|:-----------------|:-----------|:-----------|:---------|
| LOGIX_M_SETUPMEI | ENTRY      | 登録日     | （なし） |
| LOGIX_M_SETUPMEI | KOUTEI     | 工程       | （なし） |
| LOGIX_M_SETUPMEI | LINED      | ライン     | （なし） |
| LOGIX_M_SETUPMEI | OR_F       | OR_F       | （なし） |
| LOGIX_M_SETUPMEI | SETUPGROUP | 段取G      | （なし） |
| LOGIX_M_SETUPMEI | SETUPMEI   | 段取特性名 | （なし） |
| LOGIX_M_SETUPMEI | SETUPTI    | 段取特性値 | （なし） |

## テーブル: LOGIX_M_SIKAKARI

| テーブル名       | 列ID         | 列名                       | 備考     |
|:-----------------|:-------------|:---------------------------|:---------|
| LOGIX_M_SIKAKARI | BKTNO        | バケットNo                 | （なし） |
| LOGIX_M_SIKAKARI | BKTYEAR      | バケット年                 | （なし） |
| LOGIX_M_SIKAKARI | EDABAN       | 枝番                       | （なし） |
| LOGIX_M_SIKAKARI | HINMOKU      | 品目                       | （なし） |
| LOGIX_M_SIKAKARI | KDAN_BATCH   | 前回固定段取経過バッチ数   | （なし） |
| LOGIX_M_SIKAKARI | KOUTEI       | 工程                       | （なし） |
| LOGIX_M_SIKAKARI | LINED        | ライン                     | （なし） |
| LOGIX_M_SIKAKARI | LOTZAN       | ロット残数                 | （なし） |
| LOGIX_M_SIKAKARI | SEIBAN       | 製番                       | （なし） |
| LOGIX_M_SIKAKARI | SEISAN_LOT   | 前回生産済バッチ数         | （なし） |
| LOGIX_M_SIKAKARI | SETUPTIME    | 段取残時間(分)             | （なし） |
| LOGIX_M_SIKAKARI | STRAGE_ZAIKO | ストレージ在庫数           | （なし） |
| LOGIX_M_SIKAKARI | TDAN_BATCH   | 前回定期段取生産済バッチ数 | （なし） |
| LOGIX_M_SIKAKARI | TDAN_KIKAN   | 前回定期段取経過日数       | （なし） |
| LOGIX_M_SIKAKARI | VENDOR       | 仕入先                     | （なし） |

## テーブル: LOGIX_M_TANTOU

| テーブル名     | 列ID   | 列名     | 備考     |
|:---------------|:-------|:---------|:---------|
| LOGIX_M_TANTOU | ENTRY  | 登録日   | （なし） |
| LOGIX_M_TANTOU | TANID  | 担当者   | （なし） |
| LOGIX_M_TANTOU | TANMEI | 担当者名 | （なし） |

## テーブル: LOGIX_M_VENDOR

| テーブル名     | 列ID      | 列名     | 備考     |
|:---------------|:----------|:---------|:---------|
| LOGIX_M_VENDOR | ADDRESS   | 住所     | （なし） |
| LOGIX_M_VENDOR | ENTRY     | 登録日   | （なし） |
| LOGIX_M_VENDOR | FAX       | FAX      | （なし） |
| LOGIX_M_VENDOR | TEL       | TEL      | （なし） |
| LOGIX_M_VENDOR | VENDOR    | 仕入先   | （なし） |
| LOGIX_M_VENDOR | VENDORMEI | 仕入先名 | （なし） |
| LOGIX_M_VENDOR | YUBIN     | 郵便番号 | （なし） |

## テーブル: LOGIX_R_FUKA

| テーブル名   | 列ID        | 列名           | 備考     |
|:-------------|:------------|:---------------|:---------|
| LOGIX_R_FUKA | BKTNO       | バケットNo     | （なし） |
| LOGIX_R_FUKA | BKTYEAR     | バケット年     | （なし） |
| LOGIX_R_FUKA | DATED       | 日付           | （なし） |
| LOGIX_R_FUKA | HYOUJUNTIME | 操業時間(時間) | （なし） |
| LOGIX_R_FUKA | KADOUTIME   | 稼働時間(時間) | （なし） |
| LOGIX_R_FUKA | KOUTEI      | 工程           | （なし） |
| LOGIX_R_FUKA | LINED       | ライン         | （なし） |
| LOGIX_R_FUKA | LOSSTIME    | ロス時間(時間) | （なし） |
| LOGIX_R_FUKA | SETUPTIME   | 段取時間(時間) | （なし） |

## テーブル: LOGIX_R_KADOU

| テーブル名    | 列ID      | 列名            | 備考                                    |
|:--------------|:----------|:----------------|:----------------------------------------|
| LOGIX_R_KADOU | BKTNO     | バケットNo      | （なし）                                |
| LOGIX_R_KADOU | BKTYEAR   | バケット年      | （なし）                                |
| LOGIX_R_KADOU | DATED     | 日付            | （なし）                                |
| LOGIX_R_KADOU | KADOU_CD  | 稼働時間帯      | （なし）                                |
| LOGIX_R_KADOU | KOURITU   | 有効時間比率(%) | （なし）                                |
| LOGIX_R_KADOU | KOUTEI    | 工程            | （なし）                                |
| LOGIX_R_KADOU | LINED     | ライン          | （なし）                                |
| LOGIX_R_KADOU | SOGYOOP   | 操業最適化      | 0;"しない";1;"する"                     |
| LOGIX_R_KADOU | YOUBI     | 曜日            | （なし）                                |
| LOGIX_R_KADOU | ZANGYOKA  | 操業モード      | 0;"定時";1;"定時＋残業";2;"休日出勤"    |
| LOGIX_R_KADOU | ZANGYOU_F | 残業Ｆ          | 0;"残業・休出しない";1;"残業・休出する" |

## テーブル: LOGIX_R_KADOU2

| テーブル名     | 列ID      | 列名            | 備考                                    |
|:---------------|:----------|:----------------|:----------------------------------------|
| LOGIX_R_KADOU2 | BKTNO     | バケットNo      | （なし）                                |
| LOGIX_R_KADOU2 | BKTYEAR   | バケット年      | （なし）                                |
| LOGIX_R_KADOU2 | DATED     | 日付            | （なし）                                |
| LOGIX_R_KADOU2 | KADOU_CD  | 稼働時間帯      | （なし）                                |
| LOGIX_R_KADOU2 | KOURITU   | 有効時間比率(%) | （なし）                                |
| LOGIX_R_KADOU2 | KOUTEI    | 工程            | （なし）                                |
| LOGIX_R_KADOU2 | LINED     | ライン          | （なし）                                |
| LOGIX_R_KADOU2 | SOGYOOP   | 操業最適化      | 0;"しない";1;"する"                     |
| LOGIX_R_KADOU2 | YOUBI     | 曜日            | （なし）                                |
| LOGIX_R_KADOU2 | ZANGYOKA  | 操業モード      | 0;"定時";1;"定時＋残業";2;"休日出勤"    |
| LOGIX_R_KADOU2 | ZANGYOU_F | 残業Ｆ          | 0;"残業・休出しない";1;"残業・休出する" |

## テーブル: LOGIX_R_KOTEI

| テーブル名    | 列ID    | 列名           | 備考     |
|:--------------|:--------|:---------------|:---------|
| LOGIX_R_KOTEI | BKTNO   | バケットNo     | （なし） |
| LOGIX_R_KOTEI | BKTYEAR | バケット年     | （なし） |
| LOGIX_R_KOTEI | DATED   | 指示日         | （なし） |
| LOGIX_R_KOTEI | EDABAN  | 枝番           | （なし） |
| LOGIX_R_KOTEI | HINMOKU | 品目           | （なし） |
| LOGIX_R_KOTEI | KOSUU   | 指示数         | （なし） |
| LOGIX_R_KOTEI | KOUTEI  | 工程           | （なし） |
| LOGIX_R_KOTEI | LINED   | ライン         | （なし） |
| LOGIX_R_KOTEI | SEIBAN  | 製番           | （なし） |
| LOGIX_R_KOTEI | TIMED   | 開始時間(時分) | （なし） |
| LOGIX_R_KOTEI | VENDOR  | 仕入先         | （なし） |

## テーブル: LOGIX_R_KOUFUSOKU

| テーブル名        | 列ID      | 列名       | 備考     |
|:------------------|:----------|:-----------|:---------|
| LOGIX_R_KOUFUSOKU | BKTNO     | バケットNo | （なし） |
| LOGIX_R_KOUFUSOKU | BKTYEAR   | バケット年 | （なし） |
| LOGIX_R_KOUFUSOKU | FUSOKUDAY | 不足日     | （なし） |
| LOGIX_R_KOUFUSOKU | FUSOKUSU  | 不足数     | （なし） |
| LOGIX_R_KOUFUSOKU | HINMEI    | 品名       | （なし） |
| LOGIX_R_KOUFUSOKU | HINMOKU   | 品目       | （なし） |
| LOGIX_R_KOUFUSOKU | KOUTEI    | 工程       | （なし） |
| LOGIX_R_KOUFUSOKU | VENDOR    | 仕入先     | （なし） |

## テーブル: LOGIX_R_MKADOU

| テーブル名     | 列ID     | 列名       | 備考     |
|:---------------|:---------|:-----------|:---------|
| LOGIX_R_MKADOU | BKTNO    | バケットNo | （なし） |
| LOGIX_R_MKADOU | BKTYEAR  | バケット年 | （なし） |
| LOGIX_R_MKADOU | DATED    | 日付       | （なし） |
| LOGIX_R_MKADOU | KADOU_CD | 稼働時間帯 | （なし） |
| LOGIX_R_MKADOU | MAN      | 生産人員Ｇ | （なし） |
| LOGIX_R_MKADOU | YOUBI    | 曜日       | （なし） |

## テーブル: LOGIX_R_MKADOU2

| テーブル名      | 列ID     | 列名       | 備考     |
|:----------------|:---------|:-----------|:---------|
| LOGIX_R_MKADOU2 | BKTNO    | バケットNo | （なし） |
| LOGIX_R_MKADOU2 | BKTYEAR  | バケット年 | （なし） |
| LOGIX_R_MKADOU2 | DATED    | 日付       | （なし） |
| LOGIX_R_MKADOU2 | KADOU_CD | 稼働時間帯 | （なし） |
| LOGIX_R_MKADOU2 | MAN      | 生産人員Ｇ | （なし） |
| LOGIX_R_MKADOU2 | YOUBI    | 曜日       | （なし） |

## テーブル: LOGIX_R_ORDERNO

| テーブル名      | 列ID      | 列名       | 備考     |
|:----------------|:----------|:-----------|:---------|
| LOGIX_R_ORDERNO | BKTNO     | バケットNo | （なし） |
| LOGIX_R_ORDERNO | BKTYEAR   | バケット年 | （なし） |
| LOGIX_R_ORDERNO | ID_NO     | ID         | （なし） |
| LOGIX_R_ORDERNO | ORDER_NO  |            | （なし） |
| LOGIX_R_ORDERNO | ORDER_NO2 |            | （なし） |

## テーブル: LOGIX_R_ORDERNO2

| テーブル名       | 列ID     | 列名         | 備考     |
|:-----------------|:---------|:-------------|:---------|
| LOGIX_R_ORDERNO2 | BKTNO    | バケットNo   | （なし） |
| LOGIX_R_ORDERNO2 | BKTYEAR  | バケット年   | （なし） |
| LOGIX_R_ORDERNO2 | ID_NO    | ID           | （なし） |
| LOGIX_R_ORDERNO2 | LAST_OD1 | 最終オーダNo | （なし） |
| LOGIX_R_ORDERNO2 | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: LOGIX_R_SAGYOU

| テーブル名     | 列ID          | 列名                         | 備考                |
|:---------------|:--------------|:-----------------------------|:--------------------|
| LOGIX_R_SAGYOU | AKAISHI       | 開始予定時間(時分)           | （なし）            |
| LOGIX_R_SAGYOU | AM_SETUP      | 人後段取時間（人時）         | （なし）            |
| LOGIX_R_SAGYOU | ASETUP        | 後段取時間                   | （なし）            |
| LOGIX_R_SAGYOU | BKTNO         | バケットNo                   | （なし）            |
| LOGIX_R_SAGYOU | BKTYEAR       | バケット年                   | （なし）            |
| LOGIX_R_SAGYOU | CYCLETIME     | サイクルタイム(秒)           | （なし）            |
| LOGIX_R_SAGYOU | DATED         | 指示日                       | （なし）            |
| LOGIX_R_SAGYOU | DATED2        | 外注納期                     | （なし）            |
| LOGIX_R_SAGYOU | EDABAN        | 枝番                         | （なし）            |
| LOGIX_R_SAGYOU | ENDTDAY       | 完了日                       | （なし）            |
| LOGIX_R_SAGYOU | ENDTIME       | 完了時間(時分)               | （なし）            |
| LOGIX_R_SAGYOU | FURYOSU       | 不良数                       | （なし）            |
| LOGIX_R_SAGYOU | HINMOKU       | 品目                         | （なし）            |
| LOGIX_R_SAGYOU | J_LOSS        | 指示ロス量                   | （なし）            |
| LOGIX_R_SAGYOU | JUNJO         | 順序                         | （なし）            |
| LOGIX_R_SAGYOU | KADOU         | 稼働時間(分)                 | （なし）            |
| LOGIX_R_SAGYOU | KADOU_ST_DATE | 稼働開始日                   | （なし）            |
| LOGIX_R_SAGYOU | KADOU_ST_TIME | 稼働開始時間(時分)           | （なし）            |
| LOGIX_R_SAGYOU | KAISHI        | 開始予定時間(相対時間(時分)) | （なし）            |
| LOGIX_R_SAGYOU | KAN_F         | 完了Ｆ                       | 0;"未完了";1;"完了" |
| LOGIX_R_SAGYOU | KANSEISU      | 完成数                       | （なし）            |
| LOGIX_R_SAGYOU | KBUNNOUDAY    | 生産日(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU | KBUNNOUSU     | 生産数(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU | KBUNNOUTIME   | 生産終了時間(TMP)            | （なし）            |
| LOGIX_R_SAGYOU | KFURYOUSU     | 不良数(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU | KJININSU      | 生産人員数(TMP)              | （なし）            |
| LOGIX_R_SAGYOU | KOUTEI        | 工程                         | （なし）            |
| LOGIX_R_SAGYOU | KSTARTTIME    | 生産開始時間(TMP)            | （なし）            |
| LOGIX_R_SAGYOU | KTANID        | 担当者(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU | LEVELD        | ﾚﾍﾞﾙ                         | （なし）            |
| LOGIX_R_SAGYOU | LINED         | 指示ライン                   | （なし）            |
| LOGIX_R_SAGYOU | M_KADOU       | 人稼働時間（人時）           | （なし）            |
| LOGIX_R_SAGYOU | M_SETUP       | 人段取時間（人時）           | （なし）            |
| LOGIX_R_SAGYOU | NAI_F         | 確定/内示Ｆ                  | 0;"内示";1;"確定"   |
| LOGIX_R_SAGYOU | NEEDSU        | 必要数                       | （なし）            |
| LOGIX_R_SAGYOU | NOUKI         | 完了予定日                   | （なし）            |
| LOGIX_R_SAGYOU | NOUKITIME     | 完了予定時間(時分)           | （なし）            |
| LOGIX_R_SAGYOU | ORDERNO       | オーダNo                     | （なし）            |
| LOGIX_R_SAGYOU | PRN_F         | 印刷Ｆ                       | 0;"未完了";1;"完了" |
| LOGIX_R_SAGYOU | SEIBAN        | 製番                         | （なし）            |
| LOGIX_R_SAGYOU | SEIBAN_F      | 製番管理Ｆ                   | （なし）            |
| LOGIX_R_SAGYOU | SETUP         | 段取時間(分)                 | （なし）            |
| LOGIX_R_SAGYOU | SIJISU        | 指示数                       | （なし）            |
| LOGIX_R_SAGYOU | STARTDAY      | 開始日                       | （なし）            |
| LOGIX_R_SAGYOU | STARTTIME     | 開始時間(時分)               | （なし）            |
| LOGIX_R_SAGYOU | TMP_F         | 一括登録F                    | 0;しない;1;する     |
| LOGIX_R_SAGYOU | TORDER_F      | 追加Ｆ(未使用)               | 0;"未完了";1;"完了" |
| LOGIX_R_SAGYOU | VENDOR        | 仕入先                       | （なし）            |
| LOGIX_R_SAGYOU | Y_LOSS        | 展開ロス量                   | （なし）            |

## テーブル: LOGIX_R_SAGYOU2

| テーブル名      | 列ID          | 列名                         | 備考                |
|:----------------|:--------------|:-----------------------------|:--------------------|
| LOGIX_R_SAGYOU2 | AKAISHI       | 開始予定時間(時分)           | （なし）            |
| LOGIX_R_SAGYOU2 | AM_SETUP      | 人後段取時間（人時）         | （なし）            |
| LOGIX_R_SAGYOU2 | ASETUP        | 後段取時間                   | （なし）            |
| LOGIX_R_SAGYOU2 | BKTNO         | バケットNo                   | （なし）            |
| LOGIX_R_SAGYOU2 | BKTYEAR       | バケット年                   | （なし）            |
| LOGIX_R_SAGYOU2 | CYCLETIME     | サイクルタイム(秒)           | （なし）            |
| LOGIX_R_SAGYOU2 | DATED         | 指示日                       | （なし）            |
| LOGIX_R_SAGYOU2 | DATED2        | 外注納期                     | （なし）            |
| LOGIX_R_SAGYOU2 | EDABAN        | 枝番                         | （なし）            |
| LOGIX_R_SAGYOU2 | ENDTDAY       | 完了日                       | （なし）            |
| LOGIX_R_SAGYOU2 | ENDTIME       | 完了時間(時分)               | （なし）            |
| LOGIX_R_SAGYOU2 | FURYOSU       | 不良数                       | （なし）            |
| LOGIX_R_SAGYOU2 | HINMOKU       | 品目                         | （なし）            |
| LOGIX_R_SAGYOU2 | J_LOSS        | 指示ロス量                   | （なし）            |
| LOGIX_R_SAGYOU2 | JUNJO         | 順序                         | （なし）            |
| LOGIX_R_SAGYOU2 | KADOU         | 稼働時間(分)                 | （なし）            |
| LOGIX_R_SAGYOU2 | KADOU_ST_DATE | 稼働開始日                   | （なし）            |
| LOGIX_R_SAGYOU2 | KADOU_ST_TIME | 稼働開始時間(時分)           | （なし）            |
| LOGIX_R_SAGYOU2 | KAISHI        | 開始予定時間(相対時間(時分)) | （なし）            |
| LOGIX_R_SAGYOU2 | KAN_F         | 完了Ｆ                       | 0;"未完了";1;"完了" |
| LOGIX_R_SAGYOU2 | KANSEISU      | 完成数                       | （なし）            |
| LOGIX_R_SAGYOU2 | KBUNNOUDAY    | 生産日(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU2 | KBUNNOUSU     | 生産数(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU2 | KBUNNOUTIME   | 生産終了時間(TMP)            | （なし）            |
| LOGIX_R_SAGYOU2 | KFURYOUSU     | 不良数(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU2 | KJININSU      | 生産人員数(TMP)              | （なし）            |
| LOGIX_R_SAGYOU2 | KOUTEI        | 工程                         | （なし）            |
| LOGIX_R_SAGYOU2 | KSTARTTIME    | 生産開始時間(TMP)            | （なし）            |
| LOGIX_R_SAGYOU2 | KTANID        | 担当者(TMP)                  | （なし）            |
| LOGIX_R_SAGYOU2 | LEVELD        | ﾚﾍﾞﾙ                         | （なし）            |
| LOGIX_R_SAGYOU2 | LINED         | 指示ライン                   | （なし）            |
| LOGIX_R_SAGYOU2 | M_KADOU       | 人稼働時間（人時）           | （なし）            |
| LOGIX_R_SAGYOU2 | M_SETUP       | 人段取時間（人時）           | （なし）            |
| LOGIX_R_SAGYOU2 | NAI_F         | 確定/内示Ｆ                  | 0;"内示";1;"確定"   |
| LOGIX_R_SAGYOU2 | NEEDSU        | 必要数                       | （なし）            |
| LOGIX_R_SAGYOU2 | NOUKI         | 完了予定日                   | （なし）            |
| LOGIX_R_SAGYOU2 | NOUKITIME     | 完了予定時間(時分)           | （なし）            |
| LOGIX_R_SAGYOU2 | ORDERNO       | オーダNo                     | （なし）            |
| LOGIX_R_SAGYOU2 | PRN_F         | 印刷Ｆ                       | 0;"未完了";1;"完了" |
| LOGIX_R_SAGYOU2 | SEIBAN        | 製番                         | （なし）            |
| LOGIX_R_SAGYOU2 | SEIBAN_F      | 製番管理Ｆ                   | （なし）            |
| LOGIX_R_SAGYOU2 | SETUP         | 段取時間(分)                 | （なし）            |
| LOGIX_R_SAGYOU2 | SIJISU        | 指示数                       | （なし）            |
| LOGIX_R_SAGYOU2 | STARTDAY      | 開始日                       | （なし）            |
| LOGIX_R_SAGYOU2 | STARTTIME     | 開始時間(時分)               | （なし）            |
| LOGIX_R_SAGYOU2 | TMP_F         | 一括登録F                    | 0;しない;1;する     |
| LOGIX_R_SAGYOU2 | TORDER_F      | 追加Ｆ(未使用)               | 0;"未完了";1;"完了" |
| LOGIX_R_SAGYOU2 | UPDATEF       | UPDATEF                      | （なし）            |
| LOGIX_R_SAGYOU2 | VENDOR        | 仕入先                       | （なし）            |
| LOGIX_R_SAGYOU2 | Y_LOSS        | 展開ロス量                   | （なし）            |

## テーブル: LOGIX_S_BUNNOU

| テーブル名     | 列ID       | 列名         | 備考     |
|:---------------|:-----------|:-------------|:---------|
| LOGIX_S_BUNNOU | BUNNOUDAY  | 生産日       | （なし） |
| LOGIX_S_BUNNOU | BUNNOUSU   | 生産数       | （なし） |
| LOGIX_S_BUNNOU | BUNNOUTIME | 生産終了時間 | （なし） |
| LOGIX_S_BUNNOU | FURYOUSU   | 不良数       | （なし） |
| LOGIX_S_BUNNOU | JININSU    | 生産人員数   | （なし） |
| LOGIX_S_BUNNOU | ORDERNO    | オーダNo     | （なし） |
| LOGIX_S_BUNNOU | STARTTIME  | 生産開始時間 | （なし） |
| LOGIX_S_BUNNOU | TANID      | 担当者       | （なし） |

## テーブル: LOGIX_T_BUCKET

| テーブル名     | 列ID     | 列名               | 備考            |
|:---------------|:---------|:-------------------|:----------------|
| LOGIX_T_BUCKET | BKTNO    | バケットNo         | （なし）        |
| LOGIX_T_BUCKET | BKTYEAR  | バケット年         | （なし）        |
| LOGIX_T_BUCKET | ENDDAY   | ﾊﾞｹｯﾄ最終日        | （なし）        |
| LOGIX_T_BUCKET | ENTRY    | 登録日             | （なし）        |
| LOGIX_T_BUCKET | RADISH   | 受注取込最終日     | （なし）        |
| LOGIX_T_BUCKET | SCHEDULE | スケジュール最終日 | （なし）        |
| LOGIX_T_BUCKET | SEIORDER | 作業指示確定F      | 0;未完了;1;完了 |
| LOGIX_T_BUCKET | STARTDAY | バケット開始日     | （なし）        |

## テーブル: LOGIX_T_HIKIATE

| テーブル名      | 列ID       | 列名       | 備考     |
|:----------------|:-----------|:-----------|:---------|
| LOGIX_T_HIKIATE | BKTNO      | バケットNo | （なし） |
| LOGIX_T_HIKIATE | BKTYEAR    | バケット年 | （なし） |
| LOGIX_T_HIKIATE | CH_AKAISHI | CH_AKAISHI | （なし） |
| LOGIX_T_HIKIATE | CH_DATED   | CH_DATED   | （なし） |
| LOGIX_T_HIKIATE | CH_HINMOKU | CH_HINMOKU | （なし） |
| LOGIX_T_HIKIATE | CH_KOUTEI  | CH_KOUTEI  | （なし） |
| LOGIX_T_HIKIATE | CH_LEVELED | CH_LEVELED | （なし） |
| LOGIX_T_HIKIATE | CH_LINED   | CH_LINED   | （なし） |
| LOGIX_T_HIKIATE | CH_ORDERNO | CH_ORDERNO | （なし） |
| LOGIX_T_HIKIATE | CH_SEIBANF | CH_SEIBANF | （なし） |
| LOGIX_T_HIKIATE | CH_SIJISU  | CH_SIJISU  | （なし） |
| LOGIX_T_HIKIATE | CH_TANI    | CH_TANI    | （なし） |
| LOGIX_T_HIKIATE | HIKIATEFLG | HIKIATEFLG | （なし） |
| LOGIX_T_HIKIATE | HIKIATESU  | HIKIATESU  | （なし） |
| LOGIX_T_HIKIATE | PA_AKAISHI | PA_AKAISHI | （なし） |
| LOGIX_T_HIKIATE | PA_DATED   | PA_DATED   | （なし） |
| LOGIX_T_HIKIATE | PA_EDABAN  | PA_EDABAN  | （なし） |
| LOGIX_T_HIKIATE | PA_HINMOKU | PA_HINMOKU | （なし） |
| LOGIX_T_HIKIATE | PA_KOUTEI  | PA_KOUTEI  | （なし） |
| LOGIX_T_HIKIATE | PA_LEVELED | PA_LEVELED | （なし） |
| LOGIX_T_HIKIATE | PA_LINED   | PA_LINED   | （なし） |
| LOGIX_T_HIKIATE | PA_NO      | PA_NO      | （なし） |
| LOGIX_T_HIKIATE | PA_ORDERNO | PA_ORDERNO | （なし） |
| LOGIX_T_HIKIATE | PA_SEIBAN  | PA_SEIBAN  | （なし） |
| LOGIX_T_HIKIATE | PA_SEIBANF | PA_SEIBANF | （なし） |
| LOGIX_T_HIKIATE | PA_SIJISU  | PA_SIJISU  | （なし） |
| LOGIX_T_HIKIATE | PA_TANI    | PA_TANI    | （なし） |

## テーブル: LOGIX_T_KADOU

| テーブル名    | 列ID      | 列名            | 備考                                    |
|:--------------|:----------|:----------------|:----------------------------------------|
| LOGIX_T_KADOU | BKTNO     | バケットNo      | （なし）                                |
| LOGIX_T_KADOU | BKTYEAR   | バケット年      | （なし）                                |
| LOGIX_T_KADOU | DATED     | 日付            | （なし）                                |
| LOGIX_T_KADOU | KADOU_CD  | 稼働時間帯      | （なし）                                |
| LOGIX_T_KADOU | KOURITU   | 有効時間比率(%) | （なし）                                |
| LOGIX_T_KADOU | KOUTEI    | 工程            | （なし）                                |
| LOGIX_T_KADOU | LINED     | ライン          | （なし）                                |
| LOGIX_T_KADOU | SOGYOOP   | 操業最適化      | 0;"しない";1;"する"                     |
| LOGIX_T_KADOU | ZANGYOKA  | 操業モード      | 0;"定時";1;"定時＋残業";2;"休日出勤"    |
| LOGIX_T_KADOU | ZANGYOU_F | 残業Ｆ          | 0;"残業・休出しない";1;"残業・休出する" |

## テーブル: LOGIX_T_KOTEI

| テーブル名    | 列ID      | 列名       | 備考     |
|:--------------|:----------|:-----------|:---------|
| LOGIX_T_KOTEI | BKTNO     | バケットNo | （なし） |
| LOGIX_T_KOTEI | BKTYEAR   | バケット年 | （なし） |
| LOGIX_T_KOTEI | EDABAN    | 枝番       | （なし） |
| LOGIX_T_KOTEI | HINMOKU   | 品目       | （なし） |
| LOGIX_T_KOTEI | K_DATE    | 固定日     | （なし） |
| LOGIX_T_KOTEI | KAN_F     | 完了F      | （なし） |
| LOGIX_T_KOTEI | KANSEI_SU | 完成数     | （なし） |
| LOGIX_T_KOTEI | KOSUU     | 固定数     | （なし） |
| LOGIX_T_KOTEI | KOUTEI    | 工程       | （なし） |
| LOGIX_T_KOTEI | LINED     | ライン     | （なし） |
| LOGIX_T_KOTEI | SEIBAN    | 製番       | （なし） |
| LOGIX_T_KOTEI | STARTD    | 開始日     | （なし） |
| LOGIX_T_KOTEI | VENDOR    | 仕入先     | （なし） |

## テーブル: LOGIX_T_LINERIREKI

| テーブル名         | 列ID     | 列名          | 備考     |
|:-------------------|:---------|:--------------|:---------|
| LOGIX_T_LINERIREKI | BKTNO    | バケットNo    | （なし） |
| LOGIX_T_LINERIREKI | BKTYEAR  | バケット年    | （なし） |
| LOGIX_T_LINERIREKI | FUKARITU | 計画稼働率(%) | （なし） |
| LOGIX_T_LINERIREKI | KOUTEI   | 工程          | （なし） |
| LOGIX_T_LINERIREKI | LINED    | ライン        | （なし） |

## テーブル: LOGIX_T_SHOYO

| テーブル名    | 列ID     | 列名                   | 備考     |
|:--------------|:---------|:-----------------------|:---------|
| LOGIX_T_SHOYO | BKTMAE   | ﾊﾞｹｯﾄ期間所要量        | （なし） |
| LOGIX_T_SHOYO | BKTNO    | バケットNo             | （なし） |
| LOGIX_T_SHOYO | BKTYEAR  | バケット年             | （なし） |
| LOGIX_T_SHOYO | HINMOKU  | 品目                   | （なし） |
| LOGIX_T_SHOYO | KOUTEI   | 工程                   | （なし） |
| LOGIX_T_SHOYO | SCHEDULE | スケジュール期間所要量 | （なし） |
| LOGIX_T_SHOYO | VENDOR   | 仕入先                 | （なし） |

## テーブル: LOGIX_T_SHOYOMEISAI

| テーブル名          | 列ID    | 列名       | 備考     |
|:--------------------|:--------|:-----------|:---------|
| LOGIX_T_SHOYOMEISAI | BKTNO   | バケットNo | （なし） |
| LOGIX_T_SHOYOMEISAI | BKTYEAR | バケット年 | （なし） |
| LOGIX_T_SHOYOMEISAI | DATED   | 日付       | （なし） |
| LOGIX_T_SHOYOMEISAI | HINMOKU | 品目       | （なし） |
| LOGIX_T_SHOYOMEISAI | KOUTEI  | 工程       | （なし） |
| LOGIX_T_SHOYOMEISAI | SUURYO  | 数量       | （なし） |
| LOGIX_T_SHOYOMEISAI | VENDOR  | 仕入先     | （なし） |

## テーブル: LOGIX_T_YAMA

| テーブル名   | 列ID    | 列名       | 備考     |
|:-------------|:--------|:-----------|:---------|
| LOGIX_T_YAMA | BKTNO   | バケットNo | （なし） |
| LOGIX_T_YAMA | BKTYEAR | バケット年 | （なし） |
| LOGIX_T_YAMA | DATED   | 日付       | （なし） |
| LOGIX_T_YAMA | HINMOKU | 品目       | （なし） |
| LOGIX_T_YAMA | KOUTEI  | 工程       | （なし） |
| LOGIX_T_YAMA | OD      | オーダ数   | （なし） |
| LOGIX_T_YAMA | RD      | 必要数     | （なし） |
| LOGIX_T_YAMA | VENDOR  | 仕入先     | （なし） |
| LOGIX_T_YAMA | ZAIKO   | 在庫数     | （なし） |

## テーブル: LOGIX_Z_HORYUZAIKO

| テーブル名         | 列ID     | 列名       | 備考     |
|:-------------------|:---------|:-----------|:---------|
| LOGIX_Z_HORYUZAIKO | BKTNO    | バケットNo | （なし） |
| LOGIX_Z_HORYUZAIKO | BKTYEAR  | バケット年 | （なし） |
| LOGIX_Z_HORYUZAIKO | HINMOKU  | 品目       | （なし） |
| LOGIX_Z_HORYUZAIKO | HORYUDAY | 保留解除日 | （なし） |
| LOGIX_Z_HORYUZAIKO | HORYUSUU | 保留在庫数 | （なし） |
| LOGIX_Z_HORYUZAIKO | KOUTEI   | 工程       | （なし） |
| LOGIX_Z_HORYUZAIKO | VENDOR   | 仕入先     | （なし） |

## テーブル: LOGIX_Z_SEIBANMEI

| テーブル名        | 列ID       | 列名       | 備考                                                         |
|:------------------|:-----------|:-----------|:-------------------------------------------------------------|
| LOGIX_Z_SEIBANMEI | BKTNO      | バケットNo | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | BKTYEAR    | バケット年 | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | EDABAN     | 枝番       | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | HINMOKU    | 品目       | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | KAN_F      | 完了Ｆ     | 0;"生産途中";1;"生産完了、消費未完了";2;"生産完了、消費完了" |
| LOGIX_Z_SEIBANMEI | KANOUTIME  | 可能時間   | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | KANSEI     | 完成数     | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | KOUTEI     | 工程       | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | LEVELD     | レベル     | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | LEVELJUN   | レベル順   | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | LINED      | 指示ライン | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | LOSS       | ロス       | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | MAE_HIN_NO | 前品番     | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | SEIBAN     | 製番       | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | SHOUHI     | 消費数     | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | TOUNYU     | 指示数     | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | VENDOR     | 仕入先     | （なし）                                                     |
| LOGIX_Z_SEIBANMEI | YOTEI      | 予定日     | （なし）                                                     |

## テーブル: LOGIX_Z_SEIBANZAIKO

| テーブル名          | 列ID      | 列名       | 備考                                                                                         |
|:--------------------|:----------|:-----------|:---------------------------------------------------------------------------------------------|
| LOGIX_Z_SEIBANZAIKO | BKTNO     | バケットNo | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | BKTYEAR   | バケット年 | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | EDABAN    | 枝番       | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | HINMOKU   | 品目       | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | KAN_F     | 完了Ｆ     | -2;内示分引当残在庫;-1;内示分引当在庫;0;生産途中;1;生産完了、消費未完了;2;生産完了、消費完了 |
| LOGIX_Z_SEIBANZAIKO | KANOUTIME | 可能時間   | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | KANSEI    | 完成数     | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | KOUTEI    | 工程       | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | LINED     | 指示ライン | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | SEIBAN    | 製番       | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | SHOUHI    | 消費数     | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | TOUNYU    | 指示数     | （なし）                                                                                     |
| LOGIX_Z_SEIBANZAIKO | VENDOR    | 仕入先     | （なし）                                                                                     |

## テーブル: LOGIX_Z_SYOKIZAIKO

| テーブル名         | 列ID    | 列名       | 備考     |
|:-------------------|:--------|:-----------|:---------|
| LOGIX_Z_SYOKIZAIKO | BKTNO   | バケットNo | （なし） |
| LOGIX_Z_SYOKIZAIKO | BKTYEAR | バケット年 | （なし） |
| LOGIX_Z_SYOKIZAIKO | HINMOKU | 品目       | （なし） |
| LOGIX_Z_SYOKIZAIKO | KOUTEI  | 工程       | （なし） |
| LOGIX_Z_SYOKIZAIKO | VENDOR  | 仕入先     | （なし） |
| LOGIX_Z_SYOKIZAIKO | ZAIKO   | 在庫数     | （なし） |

## テーブル: LOGIX_Z_ZAIKOGANT

| テーブル名        | 列ID    | 列名       | 備考     |
|:------------------|:--------|:-----------|:---------|
| LOGIX_Z_ZAIKOGANT | BKTNO   | バケットNo | （なし） |
| LOGIX_Z_ZAIKOGANT | BKTYEAR | バケット年 | （なし） |
| LOGIX_Z_ZAIKOGANT | DATED   | 指示日     | （なし） |
| LOGIX_Z_ZAIKOGANT | HINMOKU | 品目       | （なし） |
| LOGIX_Z_ZAIKOGANT | KOUTEI  | 工程       | （なし） |
| LOGIX_Z_ZAIKOGANT | LINED   | 指示ライン | （なし） |
| LOGIX_Z_ZAIKOGANT | SEISAN  | 生産数     | （なし） |
| LOGIX_Z_ZAIKOGANT | SHOUHI  | 消費数     | （なし） |
| LOGIX_Z_ZAIKOGANT | SHOYOU  | 所要量     | （なし） |
| LOGIX_Z_ZAIKOGANT | VENDOR  | 仕入先     | （なし） |
| LOGIX_Z_ZAIKOGANT | ZAIKO   | 在庫数     | （なし） |

## テーブル: LOSS_HISTORY

| テーブル名   | 列ID      | 列名         | 備考                       |
|:-------------|:----------|:-------------|:---------------------------|
| LOSS_HISTORY | ACTFNTIME | 生産終了日時 | （なし）                   |
| LOSS_HISTORY | ACTSTDATE | 生産日       | （なし）                   |
| LOSS_HISTORY | ACTSTTIME | 生産開始日時 | （なし）                   |
| LOSS_HISTORY | COUNTER   | 内部登録No   | 'PRODUCT_HISTORYよりセット |
| LOSS_HISTORY | FCDTY     | タイプ       | （なし）                   |
| LOSS_HISTORY | FCODE     | コード       | （なし）                   |
| LOSS_HISTORY | ITEM      | 品目         | （なし）                   |
| LOSS_HISTORY | OEE_LINED | 実績ライン   | （なし）                   |
| LOSS_HISTORY | PROCESS   | 工程         | （なし）                   |
| LOSS_HISTORY | RGSTD     | 登録日       | YYYY/MM/DD HH;MM;SS        |
| LOSS_HISTORY | RGSTWKCD  | 登録担当者   | （なし）                   |
| LOSS_HISTORY | SHIFTF    | 直区分       | 1;1直;2;2直;3;3直          |
| LOSS_HISTORY | VENDOR    | 仕入先       | （なし）                   |

## テーブル: MC_CHORDER

| テーブル名   | 列ID         | 列名       | 備考                    |
|:-------------|:-------------|:-----------|:------------------------|
| MC_CHORDER   | BKTNO        | バケットNo | （なし）                |
| MC_CHORDER   | BKTYEAR      | バケット年 | （なし）                |
| MC_CHORDER   | CHANGEDATE   | 変更納期   | （なし）                |
| MC_CHORDER   | CHANGEDAY    | 変更日数   | （なし）                |
| MC_CHORDER   | DELAYPROCESS | 遅れ工程   | （なし）                |
| MC_CHORDER   | ITEM         | 品目       | （なし）                |
| MC_CHORDER   | MCORDERNO    | オーダNo   | （なし）                |
| MC_CHORDER   | PLANDATE     | 計画納期   | （なし）                |
| MC_CHORDER   | PRCD_F       | 先行Ｆ     | 0;納期後倒し;1;先行する |
| MC_CHORDER   | PRDCTBNO     | 枝番       | （なし）                |
| MC_CHORDER   | PRDCTNO      | 製番       | （なし）                |
| MC_CHORDER   | PRDCTQTY     | 受注数     | （なし）                |
| MC_CHORDER   | PROCESS      | 工程       | （なし）                |
| MC_CHORDER   | RCORDERNO    | 受注No     | （なし）                |
| MC_CHORDER   | REPDELIDATE  | 回答納期   | （なし）                |
| MC_CHORDER   | RGSTD        | 登録日     | （なし）                |
| MC_CHORDER   | STARTDATE    | 着手可能日 | （なし）                |
| MC_CHORDER   | UPDTD        | 更新日     | （なし）                |
| MC_CHORDER   | UPDTWKCD     | 更新担当者 | （なし）                |
| MC_CHORDER   | VENDOR       | 仕入先     | （なし）                |

## テーブル: MC_DLLEQUIPMENTM

| テーブル名       | 列ID      | 列名           | 備考     |
|:-----------------|:----------|:---------------|:---------|
| MC_DLLEQUIPMENTM | BKTNO     | バケットNo     | （なし） |
| MC_DLLEQUIPMENTM | BKTYEAR   | バケット年     | （なし） |
| MC_DLLEQUIPMENTM | DATED     | 日付           | （なし） |
| MC_DLLEQUIPMENTM | LINED     | ライン         | （なし） |
| MC_DLLEQUIPMENTM | LOADTIME  | 負荷時間(時間) | （なし） |
| MC_DLLEQUIPMENTM | LOSSTIME  | ロス時間(時間) | （なし） |
| MC_DLLEQUIPMENTM | PRDCTTIME | 稼働時間(時間) | （なし） |
| MC_DLLEQUIPMENTM | PROCESS   | 工程           | （なし） |
| MC_DLLEQUIPMENTM | RGSTD     | 登録日         | （なし） |
| MC_DLLEQUIPMENTM | SETUPTIME | 段取時間(時間) | （なし） |
| MC_DLLEQUIPMENTM | UPDTD     | 更新日         | （なし） |
| MC_DLLEQUIPMENTM | UPDTWKCD  | 更新担当者     | （なし） |

## テーブル: MC_DLLEQUIPMENTS

| テーブル名       | 列ID      | 列名           | 備考     |
|:-----------------|:----------|:---------------|:---------|
| MC_DLLEQUIPMENTS | BKTNO     | バケットNo     | （なし） |
| MC_DLLEQUIPMENTS | BKTYEAR   | バケット年     | （なし） |
| MC_DLLEQUIPMENTS | DATED     | 日付           | （なし） |
| MC_DLLEQUIPMENTS | LINED     | ライン         | （なし） |
| MC_DLLEQUIPMENTS | LOADTIME  | 負荷時間(時間) | （なし） |
| MC_DLLEQUIPMENTS | LOSSTIME  | ロス時間(時間) | （なし） |
| MC_DLLEQUIPMENTS | PRDCTTIME | 稼働時間(時間) | （なし） |
| MC_DLLEQUIPMENTS | PROCESS   | 工程           | （なし） |
| MC_DLLEQUIPMENTS | RGSTD     | 登録日         | （なし） |
| MC_DLLEQUIPMENTS | SETUPTIME | 段取時間(時間) | （なし） |
| MC_DLLEQUIPMENTS | UPDTD     | 更新日         | （なし） |
| MC_DLLEQUIPMENTS | UPDTWKCD  | 更新担当者     | （なし） |

## テーブル: MC_LLEQUIPMENTM

| テーブル名      | 列ID        | 列名                             | 備考     |
|:----------------|:------------|:---------------------------------|:---------|
| MC_LLEQUIPMENTM | B_LOSSTIME  | バケット期間ロス時間(時間)       | （なし） |
| MC_LLEQUIPMENTM | B_PRDCTTIME | バケット期間稼働時間(時間)       | （なし） |
| MC_LLEQUIPMENTM | B_SETUPTIME | バケット期間段取時間(時間)       | （なし） |
| MC_LLEQUIPMENTM | B_TOTALTIME | バケット期間総負荷時間(時間)     | （なし） |
| MC_LLEQUIPMENTM | BKTNO       | バケットNo                       | （なし） |
| MC_LLEQUIPMENTM | BKTYEAR     | バケット年                       | （なし） |
| MC_LLEQUIPMENTM | LINED       | ライン                           | （なし） |
| MC_LLEQUIPMENTM | PROCESS     | 工程                             | （なし） |
| MC_LLEQUIPMENTM | RGSTD       | 登録日                           | （なし） |
| MC_LLEQUIPMENTM | S_LOSSTIME  | スケジュール期間ロス時間(時間)   | （なし） |
| MC_LLEQUIPMENTM | S_PRDCTTIME | スケジュール期間稼働時間(時間)   | （なし） |
| MC_LLEQUIPMENTM | S_SETUPTIME | スケジュール期間段取時間(時間)   | （なし） |
| MC_LLEQUIPMENTM | S_TOTALTIME | スケジュール期間総負荷時間(時間) | （なし） |
| MC_LLEQUIPMENTM | SERIALNO    | シリアルNo                       | （なし） |
| MC_LLEQUIPMENTM | UPDTD       | 更新日                           | （なし） |
| MC_LLEQUIPMENTM | UPDTWKCD    | 更新担当者                       | （なし） |

## テーブル: MC_LLEQUIPMENTS

| テーブル名      | 列ID        | 列名                             | 備考     |
|:----------------|:------------|:---------------------------------|:---------|
| MC_LLEQUIPMENTS | B_LOSSTIME  | バケット期間ロス時間(時間)       | （なし） |
| MC_LLEQUIPMENTS | B_PRDCTTIME | バケット期間稼働時間(時間)       | （なし） |
| MC_LLEQUIPMENTS | B_SETUPTIME | バケット期間段取時間(時間)       | （なし） |
| MC_LLEQUIPMENTS | B_TOTALTIME | バケット期間総負荷時間(時間)     | （なし） |
| MC_LLEQUIPMENTS | BKTNO       | バケットNo                       | （なし） |
| MC_LLEQUIPMENTS | BKTYEAR     | バケット年                       | （なし） |
| MC_LLEQUIPMENTS | LINED       | ライン                           | （なし） |
| MC_LLEQUIPMENTS | PROCESS     | 工程                             | （なし） |
| MC_LLEQUIPMENTS | RGSTD       | 登録日                           | （なし） |
| MC_LLEQUIPMENTS | S_LOSSTIME  | スケジュール期間ロス時間(時間)   | （なし） |
| MC_LLEQUIPMENTS | S_PRDCTTIME | スケジュール期間稼働時間(時間)   | （なし） |
| MC_LLEQUIPMENTS | S_SETUPTIME | スケジュール期間段取時間(時間)   | （なし） |
| MC_LLEQUIPMENTS | S_TOTALTIME | スケジュール期間総負荷時間(時間) | （なし） |
| MC_LLEQUIPMENTS | SERIALNO    | シリアルNo                       | （なし） |
| MC_LLEQUIPMENTS | UPDTD       | 更新日                           | （なし） |
| MC_LLEQUIPMENTS | UPDTWKCD    | 更新担当者                       | （なし） |

## テーブル: MC_LLPROCESS

| テーブル名   | 列ID        | 列名                             | 備考     |
|:-------------|:------------|:---------------------------------|:---------|
| MC_LLPROCESS | B_PRDCTQTY  | バケット期間生産数               | （なし） |
| MC_LLPROCESS | B_PRDCTTIME | バケット期間生産時間（時間）     | （なし） |
| MC_LLPROCESS | BKTNO       | バケットNo                       | （なし） |
| MC_LLPROCESS | BKTYEAR     | バケット年                       | （なし） |
| MC_LLPROCESS | PROCESS     | 工程                             | （なし） |
| MC_LLPROCESS | RGSTD       | 登録日                           | （なし） |
| MC_LLPROCESS | S_PRDCTQTY  | スケジュール期間生産数           | （なし） |
| MC_LLPROCESS | S_PRDCTTIME | スケジュール期間生産時間（時間） | （なし） |
| MC_LLPROCESS | UPDTD       | 更新日                           | （なし） |
| MC_LLPROCESS | UPDTWKCD    | 更新担当者                       | （なし） |

## テーブル: MPS

| テーブル名   | 列ID         | 列名                 | 備考                                                                                                                       |
|:-------------|:-------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------|
| MPS          | A_CARD_FLG   | カード区分           | （なし）                                                                                                                   |
| MPS          | A_COLOR      | 色指示コード         | （なし）                                                                                                                   |
| MPS          | A_EDI_F      | EDI取込F             | 0;EDI以外;1;YMC20L;2;MORIC;3;YMC01                                                                                         |
| MPS          | A_ODRCD      | 発注方針コード       | （なし）                                                                                                                   |
| MPS          | A_PACKCD     | 荷姿コード           | （なし）                                                                                                                   |
| MPS          | A_PACKNM     | 荷姿名称             | （なし）                                                                                                                   |
| MPS          | A_PACKQTY    | 荷姿収容数           | （なし）                                                                                                                   |
| MPS          | A_PROCESS    | 工程番号             | （なし）                                                                                                                   |
| MPS          | A_STATUS     | 生試区分             | （なし）                                                                                                                   |
| MPS          | A_SUPPLIER   | 供給者               | （なし）                                                                                                                   |
| MPS          | A_SUPPLIERNM | 供給者名称           | （なし）                                                                                                                   |
| MPS          | A_USER       | 使用者               | （なし）                                                                                                                   |
| MPS          | A_USERNM     | 使用者名称           | （なし）                                                                                                                   |
| MPS          | ADDFLG       | 追加Ｆ               | 0;通常;1;追加                                                                                                              |
| MPS          | ASTARTDATE   | 先行着手可能日       | （なし）                                                                                                                   |
| MPS          | BKTNO        | 受注読込バケットNo   | （なし）                                                                                                                   |
| MPS          | BKTYEAR      | 受注読込バケット年   | （なし）                                                                                                                   |
| MPS          | CHANGEDATE   | 変更納期             | （なし）                                                                                                                   |
| MPS          | CUSTOM       | 顧客                 | （なし）                                                                                                                   |
| MPS          | DELAYPROCESS | 遅れ工程             | （なし）                                                                                                                   |
| MPS          | DELIDATE     | 顧客納期             | （なし）                                                                                                                   |
| MPS          | DMTYP        | 需要区分             | 0;独立需要;1;従属需要                                                                                                      |
| MPS          | EDDATE       | 終了日               | （なし）                                                                                                                   |
| MPS          | INVOICENO    | 納品書番号           | （なし）                                                                                                                   |
| MPS          | ITEM         | 品目                 | （なし）                                                                                                                   |
| MPS          | LOCT         | 納入プラットフォーム | （なし）                                                                                                                   |
| MPS          | MOVELV       | 移動LV               | 0;前後倒し;1;前倒し第２優先;2;前倒し第１優先;10;先行ありで前後倒し;11;先行ありで前倒し第２優先;12;先行ありで前倒し第１優先 |
| MPS          | MPSORDERNO   | オーダNo             | （なし）                                                                                                                   |
| MPS          | OFFCLF       | 確定/内示Ｆ          | 0;内示;1;確定                                                                                                              |
| MPS          | ORDERCL      | 受注区分             | 0;新規;-1;受注取消                                                                                                         |
| MPS          | ORDERQTY     | 受注数               | （なし）                                                                                                                   |
| MPS          | PBKTNO       | 生産確定バケットNo   | （なし）                                                                                                                   |
| MPS          | PBKTYEAR     | 生産確定バケット年   | （なし）                                                                                                                   |
| MPS          | PER_DAY      | パー割分割日数       | （なし）                                                                                                                   |
| MPS          | PER_F        | パー割F              | （なし）                                                                                                                   |
| MPS          | PERMODE_F    | パー割モード選択     | （なし）                                                                                                                   |
| MPS          | PLANDATE     | 計画納期             | （なし）                                                                                                                   |
| MPS          | PRDCTBNO     | 枝番                 | （なし）                                                                                                                   |
| MPS          | PRDCTFLG     | 生産確定F            | 0;未確定;1;仕掛中;2;確定                                                                                                   |
| MPS          | PRDCTNO      | 製番                 | （なし）                                                                                                                   |
| MPS          | PROCESS      | 工程                 | （なし）                                                                                                                   |
| MPS          | PROGDATE     | 進捗日付             | 実績入力時、完了日をセット                                                                                                 |
| MPS          | PROGPROCESS  | 仕掛工程             | （なし）                                                                                                                   |
| MPS          | PROGTIME     | 進捗時刻             | 実績入力時、完了時間をセット                                                                                               |
| MPS          | RCORDERNO    | 受注No               | （なし）                                                                                                                   |
| MPS          | REMARK       | 備考                 | （なし）                                                                                                                   |
| MPS          | SORT1        | 山積用ソート１       | （なし）                                                                                                                   |
| MPS          | SORT2        | 山積用ソート２       | （なし）                                                                                                                   |
| MPS          | SORT3        | 山積用ソート３       | （なし）                                                                                                                   |
| MPS          | STARTDATE    | 着手可能日           | （なし）                                                                                                                   |
| MPS          | STATUS       | ステータス           | 0;未着手;1;着手;2;完了                                                                                                     |
| MPS          | STDATE       | 開始日               | （なし）                                                                                                                   |
| MPS          | UPDTD        | 更新日               | （なし）                                                                                                                   |
| MPS          | UPDTWKCD     | 更新担当者           | （なし）                                                                                                                   |
| MPS          | URGENCYFLG   | 山積用特急F          | 0;通常;1;特急;2;超特急                                                                                                     |
| MPS          | VENDOR       | 仕入先               | （なし）                                                                                                                   |

## テーブル: MPS_FORECAST

| テーブル名   | 列ID      | 列名             | 備考          |
|:-------------|:----------|:-----------------|:--------------|
| MPS_FORECAST | CUSTOM    | 顧客             | （なし）      |
| MPS_FORECAST | EDDATE    | 終了日           | （なし）      |
| MPS_FORECAST | ITEM      | 品目             | （なし）      |
| MPS_FORECAST | OFFCLF    | 確定/内示Ｆ      | 0;内示;1;確定 |
| MPS_FORECAST | ORDERQTY  | 受注数           | （なし）      |
| MPS_FORECAST | PER_DAY   | パー割分割日数   | （なし）      |
| MPS_FORECAST | PER_F     | パー割F          | （なし）      |
| MPS_FORECAST | PERMODE_F | パー割モード選択 | （なし）      |
| MPS_FORECAST | PLANDATE  | 計画納期         | （なし）      |
| MPS_FORECAST | PROCESS   | 工程             | （なし）      |
| MPS_FORECAST | RCORDERNO | 受注No           | （なし）      |
| MPS_FORECAST | RGSTD     | 登録日           | （なし）      |
| MPS_FORECAST | STDATE    | 開始日           | （なし）      |
| MPS_FORECAST | UPDTD     | 更新日           | （なし）      |
| MPS_FORECAST | UPDTWKCD  | 更新担当者       | （なし）      |
| MPS_FORECAST | VENDOR    | 仕入先           | （なし）      |

## テーブル: MPS_ORDERNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| MPS_ORDERNO  | K_NO     | キー項目     | （なし） |
| MPS_ORDERNO  | LAST_OD1 | 最終オーダNo | （なし） |
| MPS_ORDERNO  | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: M_BANK

| テーブル名   | 列ID     | 列名                        | 備考     |
|:-------------|:---------|:----------------------------|:---------|
| M_BANK       | ADR      | 住所                        | （なし） |
| M_BANK       | BANKCD   | 銀行コード                  | （なし） |
| M_BANK       | BANKNM   | 銀行名                      | （なし） |
| M_BANK       | CMMS1    | 手数料（振込金額3万円未満） | （なし） |
| M_BANK       | CMMS2    | 手数料（振込金額3万円以上） | （なし） |
| M_BANK       | CMMS3    | 手数料3                     | （なし） |
| M_BANK       | CMMSTYP  | 手数料種別                  | （なし） |
| M_BANK       | FAX      | FAX                         | （なし） |
| M_BANK       | POSTCD   | 郵便番号                    | （なし） |
| M_BANK       | REMARK   | 備考                        | （なし） |
| M_BANK       | RGSTD    | 登録日                      | （なし） |
| M_BANK       | TEL      | TEL                         | （なし） |
| M_BANK       | TERMINAL | 端末情報                    | （なし） |
| M_BANK       | UPDTD    | 更新日                      | （なし） |
| M_BANK       | UPDTWKCD | 更新担当者                  | （なし） |

## テーブル: M_BOM

| テーブル名   | 列ID      | 列名        | 備考                        |
|:-------------|:----------|:------------|:----------------------------|
| M_BOM        | A_FSEQNO  | 出力順序    | （なし）                    |
| M_BOM        | CHK       | チェック    | （なし）                    |
| M_BOM        | HIMQTY    | 親基準数    | （なし）                    |
| M_BOM        | HITEM     | 親品目      | （なし）                    |
| M_BOM        | HPROCESS  | 親工程      | （なし）                    |
| M_BOM        | HVENDOR   | 親仕入先    | （なし）                    |
| M_BOM        | ISSUEQTY  | 出庫数      | （なし）                    |
| M_BOM        | LIMQTY    | 子基準数    | （なし）                    |
| M_BOM        | LITEM     | 子品目      | （なし）                    |
| M_BOM        | LOCT      | 入出庫場所  | （なし）                    |
| M_BOM        | LPROCESS  | 子工程      | （なし）                    |
| M_BOM        | LVENDOR   | 子仕入先    | （なし）                    |
| M_BOM        | ODEDDATE  | 失効日      | （なし）                    |
| M_BOM        | ODSTDATE  | 発効日      | （なし）                    |
| M_BOM        | PHUNIT    | 員数        | （なし）                    |
| M_BOM        | RGSTD     | 登録日      | （なし）                    |
| M_BOM        | SHARERTIO | 共用比率(%) | （なし）                    |
| M_BOM        | SHARETYP  | 共用区分    | （なし）                    |
| M_BOM        | STDPHUNIT | 基準員数    | （なし）                    |
| M_BOM        | SWEDDATE  | 切替失効日  | （なし）                    |
| M_BOM        | SWSTDATE  | 切替発効日  | （なし）                    |
| M_BOM        | UNITTYP   | 員数区分    | 0;基準員数優先;1;基準数優先 |
| M_BOM        | UPDTD     | 更新日      | （なし）                    |
| M_BOM        | UPDTWKCD  | 更新担当者  | （なし）                    |
| M_BOM        | YIELD     | 歩留(%)     | （なし）                    |

## テーブル: M_BOM2

| テーブル名   | 列ID           | 列名               | 備考     |
|:-------------|:---------------|:-------------------|:---------|
| M_BOM2       | A_FSEQNO       | 出力順序           | （なし） |
| M_BOM2       | ACT_PHUNIT     | 実際投入重量       | （なし） |
| M_BOM2       | ACT_SCR_PHUNIT | 実際スクラップ重量 | （なし） |
| M_BOM2       | APPLYDATE      | 適用日             | （なし） |
| M_BOM2       | APPLYDATE_F    | 適用日選択区分     | （なし） |
| M_BOM2       | CONTRACTDATE   | 契約成立日         | （なし） |
| M_BOM2       | HITEM          | 親品目             | （なし） |
| M_BOM2       | HPROCESS       | 親工程             | （なし） |
| M_BOM2       | HVENDOR        | 親仕入先           | （なし） |
| M_BOM2       | LITEM          | 子品目             | （なし） |
| M_BOM2       | LPROCESS       | 子工程             | （なし） |
| M_BOM2       | LVENDOR        | 子仕入先           | （なし） |
| M_BOM2       | ODEDDATE       | 失効日             | （なし） |
| M_BOM2       | ODSTDATE       | 発効日             | （なし） |
| M_BOM2       | OPERABLEF      | 使用F              | （なし） |
| M_BOM2       | PRICE          | 投入単価           | （なし） |
| M_BOM2       | REASONCD       | 原因CD             | （なし） |
| M_BOM2       | RGSTD          | 登録日             | （なし） |
| M_BOM2       | SCR_PRICE      | スクラップ単価     | （なし） |
| M_BOM2       | STD_PHUNIT     | 標準投入重量       | （なし） |
| M_BOM2       | STD_SCR_PHUNIT | 標準スクラップ重量 | （なし） |
| M_BOM2       | UPDTD          | 更新日             | （なし） |
| M_BOM2       | UPDTWKCD       | 更新担当者         | （なし） |

## テーブル: M_BOM2_EDIT

| テーブル名   | 列ID           | 列名               | 備考     |
|:-------------|:---------------|:-------------------|:---------|
| M_BOM2_EDIT  | A_FSEQNO       | 出力順序           | （なし） |
| M_BOM2_EDIT  | ACT_PHUNIT     | 実際投入重量       | （なし） |
| M_BOM2_EDIT  | ACT_SCR_PHUNIT | 実際スクラップ重量 | （なし） |
| M_BOM2_EDIT  | APPLYDATE      | 適用日             | （なし） |
| M_BOM2_EDIT  | APPLYDATE_F    | 適用日選択区分     | （なし） |
| M_BOM2_EDIT  | CONTRACTDATE   | 契約成立日         | （なし） |
| M_BOM2_EDIT  | HITEM          | 親品目             | （なし） |
| M_BOM2_EDIT  | HPROCESS       | 親工程             | （なし） |
| M_BOM2_EDIT  | HVENDOR        | 親仕入先           | （なし） |
| M_BOM2_EDIT  | LITEM          | 子品目             | （なし） |
| M_BOM2_EDIT  | LPROCESS       | 子工程             | （なし） |
| M_BOM2_EDIT  | LVENDOR        | 子仕入先           | （なし） |
| M_BOM2_EDIT  | NEW_APPLYDATE  | 適用日             | （なし） |
| M_BOM2_EDIT  | ODEDDATE       | 失効日             | （なし） |
| M_BOM2_EDIT  | ODSTDATE       | 発効日             | （なし） |
| M_BOM2_EDIT  | OPERABLEF      | 使用F              | （なし） |
| M_BOM2_EDIT  | PRICE          | 投入単価           | （なし） |
| M_BOM2_EDIT  | REASONCD       | 原因CD             | （なし） |
| M_BOM2_EDIT  | RGSTD          | 登録日             | （なし） |
| M_BOM2_EDIT  | SCR_PRICE      | スクラップ単価     | （なし） |
| M_BOM2_EDIT  | STD_PHUNIT     | 標準投入重量       | （なし） |
| M_BOM2_EDIT  | STD_SCR_PHUNIT | 標準スクラップ重量 | （なし） |
| M_BOM2_EDIT  | UPDTD          | 更新日             | （なし） |
| M_BOM2_EDIT  | UPDTWKCD       | 更新担当者         | （なし） |

## テーブル: M_BOM_TMP

| テーブル名   | 列ID      | 列名        | 備考                        |
|:-------------|:----------|:------------|:----------------------------|
| M_BOM_TMP    | A_FSEQNO  | 出力順序    | （なし）                    |
| M_BOM_TMP    | CNT       | キー        | （なし）                    |
| M_BOM_TMP    | HIMQTY    | 親基準数    | （なし）                    |
| M_BOM_TMP    | HITEM     | 親品目      | （なし）                    |
| M_BOM_TMP    | HPROCESS  | 親工程      | （なし）                    |
| M_BOM_TMP    | HVENDOR   | 親仕入先    | （なし）                    |
| M_BOM_TMP    | LIMQTY    | 子基準数    | （なし）                    |
| M_BOM_TMP    | LITEM     | 子品目      | （なし）                    |
| M_BOM_TMP    | LPROCESS  | 子工程      | （なし）                    |
| M_BOM_TMP    | LVENDOR   | 子仕入先    | （なし）                    |
| M_BOM_TMP    | ODEDDATE  | 失効日      | （なし）                    |
| M_BOM_TMP    | ODSTDATE  | 発効日      | （なし）                    |
| M_BOM_TMP    | PHUNIT    | 員数        | （なし）                    |
| M_BOM_TMP    | RGSTD     | 登録日      | （なし）                    |
| M_BOM_TMP    | SHARERTIO | 共用比率(%) | （なし）                    |
| M_BOM_TMP    | SHARETYP  | 共用区分    | （なし）                    |
| M_BOM_TMP    | STDPHUNIT | 基準員数    | （なし）                    |
| M_BOM_TMP    | SWEDDATE  | 切替失効日  | （なし）                    |
| M_BOM_TMP    | SWSTDATE  | 切替発効日  | （なし）                    |
| M_BOM_TMP    | UNITTYP   | 員数区分    | 0;基準員数優先;1;基準数優先 |
| M_BOM_TMP    | UPDTD     | 更新日      | （なし）                    |
| M_BOM_TMP    | UPDTWKCD  | 更新担当者  | （なし）                    |
| M_BOM_TMP    | YIELD     | 歩留(%)     | （なし）                    |

## テーブル: M_BUCKET

| テーブル名   | 列ID     | 列名                     | 備考           |
|:-------------|:---------|:-------------------------|:---------------|
| M_BUCKET     | BEAF_F   | 期間指定F                | （なし）       |
| M_BUCKET     | BKTEDD   | ﾊﾞｹｯﾄ最終日              | （なし）       |
| M_BUCKET     | BKTNO    | バケットNo               | （なし）       |
| M_BUCKET     | BKTSTD   | バケット開始日           | （なし）       |
| M_BUCKET     | BKTYEAR  | バケット年               | （なし）       |
| M_BUCKET     | MRPEDD   | 所要量計算最終日         | （なし）       |
| M_BUCKET     | ODEDD    | 所要量計算受注取込最終日 | （なし）       |
| M_BUCKET     | ODRDEDD  | 受注取込最終日           | （なし）       |
| M_BUCKET     | PODEDD   | 購入品外注品確定最終日   | （なし）       |
| M_BUCKET     | PRDCTODF | 作業指示確定F            | 0;未完了1;完了 |
| M_BUCKET     | RGSTD    | 登録日                   | （なし）       |
| M_BUCKET     | SCHEDD   | ｽｹｼﾞｭｰﾙ最終日            | （なし）       |
| M_BUCKET     | UPDTD    | 更新日                   | （なし）       |
| M_BUCKET     | UPDTWKCD | 更新担当者               | （なし）       |

## テーブル: M_BUYPRICE

| テーブル名   | 列ID      | 列名       | 備考     |
|:-------------|:----------|:-----------|:---------|
| M_BUYPRICE   | APPLYDATE | 適用日     | （なし） |
| M_BUYPRICE   | INVLF     | INVLF      | （なし） |
| M_BUYPRICE   | ITEM      | 品目       | （なし） |
| M_BUYPRICE   | ITEMF2    | ITEMF2     | （なし） |
| M_BUYPRICE   | PRICE     | 単価       | （なし） |
| M_BUYPRICE   | PRICEF    | 単価区分   | （なし） |
| M_BUYPRICE   | PROCESS   | 工程       | （なし） |
| M_BUYPRICE   | RGSTD     | 登録日     | （なし） |
| M_BUYPRICE   | TERMINAL  | 端末情報   | （なし） |
| M_BUYPRICE   | UPDTD     | 更新日     | （なし） |
| M_BUYPRICE   | UPDTWKCD  | 更新担当者 | （なし） |
| M_BUYPRICE   | VENDOR    | 仕入先     | （なし） |
| M_BUYPRICE   | VENDOR2   | 外注先     | （なし） |

## テーブル: M_CASE

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_CASE       | CASECD   | 容器       | （なし） |
| M_CASE       | CASENM   | 容器名称   | （なし） |
| M_CASE       | RGSTD    | 登録日     | （なし） |
| M_CASE       | SIZE1    | サイズ1    | （なし） |
| M_CASE       | SIZE2    | サイズ2    | （なし） |
| M_CASE       | SIZE3    | サイズ3    | （なし） |
| M_CASE       | UPDTD    | 更新日     | （なし） |
| M_CASE       | UPDTWKCD | 更新担当者 | （なし） |

## テーブル: M_CLLCTYPE

| テーブル名   | 列ID       | 列名         | 備考     |
|:-------------|:-----------|:-------------|:---------|
| M_CLLCTYPE   | CLLCTYPE   | 集荷タイプ   | （なし） |
| M_CLLCTYPE   | CLLCTYPENM | 集荷タイプ名 | （なし） |
| M_CLLCTYPE   | RGSTD      | 登録日       | （なし） |
| M_CLLCTYPE   | UPDTD      | 更新日       | （なし） |
| M_CLLCTYPE   | UPDTWKCD   | 更新担当者   | （なし） |

## テーブル: M_CLNDD

| テーブル名   | 列ID     | 列名       | 備考               |
|:-------------|:---------|:-----------|:-------------------|
| M_CLNDD      | CLNDDATE | 日付       | （なし）           |
| M_CLNDD      | CLNDNO   | ｶﾚﾝﾀﾞ番号  | （なし）           |
| M_CLNDD      | OPDAY    | 稼働日     | 0;非稼働1;稼働     |
| M_CLNDD      | OVTM     | 残業可     | 0;残業不可1;残業可 |
| M_CLNDD      | RGSTD    | 登録日     | （なし）           |
| M_CLNDD      | UPDTD    | 更新日     | （なし）           |
| M_CLNDD      | UPDTWKCD | 更新担当者 | （なし）           |

## テーブル: M_CLNDNO

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_CLNDNO     | CLNDNM   | ｶﾚﾝﾀﾞｰ名   | （なし） |
| M_CLNDNO     | CLNDNO   | ｶﾚﾝﾀﾞｰ番号 | （なし） |
| M_CLNDNO     | RGSTD    | 登録日     | （なし） |
| M_CLNDNO     | UPDTD    | 更新日     | （なし） |
| M_CLNDNO     | UPDTWKCD | 更新担当者 | （なし） |

## テーブル: M_CNCTEQP

| テーブル名   | 列ID      | 列名       | 備考     |
|:-------------|:----------|:-----------|:---------|
| M_CNCTEQP    | FRITEM    | 出力品目   | （なし） |
| M_CNCTEQP    | FRLINED   | 出力ライン | （なし） |
| M_CNCTEQP    | FRPROCESS | 出力工程   | （なし） |
| M_CNCTEQP    | FRVENDOR  | 出力仕入先 | （なし） |
| M_CNCTEQP    | RGSTD     | 登録日     | （なし） |
| M_CNCTEQP    | TOITEM    | 入力品目   | （なし） |
| M_CNCTEQP    | TOLINED   | 入力ライン | （なし） |
| M_CNCTEQP    | TOPROCESS | 入力工程   | （なし） |
| M_CNCTEQP    | TOVENDOR  | 入力仕入先 | （なし） |
| M_CNCTEQP    | UPDTD     | 更新日     | （なし） |
| M_CNCTEQP    | UPDTWKCD  | 更新担当者 | （なし） |

## テーブル: M_CODE

| テーブル名   | 列ID       | 列名             | 備考                              |
|:-------------|:-----------|:-----------------|:----------------------------------|
| M_CODE       | FCDTY      | タイプ           | （なし）                          |
| M_CODE       | FCNAME     | 内容１           | （なし）                          |
| M_CODE       | FCNAME2    | 内容２           | （なし）                          |
| M_CODE       | FCNAME3    | 内容３           | （なし）                          |
| M_CODE       | FCNAME4    | 内容４           | （なし）                          |
| M_CODE       | FCNAME5    | 内容５           | （なし）                          |
| M_CODE       | FCODE      | コード           | （なし）                          |
| M_CODE       | FCODENM_EN | コード名（英名） | （なし）                          |
| M_CODE       | RGSTD      | 登録日           | （なし）                          |
| M_CODE       | TABLETF    | タブレット表示F  | 0;非表示;1;鋳造以外;2;鋳造;3;両方 |
| M_CODE       | UPDTD      | 更新日           | （なし）                          |
| M_CODE       | UPDTWKCD   | 更新担当者       | （なし）                          |

## テーブル: M_CONSUMPTTAX

| テーブル名    | 列ID      | 列名       | 備考     |
|:--------------|:----------|:-----------|:---------|
| M_CONSUMPTTAX | APPLYDATE | 適用日     | （なし） |
| M_CONSUMPTTAX | RGSTD     | 登録日     | （なし） |
| M_CONSUMPTTAX | TAXRETE   | 税率       | （なし） |
| M_CONSUMPTTAX | TERMINAL  | TERMINAL   | （なし） |
| M_CONSUMPTTAX | UPDTD     | 更新日     | （なし） |
| M_CONSUMPTTAX | UPDTWKCD  | 更新担当者 | （なし） |

## テーブル: M_COST

| テーブル名   | 列ID        | 列名           | 備考        |
|:-------------|:------------|:---------------|:------------|
| M_COST       | ACTCOST1    | 実際加工費     | （なし）    |
| M_COST       | ACTCOST2    | 実際管理費     | （なし）    |
| M_COST       | ACTCOST3    | 実際予備1      | （なし）    |
| M_COST       | ACTCOST4    | 実際予備2      | （なし）    |
| M_COST       | ACTCOST5    | 実際予備3      | （なし）    |
| M_COST       | ACTCOST6    | 実際予備4      | （なし）    |
| M_COST       | APPLYDATE   | 適用日         | （なし）    |
| M_COST       | APPLYDATE_F | 適用日選択区分 | （なし）    |
| M_COST       | COSTF       | 原価区分       | 0;決定;1;仮 |
| M_COST       | ITEM        | 品目           | （なし）    |
| M_COST       | PROCESS     | 工程           | （なし）    |
| M_COST       | RGSTD       | 登録日         | （なし）    |
| M_COST       | STDCOST1    | 標準加工費     | （なし）    |
| M_COST       | STDCOST2    | 標準管理費     | （なし）    |
| M_COST       | STDCOST3    | 標準予備1      | （なし）    |
| M_COST       | STDCOST4    | 標準予備2      | （なし）    |
| M_COST       | STDCOST5    | 標準予備3      | （なし）    |
| M_COST       | STDCOST6    | 標準予備4      | （なし）    |
| M_COST       | UPDTD       | 更新日         | （なし）    |
| M_COST       | UPDTWKCD    | 更新担当者     | （なし）    |
| M_COST       | VENDOR      | 仕入先         | （なし）    |

## テーブル: M_COST_EDIT

| テーブル名   | 列ID          | 列名       | 備考        |
|:-------------|:--------------|:-----------|:------------|
| M_COST_EDIT  | ACTCOST1      | 実際加工費 | （なし）    |
| M_COST_EDIT  | ACTCOST2      | 実際管理費 | （なし）    |
| M_COST_EDIT  | ACTCOST3      | 実際予備1  | （なし）    |
| M_COST_EDIT  | ACTCOST4      | 実際予備2  | （なし）    |
| M_COST_EDIT  | ACTCOST5      | 実際予備3  | （なし）    |
| M_COST_EDIT  | ACTCOST6      | 実際予備4  | （なし）    |
| M_COST_EDIT  | APPLYDATE     | 適用日     | （なし）    |
| M_COST_EDIT  | COSTF         | 原価区分   | 0;決定;1;仮 |
| M_COST_EDIT  | ITEM          | 品目       | （なし）    |
| M_COST_EDIT  | NEW_APPLYDATE | 適用日     | （なし）    |
| M_COST_EDIT  | PROCESS       | 工程       | （なし）    |
| M_COST_EDIT  | RGSTD         | 登録日     | （なし）    |
| M_COST_EDIT  | STDCOST1      | 標準加工費 | （なし）    |
| M_COST_EDIT  | STDCOST2      | 標準管理費 | （なし）    |
| M_COST_EDIT  | STDCOST3      | 標準予備1  | （なし）    |
| M_COST_EDIT  | STDCOST4      | 標準予備2  | （なし）    |
| M_COST_EDIT  | STDCOST5      | 標準予備3  | （なし）    |
| M_COST_EDIT  | STDCOST6      | 標準予備4  | （なし）    |
| M_COST_EDIT  | UPDTD         | 更新日     | （なし）    |
| M_COST_EDIT  | UPDTWKCD      | 更新担当者 | （なし）    |
| M_COST_EDIT  | VENDOR        | 仕入先     | （なし）    |

## テーブル: M_CUSTOM

| テーブル名   | 列ID       | 列名              | 備考                                |
|:-------------|:-----------|:------------------|:------------------------------------|
| M_CUSTOM     | ACCNM      | 口座番号          | （なし）                            |
| M_CUSTOM     | ACCTYP     | 口座種別          | （なし）                            |
| M_CUSTOM     | ADDODFILE  | 追加受注ファイル  | （なし）                            |
| M_CUSTOM     | ADR        | 住所              | （なし）                            |
| M_CUSTOM     | AMCSHCLL   | 未満現金回収額    | （なし）                            |
| M_CUSTOM     | BANKCD     | 銀行コード        | （なし）                            |
| M_CUSTOM     | BILRT      | 手形割合(%)       | （なし）                            |
| M_CUSTOM     | CLLCTCY    | 入金予定月        | （なし）                            |
| M_CUSTOM     | CLLCTD     | 入金予定日        | （なし）                            |
| M_CUSTOM     | CLMCD      | 請求先            | （なし）                            |
| M_CUSTOM     | CLND       | 顧客ｶﾚﾝﾀﾞｰ        | （なし）                            |
| M_CUSTOM     | CMMSF      | 手数料区分        | （なし）                            |
| M_CUSTOM     | CSHDISRT   | 現金割引率(%)     | （なし）                            |
| M_CUSTOM     | CSV1F      | 納品書CSV出力区分 | （なし）                            |
| M_CUSTOM     | CSV2F      | 請求書CSV出力区分 | （なし）                            |
| M_CUSTOM     | CUSTOM     | 顧客              | （なし）                            |
| M_CUSTOM     | CUSTOMNM   | 顧客名            | （なし）                            |
| M_CUSTOM     | DLVLT      | 納入L/T(日)       | （なし）                            |
| M_CUSTOM     | FAX        | FAX               | （なし）                            |
| M_CUSTOM     | FRACT      | 金額端数区分      | （なし）                            |
| M_CUSTOM     | INVISSF    | 請求書発行区分    | （なし）                            |
| M_CUSTOM     | KANRIBASYO | 管理場所区分      | （なし）                            |
| M_CUSTOM     | LOTCTRLF   | ロット管理F       | 0;ロット管理しない;1;ロット管理する |
| M_CUSTOM     | MAILADR    | ﾒｰﾙｱﾄﾞﾚｽ          | （なし）                            |
| M_CUSTOM     | MCLLDNF    | メイン金種区分    | （なし）                            |
| M_CUSTOM     | ODFILE     | 受注ファイル      | （なし）                            |
| M_CUSTOM     | ODRPRCF    | 売上単価区分      | （なし）                            |
| M_CUSTOM     | POSTCD     | 郵便番号          | （なし）                            |
| M_CUSTOM     | PR_AP_F    | 売上計上区分      | （なし）                            |
| M_CUSTOM     | PRINT1F    | 納品書発行        | （なし）                            |
| M_CUSTOM     | PRINT2F    | 請求書発行        | （なし）                            |
| M_CUSTOM     | PSTF       | 郵送料(金額入力)  | （なし）                            |
| M_CUSTOM     | RGSTD      | 登録日            | （なし）                            |
| M_CUSTOM     | SGTBIL     | 手形サイト(日数)  | （なし）                            |
| M_CUSTOM     | TAXCLCF    | 消費税計算区分    | （なし）                            |
| M_CUSTOM     | TAXCLDGT   | 消費税端数桁数    | （なし）                            |
| M_CUSTOM     | TAXF       | 消費税区分        | （なし）                            |
| M_CUSTOM     | TAXFRF     | 消費税端数区分    | （なし）                            |
| M_CUSTOM     | TEL        | TEL               | （なし）                            |
| M_CUSTOM     | TRNSCLND   | 配送便ｶﾚﾝﾀﾞｰ      | （なし）                            |
| M_CUSTOM     | UPDTD      | 更新日            | （なし）                            |
| M_CUSTOM     | UPDTWKCD   | 更新担当者        | （なし）                            |
| M_CUSTOM     | WSETD      | 締日              | （なし）                            |

## テーブル: M_CUSTOM2

| テーブル名   | 列ID      | 列名                  | 備考     |
|:-------------|:----------|:----------------------|:---------|
| M_CUSTOM2    | CLAIMNO   | 請求No                | （なし） |
| M_CUSTOM2    | CLAIMTD   | 請求処理日            | （なし） |
| M_CUSTOM2    | CUSTOM    | 取引先                | （なし） |
| M_CUSTOM2    | CUSTOMNM  | 顧客名                | （なし） |
| M_CUSTOM2    | LSTADJ    | 前回請求調整金額      | （なし） |
| M_CUSTOM2    | LSTCORMCL | 前回請求繰越残        | （なし） |
| M_CUSTOM2    | LSTCORMPE | 前回支払繰越残        | （なし） |
| M_CUSTOM2    | LSTCORMPY | 前回売掛繰越残        | （なし） |
| M_CUSTOM2    | LSTCORMRC | 前回買掛繰越残        | （なし） |
| M_CUSTOM2    | LSTMCL    | 前回請求金額          | （なし） |
| M_CUSTOM2    | LSTPYE    | 前回支払金額          | （なし） |
| M_CUSTOM2    | NOTICENO  | 計上通知No            | （なし） |
| M_CUSTOM2    | ODETD     | 請求終了処理日        | （なし） |
| M_CUSTOM2    | ODSTD     | 請求開始処理日        | （なし） |
| M_CUSTOM2    | PPRNF     | 買掛元帳印刷フラグ    | （なし） |
| M_CUSTOM2    | PYBLMTD   | 買掛処理日            | （なし） |
| M_CUSTOM2    | PYEADJ    | 前回支払調整金額      | （なし） |
| M_CUSTOM2    | PYEENO    | 支払書No(計上通知No） | （なし） |
| M_CUSTOM2    | PYEMTD    | 支払処理日            | （なし） |
| M_CUSTOM2    | RCBLMTD   | 売掛処理日            | （なし） |
| M_CUSTOM2    | SPRNF     | 売掛元帳印刷フラグ    | （なし） |

## テーブル: M_ITEM

| テーブル名   | 列ID                | 列名                 | 備考                                                                                                                                 |
|:-------------|:--------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| M_ITEM       | A_CARD              | 現品票区分           | 0;不要;1;必要                                                                                                                        |
| M_ITEM       | A_FCHGUNI           | 手配換算値           | （なし）                                                                                                                             |
| M_ITEM       | A_FGROUP            | 商品分類             | （なし）                                                                                                                             |
| M_ITEM       | A_FMCUS             | 代表得意先           | （なし）                                                                                                                             |
| M_ITEM       | A_FOUNIT            | 手配単位             | （なし）                                                                                                                             |
| M_ITEM       | A_FPCLASS           | クラス               | （なし）                                                                                                                             |
| M_ITEM       | A_FPCLASS2          | クラス2              | （なし）                                                                                                                             |
| M_ITEM       | A_FPLACE1           | 場所1                | （なし）                                                                                                                             |
| M_ITEM       | A_FPLACE2           | 場所2                | （なし）                                                                                                                             |
| M_ITEM       | A_FPLACE3           | 場所3                | （なし）                                                                                                                             |
| M_ITEM       | A_FPLACE4           | 場所4                | （なし）                                                                                                                             |
| M_ITEM       | A_FPLACE5           | 場所5                | （なし）                                                                                                                             |
| M_ITEM       | A_FPTYPE            | 購入区分             | R;固定自給;Y;有償支給;N;無償支給;G;変動自給                                                                                          |
| M_ITEM       | A_FRELEASE          | オーダ発行区分       | 0;発行する;1;発行しない                                                                                                              |
| M_ITEM       | A_ISOCARD           | ISO移動票区分        | 0;不要;1;必要                                                                                                                        |
| M_ITEM       | A_ITMSTATUS         | ステータス           | 1;試作;2;生試;3;初品;4;量産;6;製品打切;7;サービスパーツ;8;削除;9;製作不可                                                            |
| M_ITEM       | A_ODRF              | 指示発行済F          | 0:未発行　1:発行済                                                                                                                   |
| M_ITEM       | A_PROCURE           | 調達区分             | 0;国内;1;海外                                                                                                                        |
| M_ITEM       | A_QLTYREP           | 成績表添付区分       | 0;不要;1;必要                                                                                                                        |
| M_ITEM       | A_RCVTEST           | 受入検査区分         | 0;不要;1;必要                                                                                                                        |
| M_ITEM       | A_SHIPSECT          | 出荷担当部門         | （なし）                                                                                                                             |
| M_ITEM       | A_SUPPLIER          | 供給者               | 有償支給の供給者                                                                                                                     |
| M_ITEM       | A_USER              | 使用者               | 有償支給の供給者                                                                                                                     |
| M_ITEM       | A_VENDOR            | 発注先               | 購入品、外注品の発注先                                                                                                               |
| M_ITEM       | A_WBIN              | ダブルビン区分       | （なし）                                                                                                                             |
| M_ITEM       | ABNM                | 略称                 | （なし）                                                                                                                             |
| M_ITEM       | ACCEPTLOC           | 納入場所             | （なし）                                                                                                                             |
| M_ITEM       | ACCLT               | 受入L/T(日)          | （なし）                                                                                                                             |
| M_ITEM       | ACHV                | 達成率(%)            | 未使用                                                                                                                               |
| M_ITEM       | ACTCST              | 現在単価             | （なし）                                                                                                                             |
| M_ITEM       | ACTSCRP             | 仕損率(%)            | （なし）                                                                                                                             |
| M_ITEM       | ACTSFTY             | 変動安全在庫         | 非表示項目                                                                                                                           |
| M_ITEM       | ARRIVEDATE          | 入荷予定日           | （なし）                                                                                                                             |
| M_ITEM       | CASECD              | 容器                 | （なし）                                                                                                                             |
| M_ITEM       | CSTTYP              | 単価区分             | 0;入庫時、単価ﾃﾞﾌｫﾙﾄを品目マスタより;1;入庫時、単価ﾃﾞﾌｫﾙﾄをオーダより                                                                |
| M_ITEM       | DRWNO               | 部品番号             | （なし）                                                                                                                             |
| M_ITEM       | EDDATE              | 失効日               | （なし）                                                                                                                             |
| M_ITEM       | FIXLT               | 固定L/T(日)          | （なし）                                                                                                                             |
| M_ITEM       | IMNM                | 品名                 | （なし）                                                                                                                             |
| M_ITEM       | IMTYP               | 製品区分             | 0;製造品､1;購入品､2;外注品                                                                                                           |
| M_ITEM       | INDP                | 独立需要F            | 0;従属需要;1;独立需要                                                                                                                |
| M_ITEM       | ITEM                | 品目                 | （なし）                                                                                                                             |
| M_ITEM       | LINED               | ライン               | （なし）                                                                                                                             |
| M_ITEM       | LOTCTRLF            | ロット管理F          | 0;ロット管理しない;1;ロット管理する                                                                                                  |
| M_ITEM       | LOTSIZING           | 所要量丸め           | （なし）                                                                                                                             |
| M_ITEM       | MAXINVNT            | 最大在庫             | （なし）                                                                                                                             |
| M_ITEM       | MAXLOT              | 最大発注ﾛｯﾄｻｲｽﾞ      | （なし）                                                                                                                             |
| M_ITEM       | MEMO1               | 選択                 | （なし）                                                                                                                             |
| M_ITEM       | MININVNT            | 最小在庫             | （なし）                                                                                                                             |
| M_ITEM       | MINLOT              | 最小発注ﾛｯﾄｻｲｽﾞ      | （なし）                                                                                                                             |
| M_ITEM       | MRPF                | 所要量計算LV         | 0;受注による所要量計算;1;生産指示による所要量計算                                                                                    |
| M_ITEM       | NUMJIG              | 治具数               | （なし）                                                                                                                             |
| M_ITEM       | ODLOT               | 発注ﾛｯﾄｻｲｽﾞ          | （なし）                                                                                                                             |
| M_ITEM       | ODPLCY              | 発注LV               | 0;ロットまとめ;1;日数まとめ                                                                                                          |
| M_ITEM       | ODRDELF             | 確定指示取消F        | 0;取消対象外;1;取消対象                                                                                                              |
| M_ITEM       | ODSUMTERM           | 指示まとめ日数       | 未使用                                                                                                                               |
| M_ITEM       | OFCLTRM             | 確定期間(日)         | （なし）                                                                                                                             |
| M_ITEM       | OPTDAY              | 最適化日数(日)       | （なし）                                                                                                                             |
| M_ITEM       | PACKAGECD           | 荷姿                 | （なし）                                                                                                                             |
| M_ITEM       | PACKQTY             | 入数                 | （なし）                                                                                                                             |
| M_ITEM       | PKQTY               | 入数(旧)             | （なし）                                                                                                                             |
| M_ITEM       | PRDCTCTRL           | 製番管理F            | 0;オーダ管理(すべての受注に対して作業指示作成);1;製番管理(確定受注に対して作業指示作成);2;製番管理(すべての受注に対して作業指示作成) |
| M_ITEM       | PRLT                | 自工程L/T(日)        | （なし）                                                                                                                             |
| M_ITEM       | PRMRYF              | 主材区分             | 0;部品;1;主材;2;副材                                                                                                                 |
| M_ITEM       | PROCESS             | 工程                 | （なし）                                                                                                                             |
| M_ITEM       | PURCHASEORDER_PRN_F | 購入品発注伝票印刷Ｆ | 0;印刷する;1;印刷しない                                                                                                              |
| M_ITEM       | PURCHSF             | 購納F                | 0;納期をスケジュールに加味しない;1;納期をスケジュールに加味する                                                                      |
| M_ITEM       | RECLT               | 納入L/T(日)          | （なし）                                                                                                                             |
| M_ITEM       | RGSTD               | 登録日               | （なし）                                                                                                                             |
| M_ITEM       | SBJCT               | 科目                 | （なし）                                                                                                                             |
| M_ITEM       | SECT                | 担当部門             | （なし）                                                                                                                             |
| M_ITEM       | SFTYDAY             | 安全在庫日数         | （なし）                                                                                                                             |
| M_ITEM       | SFTYTRM             | 安全在庫計算期間     | （なし）                                                                                                                             |
| M_ITEM       | SIZE1               | SIZE1                | （なし）                                                                                                                             |
| M_ITEM       | SIZE2               | SIZE2                | （なし）                                                                                                                             |
| M_ITEM       | SIZE3               | SIZE3                | （なし）                                                                                                                             |
| M_ITEM       | SIZE4               | SIZE4                | 有償支給の供給者                                                                                                                     |
| M_ITEM       | SIZE5               | SIZE5                | 有償支給の供給者                                                                                                                     |
| M_ITEM       | SPLITPR             | 受注分割端数         | （なし）                                                                                                                             |
| M_ITEM       | SPLITQTY            | 受注分割ｻｲｽﾞ         | （なし）                                                                                                                             |
| M_ITEM       | ST_ZERO_CTG         | 在庫０区分           | 0;通常;1;在庫０                                                                                                                      |
| M_ITEM       | STCKF               | 在庫引落区分         | 0;理論消費しない;1;理論消費する                                                                                                      |
| M_ITEM       | STDATE              | 発効日               | （なし）                                                                                                                             |
| M_ITEM       | STDCST              | 標準単価             | （なし）                                                                                                                             |
| M_ITEM       | STDSCRP             | 原価仕損率(%)        | （なし）                                                                                                                             |
| M_ITEM       | STGSECT             | 保管部門             | （なし）                                                                                                                             |
| M_ITEM       | STGTYP              | 保管F                | 0;休日を加味しない;1;休日を加味する                                                                                                  |
| M_ITEM       | STLOC               | 保管場所             | （なし）                                                                                                                             |
| M_ITEM       | SUMDAY              | まとめ日数           | （なし）                                                                                                                             |
| M_ITEM       | TOTALLT             | 累計L/T(日)          | （なし）                                                                                                                             |
| M_ITEM       | TRLT                | 搬送L/T(分)          | （なし）                                                                                                                             |
| M_ITEM       | UNIT                | 単位                 | （なし）                                                                                                                             |
| M_ITEM       | UNOFCLTRM           | 内示期間(日)         | （なし）                                                                                                                             |
| M_ITEM       | UPDTD               | 更新日               | （なし）                                                                                                                             |
| M_ITEM       | UPDTWKCD            | 更新担当者           | （なし）                                                                                                                             |
| M_ITEM       | USELT               | 使用期限(分)         | （なし）                                                                                                                             |
| M_ITEM       | USEUPF              | 半製品使切F          | 0;使切らない;1;使切る                                                                                                                |
| M_ITEM       | VENDOR              | 仕入先               | （なし）                                                                                                                             |
| M_ITEM       | WRATIO              | 比重                 | （なし）                                                                                                                             |

## テーブル: M_ITEMCLASS

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_ITEMCLASS  | CLASSD   | クラス     | （なし） |
| M_ITEMCLASS  | CLASSNM  | クラス名   | （なし） |
| M_ITEMCLASS  | RGSTD    | 登録日     | （なし） |
| M_ITEMCLASS  | UPDTD    | 更新日     | （なし） |
| M_ITEMCLASS  | UPDTWKCD | 更新担当者 | （なし） |

## テーブル: M_ITEMF

| テーブル名   | 列ID     | 列名           | 備考     |
|:-------------|:---------|:---------------|:---------|
| M_ITEMF      | ITEMF    | 受注品目区分   | （なし） |
| M_ITEMF      | ITEMFNM  | 受注品目区分名 | （なし） |
| M_ITEMF      | RGSTD    | 登録日         | （なし） |
| M_ITEMF      | UPDTD    | 更新日         | （なし） |
| M_ITEMF      | UPDTWKCD | 更新担当者     | （なし） |

## テーブル: M_JIG

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_JIG        | ENRPR    | 修理完了日 | （なし） |
| M_JIG        | JIG      | 治具番号   | （なし） |
| M_JIG        | JIGNM    | 治具名     | （なし） |
| M_JIG        | NUMJIG   | 治具数     | （なし） |
| M_JIG        | NUMRPR   | 修理数     | （なし） |
| M_JIG        | RGSTD    | 登録日     | （なし） |
| M_JIG        | STLOC    | 保管場所   | （なし） |
| M_JIG        | STRPR    | 修理開始日 | （なし） |
| M_JIG        | UPDTD    | 更新日     | （なし） |
| M_JIG        | UPDTWKCD | 更新担当者 | （なし） |

## テーブル: M_LINED

| テーブル名   | 列ID        | 列名                  | 備考                                                                         |
|:-------------|:------------|:----------------------|:-----------------------------------------------------------------------------|
| M_LINED      | BATCH       | バッチ処理F           | YES/NO                                                                       |
| M_LINED      | CASTINGF    | 鋳造F                 | 0;鋳造以外;1;鋳造                                                            |
| M_LINED      | CLNDNO      | ｶﾚﾝﾀﾞｰ番号            | （なし）                                                                     |
| M_LINED      | CNCTFLG     | 連結F                 | 0;連結無し;1;連結有り                                                        |
| M_LINED      | CNCTLINED   | 連結ライン            | （なし）                                                                     |
| M_LINED      | CNCTPRCS    | 連結工程              | （なし）                                                                     |
| M_LINED      | ENTMAJ      | 終業時刻調整F         | 0;終業時刻短縮;1;終業時刻延長;2;翌日に作業がまたがらない                     |
| M_LINED      | EQPF        | ｽﾄﾚｰｼﾞF               | 0;設備;1;ストレージ装置                                                      |
| M_LINED      | FIFO        | 先入先出F             | 0;しない;1;する                                                              |
| M_LINED      | FRCTLM      | 端数処理数            | （なし）                                                                     |
| M_LINED      | GNTDSPF     | ガントチャート非表示F | 0;表示する;1;表示しない                                                      |
| M_LINED      | ISLOCTDEF   | 出庫場所規定値        | （なし）                                                                     |
| M_LINED      | LINED       | ライン                | （なし）                                                                     |
| M_LINED      | LINENM      | ライン名              | （なし）                                                                     |
| M_LINED      | LOADLV      | 平均負荷割F           | 0;しない;1;する                                                              |
| M_LINED      | LOTGRNT     | ﾛｯﾄｻｲｽﾞ保証F          | 0;しない;1;する                                                              |
| M_LINED      | MCREFF      | MPS効率(%)            | （なし）                                                                     |
| M_LINED      | NUMCART     | 供給台車数            | （なし）                                                                     |
| M_LINED      | ODTPY       | 指示発行区分          | 0;指示まとめをする;1;翌日にまたがる指示を分ける;2;ロット単位の指示を発行する |
| M_LINED      | OFFTMTBL    | 休出稼働時間帯        | （なし）                                                                     |
| M_LINED      | OPRTRATIO   | 計画稼働率(%)         | （なし）                                                                     |
| M_LINED      | OPTDAY      | 最適化日数(日)        | （なし）                                                                     |
| M_LINED      | OVLAPF      | オーバーラップF       | 0;しない;1;する                                                              |
| M_LINED      | OVWKRAIO    | 残業比率(%)           | （なし）                                                                     |
| M_LINED      | PROCESS     | 工程                  | （なし）                                                                     |
| M_LINED      | PRODSETD    | 定期段取期間(日)      | （なし）                                                                     |
| M_LINED      | PRODSETM    | 定期段取時間(分)      | （なし）                                                                     |
| M_LINED      | PRODSETUP   | 定期段取バッチ数      | （なし）                                                                     |
| M_LINED      | PRODSETUPF  | 定期段取区分          | 0;なし;1;バッチ数により発生;2;期間により発生                                 |
| M_LINED      | PRODWKGRP   | 定期段取人員G         | （なし）                                                                     |
| M_LINED      | PRODWKNUM   | 定期段取人数          | （なし）                                                                     |
| M_LINED      | RCLOCTDEF   | 入庫場所規定値        | （なし）                                                                     |
| M_LINED      | RGSTD       | 登録日                | （なし）                                                                     |
| M_LINED      | SBCNTCD     | 外注ｺｰﾄﾞ              | （なし）                                                                     |
| M_LINED      | SBCNTF      | 外注F                 | 0;内作;1;外作                                                                |
| M_LINED      | SCHEFF      | スケジューラ効率(%)   | （なし）                                                                     |
| M_LINED      | SECT        | 担当部門              | （なし）                                                                     |
| M_LINED      | SORTCND     | ソート条件            | （なし）                                                                     |
| M_LINED      | STDCSTEFF   | 標準原価稼働率(%)     | 標準原価計算に使用                                                           |
| M_LINED      | STDLOT      | 標準原価作業者数      | 標準原価計算に使用                                                           |
| M_LINED      | STDTMTBL    | 標準稼働時間帯        | （なし）                                                                     |
| M_LINED      | STGF        | ｽﾄﾚｰｼﾞ区分            | 0;タンク;1;供給台車                                                          |
| M_LINED      | STGMAXINVNT | ｽﾄﾚｰｼﾞ最大在庫        | （なし）                                                                     |
| M_LINED      | STGMININVNT | ｽﾄﾚｰｼﾞ最小在庫        | （なし）                                                                     |
| M_LINED      | UPDTD       | 更新日                | （なし）                                                                     |
| M_LINED      | UPDTWKCD    | 更新担当者            | （なし）                                                                     |
| M_LINED      | WGTCNVF     | 比重変換F             | 0;なし;1;あり                                                                |
| M_LINED      | WKCD        | 担当者CD              | （なし）                                                                     |

## テーブル: M_LOCATION

| テーブル名   | 列ID       | 列名               | 備考                            |
|:-------------|:-----------|:-------------------|:--------------------------------|
| M_LOCATION   | A_CLND     | 納入先カレンダーNo | （なし）                        |
| M_LOCATION   | A_FACCFLG  | 集荷区分           | 0;当日;1;1日前;2;2日前;5;半日前 |
| M_LOCATION   | A_LOCTF    | 場所区分           | 0;社内;1;外注;2;納入先          |
| M_LOCATION   | ADR        | 住所               | （なし）                        |
| M_LOCATION   | CLLCTYPE   | 午前集荷便         | （なし）                        |
| M_LOCATION   | CLLCTYPE2  | 午後集荷便         | （なし）                        |
| M_LOCATION   | DLVLT      | 納入L/T（日）      | （なし）                        |
| M_LOCATION   | FAX        | FAX                | （なし）                        |
| M_LOCATION   | LOCT       | 場所               | （なし）                        |
| M_LOCATION   | LOCTNM     | 場所名             | （なし）                        |
| M_LOCATION   | PARTSF     | パーツ区分         | 0;単価のみ;1;パーツ単価計上     |
| M_LOCATION   | POSTCD     | 郵便番号           | （なし）                        |
| M_LOCATION   | RGSTD      | 登録日             | （なし）                        |
| M_LOCATION   | TEL        | TEL                | （なし）                        |
| M_LOCATION   | TRANSACTOR | 取引先             | （なし）                        |
| M_LOCATION   | UPDTD      | 更新日             | （なし）                        |
| M_LOCATION   | UPDTWKCD   | 更新担当者         | （なし）                        |

## テーブル: M_MAXMININVT

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_MAXMININVT | EDDATE   | 終了日     | （なし） |
| M_MAXMININVT | ITEM     | 品目       | （なし） |
| M_MAXMININVT | MAXINVNT | 最大在庫   | （なし） |
| M_MAXMININVT | MININVNT | 最小在庫   | （なし） |
| M_MAXMININVT | PROCESS  | 工程       | （なし） |
| M_MAXMININVT | RGSTD    | 登録日     | （なし） |
| M_MAXMININVT | STDATE   | 開始日     | （なし） |
| M_MAXMININVT | UPDTD    | 更新日     | （なし） |
| M_MAXMININVT | UPDTWKCD | 更新担当者 | （なし） |
| M_MAXMININVT | VENDOR   | 仕入先     | （なし） |

## テーブル: M_MYCOMP

| テーブル名   | 列ID        | 列名         | 備考     |
|:-------------|:------------|:-------------|:---------|
| M_MYCOMP     | A_FSEQNO    | 出力順序     | （なし） |
| M_MYCOMP     | ADR         | 住所1        | （なし） |
| M_MYCOMP     | ADR2        | 住所2        | （なし） |
| M_MYCOMP     | COMPCODE    | 工場コード   | （なし） |
| M_MYCOMP     | COMPNM      | 工場名       | （なし） |
| M_MYCOMP     | DISPSQ      | 表示順       | （なし） |
| M_MYCOMP     | FAX         | FAX          | （なし） |
| M_MYCOMP     | MAILADR     | ﾒｰﾙｱﾄﾞﾚｽ     | （なし） |
| M_MYCOMP     | POSTCD      | 郵便番号     | （なし） |
| M_MYCOMP     | RGSTD       | 登録日       | （なし） |
| M_MYCOMP     | TEL         | TEL          | （なし） |
| M_MYCOMP     | TMTBLSTTIME | 稼働開始時間 | （なし） |
| M_MYCOMP     | UPDTD       | 更新日       | （なし） |
| M_MYCOMP     | UPDTWKCD    | 更新担当者   | （なし） |
| M_MYCOMP     | URL         | URL          | （なし） |

## テーブル: M_OEE_PRDCTCAPA

| テーブル名      | 列ID       | 列名         | 備考     |
|:----------------|:-----------|:-------------|:---------|
| M_OEE_PRDCTCAPA | INVLF      | 無効Ｆ       | YES/NO   |
| M_OEE_PRDCTCAPA | ITEM       | 品目         | （なし） |
| M_OEE_PRDCTCAPA | LINED      | ライン       | （なし） |
| M_OEE_PRDCTCAPA | PROCESS    | 工程         | （なし） |
| M_OEE_PRDCTCAPA | RGSTD      | 登録日       | （なし） |
| M_OEE_PRDCTCAPA | STDCSTCAPA | 基準CT（秒） | （なし） |
| M_OEE_PRDCTCAPA | UPDTD      | 更新日       | （なし） |
| M_OEE_PRDCTCAPA | UPDTWKCD   | 更新担当者   | （なし） |
| M_OEE_PRDCTCAPA | VENDOR     | 仕入先       | （なし） |

## テーブル: M_OVSPROCURE

| テーブル名   | 列ID          | 列名       | 備考     |
|:-------------|:--------------|:-----------|:---------|
| M_OVSPROCURE | ALLOCD        | 引当期限日 | （なし） |
| M_OVSPROCURE | ESTARV        | 到着予定日 | （なし） |
| M_OVSPROCURE | ESTDEP        | 出港予定日 | （なし） |
| M_OVSPROCURE | ORDEREDF      | 内示確定F  | （なし） |
| M_OVSPROCURE | PROCURE_BKTNO | 調達BKTNo  | （なし） |
| M_OVSPROCURE | PROCURE_YM    | 調達年月   | （なし） |
| M_OVSPROCURE | RGSTD         | 登録日     | （なし） |
| M_OVSPROCURE | TRANSACTOR    | 発注先     | （なし） |
| M_OVSPROCURE | UPDTD         | 更新日     | （なし） |
| M_OVSPROCURE | UPDTWKCD      | 更新担当者 | （なし） |

## テーブル: M_PACKAGE

| テーブル名   | 列ID      | 列名       | 備考     |
|:-------------|:----------|:-----------|:---------|
| M_PACKAGE    | PACKAGECD | 荷姿       | （なし） |
| M_PACKAGE    | PACKAGENM | 荷姿名称   | （なし） |
| M_PACKAGE    | RGSTD     | 登録日     | （なし） |
| M_PACKAGE    | UPDTD     | 更新日     | （なし） |
| M_PACKAGE    | UPDTWKCD  | 更新担当者 | （なし） |

## テーブル: M_PRDCTCAPA

| テーブル名   | 列ID        | 列名                      | 備考                                                                   |
|:-------------|:------------|:--------------------------|:-----------------------------------------------------------------------|
| M_PRDCTCAPA  | AMAN        | 後段取人数                | （なし）                                                               |
| M_PRDCTCAPA  | AMANG       | 後段取人員G               | （なし）                                                               |
| M_PRDCTCAPA  | ASTUP       | 後段取時間(分)            | （なし）                                                               |
| M_PRDCTCAPA  | CAPA        | 時間当生産能力(生産数/時) | （なし）                                                               |
| M_PRDCTCAPA  | CNCTFLG     | 連結F                     | 0;連結無し;1;連結有り                                                  |
| M_PRDCTCAPA  | CNCTLINED   | 連結ライン                | （なし）                                                               |
| M_PRDCTCAPA  | CNCTPRCS    | 連結工程                  | （なし）                                                               |
| M_PRDCTCAPA  | DSTUP1      | 段取Ｇ１                  | （なし）                                                               |
| M_PRDCTCAPA  | DSTUP2      | 段取Ｇ２                  | （なし）                                                               |
| M_PRDCTCAPA  | DSTUP3      | 段取Ｇ３                  | （なし）                                                               |
| M_PRDCTCAPA  | DSTUP4      | 段取Ｇ４                  | （なし）                                                               |
| M_PRDCTCAPA  | DSTUP5      | 段取Ｇ５                  | （なし）                                                               |
| M_PRDCTCAPA  | DSTUP6      | 段取Ｇ６                  | （なし）                                                               |
| M_PRDCTCAPA  | DSTUP7      | 段取Ｇ７                  | （なし）                                                               |
| M_PRDCTCAPA  | EDDATE      | 失効日                    | （なし）                                                               |
| M_PRDCTCAPA  | FIXLOSS     | 固定ロス量                | （なし）                                                               |
| M_PRDCTCAPA  | FMAN        | 段取人数                  | （なし）                                                               |
| M_PRDCTCAPA  | FMANG       | 段取人員G                 | （なし）                                                               |
| M_PRDCTCAPA  | FSTUP       | 固定段取時間(分)          | （なし）                                                               |
| M_PRDCTCAPA  | INVLF       | 無効Ｆ                    | YES/NO                                                                 |
| M_PRDCTCAPA  | ITEM        | 品目                      | （なし）                                                               |
| M_PRDCTCAPA  | JIG1        | 治具１                    | （なし）                                                               |
| M_PRDCTCAPA  | JIG2        | 治具２                    | （なし）                                                               |
| M_PRDCTCAPA  | JIG3        | 治具３                    | （なし）                                                               |
| M_PRDCTCAPA  | JIG4        | 治具４                    | （なし）                                                               |
| M_PRDCTCAPA  | JIG5        | 治具５                    | （なし）                                                               |
| M_PRDCTCAPA  | LINED       | ライン                    | （なし）                                                               |
| M_PRDCTCAPA  | MAXBAT      | 最大可能バッチ数          | （なし）                                                               |
| M_PRDCTCAPA  | MINBAT      | 最小生産バッチ数          | （なし）                                                               |
| M_PRDCTCAPA  | MINWKNUM    | 最少人員(人)              | （なし）                                                               |
| M_PRDCTCAPA  | PREFER      | 優先順位                  | 第１優先〜第99優先                                                     |
| M_PRDCTCAPA  | PROCESS     | 工程                      | （なし）                                                               |
| M_PRDCTCAPA  | QLTY1       | 品質Ｇ１                  | （なし）                                                               |
| M_PRDCTCAPA  | QLTY2       | 品質Ｇ２                  | （なし）                                                               |
| M_PRDCTCAPA  | QLTY3       | 品質Ｇ３                  | （なし）                                                               |
| M_PRDCTCAPA  | QLTY4       | 品質Ｇ４                  | （なし）                                                               |
| M_PRDCTCAPA  | QLTY5       | 品質Ｇ５                  | （なし）                                                               |
| M_PRDCTCAPA  | QLTY6       | 品質Ｇ６                  | （なし）                                                               |
| M_PRDCTCAPA  | QLTY7       | 品質Ｇ７                  | （なし）                                                               |
| M_PRDCTCAPA  | RDCTEFF     | 人員減効率(%)             | （なし）                                                               |
| M_PRDCTCAPA  | RGSTD       | 登録日                    | （なし）                                                               |
| M_PRDCTCAPA  | SBCNTACTCST | 外注現在単価              | （なし）                                                               |
| M_PRDCTCAPA  | SBCNTCSTF   | 外注単価区分              | 0;入庫時、単価ﾃﾞﾌｫﾙﾄを品目マスタより;1;入庫時、単価ﾃﾞﾌｫﾙﾄをオーダより  |
| M_PRDCTCAPA  | SBCNTLT     | 外注自工程L/T(日)         | （なし）                                                               |
| M_PRDCTCAPA  | SBCNTSTDCST | 外注標準単価              | （なし）                                                               |
| M_PRDCTCAPA  | SBCNTTLT    | 外注累計L/T(日)           | （なし）                                                               |
| M_PRDCTCAPA  | SCHMETH     | 立案方法                  | 1;稼働率優先;2;同期化優先;3;最適化日数内稼働率優先                     |
| M_PRDCTCAPA  | SMIMSETUPF  | 同一品目固定段取F         | 0;固定段取しない;1;固定段取する;2;最大可能バッチ数以上で固定段取りする |
| M_PRDCTCAPA  | SQUGRP      | 順序Ｇ                    | （なし）                                                               |
| M_PRDCTCAPA  | STDATE      | 発効日                    | （なし）                                                               |
| M_PRDCTCAPA  | STDCSTCAPA  | 時間当原価能力(生産数/時) | （なし）                                                               |
| M_PRDCTCAPA  | STDLOT      | ロットサイズ              | （なし）                                                               |
| M_PRDCTCAPA  | STDWKNUM    | 標準人員(人)              | （なし）                                                               |
| M_PRDCTCAPA  | UPDTD       | 更新日                    | （なし）                                                               |
| M_PRDCTCAPA  | UPDTWKCD    | 更新担当者                | （なし）                                                               |
| M_PRDCTCAPA  | VENDOR      | 仕入先                    | （なし）                                                               |
| M_PRDCTCAPA  | WKGRP1      | 人員Ｇ１                  | （なし）                                                               |
| M_PRDCTCAPA  | WKGRP2      | 人員Ｇ２                  | （なし）                                                               |
| M_PRDCTCAPA  | WKGRP3      | 人員Ｇ３                  | （なし）                                                               |

## テーブル: M_PRDCTGRP

| テーブル名   | 列ID       | 列名       | 備考                      |
|:-------------|:-----------|:-----------|:--------------------------|
| M_PRDCTGRP   | COMF       | 共通Ｆ     | 0;共通でない;1;共通とする |
| M_PRDCTGRP   | PRDCTGRP   | 製品群     | （なし）                  |
| M_PRDCTGRP   | PRDCTGRPNM | 製品群名   | （なし）                  |
| M_PRDCTGRP   | RGSTD      | 登録日     | （なし）                  |
| M_PRDCTGRP   | UPDTD      | 更新日     | （なし）                  |
| M_PRDCTGRP   | UPDTWKCD   | 更新担当者 | （なし）                  |

## テーブル: M_PRICE

| テーブル名   | 列ID            | 列名           | 備考                   |
|:-------------|:----------------|:---------------|:-----------------------|
| M_PRICE      | ACT_PRICE       | 実際単価       | （なし）               |
| M_PRICE      | ACT_PROC_CHARGE | 実際加工単価   | （なし）               |
| M_PRICE      | APPLYDATE       | 適用日         | （なし）               |
| M_PRICE      | APPLYDATE_F     | 適用日選択区分 | （なし）               |
| M_PRICE      | CKDPACKPRICE    | CKD梱包単価    | （なし）               |
| M_PRICE      | ISSUE_DATE      | 入庫日         | （なし）               |
| M_PRICE      | ITEM            | 品目           | （なし）               |
| M_PRICE      | PRICE           | 標準単価       | （なし）               |
| M_PRICE      | PRICEF          | 単価区分       | 0;決定;1;仮            |
| M_PRICE      | PROCESS         | 工程           | （なし）               |
| M_PRICE      | PRTPACKPRICE    | パーツ梱包単価 | （なし）               |
| M_PRICE      | RGSTD           | 登録日         | （なし）               |
| M_PRICE      | SPFLAG          | 売買区分       | S;売上単価;P; 仕入単価 |
| M_PRICE      | STD_PROC_CHARGE | 標準加工単価   | （なし）               |
| M_PRICE      | THAI_PRICE      | バーツ単価     | （なし）               |
| M_PRICE      | THAI_RATE       | バーツレート   | （なし）               |
| M_PRICE      | TRANSACTOR      | 取引先         | （なし）               |
| M_PRICE      | UPDTD           | 更新日         | （なし）               |
| M_PRICE      | UPDTWKCD        | 更新担当者     | （なし）               |
| M_PRICE      | USD_PRICE       | 米ドル単価     | 海外調達品＄単価       |
| M_PRICE      | USD_RATE        | 米ドルレート   | （なし）               |
| M_PRICE      | VENDOR          | 仕入先         | （なし）               |

## テーブル: M_PRICE_EDIT

| テーブル名   | 列ID            | 列名           | 備考                   |
|:-------------|:----------------|:---------------|:-----------------------|
| M_PRICE_EDIT | ACT_PRICE       | 実際単価       | （なし）               |
| M_PRICE_EDIT | ACT_PROC_CHARGE | 実際加工単価   | （なし）               |
| M_PRICE_EDIT | APPLYDATE       | 適用日         | （なし）               |
| M_PRICE_EDIT | CKDPACKPRICE    | CKD梱包単価    | （なし）               |
| M_PRICE_EDIT | ISSUE_DATE      | 入庫日         | （なし）               |
| M_PRICE_EDIT | ITEM            | 品目           | （なし）               |
| M_PRICE_EDIT | NEW_APPLYDATE   | 適用日         | （なし）               |
| M_PRICE_EDIT | PRICE           | 標準単価       | （なし）               |
| M_PRICE_EDIT | PRICEF          | 単価区分       | 0;決定;1;仮            |
| M_PRICE_EDIT | PROCESS         | 工程           | （なし）               |
| M_PRICE_EDIT | PRTPACKPRICE    | パーツ梱包単価 | （なし）               |
| M_PRICE_EDIT | RGSTD           | 登録日         | （なし）               |
| M_PRICE_EDIT | SPFLAG          | 売買区分       | S;売上単価;P; 仕入単価 |
| M_PRICE_EDIT | STD_PROC_CHARGE | 標準加工単価   | （なし）               |
| M_PRICE_EDIT | THAI_PRICE      | バーツ単価     | （なし）               |
| M_PRICE_EDIT | TRANSACTOR      | 取引先         | （なし）               |
| M_PRICE_EDIT | UPDTD           | 更新日         | （なし）               |
| M_PRICE_EDIT | UPDTWKCD        | 更新担当者     | （なし）               |
| M_PRICE_EDIT | USD_PRICE       | 米ドル単価     | 海外調達品＄単価       |
| M_PRICE_EDIT | VENDOR          | 仕入先         | （なし）               |

## テーブル: M_PRMST

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_PRMST      | CALF     | 計算区分   | （なし） |
| M_PRMST      | PRF      | 売買区分   | （なし） |
| M_PRMST      | RGSTD    | 登録日     | （なし） |
| M_PRMST      | RGSTWKCD | 登録担当者 | （なし） |
| M_PRMST      | SLPF     | 伝票区分   | （なし） |
| M_PRMST      | SLPNM    | 伝票区分名 | （なし） |
| M_PRMST      | TERMINAL | 端末情報   | （なし） |
| M_PRMST      | UPDTD    | 更新日     | （なし） |
| M_PRMST      | UPDTWKCD | 更新担当者 | （なし） |

## テーブル: M_PROCESS

| テーブル名   | 列ID        | 列名              | 備考                                                                                                                                 |
|:-------------|:------------|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| M_PROCESS    | A_EVAL_F    | 評価区分          | 1;加工素材;2;子部品;3;中間加工品;4;外注品;5;単品検査完成品;6;組立完成品                                                              |
| M_PROCESS    | CLNDNO      | ｶﾚﾝﾀﾞｰ番号        | （なし）                                                                                                                             |
| M_PROCESS    | CSTF        | 原価計算Ｆ        | 0;加工時間比例配賦1;人工数比例配賦                                                                                                   |
| M_PROCESS    | DEFECTFLG   | 仕損返品在庫消費F | 0:消費する;1;消費しない                                                                                                              |
| M_PROCESS    | DUEDOPT     | 納期最適化F       | 0;しない;1;する                                                                                                                      |
| M_PROCESS    | MAXINVNT    | 最大在庫          | （なし）                                                                                                                             |
| M_PROCESS    | PAYSAL_F    | 売買作成F         | 0;作成する;1;作成しない                                                                                                              |
| M_PROCESS    | PRDCTCTRL   | 製番管理F         | 0;オーダ管理(すべての受注に対して作業指示作成);1;製番管理(確定受注に対して作業指示作成);2;製番管理(すべての受注に対して作業指示作成) |
| M_PROCESS    | PRDCTGRP    | 製品群            | （なし）                                                                                                                             |
| M_PROCESS    | PRDCTINST_F | 指示書区分        | 0：カード；1：一覧                                                                                                                   |
| M_PROCESS    | PRICE_F     | 単価登録F         | （なし）                                                                                                                             |
| M_PROCESS    | PROCESS     | 工程              | （なし）                                                                                                                             |
| M_PROCESS    | PROCESSNM   | 工程名            | （なし）                                                                                                                             |
| M_PROCESS    | QLTYOPT     | 品質最適化F       | 0;しない;1;する                                                                                                                      |
| M_PROCESS    | RGSTD       | 登録日            | （なし）                                                                                                                             |
| M_PROCESS    | SCHPASS     | スケジュールPASS  | 未使用                                                                                                                               |
| M_PROCESS    | SETUPOPT    | 段取最適化F       | 0;しない;1;する                                                                                                                      |
| M_PROCESS    | SORTCND     | ソート条件        | （なし）                                                                                                                             |
| M_PROCESS    | UPDTD       | 更新日            | （なし）                                                                                                                             |
| M_PROCESS    | UPDTWKCD    | 更新担当者        | （なし）                                                                                                                             |
| M_PROCESS    | WRHOUSEF    | 倉庫工程          | YES/NO                                                                                                                               |
| M_PROCESS    | WRKROPT     | 人員最適化F       | 0;しない;1;する                                                                                                                      |

## テーブル: M_PROVIDEPRICE

| テーブル名     | 列ID      | 列名           | 備考     |
|:---------------|:----------|:---------------|:---------|
| M_PROVIDEPRICE | APPLYDATE | 適用日         | （なし） |
| M_PROVIDEPRICE | GRA_FLG   | 有償無償フラグ | （なし） |
| M_PROVIDEPRICE | IMTYP     | 製品区分       | （なし） |
| M_PROVIDEPRICE | INVLF     | 無効フラグ     | （なし） |
| M_PROVIDEPRICE | ITEM      | 品目           | （なし） |
| M_PROVIDEPRICE | ITEMF2    | 品目区分2      | （なし） |
| M_PROVIDEPRICE | PRICE     | 単価           | （なし） |
| M_PROVIDEPRICE | PRICEF    | 単価区分       | （なし） |
| M_PROVIDEPRICE | PROCESS   | 工程           | （なし） |
| M_PROVIDEPRICE | PRVD      | 支給先         | （なし） |
| M_PROVIDEPRICE | RGSTD     | 登録日         | （なし） |
| M_PROVIDEPRICE | TERMINAL  | TERMINAL       | （なし） |
| M_PROVIDEPRICE | UPDTD     | 更新日         | （なし） |
| M_PROVIDEPRICE | UPDTWKCD  | 更新担当者     | （なし） |
| M_PROVIDEPRICE | VENDOR    | 仕入先         | （なし） |

## テーブル: M_PRVDCST

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_PRVDCST    | ACTCST   | 現在単価   | （なし） |
| M_PRVDCST    | ITEM     | 品目       | （なし） |
| M_PRVDCST    | PROCESS  | 工程       | （なし） |
| M_PRVDCST    | PRVD     | 支給先     | （なし） |
| M_PRVDCST    | RGSTD    | 登録日     | （なし） |
| M_PRVDCST    | STDCST   | 標準単価   | （なし） |
| M_PRVDCST    | UPDTD    | 更新日     | （なし） |
| M_PRVDCST    | UPDTWKCD | 更新担当者 | （なし） |
| M_PRVDCST    | VENDOR   | 仕入先     | （なし） |

## テーブル: M_QLTY

| テーブル名   | 列ID     | 列名        | 備考     |
|:-------------|:---------|:------------|:---------|
| M_QLTY       | LINED    | ライン      | （なし） |
| M_QLTY       | PROCESS  | 工程        | （なし） |
| M_QLTY       | QLTYATR1 | 品質特性値1 | （なし） |
| M_QLTY       | QLTYATR2 | 品質特性値2 | （なし） |
| M_QLTY       | QLTYG    | 品質G       | （なし） |
| M_QLTY       | QLTYW    | 品質重み    | （なし） |
| M_QLTY       | RGSTD    | 登録日      | （なし） |
| M_QLTY       | UPDTD    | 更新日      | （なし） |
| M_QLTY       | UPDTWKCD | 更新担当者  | （なし） |

## テーブル: M_QLTYATR

| テーブル名   | 列ID     | 列名       | 備考                                                                         |
|:-------------|:---------|:-----------|:-----------------------------------------------------------------------------|
| M_QLTYATR    | LINED    | ライン     | （なし）                                                                     |
| M_QLTYATR    | PROCESS  | 工程       | （なし）                                                                     |
| M_QLTYATR    | QLTYA    | 品質特性値 | （なし）                                                                     |
| M_QLTYATR    | QLTYG    | 品質G      | 1;第１優先;2;第２優先;3;第３優先;4;第４優先;5;第５優先;6;第６優先;7;第７優先 |
| M_QLTYATR    | QLTYNM   | 品質特性名 | （なし）                                                                     |
| M_QLTYATR    | RGSTD    | 登録日     | （なし）                                                                     |
| M_QLTYATR    | UPDTD    | 更新日     | （なし）                                                                     |
| M_QLTYATR    | UPDTWKCD | 更新担当者 | （なし）                                                                     |

## テーブル: M_RCISMST

| テーブル名   | 列ID     | 列名           | 備考                               |
|:-------------|:---------|:---------------|:-----------------------------------|
| M_RCISMST    | CSTF     | 原価計算区分   | 0;原価計算しない;1;原価計算する    |
| M_RCISMST    | MNYF     | 金額計上F      | （なし）                           |
| M_RCISMST    | PRVDF    | 支給区分       | 0;支給しない;1;無償支給;2;有償支給 |
| M_RCISMST    | RCISCD   | 入出庫区分     | （なし）                           |
| M_RCISMST    | RCISF    | 入庫・出庫区分 | 0;入庫;1;出庫                      |
| M_RCISMST    | RCISNM   | 入出庫区分名   | （なし）                           |
| M_RCISMST    | RETURNF  | 返品区分       | 0;返品でない;1;返品である          |
| M_RCISMST    | RGSTD    | 登録日         | （なし）                           |
| M_RCISMST    | STCKF    | 在庫計上区分   | 0;在庫計上しない;1;在庫計上する    |
| M_RCISMST    | UPDTD    | 更新日         | （なし）                           |
| M_RCISMST    | UPDTWKCD | 更新担当者     | （なし）                           |

## テーブル: M_RMPRDCT

| テーブル名   | 列ID      | 列名                       | 備考     |
|:-------------|:----------|:---------------------------|:---------|
| M_RMPRDCT    | BKTNO     | バケットNo                 | （なし） |
| M_RMPRDCT    | BKTYEAR   | バケット年                 | （なし） |
| M_RMPRDCT    | FIXPRDCT  | 前回生産済バッチ数         | （なし） |
| M_RMPRDCT    | FIXSETUP  | 前回固定段取経過バッチ数   | （なし） |
| M_RMPRDCT    | ITEM      | 品目                       | （なし） |
| M_RMPRDCT    | LINED     | ライン                     | （なし） |
| M_RMPRDCT    | PRDCTBNO  | 枝番                       | （なし） |
| M_RMPRDCT    | PRDCTNO   | 製番                       | （なし） |
| M_RMPRDCT    | PROCESS   | 工程                       | （なし） |
| M_RMPRDCT    | PRODSETD  | 前回定期段取経過日数       | （なし） |
| M_RMPRDCT    | PRODSETUP | 前回定期段取生産済バッチ数 | （なし） |
| M_RMPRDCT    | RGSTD     | 登録日                     | （なし） |
| M_RMPRDCT    | RMLOTNUM  | ロット残数                 | （なし） |
| M_RMPRDCT    | SETUPTM   | 段取残時間(分)             | （なし） |
| M_RMPRDCT    | STRGINVNT | ストレージ在庫数           | （なし） |
| M_RMPRDCT    | UPDTD     | 更新日                     | （なし） |
| M_RMPRDCT    | UPDTWKCD  | 更新担当者                 | （なし） |
| M_RMPRDCT    | VENDOR    | 仕入先                     | （なし） |

## テーブル: M_SALESPRICE

| テーブル名   | 列ID      | 列名         | 備考     |
|:-------------|:----------|:-------------|:---------|
| M_SALESPRICE | APPLYDATE | 適用日       | （なし） |
| M_SALESPRICE | CUSTOM    | 顧客         | （なし） |
| M_SALESPRICE | IMTYP     | 製品区分     | （なし） |
| M_SALESPRICE | INVLF     | 無効フラグ   | （なし） |
| M_SALESPRICE | ITEM      | 品目         | （なし） |
| M_SALESPRICE | ITEMF     | 受注品目区分 | （なし） |
| M_SALESPRICE | ITEMF2    | 品目区分2    | （なし） |
| M_SALESPRICE | PRICE     | 単価         | （なし） |
| M_SALESPRICE | PRICEF    | 単価区分     | （なし） |
| M_SALESPRICE | PROCESS   | 工程         | （なし） |
| M_SALESPRICE | RGSTD     | 登録日       | （なし） |
| M_SALESPRICE | TERMINAL  | TERMINAL     | （なし） |
| M_SALESPRICE | UPDTD     | 更新日       | （なし） |
| M_SALESPRICE | UPDTWKCD  | 更新担当者   | （なし） |
| M_SALESPRICE | VENDOR    | 仕入先       | （なし） |

## テーブル: M_SECTION

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_SECTION    | RGSTD    | 登録日     | （なし） |
| M_SECTION    | SECT     | 部門       | （なし） |
| M_SECTION    | SECTNM   | 部門名     | （なし） |
| M_SECTION    | UPDTD    | 更新日     | （なし） |
| M_SECTION    | UPDTWKCD | 更新担当者 | （なし） |

## テーブル: M_SETUP

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| M_SETUP      | LINED    | ライン       | （なし） |
| M_SETUP      | MANGRP   | 人員G        | （なし） |
| M_SETUP      | PROCESS  | 工程         | （なし） |
| M_SETUP      | RGSTD    | 登録日       | （なし） |
| M_SETUP      | SETUPA1  | 段取特性値1  | （なし） |
| M_SETUP      | SETUPA2  | 段取特性値2  | （なし） |
| M_SETUP      | SETUPG   | 段取G        | （なし） |
| M_SETUP      | SETUPTM  | 段取時間(分) | （なし） |
| M_SETUP      | UPDTD    | 更新日       | （なし） |
| M_SETUP      | UPDTWKCD | 更新担当者   | （なし） |
| M_SETUP      | WKNUM    | 人数         | （なし） |

## テーブル: M_SETUPATR

| テーブル名   | 列ID     | 列名       | 備考                                                                         |
|:-------------|:---------|:-----------|:-----------------------------------------------------------------------------|
| M_SETUPATR   | LINED    | ライン     | （なし）                                                                     |
| M_SETUPATR   | PROCESS  | 工程       | （なし）                                                                     |
| M_SETUPATR   | RGSTD    | 登録日     | （なし）                                                                     |
| M_SETUPATR   | SETUPA   | 段取特性値 | （なし）                                                                     |
| M_SETUPATR   | SETUPANM | 段取特性名 | （なし）                                                                     |
| M_SETUPATR   | SETUPG   | 段取G      | 1;第１特性;2;第２特性;3;第３特性;4;第４特性;5;第５特性;6;第６特性;7;第７特性 |
| M_SETUPATR   | UPDTD    | 更新日     | （なし）                                                                     |
| M_SETUPATR   | UPDTWKCD | 更新担当者 | （なし）                                                                     |

## テーブル: M_SMPRDCT

| テーブル名   | 列ID      | 列名             | 備考                      |
|:-------------|:----------|:-----------------|:--------------------------|
| M_SMPRDCT    | ITEM      | 品目             | （なし）                  |
| M_SMPRDCT    | PROCESS   | 工程             | （なし）                  |
| M_SMPRDCT    | QTY       | 品目取数         | （なし）                  |
| M_SMPRDCT    | RGSTD     | 登録日           | （なし）                  |
| M_SMPRDCT    | SMPRDCTF  | 同時生産区分     | 0;同時に生産;1;事前に生産 |
| M_SMPRDCT    | SMPRDCTIM | 同時生産品目     | （なし）                  |
| M_SMPRDCT    | SMQTY     | 同時生産品目取数 | （なし）                  |
| M_SMPRDCT    | UPDTD     | 更新日           | （なし）                  |
| M_SMPRDCT    | UPDTWKCD  | 更新担当者       | （なし）                  |
| M_SMPRDCT    | VENDOR    | 仕入先           | （なし）                  |

## テーブル: M_SUBJECT

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| M_SUBJECT    | RGSTD    | 登録日     | （なし） |
| M_SUBJECT    | SBJCT    | 科目       | （なし） |
| M_SUBJECT    | SBJCTNM  | 科目名     | （なし） |
| M_SUBJECT    | UPDTD    | 更新日     | （なし） |
| M_SUBJECT    | UPDTWKCD | 更新担当者 | （なし） |

## テーブル: M_SYSMANAGE

| テーブル名   | 列ID        | 列名                   | 備考     |
|:-------------|:------------|:-----------------------|:---------|
| M_SYSMANAGE  | ADDRESS     | 住所                   | （なし） |
| M_SYSMANAGE  | BANKCD      | 銀行コード             | （なし） |
| M_SYSMANAGE  | BIKO_KEIJYO | 買掛金計上通知書用備考 | （なし） |
| M_SYSMANAGE  | BIKO_SEIKYU | 請求書用備考           | （なし） |
| M_SYSMANAGE  | CLMTD       | 前回請求処理日         | （なし） |
| M_SYSMANAGE  | CMMS        | 郵送料                 | （なし） |
| M_SYSMANAGE  | COMPNM      | 会社名                 | （なし） |
| M_SYSMANAGE  | FAX         | FAX                    | （なし） |
| M_SYSMANAGE  | KOZA_F      | 口座種別               | （なし） |
| M_SYSMANAGE  | KOZA_NM     | 口座名称               | （なし） |
| M_SYSMANAGE  | KOZANO      | 口座番号               | （なし） |
| M_SYSMANAGE  | MAILADR     | ﾒｰﾙｱﾄﾞﾚｽ               | （なし） |
| M_SYSMANAGE  | ODETD       | 請求終了処理日         | （なし） |
| M_SYSMANAGE  | ODRSTD      | 請求締日               | （なし） |
| M_SYSMANAGE  | ODSTD       | 請求開始処理日         | （なし） |
| M_SYSMANAGE  | POSTCD      | 郵便番号               | （なし） |
| M_SYSMANAGE  | PYBLMTD     | 前回買掛処理日         | （なし） |
| M_SYSMANAGE  | PYBLWSTD    | 買掛締日               | （なし） |
| M_SYSMANAGE  | PYEMTD      | 前回支払処理日         | （なし） |
| M_SYSMANAGE  | PYESTD      | 支払締日               | （なし） |
| M_SYSMANAGE  | RCBLMTD     | 前回売掛処理日         | （なし） |
| M_SYSMANAGE  | RCBLWSTD    | 売掛締日               | （なし） |
| M_SYSMANAGE  | RGSTD       | 登録日                 | （なし） |
| M_SYSMANAGE  | TAXCLCF     | 消費税計算区分         | （なし） |
| M_SYSMANAGE  | TAXCLDGT    | 消費税端数桁数         | （なし） |
| M_SYSMANAGE  | TAXF        | 消費税区分             | （なし） |
| M_SYSMANAGE  | TAXFRF      | 消費税端数区分         | （なし） |
| M_SYSMANAGE  | TEL         | TEL                    | （なし） |
| M_SYSMANAGE  | TERMINAL    | 端末情報               | （なし） |
| M_SYSMANAGE  | TRANSACTOR1 | 取引先コード1          | （なし） |
| M_SYSMANAGE  | TRANSACTOR2 | 取引先コード2          | （なし） |
| M_SYSMANAGE  | TRANSACTOR3 | 取引先コード3          | （なし） |
| M_SYSMANAGE  | TRANSACTOR4 | 取引先コード4          | （なし） |
| M_SYSMANAGE  | UPDTD       | 更新日                 | （なし） |
| M_SYSMANAGE  | UPDTWKCD    | 更新担当者             | （なし） |
| M_SYSMANAGE  | URL         | URL                    | （なし） |

## テーブル: M_TMTBL

| テーブル名   | 列ID      | 列名         | 備考     |
|:-------------|:----------|:-------------|:---------|
| M_TMTBL      | OVWKTM    | 標準残業(時) | （なし） |
| M_TMTBL      | RGSTD     | 登録日       | （なし） |
| M_TMTBL      | STDOPRTTM | 定時時間(時) | （なし） |
| M_TMTBL      | TMTBL     | 稼働時間帯   | （なし） |
| M_TMTBL      | TMTBLNM   | 稼働時間帯名 | （なし） |
| M_TMTBL      | UPDTD     | 更新日       | （なし） |
| M_TMTBL      | UPDTWKCD  | 更新担当者   | （なし） |

## テーブル: M_TMTBLD

| テーブル名   | 列ID     | 列名       | 備考          |
|:-------------|:---------|:-----------|:--------------|
| M_TMTBLD     | ENHR     | 終了時     | （なし）      |
| M_TMTBLD     | ENMN     | 終了分     | （なし）      |
| M_TMTBLD     | OPFLG    | 稼働F      | 0;定時;1;残業 |
| M_TMTBLD     | RGSTD    | 登録日     | （なし）      |
| M_TMTBLD     | SQNO     | 稼働番号   | （なし）      |
| M_TMTBLD     | STHR     | 開始時     | （なし）      |
| M_TMTBLD     | STMN     | 開始分     | （なし）      |
| M_TMTBLD     | TMTBL    | 稼働時間帯 | （なし）      |
| M_TMTBLD     | UPDTD    | 更新日     | （なし）      |
| M_TMTBLD     | UPDTWKCD | 更新担当者 | （なし）      |

## テーブル: M_TRANSACTOR

| テーブル名   | 列ID           | 列名                   | 備考                                                                                |
|:-------------|:---------------|:-----------------------|:------------------------------------------------------------------------------------|
| M_TRANSACTOR | A_EDIF         | EDI取込F               | 0;EDI以外;1;YMC20L;2;MORIC;3;YMC01                                                  |
| M_TRANSACTOR | ACCNM          | 口座番号               | （なし）                                                                            |
| M_TRANSACTOR | ACCTYP         | 口座種別               | （なし）                                                                            |
| M_TRANSACTOR | ADDODFILE      | 追加受注ファイル       | （なし）                                                                            |
| M_TRANSACTOR | ADR            | 住所                   | （なし）                                                                            |
| M_TRANSACTOR | ADR2           | 住所2                  | （なし）                                                                            |
| M_TRANSACTOR | AMCSHCLL       | 未満現金回収額         | （なし）                                                                            |
| M_TRANSACTOR | BANKCD         | 銀行コード             | （なし）                                                                            |
| M_TRANSACTOR | BILRT          | 手形割合(%)            | （なし）                                                                            |
| M_TRANSACTOR | CLAIMNO        | 請求No                 | （なし）                                                                            |
| M_TRANSACTOR | CLAIMTD        | 請求処理日             | （なし）                                                                            |
| M_TRANSACTOR | CLMCD          | 請求先                 | （なし）                                                                            |
| M_TRANSACTOR | CLND           | 顧客ｶﾚﾝﾀﾞｰ             | （なし）                                                                            |
| M_TRANSACTOR | CMMSF          | 手数料区分             | （なし）                                                                            |
| M_TRANSACTOR | COPY_SLIPCTG   | 複写伝票印刷区分       | 0;対象外;1;ヤマ発;2;その他1;3;その他2                                               |
| M_TRANSACTOR | CSHDISRT       | 現金割引率(%)          | （なし）                                                                            |
| M_TRANSACTOR | CSV1F          | 納品書CSV出力区分      | （なし）                                                                            |
| M_TRANSACTOR | CSV2F          | 請求書CSV出力区分      | （なし）                                                                            |
| M_TRANSACTOR | DLVLT          | 納入L/T（日）          | （なし）                                                                            |
| M_TRANSACTOR | FAX            | FAX                    | （なし）                                                                            |
| M_TRANSACTOR | FORCASTF       | 受注タイプ             | 0;受注生産;1;見込生産                                                               |
| M_TRANSACTOR | FRACT          | 金額端数区分           | （なし）                                                                            |
| M_TRANSACTOR | INVISSF        | 請求書発行区分         | （なし）                                                                            |
| M_TRANSACTOR | INVOICE_PRN_F  | 請求書印刷対象F        | 0：印刷無,1:支給品,2:自給品                                                         |
| M_TRANSACTOR | LOTCTRLF       | ロット管理F            | 0;ロット管理しない;1;ロット管理する                                                 |
| M_TRANSACTOR | LSTADJ         | 前回請求調整金額       | （なし）                                                                            |
| M_TRANSACTOR | LSTCORMCL      | 前回請求繰越残         | （なし）                                                                            |
| M_TRANSACTOR | LSTCORMPE      | 前回支払繰越残         | （なし）                                                                            |
| M_TRANSACTOR | LSTCORMPY      | 前回売掛繰越残         | （なし）                                                                            |
| M_TRANSACTOR | LSTCORMRC      | 前回買掛繰越残         | （なし）                                                                            |
| M_TRANSACTOR | LSTMCL         | 前回請求金額           | （なし）                                                                            |
| M_TRANSACTOR | LSTPYE         | 前回支払金額           | （なし）                                                                            |
| M_TRANSACTOR | MAILADR        | ﾒｰﾙｱﾄﾞﾚｽ               | （なし）                                                                            |
| M_TRANSACTOR | MCLLDNF        | メイン金種区分         | （なし）                                                                            |
| M_TRANSACTOR | NOTICENO       | 計上通知No             | （なし）                                                                            |
| M_TRANSACTOR | ODETD          | 請求終了処理日         | （なし）                                                                            |
| M_TRANSACTOR | ODFILE         | 受注ファイル           | （なし）                                                                            |
| M_TRANSACTOR | ODRPRCF        | 売上単価区分           | 0;出荷時、売上単価デフォルトをマスタより;1;出荷時、売上単価デフォルトをオーダーより |
| M_TRANSACTOR | ODSTD          | 請求開始処理日         | （なし）                                                                            |
| M_TRANSACTOR | OVS_F          | 海外F                  | （なし）                                                                            |
| M_TRANSACTOR | PCLLCTCY       | 支払予定月             | 0;当月;1;翌月;2;翌々月                                                              |
| M_TRANSACTOR | PCLLCTD        | 支払予定日             | （なし）                                                                            |
| M_TRANSACTOR | POSTCD         | 郵便番号               | （なし）                                                                            |
| M_TRANSACTOR | PPRNF          | 買掛元帳印刷フラグ     | 0;未完了;1;完了                                                                     |
| M_TRANSACTOR | PR_AP_F        | 売上計上区分           | 0;出荷日基準;1;顧客納期基準                                                         |
| M_TRANSACTOR | PRINT1F        | 納品書発行             | （なし）                                                                            |
| M_TRANSACTOR | PRINT2F        | 請求書発行             | （なし）                                                                            |
| M_TRANSACTOR | PRINT3F        | 支払案内書発行         | （なし）                                                                            |
| M_TRANSACTOR | PSTF           | 郵送料(金額入力)       | （なし）                                                                            |
| M_TRANSACTOR | PWSETD         | 支払締日               | （なし）                                                                            |
| M_TRANSACTOR | PYBLMTD        | 買掛処理日             | （なし）                                                                            |
| M_TRANSACTOR | PYEADJ         | 前回支払調整金額       | （なし）                                                                            |
| M_TRANSACTOR | PYECD          | 支払先                 | （なし）                                                                            |
| M_TRANSACTOR | PYEENO         | 支払書No（計上通知No） | （なし）                                                                            |
| M_TRANSACTOR | PYEMTD         | 支払処理日             | （なし）                                                                            |
| M_TRANSACTOR | RCBLMTD        | 売掛処理日             | （なし）                                                                            |
| M_TRANSACTOR | RCFILE         | 支払ファイル           | （なし）                                                                            |
| M_TRANSACTOR | REGISTRATIONNO | 適格事業者番号         | （なし）                                                                            |
| M_TRANSACTOR | RGSTD          | 登録日                 | （なし）                                                                            |
| M_TRANSACTOR | SCLLCTCY       | 入金予定月             | 0;当月;1;翌月;2;翌々月                                                              |
| M_TRANSACTOR | SCLLCTD        | 入金予定日             | （なし）                                                                            |
| M_TRANSACTOR | SEPARATEPAY_F  | 個別支払F              | 0:有、1:無                                                                          |
| M_TRANSACTOR | SGTBIL         | 手形サイト(日数)       | （なし）                                                                            |
| M_TRANSACTOR | SLIPCTG        | 現品票印刷区分         | 0:対象外、1：ヤマ発                                                                 |
| M_TRANSACTOR | SPRNF          | 売掛元帳印刷フラグ     | 0;未完了;1;完了                                                                     |
| M_TRANSACTOR | SWSETD         | 請求締日               | （なし）                                                                            |
| M_TRANSACTOR | TAXCLCF        | 消費税計算区分         | （なし）                                                                            |
| M_TRANSACTOR | TAXCLDGT       | 丸め小数桁数           | （なし）                                                                            |
| M_TRANSACTOR | TAXF           | 消費税区分             | （なし）                                                                            |
| M_TRANSACTOR | TAXFRF         | 丸め区分               | （なし）                                                                            |
| M_TRANSACTOR | TEL            | TEL                    | （なし）                                                                            |
| M_TRANSACTOR | TRANSACTOR     | 取引先                 | （なし）                                                                            |
| M_TRANSACTOR | TRANSACTORFLG  | 取引区分               | 0;顧客;1;仕入先;2;両方                                                              |
| M_TRANSACTOR | TRANSACTORNM   | 取引先名               | 0;顧客;1;仕入先                                                                     |
| M_TRANSACTOR | TRNSCLND       | 配送便ｶﾚﾝﾀﾞｰ           | （なし）                                                                            |
| M_TRANSACTOR | UPDTD          | 更新日                 | （なし）                                                                            |
| M_TRANSACTOR | UPDTWKCD       | 更新担当者             | （なし）                                                                            |
| M_TRANSACTOR | URL            | URL                    | （なし）                                                                            |

## テーブル: M_VENDOR

| テーブル名   | 列ID       | 列名                   | 備考                                |
|:-------------|:-----------|:-----------------------|:------------------------------------|
| M_VENDOR     | ACCNM      | 口座番号               | （なし）                            |
| M_VENDOR     | ACCTYP     | 口座種別               | （なし）                            |
| M_VENDOR     | ADR        | 住所                   | （なし）                            |
| M_VENDOR     | AMCSHCLL   | 未満現金回収額         | （なし）                            |
| M_VENDOR     | BANKCD     | 銀行コード             | （なし）                            |
| M_VENDOR     | BILRT      | 手形割合(%)            | （なし）                            |
| M_VENDOR     | CLLCTCY    | 支払予定月             | （なし）                            |
| M_VENDOR     | CLLCTF     | 支払予定日             | （なし）                            |
| M_VENDOR     | CMMSF      | 手数料区分             | （なし）                            |
| M_VENDOR     | CSHDISRT   | 現金割引率(%)          | （なし）                            |
| M_VENDOR     | CSV1F      | 納品書CSV出力区分      | （なし）                            |
| M_VENDOR     | CSV2F      | 買掛金計上CSV出力区分  | （なし）                            |
| M_VENDOR     | FAX        | FAX                    | （なし）                            |
| M_VENDOR     | FRACT      | 金額端数区分           | （なし）                            |
| M_VENDOR     | INVISSF    | 請求書発行区分         | （なし）                            |
| M_VENDOR     | KANRIBASYO | 管理場所区分           | （なし）                            |
| M_VENDOR     | LOTCTRLF   | ロット管理F            | 0;ロット管理しない;1;ロット管理する |
| M_VENDOR     | MAILADR    | ﾒｰﾙｱﾄﾞﾚｽ               | （なし）                            |
| M_VENDOR     | MCLLDNF    | メイン金種区分         | （なし）                            |
| M_VENDOR     | POSTCD     | 郵便番号               | （なし）                            |
| M_VENDOR     | PRINT1F    | 納品書発行区分         | （なし）                            |
| M_VENDOR     | PRINT2F    | 買掛金計上通知発行区分 | （なし）                            |
| M_VENDOR     | PSTF       | 郵送料(金額入力)       | （なし）                            |
| M_VENDOR     | PYECD      | 支払先                 | （なし）                            |
| M_VENDOR     | RGSTD      | 登録日                 | （なし）                            |
| M_VENDOR     | SGTBIL     | 手形サイト(日数)       | （なし）                            |
| M_VENDOR     | TAXCLCF    | 消費税計算区分         | （なし）                            |
| M_VENDOR     | TAXCLDGT   | 消費税端数桁数         | （なし）                            |
| M_VENDOR     | TAXF       | 消費税区分             | （なし）                            |
| M_VENDOR     | TAXFRF     | 消費税端数区分         | （なし）                            |
| M_VENDOR     | TEL        | TEL                    | （なし）                            |
| M_VENDOR     | UPDTD      | 更新日                 | （なし）                            |
| M_VENDOR     | UPDTWKCD   | 更新担当者             | （なし）                            |
| M_VENDOR     | URL        | URL                    | （なし）                            |
| M_VENDOR     | VENDOR     | 仕入先                 | （なし）                            |
| M_VENDOR     | VENDORNM   | 仕入先名               | （なし）                            |
| M_VENDOR     | WSETD      | 締日                   | （なし）                            |

## テーブル: M_WORKER

| テーブル名   | 列ID       | 列名           | 備考     |
|:-------------|:-----------|:---------------|:---------|
| M_WORKER     | CLND       | ｶﾚﾝﾀﾞｰ番号     | （なし） |
| M_WORKER     | EFFICIENCY | 効率(%)        | （なし） |
| M_WORKER     | OFFTMTBL   | 休出稼働時間帯 | （なし） |
| M_WORKER     | RGSTD      | 登録日         | （なし） |
| M_WORKER     | STDTMTBL   | 標準稼働時間帯 | （なし） |
| M_WORKER     | UPDTD      | 更新日         | （なし） |
| M_WORKER     | UPDTWKCD   | 更新担当者     | （なし） |
| M_WORKER     | WKGRP      | 生産人員G      | （なし） |
| M_WORKER     | WKGRPNM    | 生産人員G名    | （なし） |
| M_WORKER     | WKNUM      | 人員数         | （なし） |

## テーブル: M_WORKER_G

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| M_WORKER_G   | RGSTD    | 登録日       | （なし） |
| M_WORKER_G   | RGSTWKCD | 登録担当者   | （なし） |
| M_WORKER_G   | SECT     | 部門         | （なし） |
| M_WORKER_G   | UPDTD    | 更新日       | （なし） |
| M_WORKER_G   | UPDTWKCD | 更新担当者   | （なし） |
| M_WORKER_G   | WORKER   | 作業者コード | （なし） |
| M_WORKER_G   | WORKERNM | 作業者名     | （なし） |

## テーブル: NNL_LOSS_HISTORY

| テーブル名       | 列ID      | 列名           | 備考                            |
|:-----------------|:----------|:---------------|:--------------------------------|
| NNL_LOSS_HISTORY | ACTFNTIME | 生産終了日時   | 'YYYY/MM/DD HH:MM               |
| NNL_LOSS_HISTORY | ACTSTDATE | 生産日         | '生産日　YYYY/MM/DD             |
| NNL_LOSS_HISTORY | ACTSTTIME | 生産開始日時   | 'YYYY/MM/DD HH:MM               |
| NNL_LOSS_HISTORY | COUNTER   | 内部登録No     | '１からの連番                   |
| NNL_LOSS_HISTORY | DEL_FLG   | 削除フラグ     | '0：通常、1:NNL削除             |
| NNL_LOSS_HISTORY | END_FLG   | 稼働終了フラグ | '0:稼働中、2：直終了            |
| NNL_LOSS_HISTORY | ITEM      | 品目           | 'OEE能力マスタの品目            |
| NNL_LOSS_HISTORY | LINED     | ライン         | 'OEE能力マスタのライン          |
| NNL_LOSS_HISTORY | LOSS3_FLG | 計画停止フラグ | 1:計画停止ロス、0：運用停止ロス |
| NNL_LOSS_HISTORY | PROCESS   | 工程           | 'OEE能力マスタの工程            |
| NNL_LOSS_HISTORY | RGSTD     | 登録日         | YYYY/MM/DD HH;MM;SS             |
| NNL_LOSS_HISTORY | RGSTWKCD  | 登録担当者     | （なし）                        |
| NNL_LOSS_HISTORY | SHIFTF    | 直区分         | 1;1直;2;2直                     |
| NNL_LOSS_HISTORY | UPDTD     | 更新日         | （なし）                        |
| NNL_LOSS_HISTORY | UPDTWKCD  | 更新担当者     | （なし）                        |
| NNL_LOSS_HISTORY | VENDOR    | 仕入先         | 'OEE能力マスタの仕入先          |

## テーブル: NNL_PRODUCT_HISTORY

| テーブル名          | 列ID      | 列名           | 備考                                     |
|:--------------------|:----------|:---------------|:-----------------------------------------|
| NNL_PRODUCT_HISTORY | ACTSTDATE | 生産日         | '生産日　YYYY/MM/DD                      |
| NNL_PRODUCT_HISTORY | CMPQTY    | 生産数         | （なし）                                 |
| NNL_PRODUCT_HISTORY | COUNTER   | 内部登録No     | '同一品目・ライン・直場合に＋１（1より） |
| NNL_PRODUCT_HISTORY | DEL_FLG   | 削除フラグ     | '0：通常、1:NNL削除                      |
| NNL_PRODUCT_HISTORY | END_FLG   | 稼働終了フラグ | '0:稼働中、2：直終了                     |
| NNL_PRODUCT_HISTORY | ITEM      | 品目           | 'OEE能力マスタの品目                     |
| NNL_PRODUCT_HISTORY | LINED     | ライン         | 'OEE能力マスタのライン                   |
| NNL_PRODUCT_HISTORY | PROCESS   | 工程           | 'OEE能力マスタの工程                     |
| NNL_PRODUCT_HISTORY | RGSTD     | 登録日         | YYYY/MM/DD HH;MM;SS                      |
| NNL_PRODUCT_HISTORY | RGSTWKCD  | 登録担当者     | （なし）                                 |
| NNL_PRODUCT_HISTORY | SHIFTF    | 直区分         | 1;1直;2;2直                              |
| NNL_PRODUCT_HISTORY | UPDTD     | 更新日         | （なし）                                 |
| NNL_PRODUCT_HISTORY | UPDTWKCD  | 更新担当者     | （なし）                                 |
| NNL_PRODUCT_HISTORY | VENDOR    | 仕入先         | 'OEE能力マスタの仕入先                   |

## テーブル: NNL_SHIFT_HISTORY

| テーブル名        | 列ID      | 列名           | 備考                              |
|:------------------|:----------|:---------------|:----------------------------------|
| NNL_SHIFT_HISTORY | ACTFNTIME | 生産終了日時   | （なし）                          |
| NNL_SHIFT_HISTORY | ACTSTDATE | 生産日         | '生産日　YYYY/MM/DD               |
| NNL_SHIFT_HISTORY | ACTSTTIME | 生産開始日時   | 'HHMM                             |
| NNL_SHIFT_HISTORY | DEL_FLG   | 削除フラグ     | '0：通常、1:NNL削除               |
| NNL_SHIFT_HISTORY | END_FLG   | 稼働終了フラグ | '0:稼働中、1:稼働終了、２：直終了 |
| NNL_SHIFT_HISTORY | ITEM      | 品目           | 'OEE能力マスタの品目              |
| NNL_SHIFT_HISTORY | LINED     | ライン         | 'OEE能力マスタのライン            |
| NNL_SHIFT_HISTORY | PROCESS   | 工程           | 'OEE能力マスタの工程              |
| NNL_SHIFT_HISTORY | RGSTD     | 登録日         | （なし）                          |
| NNL_SHIFT_HISTORY | RGSTWKCD  | 登録担当者     | （なし）                          |
| NNL_SHIFT_HISTORY | SHIFTF    | 直区分         | 1;1直;2;2直                       |
| NNL_SHIFT_HISTORY | SUB_NO    | 件数           | 'HHMM                             |
| NNL_SHIFT_HISTORY | UPDTD     | 更新日         | （なし）                          |
| NNL_SHIFT_HISTORY | UPDTWKCD  | 更新担当者     | （なし）                          |
| NNL_SHIFT_HISTORY | VENDOR    | 仕入先         | 'OEE能力マスタの仕入先            |

## テーブル: ORA_VERSION

| テーブル名   | 列ID    | 列名             | 備考     |
|:-------------|:--------|:-----------------|:---------|
| ORA_VERSION  | ORA_VER | Oracleバージョン | （なし） |

## テーブル: ORDERCMP

| テーブル名   | 列ID        | 列名   | 備考     |
|:-------------|:------------|:-------|:---------|
| ORDERCMP     | CUSTOM      | 顧客   | （なし） |
| ORDERCMP     | DATE        | 日付   | （なし） |
| ORDERCMP     | DELIDATE_EN | 終了日 | （なし） |
| ORDERCMP     | DELIDATE_ST | 開始日 | （なし） |
| ORDERCMP     | DIFQTY      | 差数   | （なし） |
| ORDERCMP     | ITEM        | 品目   | （なし） |
| ORDERCMP     | PROCESS     | 工程   | （なし） |
| ORDERCMP     | S_DIFQTY    | 差数   | （なし） |
| ORDERCMP     | VENDOR      | 仕入先 | （なし） |

## テーブル: ORDERCMP_D

| テーブル名   | 列ID       | 列名       | 備考     |
|:-------------|:-----------|:-----------|:---------|
| ORDERCMP_D   | CUSTOM     | 顧客       | （なし） |
| ORDERCMP_D   | DELIDATE   | 日付       | （なし） |
| ORDERCMP_D   | ITEM       | 品目       | （なし） |
| ORDERCMP_D   | ORDERQTY_F | 前回受注数 | （なし） |
| ORDERCMP_D   | ORDERQTY_T | 今回受注数 | （なし） |
| ORDERCMP_D   | PROCESS    | 工程       | （なし） |
| ORDERCMP_D   | S_DIFQTY   | 差異       | （なし） |
| ORDERCMP_D   | VENDOR     | 仕入先     | （なし） |

## テーブル: PASSWORD

| テーブル名   | 列ID     | 列名           | 備考     |
|:-------------|:---------|:---------------|:---------|
| PASSWORD     | LAYOUT   | レイアウト変更 | （なし） |
| PASSWORD     | PASSWORD | パスワード     | （なし） |
| PASSWORD     | RGSTD    | 登録日         | （なし） |
| PASSWORD     | SETTING  | 設定           | （なし） |
| PASSWORD     | UPDTD    | 更新日         | （なし） |
| PASSWORD     | UPDTWKCD | 更新担当者     | （なし） |
| PASSWORD     | USERID   | グループＩＤ   | （なし） |

## テーブル: PASSWORDD

| テーブル名   | 列ID        | 列名         | 備考                  |
|:-------------|:------------|:-------------|:----------------------|
| PASSWORDD    | AUTHORITY_F | 権限フラグ   | 0:権限なし;1:権限あり |
| PASSWORDD    | MENUID      | メニューID   | （なし）              |
| PASSWORDD    | NAME_C      | メニュー名称 | （なし）              |
| PASSWORDD    | NAME_E      | メニュー名称 | （なし）              |
| PASSWORDD    | NAME_I      | メニュー名称 | （なし）              |
| PASSWORDD    | NAME_J      | メニュー名称 | （なし）              |
| PASSWORDD    | NAME_T      | メニュー名称 | （なし）              |
| PASSWORDD    | NAME_Y      | メニュー名称 | （なし）              |
| PASSWORDD    | NAME_Z      | メニュー名称 | （なし）              |
| PASSWORDD    | USERID      | ユーザーＩＤ | （なし）              |

## テーブル: PAYSAL_P_PAYEED_ERR

| テーブル名          | 列ID         | 列名             | 備考     |
|:--------------------|:-------------|:-----------------|:---------|
| PAYSAL_P_PAYEED_ERR | APPLYDATE_CH | 対象適用日無     | （なし） |
| PAYSAL_P_PAYEED_ERR | ITEM         | 品目             | （なし） |
| PAYSAL_P_PAYEED_ERR | PRICE        | 標準単価=0       | （なし） |
| PAYSAL_P_PAYEED_ERR | PRICE_NL     | 単価マスタ登録無 | （なし） |
| PAYSAL_P_PAYEED_ERR | PROCESS      | 工程             | （なし） |
| PAYSAL_P_PAYEED_ERR | PYECD        | 支払先           | （なし） |
| PAYSAL_P_PAYEED_ERR | VENDOR       | 仕入先           | （なし） |

## テーブル: PAYSAL_P_SALES_D_ERR

| テーブル名           | 列ID         | 列名             | 備考     |
|:---------------------|:-------------|:-----------------|:---------|
| PAYSAL_P_SALES_D_ERR | APPLYDATE_CH | 対象適用日無     | （なし） |
| PAYSAL_P_SALES_D_ERR | CLMCD        | 請求先           | （なし） |
| PAYSAL_P_SALES_D_ERR | ITEM         | 品目             | （なし） |
| PAYSAL_P_SALES_D_ERR | PRICE        | 標準単価=0       | （なし） |
| PAYSAL_P_SALES_D_ERR | PRICE_NL     | 単価マスタ登録無 | （なし） |
| PAYSAL_P_SALES_D_ERR | PROCESS      | 工程             | （なし） |
| PAYSAL_P_SALES_D_ERR | VENDOR       | 仕入先           | （なし） |

## テーブル: PRICEUPD_ERR

| テーブル名   | 列ID          | 列名             | 備考     |
|:-------------|:--------------|:-----------------|:---------|
| PRICEUPD_ERR | APPLYDATE     | 単価発効日       | （なし） |
| PRICEUPD_ERR | CH_ITEM       | 子旧体系品目番号 | （なし） |
| PRICEUPD_ERR | CH_SUPPLIER   | 子品目供給者     | （なし） |
| PRICEUPD_ERR | CH_USER       | 子品目使用者     | （なし） |
| PRICEUPD_ERR | CONTRACTDATE  | 契約成立日       | （なし） |
| PRICEUPD_ERR | COUNTER       | 内部登録No       | （なし） |
| PRICEUPD_ERR | ERROR         | エラー内容       | （なし） |
| PRICEUPD_ERR | ITEM_CLASS    | 品目クラス       | （なし） |
| PRICEUPD_ERR | MATERIAL_COST | 材料費           | （なし） |
| PRICEUPD_ERR | PA_CH_FLG     | 親子区分         | （なし） |
| PRICEUPD_ERR | PA_ITEM       | 親旧体系品目番号 | （なし） |
| PRICEUPD_ERR | PA_PRICE      | 納入単価         | （なし） |
| PRICEUPD_ERR | PA_SUPPLIER   | 親品目供給者     | （なし） |
| PRICEUPD_ERR | PA_USER       | 親品目使用者     | （なし） |
| PRICEUPD_ERR | PARTS_PRICE   | パーツ納入単価   | （なし） |
| PRICEUPD_ERR | PHUNIT        | 投入重量         | （なし） |
| PRICEUPD_ERR | PROCESS_COST  | 加工費           | （なし） |
| PRICEUPD_ERR | REASON_CD1    | 原因コード1      | （なし） |
| PRICEUPD_ERR | REASON_CD2    | 原因コード2      | （なし） |
| PRICEUPD_ERR | SCR_PHUNIT    | スクラップ重量   | （なし） |
| PRICEUPD_ERR | SCR_PRICE     | スクラップ単価   | （なし） |
| PRICEUPD_ERR | SCRAP_COST    | スクラップ費     | （なし） |
| PRICEUPD_ERR | SU_CODE       | S/Uコード        | （なし） |
| PRICEUPD_ERR | SU_FLG        | S/U区分          | （なし） |
| PRICEUPD_ERR | TRANSACTOR    | 取引先コード     | （なし） |

## テーブル: PROCESS_CLNDD

| テーブル名    | 列ID       | 列名   | 備考     |
|:--------------|:-----------|:-------|:---------|
| PROCESS_CLNDD | CLNDDATE1  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE10 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE11 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE12 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE13 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE14 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE15 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE16 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE17 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE18 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE19 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE2  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE20 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE21 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE22 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE23 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE24 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE25 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE26 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE27 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE28 | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE3  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE4  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE5  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE6  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE7  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE8  | 日付   | （なし） |
| PROCESS_CLNDD | CLNDDATE9  | 日付   | （なし） |
| PROCESS_CLNDD | PROCESS    | 工程   | （なし） |

## テーブル: PROCESS_COST_INVO

| テーブル名        | 列ID             | 列名                     | 備考                                                                                            |
|:------------------|:-----------------|:-------------------------|:------------------------------------------------------------------------------------------------|
| PROCESS_COST_INVO | A_FPTYPE         | 処理（購入）区分         | R：固定自給 Y：有償支給 N：無償支給　G：変動自給                                                |
| PROCESS_COST_INVO | ACT_P3           | 実際外注加工費           | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_P4           | 実際社内加工費           | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PRE_PS_TTL   | 前工程実績合計           | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PRE_PS3      | 前工程実際積上げ外注費   | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PRE_PS6      | 前工程実際積上げ支給費   | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PS_TTL       | 実際積上合計             | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PS_TTL_KOB   | 親KOB積上げ合計          | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PS3          | 実際積上外注加工費       | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PS4          | 実際積上社内加工費       | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PS5          | 実際積上管理費           | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_PS6          | 実際積上支給費           | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_SHIP_PS_TTL  | 出荷工程実際積上げ実績計 | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_SHIP_PS4     | 出荷工程実際積上げ外注費 | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_SHIP_PS5     | 出荷工程実際積上げ管理費 | （なし）                                                                                        |
| PROCESS_COST_INVO | ACT_SHIP_PS6     | 出荷工程実際積上げ支給費 | （なし）                                                                                        |
| PROCESS_COST_INVO | AMTMNY           | (調整前）請求金額        | （なし）                                                                                        |
| PROCESS_COST_INVO | CLAMTMNY         | 請求金額                 | （なし）                                                                                        |
| PROCESS_COST_INVO | COUNTER          | 内部登録No               | （なし）                                                                                        |
| PROCESS_COST_INVO | CUST_ISSUENO     | 得意先伝票No             | （なし）                                                                                        |
| PROCESS_COST_INVO | DITEM            | 入力品目                 | （なし）                                                                                        |
| PROCESS_COST_INVO | DPROCESS         | 入力工程                 | （なし）                                                                                        |
| PROCESS_COST_INVO | DRWNO            | 部品番号                 | （なし）                                                                                        |
| PROCESS_COST_INVO | EDIT_CHK         | 選択                     | （なし）                                                                                        |
| PROCESS_COST_INVO | ERR_F            | エラーF                  | 原価積み上げマスタにて最上位工程の積み上げ単価取得時、最上位が複数時に1とする。                 |
| PROCESS_COST_INVO | FCNAME           | 返品理由                 | （なし）                                                                                        |
| PROCESS_COST_INVO | HITEM            | 親品目                   | （なし）                                                                                        |
| PROCESS_COST_INVO | HPROCESS         | 親工程                   | （なし）                                                                                        |
| PROCESS_COST_INVO | IMNM             | 品名                     | （なし）                                                                                        |
| PROCESS_COST_INVO | ITEM             | 品目                     | （なし）                                                                                        |
| PROCESS_COST_INVO | PRE_ITEM         | 前品目                   | （なし）                                                                                        |
| PROCESS_COST_INVO | PRE_PROCESS      | 前工程                   | （なし）                                                                                        |
| PROCESS_COST_INVO | PRICE            | 単価                     | （なし）                                                                                        |
| PROCESS_COST_INVO | PRINTF           | 請求書印刷F              | （なし）                                                                                        |
| PROCESS_COST_INVO | PROCESS          | 工程                     | （なし）                                                                                        |
| PROCESS_COST_INVO | RATE_PRICE       | 単価加工比率             | （なし）                                                                                        |
| PROCESS_COST_INVO | RCISQTY          | 数量                     | （なし）                                                                                        |
| PROCESS_COST_INVO | RECEIPT_DATE     | 伝票発行日               | （なし）                                                                                        |
| PROCESS_COST_INVO | REMARK           | 備考                     | （なし）                                                                                        |
| PROCESS_COST_INVO | RESP_SECT        | 請求先                   | （なし）                                                                                        |
| PROCESS_COST_INVO | RGSTD            | 登録日                   | （なし）                                                                                        |
| PROCESS_COST_INVO | RGSTWKCD         | 登録担当者               | （なし）                                                                                        |
| PROCESS_COST_INVO | RSPNSBL          | 組付け子部品             | （なし）                                                                                        |
| PROCESS_COST_INVO | S_DPROCESS       | 入力工程                 | （なし）                                                                                        |
| PROCESS_COST_INVO | S_HAPPENDATE     | 発生日                   | （なし）                                                                                        |
| PROCESS_COST_INVO | S_ISSUENO        | 伝票No                   | （なし）                                                                                        |
| PROCESS_COST_INVO | SEPARATEPAY_F    | 個別支払F                | 0:有、1:無                                                                                      |
| PROCESS_COST_INVO | SOZ_RECEIPT_DATE | 部品受領日               | 部品受領日とは不良発生日-品目マスタの入荷予定日を工程単位のカレンダー稼働日でオフセットしたもの |
| PROCESS_COST_INVO | TRANSACTOR_G     | 請求先G                  | （なし）                                                                                        |
| PROCESS_COST_INVO | UPDTD            | 更新日                   | （なし）                                                                                        |
| PROCESS_COST_INVO | UPDTWKCD         | 更新担当者               | （なし）                                                                                        |
| PROCESS_COST_INVO | WKRATE           | 進度(%)                  | （なし）                                                                                        |
| PROCESS_COST_INVO | YEARMONTH        | 処理年月                 | （なし）                                                                                        |

## テーブル: PRODUCT

| テーブル名   | 列ID          | 列名                       | 備考                                                                      |
|:-------------|:--------------|:---------------------------|:--------------------------------------------------------------------------|
| PRODUCT      | A_ITMSTATUS   | ステータス                 | 1;試作;2;生試;3;初品;4;量産;6;製品打切;7;サービスパーツ;8;削除;9;製作不可 |
| PRODUCT      | ACTFNDATE     | 最終生産時間               | （なし）                                                                  |
| PRODUCT      | ACTFNDATE_R   | 最終生産時間               | （なし）                                                                  |
| PRODUCT      | ACTFNTIME     | 最終生産時間(時分)         | （なし）                                                                  |
| PRODUCT      | ACTSTDATE     | 開始日                     | （なし）                                                                  |
| PRODUCT      | ACTSTDATE_R   | 開始日                     | （なし）                                                                  |
| PRODUCT      | ACTSTTIME     | 開始時間(時分)             | （なし）                                                                  |
| PRODUCT      | ACTSTTIME_R   | 開始時間(時分)             | （なし）                                                                  |
| PRODUCT      | ADDFLG        | 追加オーダＦ               | 0;通常発行1;追加発行                                                      |
| PRODUCT      | BKTNO         | バケットNo                 | （なし）                                                                  |
| PRODUCT      | BKTYEAR       | バケット年                 | （なし）                                                                  |
| PRODUCT      | CFM_F         | 確定F                      | （なし）                                                                  |
| PRODUCT      | CMPFLG        | 完了Ｆ                     | 0;未完了;1;完了                                                           |
| PRODUCT      | CMPFLG_R      | 完了Ｆ                     | 0;未完了;1;完了                                                           |
| PRODUCT      | CMPQTY        | 完成数                     | （なし）                                                                  |
| PRODUCT      | CMPQTY_R      | 完成数                     | （なし）                                                                  |
| PRODUCT      | CYCLETIME     | サイクルタイム(秒)         | （なし）                                                                  |
| PRODUCT      | FNDATE        | 完了予定日                 | （なし）                                                                  |
| PRODUCT      | FNTIME        | 完了予定時間(時分)         | （なし）                                                                  |
| PRODUCT      | ITEM          | 品目                       | （なし）                                                                  |
| PRODUCT      | LATE_F        | 遅延F                      | 0;遅延ではない;1;遅延                                                     |
| PRODUCT      | LEVELD        | ﾚﾍﾞﾙ                       | （なし）                                                                  |
| PRODUCT      | LINED         | 指示ライン                 | （なし）                                                                  |
| PRODUCT      | LINED_R       | 実績ライン                 | （なし）                                                                  |
| PRODUCT      | LOCT_R        | 場所                       | （なし）                                                                  |
| PRODUCT      | MPSORDERNO    | 基準生産計画オーダNo       | （なし）                                                                  |
| PRODUCT      | MRPLOSS       | 展開ロス量                 | （なし）                                                                  |
| PRODUCT      | OFFCLF        | 確定/内示Ｆ                | 0;内示;1;確定                                                             |
| PRODUCT      | PLANDATE      | 指示日                     | （なし）                                                                  |
| PRODUCT      | POSTSETUPMAN  | 人後段取時間（人時）       | （なし）                                                                  |
| PRODUCT      | POSTSETUPTIME | 後段取時間                 | （なし）                                                                  |
| PRODUCT      | PRDCTBNO      | 枝番                       | （なし）                                                                  |
| PRODUCT      | PRDCTMANH     | 人稼働時間（人時）         | （なし）                                                                  |
| PRODUCT      | PRDCTNO       | 製番                       | （なし）                                                                  |
| PRODUCT      | PRDCTQTY      | 指示数                     | （なし）                                                                  |
| PRODUCT      | PRDCTSQ       | 順序                       | （なし）                                                                  |
| PRODUCT      | PRDCTTIME     | 稼働時間(分)               | （なし）                                                                  |
| PRODUCT      | PRNFLG        | 製造指示表印刷完了Ｆ       | 0;印刷未完了;1;印刷完了                                                   |
| PRODUCT      | PRNFLG2       | 製造計画表印刷完了Ｆ       | 0;印刷未完了;1;印刷完了                                                   |
| PRODUCT      | PRNFLG3       | 出庫依頼書印刷完了F        | 0;印刷未完了;1;印刷完了                                                   |
| PRODUCT      | PROCESS       | 工程                       | （なし）                                                                  |
| PRODUCT      | PRODUCTITEM   | 完成品品目                 | （なし）                                                                  |
| PRODUCT      | PRORDERNO     | オーダNo                   | （なし）                                                                  |
| PRODUCT      | PRSTDATE      | 稼働開始日                 | （なし）                                                                  |
| PRODUCT      | PRSTTIME      | 稼働開始時間(時分)         | （なし）                                                                  |
| PRODUCT      | RCISCD        | 入出庫区分                 | （なし）                                                                  |
| PRODUCT      | RCORDERNO     | 受注No                     | （なし）                                                                  |
| PRODUCT      | REMARK        | 備考                       | （なし）                                                                  |
| PRODUCT      | REMARK_R      | 備考                       | （なし）                                                                  |
| PRODUCT      | REQQTY        | 必要数                     | （なし）                                                                  |
| PRODUCT      | RGSTD         | 登録日                     | （なし）                                                                  |
| PRODUCT      | SCHLOSS       | 指示ロス量                 | （なし）                                                                  |
| PRODUCT      | SCRPQTY       | 不良数                     | （なし）                                                                  |
| PRODUCT      | SCRPQTY_R     | 不良数                     | （なし）                                                                  |
| PRODUCT      | SETUPMANH     | 人段取時間（人時）         | （なし）                                                                  |
| PRODUCT      | SETUPTIME     | 段取時間(分)               | （なし）                                                                  |
| PRODUCT      | STTM          | 開始予定時間(分)           | （なし）                                                                  |
| PRODUCT      | STTMA         | 開始予定時間(相対時間(分)) | （なし）                                                                  |
| PRODUCT      | UPDTD         | 更新日                     | （なし）                                                                  |
| PRODUCT      | UPDTWKCD      | 更新担当者                 | （なし）                                                                  |
| PRODUCT      | VENDOR        | 仕入先                     | （なし）                                                                  |
| PRODUCT      | WORKCD_R      | 担当者                     | （なし）                                                                  |
| PRODUCT      | XLSXADDF      | エクセル追加F              | 0:その他;1;エクセル追加                                                   |

## テーブル: PRODUCTLOTD

| テーブル名   | 列ID         | 列名             | 備考                                 |
|:-------------|:-------------|:-----------------|:-------------------------------------|
| PRODUCTLOTD  | INLOTITEM    | 投入ロット品目   | （なし）                             |
| PRODUCTLOTD  | INLOTPROCESS | 投入ロット工程   | （なし）                             |
| PRODUCTLOTD  | INLOTVENDOR  | 投入ロット仕入先 | （なし）                             |
| PRODUCTLOTD  | INPUTLOTNO   | 投入ロットNo     | （なし）                             |
| PRODUCTLOTD  | ITEM         | 品目             | （なし）                             |
| PRODUCTLOTD  | LOTNO        | 生産ロットNo     | 日付8桁＋工程5桁＋ライン5桁＋連番5桁 |
| PRODUCTLOTD  | PROCESS      | 工程             | （なし）                             |
| PRODUCTLOTD  | RGSTD        | 登録日           | （なし）                             |
| PRODUCTLOTD  | UPDTD        | 更新日           | （なし）                             |
| PRODUCTLOTD  | UPDTWKCD     | 更新担当者       | （なし）                             |
| PRODUCTLOTD  | VENDOR       | 仕入先           | （なし）                             |

## テーブル: PRODUCTRESULT

| テーブル名    | 列ID          | 列名                   | 備考                                 |
|:--------------|:--------------|:-----------------------|:-------------------------------------|
| PRODUCTRESULT | ACTFNTIME     | 生産終了時間           | （なし）                             |
| PRODUCTRESULT | ACTLINED      | 実績ライン             | （なし）                             |
| PRODUCTRESULT | ACTSTDATE     | 生産日                 | （なし）                             |
| PRODUCTRESULT | ACTSTTIME     | 生産開始時間           | （なし）                             |
| PRODUCTRESULT | CMPFLG        | 完了Ｆ                 | 0;未完了;1;完了                      |
| PRODUCTRESULT | CMPQTY        | 生産数                 | （なし）                             |
| PRODUCTRESULT | COUNTER       | 内部登録No             | 'PRODUCT_HISTORYよりセット           |
| PRODUCTRESULT | CYCLETM       | 実績サイクルタイム(秒) | （なし）                             |
| PRODUCTRESULT | LOCT          | 場所                   | （なし）                             |
| PRODUCTRESULT | LOTNO         | ロットNo               | 日付8桁＋工程5桁＋ライン5桁＋連番5桁 |
| PRODUCTRESULT | NONOPTIME     | 実績非稼働時間(分)     | （なし）                             |
| PRODUCTRESULT | POSTSETUPTIME | 実績後段取時間(分)     | （なし）                             |
| PRODUCTRESULT | PRDCTTIME     | 実績稼働時間(分)       | （なし）                             |
| PRODUCTRESULT | PROCESS       | 工程                   | （なし）                             |
| PRODUCTRESULT | PRORDERNO     | オーダNo               | （なし）                             |
| PRODUCTRESULT | RCISCD        | 入出庫区分             | （なし）                             |
| PRODUCTRESULT | REMARK        | 備考                   | （なし）                             |
| PRODUCTRESULT | RGSTD         | 登録日時               | YYYY/MM/DD HH;MM;SS(非表示項目)      |
| PRODUCTRESULT | RGSTTM        | 登録時刻               | （なし）                             |
| PRODUCTRESULT | SCRPQTY       | 不良数                 | （なし）                             |
| PRODUCTRESULT | SETUPTIME     | 実績段取時間(分)       | （なし）                             |
| PRODUCTRESULT | UPDTD         | 更新日                 | （なし）                             |
| PRODUCTRESULT | UPDTWKCD      | 更新担当者             | （なし）                             |
| PRODUCTRESULT | WORKER        | 生産人員数             | （なし）                             |
| PRODUCTRESULT | WORKERCD      | 担当者                 | （なし）                             |

## テーブル: PRODUCT_HISTORY

| テーブル名      | 列ID      | 列名       | 備考                                       |
|:----------------|:----------|:-----------|:-------------------------------------------|
| PRODUCT_HISTORY | ACTSTDATE | 生産日     | （なし）                                   |
| PRODUCT_HISTORY | CMPQTY    | 生産数     | （なし）                                   |
| PRODUCT_HISTORY | COUNTER   | 内部登録No | （なし）                                   |
| PRODUCT_HISTORY | FIX_FLG   | 承認F      | 0:未承認（未連携）、1:承認済み（連携済み） |
| PRODUCT_HISTORY | ITEM      | 品目       | （なし）                                   |
| PRODUCT_HISTORY | LINED     | ライン     | （なし）                                   |
| PRODUCT_HISTORY | OEE_LINED | 実績ライン | （なし）                                   |
| PRODUCT_HISTORY | PROCESS   | 工程       | （なし）                                   |
| PRODUCT_HISTORY | RGSTD     | 登録日     | YYYY/MM/DD HH;MM;SS                        |
| PRODUCT_HISTORY | RGSTWKCD  | 登録担当者 | （なし）                                   |
| PRODUCT_HISTORY | SHIFTF    | 直区分     | 1;1直;2;2直;3;3直                          |
| PRODUCT_HISTORY | UPDTD     | 更新日     | （なし）                                   |
| PRODUCT_HISTORY | UPDTFLG   | 更新F      | （なし）                                   |
| PRODUCT_HISTORY | UPDTWKCD  | 更新担当者 | （なし）                                   |
| PRODUCT_HISTORY | VENDOR    | 仕入先     | （なし）                                   |

## テーブル: PR_B_LEDGERW

| テーブル名   | 列ID      | 列名           | 備考     |
|:-------------|:----------|:---------------|:---------|
| PR_B_LEDGERW | AMTMNY    | 仕入額         | （なし） |
| PR_B_LEDGERW | AMTTAX    | 消費税         | （なし） |
| PR_B_LEDGERW | CHKD      | 伝票日付       | （なし） |
| PR_B_LEDGERW | CHKNO     | 伝票番号       | （なし） |
| PR_B_LEDGERW | IMNM      | 品名           | （なし） |
| PR_B_LEDGERW | ITEM      | 品目           | （なし） |
| PR_B_LEDGERW | LSTCORMRC | 買掛残高       | （なし） |
| PR_B_LEDGERW | PAMTMNY   | 支払額         | （なし） |
| PR_B_LEDGERW | PYECD     | 支払先         | （なし） |
| PR_B_LEDGERW | SLPF      | 伝票区分       | （なし） |
| PR_B_LEDGERW | SPLYQTY   | 仕入数         | （なし） |
| PR_B_LEDGERW | TAXCLCF   | 消費税計算区分 | （なし） |
| PR_B_LEDGERW | TAXF      | 消費税区分     | （なし） |
| PR_B_LEDGERW | UNTPRC    | 単価           | （なし） |
| PR_B_LEDGERW | VENDORNM  | 支払先名称     | （なし） |

## テーブル: PR_B_LEDGERW2

| テーブル名    | 列ID      | 列名                           | 備考     |
|:--------------|:----------|:-------------------------------|:---------|
| PR_B_LEDGERW2 | ADJMNY    | 調整額                         | （なし） |
| PR_B_LEDGERW2 | AMTTAX    | 消費税                         | （なし） |
| PR_B_LEDGERW2 | LSTCORMRC | 前月繰越残高                   | （なし） |
| PR_B_LEDGERW2 | MAMTMNY   | 翌月繰越残高                   | （なし） |
| PR_B_LEDGERW2 | NAMTMNY   | 相殺額                         | （なし） |
| PR_B_LEDGERW2 | NAMTMNY2  | その他相殺額（手数料・郵送料） | （なし） |
| PR_B_LEDGERW2 | PAMTMNY   | 支払額                         | （なし） |
| PR_B_LEDGERW2 | PYECD     | 支払先                         | （なし） |
| PR_B_LEDGERW2 | SAMTMNY   | 仕入金額                       | （なし） |
| PR_B_LEDGERW2 | VENDORNM  | 支払先名称                     | （なし） |

## テーブル: PR_CLAIMNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| PR_CLAIMNO   | K_NO     | キー項目     | （なし） |
| PR_CLAIMNO   | LAST_OD1 | 最終オーダNo | （なし） |
| PR_CLAIMNO   | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: PR_DEMAND

| テーブル名   | 列ID       | 列名           | 備考             |
|:-------------|:-----------|:---------------|:-----------------|
| PR_DEMAND    | A_ORDERNO  | オーダNo       | （なし）         |
| PR_DEMAND    | AMTMNY     | 金額           | （なし）         |
| PR_DEMAND    | AMTTAX     | 税額           | （なし）         |
| PR_DEMAND    | BILNO      | 手形番号       | （なし）         |
| PR_DEMAND    | CCNO       | 請求連番       | （なし）         |
| PR_DEMAND    | CLAIMNO    | 請求No         | （なし）         |
| PR_DEMAND    | CLMCD      | 請求先         | （なし）         |
| PR_DEMAND    | CLWSTD     | 請求締日       | （なし）         |
| PR_DEMAND    | CUSTOM     | 得意先         | （なし）         |
| PR_DEMAND    | CUSTOMIMNM | 顧客品名       | （なし）         |
| PR_DEMAND    | CUSTOMITEM | 顧客品目       | （なし）         |
| PR_DEMAND    | CUSTOMNO   | 顧客注番       | （なし）         |
| PR_DEMAND    | DEMANDNO   | 社内注番       | （なし）         |
| PR_DEMAND    | GRA_FLG    | 有償無償フラグ | （なし）         |
| PR_DEMAND    | IMNM       | 品名           | （なし）         |
| PR_DEMAND    | ITEM       | 品目           | （なし）         |
| PR_DEMAND    | ITEMF      | 受注品目区分   | （なし）         |
| PR_DEMAND    | ITEMF2     | 支給区分       | （なし）         |
| PR_DEMAND    | LNNO       | 行番号         | （なし）         |
| PR_DEMAND    | PRNFLG     | 請求書印刷F    | 0,未完了;1,更新; |
| PR_DEMAND    | PROCESS    | 工程           | （なし）         |
| PR_DEMAND    | RCPEXD     | 入金予定日     | （なし）         |
| PR_DEMAND    | REMARK1    | 備考１         | （なし）         |
| PR_DEMAND    | REMARK2    | 備考２         | （なし）         |
| PR_DEMAND    | RGSTD      | 登録日         | （なし）         |
| PR_DEMAND    | SBJCT      | 科目           | （なし）         |
| PR_DEMAND    | SHIPQTY    | 出荷数         | （なし）         |
| PR_DEMAND    | SHPMNTD    | 出荷日         | （なし）         |
| PR_DEMAND    | SHPMNTNO   | 出荷No         | （なし）         |
| PR_DEMAND    | SLPF       | 伝票区分       | （なし）         |
| PR_DEMAND    | SLPF2      | 入金伝票区分   | （なし）         |
| PR_DEMAND    | SLSMUPD    | 売上計上日     | （なし）         |
| PR_DEMAND    | SP_F       | 単価参照F      | （なし）         |
| PR_DEMAND    | STLMTD     | 決済日         | （なし）         |
| PR_DEMAND    | TAXF       | 税区分         | （なし）         |
| PR_DEMAND    | TERMINAL   | 端末情報       | （なし）         |
| PR_DEMAND    | TOAMTMNY   | 税抜金額       | （なし）         |
| PR_DEMAND    | UNTPRC     | 単価           | （なし）         |
| PR_DEMAND    | UPDTD      | 更新日         | （なし）         |
| PR_DEMAND    | UPDTWKCD   | 更新担当者     | （なし）         |
| PR_DEMAND    | WSETD      | 締日           | （なし）         |

## テーブル: PR_DEMANDLIST

| テーブル名    | 列ID      | 列名                           | 備考     |
|:--------------|:----------|:-------------------------------|:---------|
| PR_DEMANDLIST | ADJMNY    | 調整額                         | （なし） |
| PR_DEMANDLIST | AMTTAX    | 消費税                         | （なし） |
| PR_DEMANDLIST | CLMCD     | 請求先                         | （なし） |
| PR_DEMANDLIST | CLWSTD    | 請求締日                       | （なし） |
| PR_DEMANDLIST | CUSTOMNM  | 請求先名称                     | （なし） |
| PR_DEMANDLIST | LSTCORMCL | 前月繰越残高                   | （なし） |
| PR_DEMANDLIST | LSTCORMPY | 前月繰越残高                   | （なし） |
| PR_DEMANDLIST | NAMTMNY   | 相殺額                         | （なし） |
| PR_DEMANDLIST | NAMTMNY2  | その他相殺額（手数料・郵送料） | （なし） |
| PR_DEMANDLIST | SAMTMNY   | 入金額                         | （なし） |
| PR_DEMANDLIST | UAMTMNY   | 売上金額                       | （なし） |

## テーブル: PR_DEMAND_LST

| テーブル名    | 列ID      | 列名               | 備考     |
|:--------------|:----------|:-------------------|:---------|
| PR_DEMAND_LST | ADJMNY    | 調整額             | （なし） |
| PR_DEMAND_LST | ADR       | 住所               | （なし） |
| PR_DEMAND_LST | AMTMNY    | 合計金額           | （なし） |
| PR_DEMAND_LST | CLAIMNO   | 請求No             | （なし） |
| PR_DEMAND_LST | CLMCD     | 請求先             | （なし） |
| PR_DEMAND_LST | CLWSTD    | 請求締日           | （なし） |
| PR_DEMAND_LST | CLWSTED   | 請求締終了日       | （なし） |
| PR_DEMAND_LST | CLWSTSD   | 請求締開始日       | （なし） |
| PR_DEMAND_LST | CUSTOMNM  | 請求先名称         | （なし） |
| PR_DEMAND_LST | FAX       | FAX                | （なし） |
| PR_DEMAND_LST | LAMTCMNY  | 前回請求額         | （なし） |
| PR_DEMAND_LST | LSTCORMPY | 今回売掛繰越残     | （なし） |
| PR_DEMAND_LST | NAMTCMNY  | 今回請求額         | （なし） |
| PR_DEMAND_LST | OAMTMNY   | その他金額         | （なし） |
| PR_DEMAND_LST | POSTCD    | 郵便番号           | （なし） |
| PR_DEMAND_LST | PRN_F     | 印刷F              | （なし） |
| PR_DEMAND_LST | RGSTD     | 登録日             | （なし） |
| PR_DEMAND_LST | TEL       | TEL                | （なし） |
| PR_DEMAND_LST | TERMINAL  | 端末情報           | （なし） |
| PR_DEMAND_LST | TTRCPBL   | 今回入金（手形）   | （なし） |
| PR_DEMAND_LST | TTRCPC    | 今回入金（その他） | （なし） |
| PR_DEMAND_LST | TTRCPCB   | 今回入金（相殺）   | （なし） |
| PR_DEMAND_LST | TTRCPCS   | 今回入金（現金）   | （なし） |
| PR_DEMAND_LST | TTSL      | 今回売上税抜金額   | （なし） |
| PR_DEMAND_LST | TTSLTX    | 今回売上税         | （なし） |
| PR_DEMAND_LST | UPDTD     | 更新日             | （なし） |
| PR_DEMAND_LST | UPDTWKCD  | 更新担当者         | （なし） |

## テーブル: PR_ODNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| PR_ODNO      | K_NO     | キー項目     | （なし） |
| PR_ODNO      | LAST_OD1 | 最終オーダNo | （なし） |
| PR_ODNO      | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: PR_ORDER

| テーブル名   | 列ID        | 列名                       | 備考                      |
|:-------------|:------------|:---------------------------|:--------------------------|
| PR_ORDER     | ADDFLG      | 追加Ｆ                     | 0;通常;1;追加             |
| PR_ORDER     | AMTMNY      | 金額                       | （なし）                  |
| PR_ORDER     | BKTNO       | バケットNo                 | （なし）                  |
| PR_ORDER     | BKTYEAR     | バケット年                 | （なし）                  |
| PR_ORDER     | CCLF        | 削除区分                   | （なし）                  |
| PR_ORDER     | CCLRMRK     | 削除備考                   | （なし）                  |
| PR_ORDER     | CMPFLG      | 完了Ｆ                     | （なし）                  |
| PR_ORDER     | COST        | 単価                       | （なし）                  |
| PR_ORDER     | DELIDATE    | 納期                       | （なし）                  |
| PR_ORDER     | IMTYP       | 製品区分                   | （なし）                  |
| PR_ORDER     | INVOICENO   | 納品書No                   | （なし）                  |
| PR_ORDER     | ITEM        | 品目                       | （なし）                  |
| PR_ORDER     | LINED       | 指示ライン                 | （なし）                  |
| PR_ORDER     | MBPRND      | 納品書現品票印刷日         | （なし）                  |
| PR_ORDER     | MBPRNF      | 納品書現品票印刷F          | （なし）                  |
| PR_ORDER     | MPSORDERNO  | 基準生産計画オーダNo       | （なし）                  |
| PR_ORDER     | OFFCLF      | 確定/内示Ｆ                | 0;内示;1;確定             |
| PR_ORDER     | ORDERFLG    | 発行F                      | 0;展開より;1;指示発行より |
| PR_ORDER     | ORDERNO     | 発注番号                   | （なし）                  |
| PR_ORDER     | ORDERQTY    | オーダー数                 | （なし）                  |
| PR_ORDER     | ORDERUNIT   | 手配単位                   | （なし）                  |
| PR_ORDER     | ORDRSCTN    | 発注部門                   | （なし）                  |
| PR_ORDER     | ORDRWKCD    | 発注担当者                 | （なし）                  |
| PR_ORDER     | PMTWSTD     | 支払締日                   | （なし）                  |
| PR_ORDER     | PRDCTBNO    | 枝番                       | （なし）                  |
| PR_ORDER     | PRDCTNO     | 製番                       | （なし）                  |
| PR_ORDER     | PRNF        | プリントフラグ             | （なし）                  |
| PR_ORDER     | PRNFLG      | オーダ票印刷完了Ｆ         | 0;印刷未完了;1;印刷完了   |
| PR_ORDER     | PRNFLG2     | 品目別出庫リスト印刷F      | 0;印刷未完了;1;印刷完了   |
| PR_ORDER     | PRNFLG3     | ｵｰﾀﾞ別出庫リスト印刷F      | 0;印刷未完了;1;印刷完了   |
| PR_ORDER     | PROCESS     | 工程                       | （なし）                  |
| PR_ORDER     | PYBLWSTD    | 買掛締日                   | （なし）                  |
| PR_ORDER     | RCDATE      | 入庫日                     | （なし）                  |
| PR_ORDER     | RCORDERNO   | 受注No                     | （なし）                  |
| PR_ORDER     | RCQTY       | 入庫数                     | （なし）                  |
| PR_ORDER     | RELEASEDATE | 発注日                     | （なし）                  |
| PR_ORDER     | REMARK      | 備考                       | （なし）                  |
| PR_ORDER     | REMARK1     | 備考１                     | （なし）                  |
| PR_ORDER     | REMARK2     | 備考２                     | （なし）                  |
| PR_ORDER     | REPDELIDATE | 回答納期                   | （なし）                  |
| PR_ORDER     | RGSTD       | 登録日                     | （なし）                  |
| PR_ORDER     | SBPRORDERNO | オーダーNO(購入品・外注品) | （なし）                  |
| PR_ORDER     | STARTDATE   | 着手日                     | （なし）                  |
| PR_ORDER     | TERMINAL    | 端末情報                   | （なし）                  |
| PR_ORDER     | TRANSACTOR  | 発注先                     | （なし）                  |
| PR_ORDER     | UPDTD       | 更新日                     | （なし）                  |
| PR_ORDER     | UPDTWKCD    | 更新担当者                 | （なし）                  |
| PR_ORDER     | VENDOR      | 仕入先                     | （なし）                  |
| PR_ORDER     | VENDOR2     | 外注コード                 | （なし）                  |

## テーブル: PR_ORDERNO

| テーブル名   | 列ID     | 列名             | 備考     |
|:-------------|:---------|:-----------------|:---------|
| PR_ORDERNO   | K_NO     | キー項目         | （なし） |
| PR_ORDERNO   | LAST_OD1 | 最終オーダNo     | （なし） |
| PR_ORDERNO   | NEXT_OD1 | 次回オーダNo     | （なし） |
| PR_ORDERNO   | NEXT_OD2 | 次回内示オーダNo | （なし） |

## テーブル: PR_PAYEE

| テーブル名   | 列ID     | 列名           | 備考     |
|:-------------|:---------|:---------------|:---------|
| PR_PAYEE     | AMTMNY   | 金額           | （なし） |
| PR_PAYEE     | AMTTAX   | 税額           | （なし） |
| PR_PAYEE     | BILNO    | 手形番号       | （なし） |
| PR_PAYEE     | LNNO     | 行番号         | （なし） |
| PR_PAYEE     | PMTWSTD  | 支払締日       | （なし） |
| PR_PAYEE     | PRTF     | プリントフラグ | （なし） |
| PR_PAYEE     | PYECD    | 支払先         | （なし） |
| PR_PAYEE     | PYED     | 支払日         | （なし） |
| PR_PAYEE     | PYEEXD   | 支払予定日     | （なし） |
| PR_PAYEE     | PYEF     | 支払区分       | （なし） |
| PR_PAYEE     | PYEPLF   | 支払予定区分   | （なし） |
| PR_PAYEE     | REMARK   | 摘要           | （なし） |
| PR_PAYEE     | RGSTD    | 登録日         | （なし） |
| PR_PAYEE     | SAMTMNY  | 支払実績金額   | （なし） |
| PR_PAYEE     | SBJCT    | 科目           | （なし） |
| PR_PAYEE     | STLMTD   | 決済日         | （なし） |
| PR_PAYEE     | TERMINAL | 端末情報       | （なし） |
| PR_PAYEE     | UPDTD    | 更新日         | （なし） |
| PR_PAYEE     | UPDTWKCD | 更新担当者     | （なし） |

## テーブル: PR_PAYEED

| テーブル名   | 列ID        | 列名                       | 備考             |
|:-------------|:------------|:---------------------------|:-----------------|
| PR_PAYEED    | AMTMNY      | 金額                       | （なし）         |
| PR_PAYEED    | AMTTAX      | 税額                       | （なし）         |
| PR_PAYEED    | BILNO       | 手形番号                   | （なし）         |
| PR_PAYEED    | CCLF        | 削除区分                   | （なし）         |
| PR_PAYEED    | IMNM        | 品名                       | （なし）         |
| PR_PAYEED    | ITEM        | 品目                       | （なし）         |
| PR_PAYEED    | NONO        | 計上通知連番               | （なし）         |
| PR_PAYEED    | NOTICENO    | 計上通知No                 | （なし）         |
| PR_PAYEED    | ORDERNO     | 発注番号                   | （なし）         |
| PR_PAYEED    | PMTWSTD     | 支払締日                   | （なし）         |
| PR_PAYEED    | PRNFLG      | 支払案内書印刷F            | 0,未完了;1,更新; |
| PR_PAYEED    | PROCESS     | 工程                       | （なし）         |
| PR_PAYEED    | PRTF        | プリントフラグ             | （なし）         |
| PR_PAYEED    | PYBLWSTD    | 買掛締日                   | （なし）         |
| PR_PAYEED    | PYECD       | 支払先                     | （なし）         |
| PR_PAYEED    | PYEEXD      | 支払予定日                 | （なし）         |
| PR_PAYEED    | PYEF        | 支払区分                   | （なし）         |
| PR_PAYEED    | RCVNO       | 受入No                     | （なし）         |
| PR_PAYEED    | REMARK1     | 備考１                     | （なし）         |
| PR_PAYEED    | REMARK2     | 備考２                     | （なし）         |
| PR_PAYEED    | REPDELIDATE | 回答納期                   | （なし）         |
| PR_PAYEED    | RGSTD       | 登録日                     | （なし）         |
| PR_PAYEED    | SBJCT       | 科目                       | （なし）         |
| PR_PAYEED    | SBORDERNO   | オーダーNO(購入品・外注品) | （なし）         |
| PR_PAYEED    | SLPF        | 伝票区分                   | （なし）         |
| PR_PAYEED    | SLPF2       | 入金伝票区分               | （なし）         |
| PR_PAYEED    | SP_F        | 単価参照F                  | （なし）         |
| PR_PAYEED    | SPLYQTY     | 仕入数                     | （なし）         |
| PR_PAYEED    | SPYSCT      | 仕入部門                   | （なし）         |
| PR_PAYEED    | SPYSMUPD    | 計上日                     | （なし）         |
| PR_PAYEED    | SPYWKCD     | 仕入担当者                 | （なし）         |
| PR_PAYEED    | STLMTD      | 決済日                     | （なし）         |
| PR_PAYEED    | TAXF        | 税区分                     | （なし）         |
| PR_PAYEED    | TERMINAL    | 端末情報                   | （なし）         |
| PR_PAYEED    | TOAMTMNY    | 税抜金額                   | （なし）         |
| PR_PAYEED    | UNTPRC      | 単価                       | （なし）         |
| PR_PAYEED    | UNTPRCF     | 単価区分                   | 0;決定;1;仮      |
| PR_PAYEED    | UPDTD       | 更新日                     | （なし）         |
| PR_PAYEED    | UPDTWKCD    | 更新担当者                 | （なし）         |
| PR_PAYEED    | VENDOR      | 仕入先                     | （なし）         |
| PR_PAYEED    | WKRATE      | 進度(%)                    | （なし）         |

## テーブル: PR_PAYEE_LST

| テーブル名   | 列ID       | 列名           | 備考     |
|:-------------|:-----------|:---------------|:---------|
| PR_PAYEE_LST | ADJMNY     | 調整額         | （なし） |
| PR_PAYEE_LST | ADR        | 住所           | （なし） |
| PR_PAYEE_LST | AMTMNY     | 合計金額       | （なし） |
| PR_PAYEE_LST | FAX        | FAX            | （なし） |
| PR_PAYEE_LST | LAMTPAYMNY | 前回支払額     | （なし） |
| PR_PAYEE_LST | LSTCORMPY  | 前月繰越残高   | （なし） |
| PR_PAYEE_LST | MAMTMNY    | 翌月繰越残高   | （なし） |
| PR_PAYEE_LST | NAMTCMNY   | 今回支払額     | （なし） |
| PR_PAYEE_LST | NOTICENO   | 計上通知No     | （なし） |
| PR_PAYEE_LST | OAMTMNY    | その他金額     | （なし） |
| PR_PAYEE_LST | PAYSTD     | 支払締日       | （なし） |
| PR_PAYEE_LST | PAYSTED    | 支払締終了日   | （なし） |
| PR_PAYEE_LST | PAYSTSD    | 支払締開始日   | （なし） |
| PR_PAYEE_LST | POSTCD     | 郵便番号       | （なし） |
| PR_PAYEE_LST | PRN_F      | 印刷F          | （なし） |
| PR_PAYEE_LST | PYECD      | 取引先         | （なし） |
| PR_PAYEE_LST | RGSTD      | 登録日         | （なし） |
| PR_PAYEE_LST | TEL        | TEL            | （なし） |
| PR_PAYEE_LST | TERMINAL   | 端末情報       | （なし） |
| PR_PAYEE_LST | TTPAY      | 仕入税抜金額   | （なし） |
| PR_PAYEE_LST | TTPAYBL    | 支払（手形）   | （なし） |
| PR_PAYEE_LST | TTPAYC     | 支払（その他） | （なし） |
| PR_PAYEE_LST | TTPAYCB    | 支払（相殺）   | （なし） |
| PR_PAYEE_LST | TTPAYCS    | 支払（現金）   | （なし） |
| PR_PAYEE_LST | TTPAYTX    | 仕入税額       | （なし） |
| PR_PAYEE_LST | UPDTD      | 更新日         | （なし） |
| PR_PAYEE_LST | UPDTWKCD   | 更新担当者     | （なし） |
| PR_PAYEE_LST | VENDORNM   | 取引先名       | （なし） |

## テーブル: PR_PAYNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| PR_PAYNO     | K_NO     | キー項目     | （なし） |
| PR_PAYNO     | LAST_OD1 | 最終オーダNo | （なし） |
| PR_PAYNO     | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: PR_PROCESS_SBCNTORDERW

| テーブル名             | 列ID        | 列名         | 備考     |
|:-----------------------|:------------|:-------------|:---------|
| PR_PROCESS_SBCNTORDERW | ADDFLG      | 追加オーダＦ | （なし） |
| PR_PROCESS_SBCNTORDERW | BKTNO       | バケットNo   | （なし） |
| PR_PROCESS_SBCNTORDERW | BKTYEAR     | バケット年   | （なし） |
| PR_PROCESS_SBCNTORDERW | CMPFLG      | 完了Ｆ       | （なし） |
| PR_PROCESS_SBCNTORDERW | COST        | 単価         | （なし） |
| PR_PROCESS_SBCNTORDERW | DELIDATE    | 納期         | （なし） |
| PR_PROCESS_SBCNTORDERW | IMTYP       | 製品区分     | （なし） |
| PR_PROCESS_SBCNTORDERW | ITEM        | 品目         | （なし） |
| PR_PROCESS_SBCNTORDERW | LINED       | 指示ライン   | （なし） |
| PR_PROCESS_SBCNTORDERW | OFFCLF      | 確定/内示Ｆ  | （なし） |
| PR_PROCESS_SBCNTORDERW | ORDERFLG    | 発行F        | （なし） |
| PR_PROCESS_SBCNTORDERW | ORDERNO     | 発注番号     | （なし） |
| PR_PROCESS_SBCNTORDERW | ORDERQTY    | オーダ数     | （なし） |
| PR_PROCESS_SBCNTORDERW | ORDRSCTN    | 発注部門     | （なし） |
| PR_PROCESS_SBCNTORDERW | ORDRWKCD    | 発注担当者   | （なし） |
| PR_PROCESS_SBCNTORDERW | PRDCTBNO    | 枝番         | （なし） |
| PR_PROCESS_SBCNTORDERW | PRDCTNO     | 製番         | （なし） |
| PR_PROCESS_SBCNTORDERW | PROCESS     | 工程         | （なし） |
| PR_PROCESS_SBCNTORDERW | RELEASEDATE | 発注日       | （なし） |
| PR_PROCESS_SBCNTORDERW | REMARK1     | 備考１       | （なし） |
| PR_PROCESS_SBCNTORDERW | REMARK2     | 備考２       | （なし） |
| PR_PROCESS_SBCNTORDERW | REPDELIDATE | 回答納期     | （なし） |
| PR_PROCESS_SBCNTORDERW | RGSTD       | 登録日       | （なし） |
| PR_PROCESS_SBCNTORDERW | SBORDERNO   | オーダNo     | （なし） |
| PR_PROCESS_SBCNTORDERW | STARTDATE   | 着手日       | （なし） |
| PR_PROCESS_SBCNTORDERW | TERMINAL    | 端末情報     | （なし） |
| PR_PROCESS_SBCNTORDERW | VENDOR      | 仕入先       | （なし） |
| PR_PROCESS_SBCNTORDERW | VENDOR2     | 外注ｺｰﾄﾞ     | （なし） |

## テーブル: PR_PURCHASE

| テーブル名   | 列ID        | 列名                       | 備考     |
|:-------------|:------------|:---------------------------|:---------|
| PR_PURCHASE  | ADDF        | 追加フラグ                 | （なし） |
| PR_PURCHASE  | AMTMNY      | 合計金額                   | （なし） |
| PR_PURCHASE  | AMTTAX      | 税額                       | （なし） |
| PR_PURCHASE  | CCLF        | 削除区分                   | （なし） |
| PR_PURCHASE  | IMNM        | 品名                       | （なし） |
| PR_PURCHASE  | ITEM        | 品目                       | （なし） |
| PR_PURCHASE  | ORDERNO     | 発注番号                   | （なし） |
| PR_PURCHASE  | PMTWSTD     | 支払締日                   | （なし） |
| PR_PURCHASE  | PRICEF      | 単価区分                   | （なし） |
| PR_PURCHASE  | PROCESS     | 工程                       | （なし） |
| PR_PURCHASE  | PRTF        | プリントフラグ             | （なし） |
| PR_PURCHASE  | PYBLWSTD    | 買掛締日                   | （なし） |
| PR_PURCHASE  | PYECD       | 支払先                     | （なし） |
| PR_PURCHASE  | PYEF        | 計上対象区分               | （なし） |
| PR_PURCHASE  | RCVNO       | 受入No                     | （なし） |
| PR_PURCHASE  | REMARK1     | 備考1                      | （なし） |
| PR_PURCHASE  | REMARK2     | 備考2                      | （なし） |
| PR_PURCHASE  | REPDELIDATE | 回答納期                   | （なし） |
| PR_PURCHASE  | RGSTD       | 登録日                     | （なし） |
| PR_PURCHASE  | SBJCT       | 科目                       | （なし） |
| PR_PURCHASE  | SBORDERNO   | オーダーNO(購入品・外注品) | （なし） |
| PR_PURCHASE  | SLPF        | 伝票区分                   | （なし） |
| PR_PURCHASE  | SPLYQTY     | 仕入数                     | （なし） |
| PR_PURCHASE  | SPYSCT      | 仕入部門                   | （なし） |
| PR_PURCHASE  | SPYSMUPD    | 仕入計上日                 | （なし） |
| PR_PURCHASE  | SPYWKCD     | 仕入担当者                 | （なし） |
| PR_PURCHASE  | TAXF        | 税区分                     | （なし） |
| PR_PURCHASE  | TERMINAL    | 端末情報                   | （なし） |
| PR_PURCHASE  | TOAMTMNY    | 税抜金額                   | （なし） |
| PR_PURCHASE  | UNTPRC      | 単価                       | （なし） |
| PR_PURCHASE  | UPDTD       | 更新日                     | （なし） |
| PR_PURCHASE  | UPDTWKCD    | 更新担当者                 | （なし） |
| PR_PURCHASE  | VENDOR      | 仕入先                     | （なし） |

## テーブル: PR_PURCHASEORDERW

| テーブル名        | 列ID        | 列名        | 備考     |
|:------------------|:------------|:------------|:---------|
| PR_PURCHASEORDERW | ADDFLG      | 追加Ｆ      | （なし） |
| PR_PURCHASEORDERW | BKTNO       | バケットNo  | （なし） |
| PR_PURCHASEORDERW | BKTYEAR     | バケット年  | （なし） |
| PR_PURCHASEORDERW | CMPFLG      | 完了Ｆ      | （なし） |
| PR_PURCHASEORDERW | COST        | 単価        | （なし） |
| PR_PURCHASEORDERW | DELIDATE    | 納期        | （なし） |
| PR_PURCHASEORDERW | IMTYP       | 製品区分    | （なし） |
| PR_PURCHASEORDERW | ITEM        | 品目        | （なし） |
| PR_PURCHASEORDERW | OFFCLF      | 確定/内示Ｆ | （なし） |
| PR_PURCHASEORDERW | ORDERNO     | 発注番号    | （なし） |
| PR_PURCHASEORDERW | ORDERQTY    | オーダ数    | （なし） |
| PR_PURCHASEORDERW | ORDRSCTN    | 発注部門    | （なし） |
| PR_PURCHASEORDERW | ORDRWKCD    | 発注担当者  | （なし） |
| PR_PURCHASEORDERW | PRICEF      | 単価区分    | （なし） |
| PR_PURCHASEORDERW | PROCESS     | 工程        | （なし） |
| PR_PURCHASEORDERW | PUORDERNO   | オーダNo    | （なし） |
| PR_PURCHASEORDERW | RELEASEDATE | 発注日      | （なし） |
| PR_PURCHASEORDERW | REMARK1     | 備考１      | （なし） |
| PR_PURCHASEORDERW | REMARK2     | 備考２      | （なし） |
| PR_PURCHASEORDERW | REPDELIDATE | 回答納期    | （なし） |
| PR_PURCHASEORDERW | RGSTD       | 登録日      | （なし） |
| PR_PURCHASEORDERW | TERMINAL    | 端末情報    | （なし） |
| PR_PURCHASEORDERW | VENDOR      | 仕入先      | （なし） |

## テーブル: PR_PURCHASEW

| テーブル名   | 列ID        | 列名                       | 備考     |
|:-------------|:------------|:---------------------------|:---------|
| PR_PURCHASEW | ADDF        | 追加フラグ                 | （なし） |
| PR_PURCHASEW | AMTMNY      | 金額                       | （なし） |
| PR_PURCHASEW | AMTTAX      | 税額                       | （なし） |
| PR_PURCHASEW | CCLF        | 削除区分                   | （なし） |
| PR_PURCHASEW | IMNM        | 品名                       | （なし） |
| PR_PURCHASEW | IMTYP       | 製品区分                   | （なし） |
| PR_PURCHASEW | ITEM        | 品目                       | （なし） |
| PR_PURCHASEW | ORDERNO     | 発注番号                   | （なし） |
| PR_PURCHASEW | PMTWSTD     | 支払締日                   | （なし） |
| PR_PURCHASEW | PRICEF      | 単価区分                   | （なし） |
| PR_PURCHASEW | PROCESS     | 工程                       | （なし） |
| PR_PURCHASEW | PRTF        | プリントフラグ             | （なし） |
| PR_PURCHASEW | PYBLWSTD    | 買掛締日                   | （なし） |
| PR_PURCHASEW | PYECD       | 支払先                     | （なし） |
| PR_PURCHASEW | PYEF        | 支払区分                   | （なし） |
| PR_PURCHASEW | RCISCD      | 入出庫区分                 | （なし） |
| PR_PURCHASEW | RCVNO       | 受入No                     | （なし） |
| PR_PURCHASEW | REMARK1     | 備考１                     | （なし） |
| PR_PURCHASEW | REMARK2     | 備考２                     | （なし） |
| PR_PURCHASEW | REPDELIDATE | 回答納期                   | （なし） |
| PR_PURCHASEW | RGSTD       | 登録日                     | （なし） |
| PR_PURCHASEW | SBJCT       | 科目                       | （なし） |
| PR_PURCHASEW | SBORDERNO   | オーダーNO(購入品・外注品) | （なし） |
| PR_PURCHASEW | SLPF        | 伝票区分                   | （なし） |
| PR_PURCHASEW | SPLYQTY     | 仕入数                     | （なし） |
| PR_PURCHASEW | SPYSCT      | 仕入部門                   | （なし） |
| PR_PURCHASEW | SPYSMUPD    | 仕入計上日                 | （なし） |
| PR_PURCHASEW | SPYWKCD     | 仕入担当者                 | （なし） |
| PR_PURCHASEW | TAXF        | 税区分                     | （なし） |
| PR_PURCHASEW | TERMINAL    | 端末情報                   | （なし） |
| PR_PURCHASEW | TOAMTMNY    | 税抜金額                   | （なし） |
| PR_PURCHASEW | UNTPRC      | 単価                       | （なし） |
| PR_PURCHASEW | UPDTD       | 更新日                     | （なし） |
| PR_PURCHASEW | UPDTWKCD    | 更新担当者                 | （なし） |
| PR_PURCHASEW | VENDOR      | 仕入先                     | （なし） |
| PR_PURCHASEW | VENDOR2     | 外注コード                 | （なし） |

## テーブル: PR_RECEIPT

| テーブル名   | 列ID     | 列名           | 備考     |
|:-------------|:---------|:---------------|:---------|
| PR_RECEIPT   | AMTMNY   | 合計金額       | （なし） |
| PR_RECEIPT   | AMTTAX   | 税額           | （なし） |
| PR_RECEIPT   | BILNO    | 手形番号       | （なし） |
| PR_RECEIPT   | CLMCD    | 請求先         | （なし） |
| PR_RECEIPT   | LNNO     | 行番号         | （なし） |
| PR_RECEIPT   | PRNF     | プリントフラグ | （なし） |
| PR_RECEIPT   | RCBLWSTD | 売掛締日       | （なし） |
| PR_RECEIPT   | RCPD     | 入金実績日     | （なし） |
| PR_RECEIPT   | RCPEXD   | 入金予定日     | （なし） |
| PR_RECEIPT   | RCPEXF   | 金種区分       | （なし） |
| PR_RECEIPT   | RCPWSD   | 入金締日       | （なし） |
| PR_RECEIPT   | REMARK   | 摘要           | （なし） |
| PR_RECEIPT   | RGSTD    | 登録日         | （なし） |
| PR_RECEIPT   | SAMTMNY  | 入金額         | （なし） |
| PR_RECEIPT   | SBJCT    | 科目           | （なし） |
| PR_RECEIPT   | SLPF     | 伝票区分       | （なし） |
| PR_RECEIPT   | STLMTD   | 決済日         | （なし） |
| PR_RECEIPT   | TERMINAL | 端末情報       | （なし） |
| PR_RECEIPT   | UPDTD    | 更新日         | （なし） |
| PR_RECEIPT   | UPDTWKCD | 更新担当者     | （なし） |

## テーブル: PR_RECEIVE

| テーブル名   | 列ID        | 列名           | 備考                        |
|:-------------|:------------|:---------------|:----------------------------|
| PR_RECEIVE   | ADDFLG      | 追加Ｆ         | 0;通常;1;追加               |
| PR_RECEIVE   | AMTMNY      | 金額           | （なし）                    |
| PR_RECEIVE   | AMTTAX      | 税額           | （なし）                    |
| PR_RECEIVE   | CCLF        | 削除区分       | （なし）                    |
| PR_RECEIVE   | IMNM        | 品名           | （なし）                    |
| PR_RECEIVE   | IMTYP       | 製品区分       | （なし）                    |
| PR_RECEIVE   | ITEM        | 品目           | （なし）                    |
| PR_RECEIVE   | LOCT        | 場所           | （なし）                    |
| PR_RECEIVE   | PMTWSTD     | 支払締日       | （なし）                    |
| PR_RECEIVE   | PRICEF      | 単価区分(旧)   | （なし）                    |
| PR_RECEIVE   | PROCESS     | 工程           | （なし）                    |
| PR_RECEIVE   | PRTF        | プリントフラグ | （なし）                    |
| PR_RECEIVE   | PYBLWSTD    | 買掛締日       | （なし）                    |
| PR_RECEIVE   | PYECD       | 支払先         | （なし）                    |
| PR_RECEIVE   | PYEF        | 支払区分       | 0;対象としない;1;対象とする |
| PR_RECEIVE   | RCISCD      | 入出庫区分     | （なし）                    |
| PR_RECEIVE   | RCVD        | 受入日         | （なし）                    |
| PR_RECEIVE   | RCVNO       | 受入No         | （なし）                    |
| PR_RECEIVE   | RCVQTY      | 受入数         | （なし）                    |
| PR_RECEIVE   | RCVSCT      | 受入部門       | （なし）                    |
| PR_RECEIVE   | RCVWKCD     | 受入担当者     | （なし）                    |
| PR_RECEIVE   | REMARK1     | 備考１         | （なし）                    |
| PR_RECEIVE   | REMARK2     | 備考２         | （なし）                    |
| PR_RECEIVE   | REPDELIDATE | 回答納期       | （なし）                    |
| PR_RECEIVE   | RGSTD       | 登録日         | （なし）                    |
| PR_RECEIVE   | RGSTTM      | 登録時刻       | （なし）                    |
| PR_RECEIVE   | SBJCT       | 科目           | （なし）                    |
| PR_RECEIVE   | SBORDERNO   | 発注番号       | （なし）                    |
| PR_RECEIVE   | SLPF        | 伝票区分       | （なし）                    |
| PR_RECEIVE   | SP_F        | 単価参照F      | 0;単価マスタより;1;特別単価 |
| PR_RECEIVE   | TAXF        | 税区分         | （なし）                    |
| PR_RECEIVE   | TERMINAL    | 端末情報       | （なし）                    |
| PR_RECEIVE   | TOAMTMNY    | 税抜金額       | （なし）                    |
| PR_RECEIVE   | TRANSACTOR  | 取引先         | （なし）                    |
| PR_RECEIVE   | UNTPRC      | 単価           | （なし）                    |
| PR_RECEIVE   | UNTPRCF     | 単価区分       | 0:単価マスタ 1:特別単価     |
| PR_RECEIVE   | UPDTD       | 更新日         | （なし）                    |
| PR_RECEIVE   | UPDTWKCD    | 更新担当者     | （なし）                    |
| PR_RECEIVE   | VENDOR      | 仕入先         | （なし）                    |
| PR_RECEIVE   | WKRATE      | 進度(%)        | （なし）                    |

## テーブル: PR_RECIVENO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| PR_RECIVENO  | K_NO     | キー項目     | （なし） |
| PR_RECIVENO  | LAST_OD1 | 最終オーダNo | （なし） |
| PR_RECIVENO  | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: PR_R_DEMAND

| テーブル名   | 列ID        | 列名                   | 備考     |
|:-------------|:------------|:-----------------------|:---------|
| PR_R_DEMAND  | A_ORDERNO   | オーダNo               | （なし） |
| PR_R_DEMAND  | AMTMNY      | 金額                   | （なし） |
| PR_R_DEMAND  | AMTTAX      | 税額                   | （なし） |
| PR_R_DEMAND  | BILNO       | 手形番号               | （なし） |
| PR_R_DEMAND  | CCNO        | 請求連番               | （なし） |
| PR_R_DEMAND  | CLAIMNO     | 請求No                 | （なし） |
| PR_R_DEMAND  | CLMCD       | 請求先                 | （なし） |
| PR_R_DEMAND  | CLWSTD      | 請求締日               | （なし） |
| PR_R_DEMAND  | CUST_PRNFLG | 今回対象プリントフラグ | （なし） |
| PR_R_DEMAND  | CUSTOM      | 得意先                 | （なし） |
| PR_R_DEMAND  | CUSTOMIMNM  | 顧客品名               | （なし） |
| PR_R_DEMAND  | CUSTOMITEM  | 顧客品目               | （なし） |
| PR_R_DEMAND  | CUSTOMNO    | 顧客注番               | （なし） |
| PR_R_DEMAND  | DEMANDNO    | 社内注番               | （なし） |
| PR_R_DEMAND  | GRA_FLG     | 有償無償フラグ         | （なし） |
| PR_R_DEMAND  | IMNM        | 品名                   | （なし） |
| PR_R_DEMAND  | ITEM        | 品目                   | （なし） |
| PR_R_DEMAND  | ITEMF       | 受注品目区分           | （なし） |
| PR_R_DEMAND  | ITEMF2      | 支給区分               | （なし） |
| PR_R_DEMAND  | LNNO        | 行番号                 | （なし） |
| PR_R_DEMAND  | PRNFLG      | 請求書印刷F            | （なし） |
| PR_R_DEMAND  | PROCESS     | 工程                   | （なし） |
| PR_R_DEMAND  | RCPEXD      | 入金予定日             | （なし） |
| PR_R_DEMAND  | REMARK1     | 備考１                 | （なし） |
| PR_R_DEMAND  | REMARK2     | 備考２                 | （なし） |
| PR_R_DEMAND  | RGSTD       | 登録日                 | （なし） |
| PR_R_DEMAND  | SHIPQTY     | 出荷数                 | （なし） |
| PR_R_DEMAND  | SHPMNTD     | 出荷日                 | （なし） |
| PR_R_DEMAND  | SHPMNTNO    | 出荷No                 | （なし） |
| PR_R_DEMAND  | SLPF        | 伝票区分               | （なし） |
| PR_R_DEMAND  | SLPF2       | 入金伝票区分           | （なし） |
| PR_R_DEMAND  | SLSMUPD     | 売上計上日             | （なし） |
| PR_R_DEMAND  | SP_F        | 単価参照F              | （なし） |
| PR_R_DEMAND  | STLMTD      | 決済日                 | （なし） |
| PR_R_DEMAND  | TAXF        | 税区分                 | （なし） |
| PR_R_DEMAND  | TERMINAL    | 端末情報               | （なし） |
| PR_R_DEMAND  | TOAMTMNY    | 税抜金額               | （なし） |
| PR_R_DEMAND  | UNTPRC      | 単価                   | （なし） |
| PR_R_DEMAND  | UPDTD       | 更新日                 | （なし） |
| PR_R_DEMAND  | UPDTWKCD    | 更新担当者             | （なし） |
| PR_R_DEMAND  | WSETD       | 締日                   | （なし） |

## テーブル: PR_R_DEMAND_LST

| テーブル名      | 列ID        | 列名                   | 備考     |
|:----------------|:------------|:-----------------------|:---------|
| PR_R_DEMAND_LST | ADJMNY      | 調整額                 | （なし） |
| PR_R_DEMAND_LST | ADR         | 住所                   | （なし） |
| PR_R_DEMAND_LST | AMTMNY      | 合計金額               | （なし） |
| PR_R_DEMAND_LST | CLAIMNO     | 請求No                 | （なし） |
| PR_R_DEMAND_LST | CLMCD       | 請求先                 | （なし） |
| PR_R_DEMAND_LST | CLWSTD      | 請求締日               | （なし） |
| PR_R_DEMAND_LST | CLWSTED     | 請求締終了日           | （なし） |
| PR_R_DEMAND_LST | CLWSTSD     | 請求締開始日           | （なし） |
| PR_R_DEMAND_LST | CUST_PRNFLG | 今回対象プリントフラグ | （なし） |
| PR_R_DEMAND_LST | CUSTOMNM    | 請求先名称             | （なし） |
| PR_R_DEMAND_LST | FAX         | FAX                    | （なし） |
| PR_R_DEMAND_LST | LAMTCMNY    | 前回請求額             | （なし） |
| PR_R_DEMAND_LST | LSTCORMPY   | 前月繰越残高           | （なし） |
| PR_R_DEMAND_LST | OAMTMNY     | その他金額             | （なし） |
| PR_R_DEMAND_LST | POSTCD      | 郵便番号               | （なし） |
| PR_R_DEMAND_LST | RGSTD       | 登録日                 | （なし） |
| PR_R_DEMAND_LST | TEL         | TEL                    | （なし） |
| PR_R_DEMAND_LST | TERMINAL    | 端末情報               | （なし） |
| PR_R_DEMAND_LST | TTRCPBL     | 今回入金（手形）       | （なし） |
| PR_R_DEMAND_LST | TTRCPC      | 今回入金（その他）     | （なし） |
| PR_R_DEMAND_LST | TTRCPCB     | 今回入金（相殺）       | （なし） |
| PR_R_DEMAND_LST | TTRCPCS     | 今回入金（現金）       | （なし） |
| PR_R_DEMAND_LST | TTSL        | 今回売上税抜金額       | （なし） |
| PR_R_DEMAND_LST | TTSLTX      | 今回売上税             | （なし） |
| PR_R_DEMAND_LST | UPDTD       | 更新日                 | （なし） |
| PR_R_DEMAND_LST | UPDTWKCD    | 更新担当者             | （なし） |

## テーブル: PR_R_PAYEED

| テーブル名   | 列ID        | 列名                       | 備考        |
|:-------------|:------------|:---------------------------|:------------|
| PR_R_PAYEED  | AMTMNY      | 金額                       | （なし）    |
| PR_R_PAYEED  | AMTTAX      | 税額                       | （なし）    |
| PR_R_PAYEED  | CCLF        | 削除区分                   | （なし）    |
| PR_R_PAYEED  | CUST_PRNFLG | 今回対象プリントフラグ     | （なし）    |
| PR_R_PAYEED  | IMNM        | 品名                       | （なし）    |
| PR_R_PAYEED  | ITEM        | 品目                       | （なし）    |
| PR_R_PAYEED  | NONO        | 計上通知連番               | （なし）    |
| PR_R_PAYEED  | NOTICENO    | 計上通知No                 | （なし）    |
| PR_R_PAYEED  | ORDERNO     | 発注番号                   | （なし）    |
| PR_R_PAYEED  | PMTWSTD     | 支払締日                   | （なし）    |
| PR_R_PAYEED  | PROCESS     | 工程                       | （なし）    |
| PR_R_PAYEED  | PRTF        | プリントフラグ             | （なし）    |
| PR_R_PAYEED  | PYBLWSTD    | 買掛締日                   | （なし）    |
| PR_R_PAYEED  | PYECD       | 支払先                     | （なし）    |
| PR_R_PAYEED  | PYEF        | 支払区分                   | （なし）    |
| PR_R_PAYEED  | RCVNO       | 受入No                     | （なし）    |
| PR_R_PAYEED  | REMARK1     | 備考１                     | （なし）    |
| PR_R_PAYEED  | REMARK2     | 備考２                     | （なし）    |
| PR_R_PAYEED  | REPDELIDATE | 回答納期                   | （なし）    |
| PR_R_PAYEED  | RGSTD       | 登録日                     | （なし）    |
| PR_R_PAYEED  | SBJCT       | 科目                       | （なし）    |
| PR_R_PAYEED  | SBORDERNO   | オーダーNO(購入品・外注品) | （なし）    |
| PR_R_PAYEED  | SLPF        | 伝票区分                   | （なし）    |
| PR_R_PAYEED  | SLPF2       | 入金伝票区分               | （なし）    |
| PR_R_PAYEED  | SP_F        | 単価参照F                  | （なし）    |
| PR_R_PAYEED  | SPLYQTY     | 仕入数                     | （なし）    |
| PR_R_PAYEED  | SPYSCT      | 仕入部門                   | （なし）    |
| PR_R_PAYEED  | SPYSMUPD    | 計上日                     | （なし）    |
| PR_R_PAYEED  | SPYWKCD     | 仕入担当者                 | （なし）    |
| PR_R_PAYEED  | TAXF        | 税区分                     | （なし）    |
| PR_R_PAYEED  | TERMINAL    | 端末情報                   | （なし）    |
| PR_R_PAYEED  | TOAMTMNY    | 税抜金額                   | （なし）    |
| PR_R_PAYEED  | UNTPRC      | 単価                       | （なし）    |
| PR_R_PAYEED  | UNTPRCF     | 単価区分                   | 0;決定;1;仮 |
| PR_R_PAYEED  | UPDTD       | 更新日                     | （なし）    |
| PR_R_PAYEED  | UPDTWKCD    | 更新担当者                 | （なし）    |
| PR_R_PAYEED  | VENDOR      | 仕入先                     | （なし）    |
| PR_R_PAYEED  | WKRATE      | 進度(%)                    | （なし）    |

## テーブル: PR_R_PAYEE_LST

| テーブル名     | 列ID        | 列名                   | 備考     |
|:---------------|:------------|:-----------------------|:---------|
| PR_R_PAYEE_LST | ADJMNY      | 調整額                 | （なし） |
| PR_R_PAYEE_LST | ADR         | 住所                   | （なし） |
| PR_R_PAYEE_LST | AMTMNY      | 合計金額               | （なし） |
| PR_R_PAYEE_LST | CUST_PRNFLG | 今回プリント対象フラグ | （なし） |
| PR_R_PAYEE_LST | FAX         | FAX                    | （なし） |
| PR_R_PAYEE_LST | LAMTPAYMNY  | 前回支払額             | （なし） |
| PR_R_PAYEE_LST | LSTCORMPY   | 前月繰越残高           | （なし） |
| PR_R_PAYEE_LST | MAMTMNY     | 翌月繰越残高           | （なし） |
| PR_R_PAYEE_LST | NOTICENO    | 計上通知No             | （なし） |
| PR_R_PAYEE_LST | OAMTMNY     | その他金額             | （なし） |
| PR_R_PAYEE_LST | PAYSTD      | 支払締日               | （なし） |
| PR_R_PAYEE_LST | PAYSTED     | 支払締終了日           | （なし） |
| PR_R_PAYEE_LST | PAYSTSD     | 支払締開始日           | （なし） |
| PR_R_PAYEE_LST | POSTCD      | 郵便番号               | （なし） |
| PR_R_PAYEE_LST | PRN_F       | 印刷F                  | （なし） |
| PR_R_PAYEE_LST | PYECD       | 支払先                 | （なし） |
| PR_R_PAYEE_LST | RGSTD       | 登録日                 | （なし） |
| PR_R_PAYEE_LST | TEL         | TEL                    | （なし） |
| PR_R_PAYEE_LST | TERMINAL    | 端末情報               | （なし） |
| PR_R_PAYEE_LST | TTPAY       | 仕入税抜金額           | （なし） |
| PR_R_PAYEE_LST | TTPAYBL     | 支払（手形）           | （なし） |
| PR_R_PAYEE_LST | TTPAYC      | 支払（その他）         | （なし） |
| PR_R_PAYEE_LST | TTPAYCB     | 支払（相殺）           | （なし） |
| PR_R_PAYEE_LST | TTPAYCS     | 支払（現金）           | （なし） |
| PR_R_PAYEE_LST | TTPAYTX     | 仕入税額               | （なし） |
| PR_R_PAYEE_LST | UPDTD       | 更新日                 | （なし） |
| PR_R_PAYEE_LST | UPDTWKCD    | 更新担当者             | （なし） |
| PR_R_PAYEE_LST | VENDORNM    | 支払先名称             | （なし） |

## テーブル: PR_R_SALES_D

| テーブル名   | 列ID        | 列名                   | 備考     |
|:-------------|:------------|:-----------------------|:---------|
| PR_R_SALES_D | A_ORDERNO   | オーダNo               | （なし） |
| PR_R_SALES_D | AMTMNY      | 合計金額               | （なし） |
| PR_R_SALES_D | AMTTAX      | 税額                   | （なし） |
| PR_R_SALES_D | BILNO       | 手形番号               | （なし） |
| PR_R_SALES_D | CCNO        | 請求連番               | （なし） |
| PR_R_SALES_D | CLMCD       | 請求先                 | （なし） |
| PR_R_SALES_D | CLWSTD      | 請求締日               | （なし） |
| PR_R_SALES_D | CUST_PRNFLG | 今回対象プリントフラグ | （なし） |
| PR_R_SALES_D | CUSTOM      | 得意先                 | （なし） |
| PR_R_SALES_D | CUSTOMIMNM  | 顧客品名               | （なし） |
| PR_R_SALES_D | CUSTOMITEM  | 顧客品目               | （なし） |
| PR_R_SALES_D | CUSTOMNO    | 顧客注番               | （なし） |
| PR_R_SALES_D | DEMANDNO    | 社内注番               | （なし） |
| PR_R_SALES_D | GRA_FLG     | 有償無償フラグ         | （なし） |
| PR_R_SALES_D | IMNM        | 品名                   | （なし） |
| PR_R_SALES_D | ITEM        | 品目                   | （なし） |
| PR_R_SALES_D | ITEMF       | 受注品目区分           | （なし） |
| PR_R_SALES_D | ITEMF2      | 支給区分               | （なし） |
| PR_R_SALES_D | LNNO        | 行番号                 | （なし） |
| PR_R_SALES_D | ORDERNO     | オーダーNo             | （なし） |
| PR_R_SALES_D | PROCESS     | 工程                   | （なし） |
| PR_R_SALES_D | RCPEXD      | 入金予定日             | （なし） |
| PR_R_SALES_D | REMARK1     | 備考１                 | （なし） |
| PR_R_SALES_D | REMARK2     | 備考２                 | （なし） |
| PR_R_SALES_D | RGSTD       | 登録日                 | （なし） |
| PR_R_SALES_D | SALENO      | 売掛No                 | （なし） |
| PR_R_SALES_D | SHIPQTY     | 出荷数                 | （なし） |
| PR_R_SALES_D | SHPMNTNO    | 出荷No                 | （なし） |
| PR_R_SALES_D | SLPF        | 伝票区分               | （なし） |
| PR_R_SALES_D | SLPF2       | 入金伝票区分           | （なし） |
| PR_R_SALES_D | SLSMUPD     | 売上計上日             | （なし） |
| PR_R_SALES_D | SP_F        | 単価参照F              | （なし） |
| PR_R_SALES_D | STLMTD      | 決済日                 | （なし） |
| PR_R_SALES_D | TAXF        | 税区分                 | （なし） |
| PR_R_SALES_D | TERMINAL    | 端末情報               | （なし） |
| PR_R_SALES_D | TOAMTMNY    | 税抜金額               | （なし） |
| PR_R_SALES_D | UNTPRC      | 単価                   | （なし） |
| PR_R_SALES_D | UPDTD       | 更新日                 | （なし） |
| PR_R_SALES_D | UPDTWKCD    | 更新担当者             | （なし） |
| PR_R_SALES_D | WSETD       | 締日                   | （なし） |

## テーブル: PR_R_SALES_D_LST

| テーブル名       | 列ID        | 列名                   | 備考     |
|:-----------------|:------------|:-----------------------|:---------|
| PR_R_SALES_D_LST | ADJMNY      | 調整額                 | （なし） |
| PR_R_SALES_D_LST | ADR         | 住所                   | （なし） |
| PR_R_SALES_D_LST | AMTMNY      | 合計金額               | （なし） |
| PR_R_SALES_D_LST | CLMCD       | 請求先                 | （なし） |
| PR_R_SALES_D_LST | CLWSTD      | 売掛締日               | （なし） |
| PR_R_SALES_D_LST | CLWSTED     | 売掛締終了日           | （なし） |
| PR_R_SALES_D_LST | CLWSTSD     | 売掛締開始日           | （なし） |
| PR_R_SALES_D_LST | CUST_PRNFLG | 今回対象プリントフラグ | （なし） |
| PR_R_SALES_D_LST | CUSTOMNM    | 請求先名称             | （なし） |
| PR_R_SALES_D_LST | FAX         | FAX                    | （なし） |
| PR_R_SALES_D_LST | LAMTCMNY    | 前回請求額             | （なし） |
| PR_R_SALES_D_LST | LSTCORMPY   | 前月繰越残高           | （なし） |
| PR_R_SALES_D_LST | MAMTMNY     | 未決済残高             | （なし） |
| PR_R_SALES_D_LST | OAMTMNY     | その他金額             | （なし） |
| PR_R_SALES_D_LST | POSTCD      | 郵便番号               | （なし） |
| PR_R_SALES_D_LST | RGSTD       | 登録日                 | （なし） |
| PR_R_SALES_D_LST | SALENO      | 売掛No                 | （なし） |
| PR_R_SALES_D_LST | TEL         | TEL                    | （なし） |
| PR_R_SALES_D_LST | TERMINAL    | 端末情報               | （なし） |
| PR_R_SALES_D_LST | TTRCPBL     | 今回入金（手形）       | （なし） |
| PR_R_SALES_D_LST | TTRCPC      | 今回入金（その他）     | （なし） |
| PR_R_SALES_D_LST | TTRCPCB     | 今回入金（相殺）       | （なし） |
| PR_R_SALES_D_LST | TTRCPCS     | 今回入金（現金）       | （なし） |
| PR_R_SALES_D_LST | TTSL        | 今回売上税抜金額       | （なし） |
| PR_R_SALES_D_LST | TTSLTX      | 今回売上税             | （なし） |
| PR_R_SALES_D_LST | UPDTD       | 更新日                 | （なし） |
| PR_R_SALES_D_LST | UPDTWKCD    | 更新担当者             | （なし） |

## テーブル: PR_SALENO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| PR_SALENO    | K_NO     | キー項目     | （なし） |
| PR_SALENO    | LAST_OD1 | 最終オーダNo | （なし） |
| PR_SALENO    | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: PR_SALES

| テーブル名   | 列ID       | 列名           | 備考     |
|:-------------|:-----------|:---------------|:---------|
| PR_SALES     | ADDF       | 追加フラグ     | （なし） |
| PR_SALES     | AMTMNY     | 金額           | （なし） |
| PR_SALES     | AMTTAX     | 税額           | （なし） |
| PR_SALES     | CCLF       | 削除区分       | （なし） |
| PR_SALES     | CLMCD      | 請求先         | （なし） |
| PR_SALES     | CLOJF      | 計上対象区分   | （なし） |
| PR_SALES     | CLWSTD     | 請求締日       | （なし） |
| PR_SALES     | CUSTOM     | 得意先         | （なし） |
| PR_SALES     | CUSTOMIMNM | 顧客品名       | （なし） |
| PR_SALES     | CUSTOMITEM | 顧客品目       | （なし） |
| PR_SALES     | CUSTOMNO   | 顧客注番       | （なし） |
| PR_SALES     | DEMANDNO   | 社内注番       | （なし） |
| PR_SALES     | GRA_FLG    | 有償無償フラグ | （なし） |
| PR_SALES     | IMNM       | 品名           | （なし） |
| PR_SALES     | ITEM       | 品目           | （なし） |
| PR_SALES     | ITEMF      | 受注品目区分   | （なし） |
| PR_SALES     | ITEMF2     | 支給区分       | （なし） |
| PR_SALES     | KDSHPMNTNO | KD出荷No       | （なし） |
| PR_SALES     | PRICEF     | 単価区分       | （なし） |
| PR_SALES     | PROCESS    | 工程           | （なし） |
| PR_SALES     | PRTF       | プリントフラグ | （なし） |
| PR_SALES     | RCBLWSTD   | 売掛締日       | （なし） |
| PR_SALES     | RCORDERNO  | 受注No         | （なし） |
| PR_SALES     | REMARK1    | 備考１         | （なし） |
| PR_SALES     | REMARK2    | 備考２         | （なし） |
| PR_SALES     | RGSTD      | 登録日         | （なし） |
| PR_SALES     | SBJCT      | 科目           | （なし） |
| PR_SALES     | SHIPQTY    | 数量           | （なし） |
| PR_SALES     | SHPMNTNO   | 出荷No         | （なし） |
| PR_SALES     | SLPF       | 伝票区分       | （なし） |
| PR_SALES     | SLSCT      | 売上部門       | （なし） |
| PR_SALES     | SLSMUPD    | 売上計上日     | （なし） |
| PR_SALES     | SLWKCD     | 売上担当者     | （なし） |
| PR_SALES     | TAXF       | 税区分         | （なし） |
| PR_SALES     | TERMINAL   | 端末情報       | （なし） |
| PR_SALES     | TOAMTMNY   | 税抜金額       | （なし） |
| PR_SALES     | UNTPRC     | 単価           | （なし） |
| PR_SALES     | UPDTD      | 更新日         | （なし） |
| PR_SALES     | UPDTWKCD   | 更新担当者     | （なし） |

## テーブル: PR_SALESW

| テーブル名   | 列ID       | 列名           | 備考     |
|:-------------|:-----------|:---------------|:---------|
| PR_SALESW    | ADDF       | 追加フラグ     | （なし） |
| PR_SALESW    | AMTMNY     | 合計金額       | （なし） |
| PR_SALESW    | AMTTAX     | 税額           | （なし） |
| PR_SALESW    | CCLF       | 削除区分       | （なし） |
| PR_SALESW    | CLMCD      | 請求先         | （なし） |
| PR_SALESW    | CLOJF      | 請求対象区分   | （なし） |
| PR_SALESW    | CLWSTD     | 請求締日       | （なし） |
| PR_SALESW    | CUSTOM     | 得意先         | （なし） |
| PR_SALESW    | CUSTOMIMNM | 顧客品名       | （なし） |
| PR_SALESW    | CUSTOMITEM | 顧客品目       | （なし） |
| PR_SALESW    | CUSTOMNO   | 顧客注番       | （なし） |
| PR_SALESW    | DEMANDNO   | 社内注番       | （なし） |
| PR_SALESW    | GRA_FLG    | 有償無償フラグ | （なし） |
| PR_SALESW    | IMNM       | 品名           | （なし） |
| PR_SALESW    | IMTYP      | 製品区分       | （なし） |
| PR_SALESW    | ITEM       | 品目           | （なし） |
| PR_SALESW    | ITEMF      | 受注品目区分   | （なし） |
| PR_SALESW    | ITEMF2     | 支給区分       | （なし） |
| PR_SALESW    | KDSHPMNTNO | KD出荷No       | （なし） |
| PR_SALESW    | PRICEF     | 単価区分       | （なし） |
| PR_SALESW    | PROCESS    | 工程           | （なし） |
| PR_SALESW    | PRTF       | プリントフラグ | （なし） |
| PR_SALESW    | RCBLWSTD   | 売掛締日       | （なし） |
| PR_SALESW    | RCISCD     | 入出庫区分     | （なし） |
| PR_SALESW    | RCORDERNO  | 受注No         | （なし） |
| PR_SALESW    | REMARK1    | 備考１         | （なし） |
| PR_SALESW    | REMARK2    | 備考２         | （なし） |
| PR_SALESW    | RGSTD      | 登録日         | （なし） |
| PR_SALESW    | SBJCT      | 科目           | （なし） |
| PR_SALESW    | SHIPQTY    | 出荷数         | （なし） |
| PR_SALESW    | SHPMNTNO   | 出荷No         | （なし） |
| PR_SALESW    | SLPF       | 伝票区分       | （なし） |
| PR_SALESW    | SLSCT      | 売上部門       | （なし） |
| PR_SALESW    | SLSMUPD    | 売上計上日     | （なし） |
| PR_SALESW    | SLWKCD     | 売上担当者     | （なし） |
| PR_SALESW    | TAXF       | 税区分         | （なし） |
| PR_SALESW    | TERMINAL   | 端末情報       | （なし） |
| PR_SALESW    | TOAMTMNY   | 税抜金額       | （なし） |
| PR_SALESW    | UNTPRC     | 単価           | （なし） |
| PR_SALESW    | UPDTD      | 更新日         | （なし） |
| PR_SALESW    | UPDTWKCD   | 更新担当者     | （なし） |
| PR_SALESW    | VENDOR     | 仕入先         | （なし） |

## テーブル: PR_SALES_D

| テーブル名   | 列ID       | 列名           | 備考     |
|:-------------|:-----------|:---------------|:---------|
| PR_SALES_D   | A_ORDERNO  | オーダNo       | （なし） |
| PR_SALES_D   | AMTMNY     | 金額           | （なし） |
| PR_SALES_D   | AMTTAX     | 税額           | （なし） |
| PR_SALES_D   | BILNO      | 手形番号       | （なし） |
| PR_SALES_D   | CCNO       | 請求連番       | （なし） |
| PR_SALES_D   | CLMCD      | 請求先         | （なし） |
| PR_SALES_D   | CLWSTD     | 請求締日       | （なし） |
| PR_SALES_D   | CUSTOM     | 得意先         | （なし） |
| PR_SALES_D   | CUSTOMIMNM | 顧客品名       | （なし） |
| PR_SALES_D   | CUSTOMITEM | 顧客品目       | （なし） |
| PR_SALES_D   | CUSTOMNO   | 顧客注番       | （なし） |
| PR_SALES_D   | DEMANDNO   | 社内注番       | （なし） |
| PR_SALES_D   | GRA_FLG    | 有償無償フラグ | （なし） |
| PR_SALES_D   | IMNM       | 品名           | （なし） |
| PR_SALES_D   | ITEM       | 品目           | （なし） |
| PR_SALES_D   | ITEMF      | 受注品目区分   | （なし） |
| PR_SALES_D   | ITEMF2     | 支給区分       | （なし） |
| PR_SALES_D   | LNNO       | 行番号         | （なし） |
| PR_SALES_D   | PROCESS    | 工程           | （なし） |
| PR_SALES_D   | RCPEXD     | 入金予定日     | （なし） |
| PR_SALES_D   | REMARK1    | 備考１         | （なし） |
| PR_SALES_D   | REMARK2    | 備考２         | （なし） |
| PR_SALES_D   | RGSTD      | 登録日         | （なし） |
| PR_SALES_D   | SALENO     | 売掛No         | （なし） |
| PR_SALES_D   | SBJCT      | 科目           | （なし） |
| PR_SALES_D   | SHIPQTY    | 出荷数         | （なし） |
| PR_SALES_D   | SHPMNTNO   | 出荷No         | （なし） |
| PR_SALES_D   | SLPF       | 伝票区分       | （なし） |
| PR_SALES_D   | SLPF2      | 入金伝票区分   | （なし） |
| PR_SALES_D   | SLSMUPD    | 売上計上日     | （なし） |
| PR_SALES_D   | SP_F       | 単価参照F      | （なし） |
| PR_SALES_D   | STLMTD     | 決済日         | （なし） |
| PR_SALES_D   | TAXF       | 税区分         | （なし） |
| PR_SALES_D   | TERMINAL   | 端末情報       | （なし） |
| PR_SALES_D   | TOAMTMNY   | 税抜金額       | （なし） |
| PR_SALES_D   | UNTPRC     | 単価           | （なし） |
| PR_SALES_D   | UPDTD      | 更新日         | （なし） |
| PR_SALES_D   | UPDTWKCD   | 更新担当者     | （なし） |
| PR_SALES_D   | WSETD      | 締日           | （なし） |

## テーブル: PR_SALES_D_LST

| テーブル名     | 列ID      | 列名               | 備考     |
|:---------------|:----------|:-------------------|:---------|
| PR_SALES_D_LST | ADJMNY    | 調整額             | （なし） |
| PR_SALES_D_LST | ADR       | 住所               | （なし） |
| PR_SALES_D_LST | AMTMNY    | 合計金額           | （なし） |
| PR_SALES_D_LST | CLMCD     | 請求先             | （なし） |
| PR_SALES_D_LST | CLWSTD    | 請求締日           | （なし） |
| PR_SALES_D_LST | CLWSTED   | 請求締終了日       | （なし） |
| PR_SALES_D_LST | CLWSTSD   | 請求締開始日       | （なし） |
| PR_SALES_D_LST | CUSTOMNM  | 請求先名称         | （なし） |
| PR_SALES_D_LST | FAX       | FAX                | （なし） |
| PR_SALES_D_LST | LAMTCMNY  | 前回請求額         | （なし） |
| PR_SALES_D_LST | LSTCORMPY | 前月繰越残高       | （なし） |
| PR_SALES_D_LST | MAMTMNY   | 翌月繰越残高       | （なし） |
| PR_SALES_D_LST | OAMTMNY   | その他金額         | （なし） |
| PR_SALES_D_LST | POSTCD    | 郵便番号           | （なし） |
| PR_SALES_D_LST | RGSTD     | 登録日             | （なし） |
| PR_SALES_D_LST | SALENO    | 売掛No             | （なし） |
| PR_SALES_D_LST | TEL       | TEL                | （なし） |
| PR_SALES_D_LST | TERMINAL  | 端末情報           | （なし） |
| PR_SALES_D_LST | TTRCPBL   | 今回入金（手形）   | （なし） |
| PR_SALES_D_LST | TTRCPC    | 今回入金（その他） | （なし） |
| PR_SALES_D_LST | TTRCPCB   | 今回入金（相殺）   | （なし） |
| PR_SALES_D_LST | TTRCPCS   | 今回入金（現金）   | （なし） |
| PR_SALES_D_LST | TTSL      | 今回売上税抜金額   | （なし） |
| PR_SALES_D_LST | TTSLTX    | 今回売上税         | （なし） |
| PR_SALES_D_LST | UPDTD     | 更新日             | （なし） |
| PR_SALES_D_LST | UPDTWKCD  | 更新担当者         | （なし） |

## テーブル: PR_SHIPMENT

| テーブル名   | 列ID         | 列名           | 備考                        |
|:-------------|:-------------|:---------------|:----------------------------|
| PR_SHIPMENT  | A_ORDERNO    | オーダNo       | （なし）                    |
| PR_SHIPMENT  | ADDF         | 追加フラグ     | （なし）                    |
| PR_SHIPMENT  | ADDFLG       | 追加Ｆ         | 0;通常;1;追加               |
| PR_SHIPMENT  | AMOUNT       | 受注金額       | （なし）                    |
| PR_SHIPMENT  | AMTMNY       | 合計金額       | （なし）                    |
| PR_SHIPMENT  | AMTTAX       | 税額           | （なし）                    |
| PR_SHIPMENT  | CCLF         | 削除区分       | （なし）                    |
| PR_SHIPMENT  | CLMCD        | 請求先         | （なし）                    |
| PR_SHIPMENT  | CLOJF        | 請求対象区分   | （なし）                    |
| PR_SHIPMENT  | CLWSTD       | 請求締日       | （なし）                    |
| PR_SHIPMENT  | CUSTOM       | 出荷先         | （なし）                    |
| PR_SHIPMENT  | CUSTOMNO     | 顧客注番       | （なし）                    |
| PR_SHIPMENT  | GRA_FLG      | 有償無償フラグ | （なし）                    |
| PR_SHIPMENT  | IMNM         | 品名           | （なし）                    |
| PR_SHIPMENT  | ITEM         | 品目           | （なし）                    |
| PR_SHIPMENT  | ITEMF2       | 支給区分       | （なし）                    |
| PR_SHIPMENT  | LOCT         | 納入先         | （なし）                    |
| PR_SHIPMENT  | MONTH        | 売上予測月     | （なし）                    |
| PR_SHIPMENT  | PRICEF       | 単価区分       | （なし）                    |
| PR_SHIPMENT  | PRNF         | プリントフラグ | （なし）                    |
| PR_SHIPMENT  | PROCESS      | 工程           | （なし）                    |
| PR_SHIPMENT  | PRTF         | プリントフラグ | （なし）                    |
| PR_SHIPMENT  | PRTPACKPRICE | パーツ梱包単価 | （なし）                    |
| PR_SHIPMENT  | RCBLWSTD     | 売掛締日       | （なし）                    |
| PR_SHIPMENT  | RCORDERNO    | 受注No         | （なし）                    |
| PR_SHIPMENT  | REMARK1      | 備考１         | （なし）                    |
| PR_SHIPMENT  | REMARK2      | 備考２         | （なし）                    |
| PR_SHIPMENT  | RGSTD        | 登録日         | （なし）                    |
| PR_SHIPMENT  | SBJCT        | 科目           | （なし）                    |
| PR_SHIPMENT  | SHPMNTD      | 出荷日         | （なし）                    |
| PR_SHIPMENT  | SHPMNTNO     | 出荷No         | （なし）                    |
| PR_SHIPMENT  | SHPMNTQTY    | 出荷数         | （なし）                    |
| PR_SHIPMENT  | SHPSCT       | 出荷部門       | （なし）                    |
| PR_SHIPMENT  | SHPWKCD      | 出荷担当者     | （なし）                    |
| PR_SHIPMENT  | SLPF         | 伝票区分       | （なし）                    |
| PR_SHIPMENT  | SLSMUPD      | 売上計上日     | （なし）                    |
| PR_SHIPMENT  | SP_F         | 単価参照F      | 0;単価マスタより;1;特別単価 |
| PR_SHIPMENT  | TAXF         | 税区分         | （なし）                    |
| PR_SHIPMENT  | TERMINAL     | 端末情報       | （なし）                    |
| PR_SHIPMENT  | TOAMTMNY     | 税抜金額       | （なし）                    |
| PR_SHIPMENT  | UNTPRC       | 単価           | （なし）                    |
| PR_SHIPMENT  | UPDTD        | 更新日         | （なし）                    |
| PR_SHIPMENT  | UPDTWKCD     | 更新担当者     | （なし）                    |
| PR_SHIPMENT  | VENDOR       | 仕入先         | （なし）                    |
| PR_SHIPMENT  | YEAR         | 売上予測年     | （なし）                    |

## テーブル: PR_SHIPMENT_TMP

| テーブル名      | 列ID        | 列名           | 備考                        |
|:----------------|:------------|:---------------|:----------------------------|
| PR_SHIPMENT_TMP | ADDF        | 追加フラグ     | （なし）                    |
| PR_SHIPMENT_TMP | AMTMNY      | 合計金額       | （なし）                    |
| PR_SHIPMENT_TMP | AMTTAX      | 税額           | （なし）                    |
| PR_SHIPMENT_TMP | CCLF        | 削除区分       | （なし）                    |
| PR_SHIPMENT_TMP | CFM_F       | 確認F          | 0;未確認;1;確認済み         |
| PR_SHIPMENT_TMP | CLMCD       | 請求先         | （なし）                    |
| PR_SHIPMENT_TMP | CLOJF       | 請求対象区分   | （なし）                    |
| PR_SHIPMENT_TMP | CLWSTD      | 請求締日       | （なし）                    |
| PR_SHIPMENT_TMP | CUSTOM      | 出荷先         | （なし）                    |
| PR_SHIPMENT_TMP | CUSTOMNO    | 顧客注番       | （なし）                    |
| PR_SHIPMENT_TMP | DIFFER      | 差             | （なし）                    |
| PR_SHIPMENT_TMP | GRA_FLG     | 有償無償フラグ | （なし）                    |
| PR_SHIPMENT_TMP | IMNM        | 品名           | （なし）                    |
| PR_SHIPMENT_TMP | INVDELIDATE | 顧客納期       | （なし）                    |
| PR_SHIPMENT_TMP | ITEM        | 品目           | （なし）                    |
| PR_SHIPMENT_TMP | ITEMF2      | 支給区分       | （なし）                    |
| PR_SHIPMENT_TMP | LOCT        | 納入先         | （なし）                    |
| PR_SHIPMENT_TMP | PRICEF      | 単価区分       | （なし）                    |
| PR_SHIPMENT_TMP | PRNF        | プリントフラグ | （なし）                    |
| PR_SHIPMENT_TMP | PROCESS     | 工程           | （なし）                    |
| PR_SHIPMENT_TMP | PRTF        | プリントフラグ | （なし）                    |
| PR_SHIPMENT_TMP | RCBLWSTD    | 売掛締日       | （なし）                    |
| PR_SHIPMENT_TMP | RCORDERNO   | 受注No         | （なし）                    |
| PR_SHIPMENT_TMP | REMARK1     | 備考１         | （なし）                    |
| PR_SHIPMENT_TMP | REMARK2     | 備考２         | （なし）                    |
| PR_SHIPMENT_TMP | RGSTD       | 登録日         | （なし）                    |
| PR_SHIPMENT_TMP | SBJCT       | 科目           | （なし）                    |
| PR_SHIPMENT_TMP | SHPMNTD     | 出荷日         | （なし）                    |
| PR_SHIPMENT_TMP | SHPMNTNO    | 出荷No         | （なし）                    |
| PR_SHIPMENT_TMP | SHPMNTQTY   | 出荷数         | （なし）                    |
| PR_SHIPMENT_TMP | SHPSCT      | 出荷部門       | （なし）                    |
| PR_SHIPMENT_TMP | SHPWKCD     | 出荷担当者     | （なし）                    |
| PR_SHIPMENT_TMP | SLPF        | 伝票区分       | （なし）                    |
| PR_SHIPMENT_TMP | SLSMUPD     | 売上計上日     | （なし）                    |
| PR_SHIPMENT_TMP | SP_F        | 単価参照F      | 0;単価マスタより;1;特別単価 |
| PR_SHIPMENT_TMP | TAXF        | 税区分         | （なし）                    |
| PR_SHIPMENT_TMP | TERMINAL    | 端末情報       | （なし）                    |
| PR_SHIPMENT_TMP | TOAMTMNY    | 税抜金額       | （なし）                    |
| PR_SHIPMENT_TMP | UNTPRC      | 単価           | （なし）                    |
| PR_SHIPMENT_TMP | UPDTD       | 更新日         | （なし）                    |
| PR_SHIPMENT_TMP | UPDTWKCD    | 更新担当者     | （なし）                    |
| PR_SHIPMENT_TMP | VENDOR      | 仕入先         | （なし）                    |

## テーブル: PR_SHIPNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| PR_SHIPNO    | K_NO     | キー項目     | （なし） |
| PR_SHIPNO    | LAST_OD1 | 最終オーダNo | （なし） |
| PR_SHIPNO    | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: PR_U_LEDGERW

| テーブル名   | 列ID      | 列名         | 備考     |
|:-------------|:----------|:-------------|:---------|
| PR_U_LEDGERW | AMTMNY    | 金額         | （なし） |
| PR_U_LEDGERW | AMTTAX    | 税額         | （なし） |
| PR_U_LEDGERW | CHKD      | 伝票日付     | （なし） |
| PR_U_LEDGERW | CHKNO     | 伝票番号     | （なし） |
| PR_U_LEDGERW | CLMCD     | 請求先       | （なし） |
| PR_U_LEDGERW | CUSTOMNM  | 請求先名称   | （なし） |
| PR_U_LEDGERW | IMNM      | 品名         | （なし） |
| PR_U_LEDGERW | ITEM      | 品目         | （なし） |
| PR_U_LEDGERW | LSTCORMPY | 前月繰越残高 | （なし） |
| PR_U_LEDGERW | SAMTMNY   | 入金額       | （なし） |
| PR_U_LEDGERW | SHIPQTY   | 出荷数       | （なし） |
| PR_U_LEDGERW | SLPF      | 伝票区分     | （なし） |
| PR_U_LEDGERW | TOUZAN    | 当月売掛残高 | （なし） |
| PR_U_LEDGERW | UNTPRC    | 単価         | （なし） |
| PR_U_LEDGERW | ZENZAN    | 前回売掛残高 | （なし） |

## テーブル: PR_U_LEDGERW2

| テーブル名    | 列ID      | 列名                           | 備考     |
|:--------------|:----------|:-------------------------------|:---------|
| PR_U_LEDGERW2 | ADJMNY    | 調整額                         | （なし） |
| PR_U_LEDGERW2 | AMTTAX    | 税額                           | （なし） |
| PR_U_LEDGERW2 | CLMCD     | 請求先                         | （なし） |
| PR_U_LEDGERW2 | CUSTOMNM  | 請求先名称                     | （なし） |
| PR_U_LEDGERW2 | LSTCORMPY | 前月繰越残高                   | （なし） |
| PR_U_LEDGERW2 | MAMTMNY   | 翌月繰越残高                   | （なし） |
| PR_U_LEDGERW2 | NAMTMNY   | 相殺額                         | （なし） |
| PR_U_LEDGERW2 | NAMTMNY2  | その他相殺額（手数料・郵送料） | （なし） |
| PR_U_LEDGERW2 | SAMTMNY   | 入金額                         | （なし） |
| PR_U_LEDGERW2 | UAMTMNY   | 売上金額                       | （なし） |

## テーブル: PR_WELLSET

| テーブル名   | 列ID      | 列名                  | 備考     |
|:-------------|:----------|:----------------------|:---------|
| PR_WELLSET   | CLAIMNO   | 請求No                | （なし） |
| PR_WELLSET   | CLAMTMNY  | 請求調整金額          | （なし） |
| PR_WELLSET   | CLWSTD    | 請求締日              | （なし） |
| PR_WELLSET   | CUSTOM    | 得意先                | （なし） |
| PR_WELLSET   | DATAF     | DATAF                 | （なし） |
| PR_WELLSET   | EDDATE    | EDDATE                | （なし） |
| PR_WELLSET   | LSTCORMPY | 前月繰越残高          | （なし） |
| PR_WELLSET   | LSTCORMRC | LSTCORMRC             | （なし） |
| PR_WELLSET   | PMTWSTD   | 支払締日              | （なし） |
| PR_WELLSET   | PYAMTMNY  | PYAMTMNY              | （なし） |
| PR_WELLSET   | PYEENO    | 支払書No(計上通知No） | （なし） |
| PR_WELLSET   | RGSTD     | 登録日                | （なし） |
| PR_WELLSET   | STDATE    | STDATE                | （なし） |
| PR_WELLSET   | TERMINAL  | 端末情報              | （なし） |
| PR_WELLSET   | TTPYEBL   | TTPYEBL               | （なし） |
| PR_WELLSET   | TTPYEC    | TTPYEC                | （なし） |
| PR_WELLSET   | TTPYECB   | TTPYECB               | （なし） |
| PR_WELLSET   | TTPYECS   | TTPYECS               | （なし） |
| PR_WELLSET   | TTRCPBL   | 今回入金（手形）      | （なし） |
| PR_WELLSET   | TTRCPC    | 今回入金（その他）    | （なし） |
| PR_WELLSET   | TTRCPCB   | 今回入金（相殺）      | （なし） |
| PR_WELLSET   | TTRCPCS   | 今回入金（現金）      | （なし） |
| PR_WELLSET   | TTSL      | 今回売上税抜金額      | （なし） |
| PR_WELLSET   | TTSLTX    | 今回売上税            | （なし） |
| PR_WELLSET   | TTSP      | TTSP                  | （なし） |
| PR_WELLSET   | TTSPTX    | TTSPTX                | （なし） |
| PR_WELLSET   | UPDTD     | 更新日                | （なし） |
| PR_WELLSET   | UPDTWKCD  | 更新担当者            | （なし） |
| PR_WELLSET   | YRDGR     | YRDGR                 | （なし） |

## テーブル: PR_W_PAYMENT

| テーブル名   | 列ID      | 列名           | 備考     |
|:-------------|:----------|:---------------|:---------|
| PR_W_PAYMENT | AMTTAX    | 当月仕入税額   | （なし） |
| PR_W_PAYMENT | LSTCORMPE | 前回支払繰越残 | （なし） |
| PR_W_PAYMENT | PAMTMNY   | 今回支払額     | （なし） |
| PR_W_PAYMENT | PMTWSTD   | 支払締日       | （なし） |
| PR_W_PAYMENT | PYECD     | 支払先         | （なし） |
| PR_W_PAYMENT | SAMTMNY   | 当月仕入額     | （なし） |
| PR_W_PAYMENT | VENDORNM  | 支払先名称     | （なし） |

## テーブル: PR_W_RECEIVE

| テーブル名   | 列ID        | 列名           | 備考     |
|:-------------|:------------|:---------------|:---------|
| PR_W_RECEIVE | AMTMNY      | 金額           | （なし） |
| PR_W_RECEIVE | AMTTAX      | 税額           | （なし） |
| PR_W_RECEIVE | CCLF        | 削除区分       | （なし） |
| PR_W_RECEIVE | COUNTER     | 内部登録No     | （なし） |
| PR_W_RECEIVE | IMNM        | 品名           | （なし） |
| PR_W_RECEIVE | IMTYP       | 製品区分       | （なし） |
| PR_W_RECEIVE | ITEM        | 品目           | （なし） |
| PR_W_RECEIVE | LOCT        | 場所           | （なし） |
| PR_W_RECEIVE | PMTWSTD     | 支払締日       | （なし） |
| PR_W_RECEIVE | PRICEF      | 単価区分       | （なし） |
| PR_W_RECEIVE | PROCESS     | 工程           | （なし） |
| PR_W_RECEIVE | PRTF        | プリントフラグ | （なし） |
| PR_W_RECEIVE | PYBLWSTD    | 買掛締日       | （なし） |
| PR_W_RECEIVE | RCISCD      | 入出庫区分     | （なし） |
| PR_W_RECEIVE | RCVD        | 受入日         | （なし） |
| PR_W_RECEIVE | RCVQTY      | 受入数         | （なし） |
| PR_W_RECEIVE | RCVSCT      | 受入部門       | （なし） |
| PR_W_RECEIVE | RCVWKCD     | 受入担当者     | （なし） |
| PR_W_RECEIVE | REMARK1     | 備考１         | （なし） |
| PR_W_RECEIVE | REMARK2     | 備考２         | （なし） |
| PR_W_RECEIVE | REPDELIDATE | 回答納期       | （なし） |
| PR_W_RECEIVE | RGSTD       | 登録日         | （なし） |
| PR_W_RECEIVE | SLPF        | 伝票区分       | （なし） |
| PR_W_RECEIVE | TAXF        | 税区分         | （なし） |
| PR_W_RECEIVE | TERMINAL    | 端末情報       | （なし） |
| PR_W_RECEIVE | TOAMTMNY    | 税抜金額       | （なし） |
| PR_W_RECEIVE | UNTPRC      | 単価           | （なし） |
| PR_W_RECEIVE | UPDTD       | 更新日         | （なし） |
| PR_W_RECEIVE | UPDTWKCD    | 更新担当者     | （なし） |
| PR_W_RECEIVE | VENDOR      | 仕入先         | （なし） |
| PR_W_RECEIVE | VENDOR2     | 外注ｺｰﾄﾞ       | （なし） |

## テーブル: PR_W_SALESBUNDLE

| テーブル名       | 列ID    | 列名       | 備考     |
|:-----------------|:--------|:-----------|:---------|
| PR_W_SALESBUNDLE | RCBLMTD | 売掛処理日 | （なし） |
| PR_W_SALESBUNDLE | UPDTFLG | 更新フラグ | （なし） |

## テーブル: PR_W_SHIPMENT

| テーブル名    | 列ID       | 列名           | 備考     |
|:--------------|:-----------|:---------------|:---------|
| PR_W_SHIPMENT | AMTMNY     | 合計金額       | （なし） |
| PR_W_SHIPMENT | AMTTAX     | 税額           | （なし） |
| PR_W_SHIPMENT | CCLF       | 削除区分       | （なし） |
| PR_W_SHIPMENT | CLWSTD     | 請求締日       | （なし） |
| PR_W_SHIPMENT | CUSTOM     | 得意先         | （なし） |
| PR_W_SHIPMENT | DELIQTY    | 分納数         | （なし） |
| PR_W_SHIPMENT | DRQTY      | 分納/返品数    | （なし） |
| PR_W_SHIPMENT | FRACT      | 金額端数区分   | （なし） |
| PR_W_SHIPMENT | IMNM       | 品名           | （なし） |
| PR_W_SHIPMENT | ITEM       | 品目           | （なし） |
| PR_W_SHIPMENT | ITEMF      | 受注品目区分   | （なし） |
| PR_W_SHIPMENT | ITEMF2     | 支給区分       | （なし） |
| PR_W_SHIPMENT | LOCT       | 場所           | （なし） |
| PR_W_SHIPMENT | PRICEF     | 単価区分       | （なし） |
| PR_W_SHIPMENT | PRNF       | プリントフラグ | （なし） |
| PR_W_SHIPMENT | PROCESS    | 工程           | （なし） |
| PR_W_SHIPMENT | RCBLWSTD   | 売掛締日       | （なし） |
| PR_W_SHIPMENT | RCISCD     | 入出庫区分     | （なし） |
| PR_W_SHIPMENT | RCORDERNO  | 受注No         | （なし） |
| PR_W_SHIPMENT | REMARK1    | 備考１         | （なし） |
| PR_W_SHIPMENT | REMARK2    | 備考２         | （なし） |
| PR_W_SHIPMENT | RETURNDATE | 分納日         | （なし） |
| PR_W_SHIPMENT | RETURNQTY  | 返品数         | （なし） |
| PR_W_SHIPMENT | RETURNTIME | 分納時間       | （なし） |
| PR_W_SHIPMENT | RGSTD      | 登録日         | （なし） |
| PR_W_SHIPMENT | SHPMNTD    | 出荷日         | （なし） |
| PR_W_SHIPMENT | SHPMNTNO   | 出荷No         | （なし） |
| PR_W_SHIPMENT | SHPMNTQTY  | 出荷数         | （なし） |
| PR_W_SHIPMENT | SHPSCT     | 出荷部門       | （なし） |
| PR_W_SHIPMENT | SHPWKCD    | 出荷担当者     | （なし） |
| PR_W_SHIPMENT | SLPF       | 伝票区分       | （なし） |
| PR_W_SHIPMENT | TAXCLDGT   | 消費税端数桁数 | （なし） |
| PR_W_SHIPMENT | TAXF       | 税区分         | （なし） |
| PR_W_SHIPMENT | TAXFRF     | 消費税端数区分 | （なし） |
| PR_W_SHIPMENT | TAXRETE    | 税率           | （なし） |
| PR_W_SHIPMENT | TERMINAL   | 端末情報       | （なし） |
| PR_W_SHIPMENT | TOAMTMNY   | 税抜金額       | （なし） |
| PR_W_SHIPMENT | UNTPRC     | 単価           | （なし） |
| PR_W_SHIPMENT | UPDTD      | 更新日         | （なし） |
| PR_W_SHIPMENT | UPDTWKCD   | 更新担当者     | （なし） |
| PR_W_SHIPMENT | VENDOR     | 仕入先         | （なし） |

## テーブル: PURCHASEORDER

| テーブル名    | 列ID        | 列名                  | 備考                                                                      |
|:--------------|:------------|:----------------------|:--------------------------------------------------------------------------|
| PURCHASEORDER | A_FPTYPE    | 購入区分              | R;固定自給;Y;有償支給;N;無償支給;G;変動自給                               |
| PURCHASEORDER | A_ITMSTATUS | ステータス            | 1;試作;2;生試;3;初品;4;量産;6;製品打切;7;サービスパーツ;8;削除;9;製作不可 |
| PURCHASEORDER | A_SUPPLIER  | 供給者                | （なし）                                                                  |
| PURCHASEORDER | A_USER      | 使用者                | （なし）                                                                  |
| PURCHASEORDER | ADDFLG      | 追加Ｆ                | 0;通常;1;追加                                                             |
| PURCHASEORDER | AMTMNY      | 金額                  | （なし）                                                                  |
| PURCHASEORDER | ARRANGEQTY  | 発注数                | （なし）                                                                  |
| PURCHASEORDER | BKTNO       | バケットNo            | （なし）                                                                  |
| PURCHASEORDER | BKTYEAR     | バケット年            | （なし）                                                                  |
| PURCHASEORDER | CCLF        | 削除区分              | （なし）                                                                  |
| PURCHASEORDER | CCLRMRK     | 削除備考              | （なし）                                                                  |
| PURCHASEORDER | CMPFLG      | 完了Ｆ                | 0;未完了;1;完了                                                           |
| PURCHASEORDER | COST        | 単価                  | （なし）                                                                  |
| PURCHASEORDER | CUSTOM2     | 顧客                  | （なし）                                                                  |
| PURCHASEORDER | CUSTOMNO    | オーダーNo            | （なし）                                                                  |
| PURCHASEORDER | DELIDATE    | 納期                  | （なし）                                                                  |
| PURCHASEORDER | IMTYP       | 製品区分              | 0;製造品1;購入品2;外注品                                                  |
| PURCHASEORDER | INVOICENO   | 納品書No              | （なし）                                                                  |
| PURCHASEORDER | ITEM        | 品目                  | （なし）                                                                  |
| PURCHASEORDER | LATE_F      | 遅延F                 | 0;遅延ではない;1;遅延                                                     |
| PURCHASEORDER | LINED       | 指示ライン            | （なし）                                                                  |
| PURCHASEORDER | MBPRND      | 納品書現品票印刷日    | （なし）                                                                  |
| PURCHASEORDER | MBPRNF      | 納品書現品票印刷F     | （なし）                                                                  |
| PURCHASEORDER | MPSORDERNO  | 基準生産計画オーダNo  | （なし）                                                                  |
| PURCHASEORDER | OFFCLF      | 確定/内示Ｆ           | 0;内示;1;確定                                                             |
| PURCHASEORDER | ORDERFLG    | 発行F                 | 0;展開より;1;指示発行より                                                 |
| PURCHASEORDER | ORDERQTY    | オーダ数              | （なし）                                                                  |
| PURCHASEORDER | ORDERUNIT   | 手配単位              | （なし）                                                                  |
| PURCHASEORDER | ORDRSCTN    | 発注部門              | （なし）                                                                  |
| PURCHASEORDER | ORDRWKCD    | 発注担当者            | （なし）                                                                  |
| PURCHASEORDER | PMTWSTD     | 支払締日              | （なし）                                                                  |
| PURCHASEORDER | PRDCTBNO    | 枝番                  | （なし）                                                                  |
| PURCHASEORDER | PRDCTNO     | 製番                  | （なし）                                                                  |
| PURCHASEORDER | PRNF        | プリントフラグ        | （なし）                                                                  |
| PURCHASEORDER | PRNFLG      | オーダー票印刷完了Ｆ  | 0;印刷未完了;1;印刷完了                                                   |
| PURCHASEORDER | PRNFLG2     | 納入計画票印刷完了Ｆ  | 0;印刷未完了;1;印刷完了                                                   |
| PURCHASEORDER | PRNFLG3     | ｵｰﾀﾞ別出庫リスト印刷F | 0;印刷未完了;1;印刷完了                                                   |
| PURCHASEORDER | PROCESS     | 工程                  | （なし）                                                                  |
| PURCHASEORDER | PRVDPRNF    | 支給計画表F           | 0;印刷する;1;印刷しない                                                   |
| PURCHASEORDER | PUORDERNO   | 発注番号              | （なし）                                                                  |
| PURCHASEORDER | PYBLWSTD    | 買掛締日              | （なし）                                                                  |
| PURCHASEORDER | RCDATE      | 入庫日                | （なし）                                                                  |
| PURCHASEORDER | RCORDERNO   | 受注No                | （なし）                                                                  |
| PURCHASEORDER | RCQTY       | 入庫数                | （なし）                                                                  |
| PURCHASEORDER | RELEASEDATE | 発注日                | （なし）                                                                  |
| PURCHASEORDER | REMARK      | 備考                  | （なし）                                                                  |
| PURCHASEORDER | REMARK1     | 備考１                | （なし）                                                                  |
| PURCHASEORDER | REMARK2     | 備考２                | （なし）                                                                  |
| PURCHASEORDER | REPDELIDATE | 回答納期              | （なし）                                                                  |
| PURCHASEORDER | RGSTD       | 登録日                | （なし）                                                                  |
| PURCHASEORDER | RGSTTM      | 登録時刻              | （なし）                                                                  |
| PURCHASEORDER | STARTDATE   | 着手日                | （なし）                                                                  |
| PURCHASEORDER | TERMINAL    | 端末情報              | （なし）                                                                  |
| PURCHASEORDER | TRANSACTOR  | 取引先                | （なし）                                                                  |
| PURCHASEORDER | UPDTD       | 更新日                | （なし）                                                                  |
| PURCHASEORDER | UPDTWKCD    | 更新担当者            | （なし）                                                                  |
| PURCHASEORDER | VENDOR      | 仕入先                | （なし）                                                                  |
| PURCHASEORDER | VENDOR2     | 外注コード            | （なし）                                                                  |

## テーブル: PU_ORDERNO

| テーブル名   | 列ID     | 列名             | 備考     |
|:-------------|:---------|:-----------------|:---------|
| PU_ORDERNO   | K_NO     | キー項目         | （なし） |
| PU_ORDERNO   | LAST_OD1 | 最終オーダNo     | （なし） |
| PU_ORDERNO   | NEXT_OD1 | 次回オーダNo     | （なし） |
| PU_ORDERNO   | NEXT_OD2 | 次回内示オーダNo | （なし） |

## テーブル: SBCNTORDER

| テーブル名   | 列ID        | 列名                  | 備考                                                                      |
|:-------------|:------------|:----------------------|:--------------------------------------------------------------------------|
| SBCNTORDER   | A_ITMSTATUS | ステータス            | 1;試作;2;生試;3;初品;4;量産;6;製品打切;7;サービスパーツ;8;削除;9;製作不可 |
| SBCNTORDER   | ADDFLG      | 追加Ｆ                | 0;通常;1;追加                                                             |
| SBCNTORDER   | AMTMNY      | 金額                  | （なし）                                                                  |
| SBCNTORDER   | ARRANGEQTY  | 発注数                | （なし）                                                                  |
| SBCNTORDER   | BKTNO       | バケットNo            | （なし）                                                                  |
| SBCNTORDER   | BKTYEAR     | バケット年            | （なし）                                                                  |
| SBCNTORDER   | CCLF        | 削除区分              | （なし）                                                                  |
| SBCNTORDER   | CCLRMRK     | 削除備考              | （なし）                                                                  |
| SBCNTORDER   | CMPFLG      | 完了Ｆ                | 0;未完了;1;完了                                                           |
| SBCNTORDER   | COST        | 単価                  | （なし）                                                                  |
| SBCNTORDER   | DELIDATE    | 納期                  | （なし）                                                                  |
| SBCNTORDER   | IMTYP       | 製品区分              | 0;製造品1;購入品2;外注品                                                  |
| SBCNTORDER   | INVOICENO   | 納品書No              | （なし）                                                                  |
| SBCNTORDER   | ITEM        | 品目                  | （なし）                                                                  |
| SBCNTORDER   | LATE_F      | 遅延F                 | 0;遅延ではない;1;遅延                                                     |
| SBCNTORDER   | LINED       | 指示ライン            | （なし）                                                                  |
| SBCNTORDER   | MBPRND      | 納品書現品票印刷日    | （なし）                                                                  |
| SBCNTORDER   | MBPRNF      | 納品書現品票印刷F     | （なし）                                                                  |
| SBCNTORDER   | MPSORDERNO  | 基準生産計画オーダNo  | （なし）                                                                  |
| SBCNTORDER   | OFFCLF      | 確定/内示Ｆ           | 0;内示;1;確定                                                             |
| SBCNTORDER   | ORDERFLG    | 発行F                 | 0;展開より;1;指示発行より                                                 |
| SBCNTORDER   | ORDERQTY    | オーダ数              | （なし）                                                                  |
| SBCNTORDER   | ORDERUNIT   | 手配単位              | （なし）                                                                  |
| SBCNTORDER   | ORDRSCTN    | 発注部門              | （なし）                                                                  |
| SBCNTORDER   | ORDRWKCD    | 発注担当者            | （なし）                                                                  |
| SBCNTORDER   | PMTWSTD     | 支払締日              | （なし）                                                                  |
| SBCNTORDER   | PRDCTBNO    | 枝番                  | （なし）                                                                  |
| SBCNTORDER   | PRDCTNO     | 製番                  | （なし）                                                                  |
| SBCNTORDER   | PRNF        | プリントフラグ        | （なし）                                                                  |
| SBCNTORDER   | PRNFLG      | オーダー票印刷完了Ｆ  | 0;印刷未完了;1;印刷完了                                                   |
| SBCNTORDER   | PRNFLG2     | 納入計画表印刷完了Ｆ  | 0;印刷未完了;1;印刷完了                                                   |
| SBCNTORDER   | PRNFLG3     | ｵｰﾀﾞ別出庫リスト印刷F | 0;印刷未完了;1;印刷完了                                                   |
| SBCNTORDER   | PROCESS     | 工程                  | （なし）                                                                  |
| SBCNTORDER   | PRVDPRNF    | 支給計画表F           | 0;印刷しない;1;印刷する                                                   |
| SBCNTORDER   | PYBLWSTD    | 買掛締日              | （なし）                                                                  |
| SBCNTORDER   | RCDATE      | 入庫日                | （なし）                                                                  |
| SBCNTORDER   | RCORDERNO   | 受注No                | （なし）                                                                  |
| SBCNTORDER   | RCQTY       | 入庫数                | （なし）                                                                  |
| SBCNTORDER   | RELEASEDATE | 発注日                | （なし）                                                                  |
| SBCNTORDER   | REMARK      | 備考                  | （なし）                                                                  |
| SBCNTORDER   | REMARK1     | 備考１                | （なし）                                                                  |
| SBCNTORDER   | REMARK2     | 備考２                | （なし）                                                                  |
| SBCNTORDER   | REPDELIDATE | 回答納期              | （なし）                                                                  |
| SBCNTORDER   | RGSTD       | 登録日                | （なし）                                                                  |
| SBCNTORDER   | RGSTTM      | 登録時刻              | （なし）                                                                  |
| SBCNTORDER   | SBORDERNO   | 発注番号              | （なし）                                                                  |
| SBCNTORDER   | SIRODENF    | 白伝区分              | 0:通常 1:白伝                                                             |
| SBCNTORDER   | STARTDATE   | 着手日                | （なし）                                                                  |
| SBCNTORDER   | TERMINAL    | 端末情報              | （なし）                                                                  |
| SBCNTORDER   | TRANSACTOR  | 取引先                | （なし）                                                                  |
| SBCNTORDER   | UPDTD       | 更新日                | （なし）                                                                  |
| SBCNTORDER   | UPDTWKCD    | 更新担当者            | （なし）                                                                  |
| SBCNTORDER   | VENDOR      | 仕入先                | （なし）                                                                  |
| SBCNTORDER   | VENDOR2     | 外注ｺｰﾄﾞ              | （なし）                                                                  |
| SBCNTORDER   | XLSXADDF    | エクセル追加          | 0:その他;1;エクセル追加                                                   |

## テーブル: SB_ORDERNO

| テーブル名   | 列ID     | 列名             | 備考     |
|:-------------|:---------|:-----------------|:---------|
| SB_ORDERNO   | K_NO     | キー項目         | （なし） |
| SB_ORDERNO   | LAST_OD1 | 最終オーダNo     | （なし） |
| SB_ORDERNO   | NEXT_OD1 | 次回オーダNo     | （なし） |
| SB_ORDERNO   | NEXT_OD2 | 次回内示オーダNo | （なし） |

## テーブル: SHIFT_HISTORY

| テーブル名    | 列ID      | 列名         | 備考                |
|:--------------|:----------|:-------------|:--------------------|
| SHIFT_HISTORY | ACTFNTIME | 生産終了時間 | （なし）            |
| SHIFT_HISTORY | ACTSTDATE | 生産日       | （なし）            |
| SHIFT_HISTORY | ACTSTTIME | 生産開始時間 | （なし）            |
| SHIFT_HISTORY | ITEM      | 品目         | （なし）            |
| SHIFT_HISTORY | OEE_LINED | 実績ライン   | （なし）            |
| SHIFT_HISTORY | PROCESS   | 工程         | （なし）            |
| SHIFT_HISTORY | RGSTD     | 登録日       | YYYY/MM/DD HH;MM;SS |
| SHIFT_HISTORY | RGSTWKCD  | 登録担当者   | （なし）            |
| SHIFT_HISTORY | SECT      | 部門         | （なし）            |
| SHIFT_HISTORY | SHIFTF    | 直区分       | 1;1直;2;2直;3;3直   |
| SHIFT_HISTORY | SUB_NO    | 件数         | （なし）            |
| SHIFT_HISTORY | VENDOR    | 仕入先       | （なし）            |
| SHIFT_HISTORY | WORKER    | 作業者コード | （なし）            |

## テーブル: SHIPMENTDATA

| テーブル名   | 列ID          | 列名        | 備考                                       |
|:-------------|:--------------|:------------|:-------------------------------------------|
| SHIPMENTDATA | DELIQTY       | 分納数      | （なし）                                   |
| SHIPMENTDATA | DRQTY         | 分納/返品数 | 非表示項目（分納数を正、返品数を負で保存） |
| SHIPMENTDATA | LOCT          | 場所        | （なし）                                   |
| SHIPMENTDATA | LOTNO         | ロットNo    | 日付8桁＋連番8桁                           |
| SHIPMENTDATA | PLANTSHIPDATE | 工場出荷日  | （なし）                                   |
| SHIPMENTDATA | RCISCD        | 入出庫区分  | （なし）                                   |
| SHIPMENTDATA | RCORDERNO     | 受注No      | （なし）                                   |
| SHIPMENTDATA | REMARK        | 備考        | （なし）                                   |
| SHIPMENTDATA | RETURNDATE    | 分納日      | （なし）                                   |
| SHIPMENTDATA | RETURNQTY     | 返品数      | （なし）                                   |
| SHIPMENTDATA | RETURNTIME    | 分納時間    | （なし）                                   |
| SHIPMENTDATA | RGSTD         | 登録日時    | YYYY/MM/DD HH;MM;SS(非表示項目)            |
| SHIPMENTDATA | UPDTD         | 更新日      | （なし）                                   |
| SHIPMENTDATA | UPDTWKCD      | 更新担当者  | （なし）                                   |
| SHIPMENTDATA | WORKERCD      | 担当者      | （なし）                                   |

## テーブル: SHIPMENTLOTD

| テーブル名   | 列ID     | 列名         | 備考                                 |
|:-------------|:---------|:-------------|:-------------------------------------|
| SHIPMENTLOTD | ACTLOTNO | 生産ロットNo | 日付8桁＋工程5桁＋ライン5桁＋連番5桁 |
| SHIPMENTLOTD | LOTNO    | 出荷ロットNo | 日付8桁＋連番8桁                     |
| SHIPMENTLOTD | RGSTD    | 登録日       | （なし）                             |
| SHIPMENTLOTD | UPDTD    | 更新日       | （なし）                             |
| SHIPMENTLOTD | UPDTWKCD | 更新担当者   | （なし）                             |

## テーブル: SHIPORDER

| テーブル名   | 列ID          | 列名                 | 備考                                  |
|:-------------|:--------------|:---------------------|:--------------------------------------|
| SHIPORDER    | A_CARD_FLG    | カード区分           | （なし）                              |
| SHIPORDER    | A_COLOR       | 色指示コード         | （なし）                              |
| SHIPORDER    | A_EDI_F       | EDI取込F             | 0;EDI以外;1;YMC20L;2;MORIC;3;YMC01    |
| SHIPORDER    | A_ODRCD       | 発注方針コード       | （なし）                              |
| SHIPORDER    | A_PACKCD      | 荷姿コード           | （なし）                              |
| SHIPORDER    | A_PACKNM      | 荷姿名称             | （なし）                              |
| SHIPORDER    | A_PACKQTY     | 荷姿収容数           | （なし）                              |
| SHIPORDER    | A_PROCESS     | 工程番号             | （なし）                              |
| SHIPORDER    | A_STATUS      | 生試区分             | （なし）                              |
| SHIPORDER    | A_STATUSNM    | 生試区分             | （なし）                              |
| SHIPORDER    | A_SUPPLIER    | 供給者               | （なし）                              |
| SHIPORDER    | A_SUPPLIERNM  | 供給者名称           | （なし）                              |
| SHIPORDER    | A_USER        | 使用者               | （なし）                              |
| SHIPORDER    | A_USERNM      | 使用者名称           | （なし）                              |
| SHIPORDER    | ADDFLG        | 追加Ｆ               | 0;通常;1;追加                         |
| SHIPORDER    | ALLOCNO       | 引当受注No           | （なし）                              |
| SHIPORDER    | AMOUNT        | 受注金額             | （なし）                              |
| SHIPORDER    | ASTARTDATE    | 先行着手可能日       | （なし）                              |
| SHIPORDER    | BKTNO         | 受注読込バケット年No | （なし）                              |
| SHIPORDER    | BKTYEAR       | 受注読込バケット年   | （なし）                              |
| SHIPORDER    | CFM_F         | 確認F                | （なし）                              |
| SHIPORDER    | CLLCTYPE      | 集荷タイプ           | （なし）                              |
| SHIPORDER    | CMPFLG        | 出荷完了             | 0;未完了;1;完了                       |
| SHIPORDER    | CUSTOM        | 顧客                 | （なし）                              |
| SHIPORDER    | CUSTOMIMNM    | 顧客品名             | （なし）                              |
| SHIPORDER    | CUSTOMITEM    | 顧客品目             | （なし）                              |
| SHIPORDER    | CUSTOMNO      | 顧客注番             | （なし）                              |
| SHIPORDER    | DELIDATE      | 顧客納期             | （なし）                              |
| SHIPORDER    | DELILT        | 顧客納入L/T（日）    | （なし）                              |
| SHIPORDER    | DELIQTY_R     | 分納数               | （なし）                              |
| SHIPORDER    | DELITIME      | 納入時間(時)         | （なし）                              |
| SHIPORDER    | DEMANDNO      | 社内注番             | （なし）                              |
| SHIPORDER    | INVOICENO     | 納品書番号           | （なし）                              |
| SHIPORDER    | ITEM          | 品目                 | （なし）                              |
| SHIPORDER    | LATE_F        | 遅延F                | 0;遅延ではない;1;遅延                 |
| SHIPORDER    | LOCT          | 納入プラットフォーム | （なし）                              |
| SHIPORDER    | LOCT_R        | 場所                 | （なし）                              |
| SHIPORDER    | OFFCLF        | 確定/内示Ｆ          | 0;内示;1;確定                         |
| SHIPORDER    | ORDERCL       | 受注区分             | 0;新規;-1;受注取消                    |
| SHIPORDER    | ORDERQTY      | 受注数               | （なし）                              |
| SHIPORDER    | PER_F         | パー割F              | （なし）                              |
| SHIPORDER    | PLANTSHIPDATE | 工場出荷日           | （なし）                              |
| SHIPORDER    | PRDCTQTY      | 生産指示数           | （なし）                              |
| SHIPORDER    | PRNFLG        | 出荷指示書印刷F      | 0;印刷未完了;1;印刷完了               |
| SHIPORDER    | PROCESS       | 工程                 | （なし）                              |
| SHIPORDER    | RCISCD_R      | 入出庫区分           | （なし）                              |
| SHIPORDER    | RCORDERNO     | 受注No               | （なし）                              |
| SHIPORDER    | REMARK        | 備考                 | （なし）                              |
| SHIPORDER    | REMARK_R      | 備考                 | （なし）                              |
| SHIPORDER    | REPDELIDATE   | 回答納期             | （なし）                              |
| SHIPORDER    | RETURNDATE_R  | 分納日               | （なし）                              |
| SHIPORDER    | RETURNTIME_R  | 分納時間             | （なし）                              |
| SHIPORDER    | RORDERDATE    | 受注日               | （なし）                              |
| SHIPORDER    | SCHCOMPDATE   | 出荷予定日           | 納期を顧客納入L/Tでオフセットした日付 |
| SHIPORDER    | SHIPDATE      | 最終出荷日           | （なし）                              |
| SHIPORDER    | SHIPQTY       | 出荷数               | （なし）                              |
| SHIPORDER    | SHIPQTYTMP    | 出荷数               | （なし）                              |
| SHIPORDER    | STARTDATE     | 着手可能日           | （なし）                              |
| SHIPORDER    | STOCKALLOC    | 在庫引当数           | （なし）                              |
| SHIPORDER    | UNITPRICE     | 受注単価             | （なし）                              |
| SHIPORDER    | UPDTD         | 更新日               | （なし）                              |
| SHIPORDER    | UPDTWKCD      | 更新担当者           | （なし）                              |
| SHIPORDER    | URGENCYFLG    | 山積用特急F          | 0;通常;1;特急;2;超特急                |
| SHIPORDER    | VENDOR        | 仕入先               | （なし）                              |
| SHIPORDER    | WORKERCD_R    | 担当者               | （なし）                              |

## テーブル: SH_AMENDSLIST

| テーブル名    | 列ID         | 列名     | 備考                                        |
|:--------------|:-------------|:---------|:--------------------------------------------|
| SH_AMENDSLIST | A_FPTYPE     | 購入区分 | R;固定自給;Y;有償支給;N;無償支給;G;変動自給 |
| SH_AMENDSLIST | A_SUPPLIER   | 供給者   | 有償支給の供給者                            |
| SH_AMENDSLIST | A_USER       | 使用者   | 有償支給の供給者                            |
| SH_AMENDSLIST | AMNDQTY      | 数量     | 数量                                        |
| SH_AMENDSLIST | DRWNO        | 部品番号 | （なし）                                    |
| SH_AMENDSLIST | ITEM         | 品目     | （なし）                                    |
| SH_AMENDSLIST | PROCESS      | 工程     | （なし）                                    |
| SH_AMENDSLIST | RESP_SECT    | 責任部門 | （なし）                                    |
| SH_AMENDSLIST | SECTNM       | 部門名   | （なし）                                    |
| SH_AMENDSLIST | TERMINAL     | 端末ID   | （なし）                                    |
| SH_AMENDSLIST | TRANSACTOR   | 取引先   | （なし）                                    |
| SH_AMENDSLIST | TRANSACTORNM | 取引先名 | 0;顧客;1;仕入先                             |
| SH_AMENDSLIST | VENDOR       | 仕入先   | （なし）                                    |

## テーブル: SH_AMENDSLIST_D

| テーブル名      | 列ID         | 列名        | 備考                                        |
|:----------------|:-------------|:------------|:--------------------------------------------|
| SH_AMENDSLIST_D | A_FMCUS      | 代表得意先  | （なし）                                    |
| SH_AMENDSLIST_D | A_FPTYPE     | 購入区分    | R;固定自給;Y;有償支給;N;無償支給;G;変動自給 |
| SH_AMENDSLIST_D | A_SUPPLIER   | 供給者      | 有償支給の供給者                            |
| SH_AMENDSLIST_D | A_SUPPLIERNM | 供給者名称  | （なし）                                    |
| SH_AMENDSLIST_D | A_USER       | 使用者      | 有償支給の供給者                            |
| SH_AMENDSLIST_D | A_VENDOR     | 発注先      | 購入品、外注品の発注先                      |
| SH_AMENDSLIST_D | A_VENDORNM   | 仕入先名    | （なし）                                    |
| SH_AMENDSLIST_D | AMNDQTY      | 仕損数      | 数量                                        |
| SH_AMENDSLIST_D | ASSYNO       | Assy子部品№ | 0:本体、1-9:Assy子部品                      |
| SH_AMENDSLIST_D | COUNTER      | COUNTER     | （なし）                                    |
| SH_AMENDSLIST_D | DRWNO        | 部品番号    | （なし）                                    |
| SH_AMENDSLIST_D | FCDTY        | 理由タイプ  | （なし）                                    |
| SH_AMENDSLIST_D | FCNAME       | 理由内容    | （なし）                                    |
| SH_AMENDSLIST_D | FCODE        | 理由コード  | （なし）                                    |
| SH_AMENDSLIST_D | HAPPENDATE   | 発生日      | （なし）                                    |
| SH_AMENDSLIST_D | IMNM         | 品名        | （なし）                                    |
| SH_AMENDSLIST_D | ISSUENO      | 伝票No      | （なし）                                    |
| SH_AMENDSLIST_D | ITEM         | 品目        | （なし）                                    |
| SH_AMENDSLIST_D | PROCESS      | 工程        | （なし）                                    |
| SH_AMENDSLIST_D | TERMINAL     | 端末ID      | （なし）                                    |
| SH_AMENDSLIST_D | VENDOR       | 仕入先      | （なし）                                    |

## テーブル: SH_AMENDSLIST_R

| テーブル名      | 列ID         | 列名        | 備考                                        |
|:----------------|:-------------|:------------|:--------------------------------------------|
| SH_AMENDSLIST_R | A_FMCUS      | 代表得意先  | （なし）                                    |
| SH_AMENDSLIST_R | A_FPTYPE     | 購入区分    | R;固定自給;Y;有償支給;N;無償支給;G;変動自給 |
| SH_AMENDSLIST_R | A_SUPPLIER   | 供給者      | 有償支給の供給者                            |
| SH_AMENDSLIST_R | A_SUPPLIERNM | 供給者名称  | （なし）                                    |
| SH_AMENDSLIST_R | A_USER       | 使用者      | 有償支給の供給者                            |
| SH_AMENDSLIST_R | A_VENDOR     | 発注先      | 購入品、外注品の発注先                      |
| SH_AMENDSLIST_R | A_VENDORNM   | 仕入先名    | （なし）                                    |
| SH_AMENDSLIST_R | AMNDQTY      | 仕損数      | 数量                                        |
| SH_AMENDSLIST_R | ASSYNO       | Assy子部品№ | 0:本体、1-9:Assy子部品                      |
| SH_AMENDSLIST_R | B_HAPPENDATE | 部品受領日  | （なし）                                    |
| SH_AMENDSLIST_R | COUNTER      | COUNTER     | （なし）                                    |
| SH_AMENDSLIST_R | DRWNO        | 部品番号    | （なし）                                    |
| SH_AMENDSLIST_R | FCDTY        | 理由タイプ  | （なし）                                    |
| SH_AMENDSLIST_R | FCNAME       | 理由内容    | （なし）                                    |
| SH_AMENDSLIST_R | FCODE        | 理由コード  | （なし）                                    |
| SH_AMENDSLIST_R | FIND_SECT    | 発生部門    | （なし）                                    |
| SH_AMENDSLIST_R | HAPPENDATE   | 発生日      | （なし）                                    |
| SH_AMENDSLIST_R | HDRWNO       | 新部品番号  | （なし）                                    |
| SH_AMENDSLIST_R | IMNM         | 品名        | （なし）                                    |
| SH_AMENDSLIST_R | ISSUENO      | 伝票No      | （なし）                                    |
| SH_AMENDSLIST_R | ITEM         | 品目        | （なし）                                    |
| SH_AMENDSLIST_R | PROCESS      | 工程        | （なし）                                    |
| SH_AMENDSLIST_R | TERMINAL     | 端末ID      | （なし）                                    |
| SH_AMENDSLIST_R | VENDOR       | 仕入先      | （なし）                                    |
| SH_AMENDSLIST_R | WKRATE       | 進度(%)     | （なし）                                    |

## テーブル: SH_AMENDSLIST_RR

| テーブル名       | 列ID         | 列名        | 備考                                        |
|:-----------------|:-------------|:------------|:--------------------------------------------|
| SH_AMENDSLIST_RR | A_FMCUS      | 代表得意先  | （なし）                                    |
| SH_AMENDSLIST_RR | A_FPTYPE     | 購入区分    | R;固定自給;Y;有償支給;N;無償支給;G;変動自給 |
| SH_AMENDSLIST_RR | A_SUPPLIER   | 供給者      | 有償支給の供給者                            |
| SH_AMENDSLIST_RR | A_SUPPLIERNM | 供給者名称  | （なし）                                    |
| SH_AMENDSLIST_RR | A_USER       | 使用者      | 有償支給の供給者                            |
| SH_AMENDSLIST_RR | A_VENDOR     | 発注先      | 購入品、外注品の発注先                      |
| SH_AMENDSLIST_RR | A_VENDORNM   | 仕入先名    | （なし）                                    |
| SH_AMENDSLIST_RR | AMNDQTY      | 仕損数      | 数量                                        |
| SH_AMENDSLIST_RR | ASSYNO       | Assy子部品№ | 0:本体、1-9:Assy子部品                      |
| SH_AMENDSLIST_RR | B_HAPPENDATE | 部品受領日  | （なし）                                    |
| SH_AMENDSLIST_RR | COUNTER      | COUNTER     | （なし）                                    |
| SH_AMENDSLIST_RR | DPROCESS     | 入力工程    | （なし）                                    |
| SH_AMENDSLIST_RR | DRWNO        | 部品番号    | （なし）                                    |
| SH_AMENDSLIST_RR | FCDTY        | 理由タイプ  | （なし）                                    |
| SH_AMENDSLIST_RR | FCNAME       | 理由内容    | （なし）                                    |
| SH_AMENDSLIST_RR | FCODE        | 理由コード  | （なし）                                    |
| SH_AMENDSLIST_RR | FIND_SECT    | 発生部門    | （なし）                                    |
| SH_AMENDSLIST_RR | HAPPENDATE   | 発生日      | （なし）                                    |
| SH_AMENDSLIST_RR | HDRWNO       | 新部品番号  | （なし）                                    |
| SH_AMENDSLIST_RR | HPROCESS     | 親工程      | （なし）                                    |
| SH_AMENDSLIST_RR | IMNM         | 品名        | （なし）                                    |
| SH_AMENDSLIST_RR | ISSUENO      | 伝票No      | （なし）                                    |
| SH_AMENDSLIST_RR | ITEM         | 品目        | （なし）                                    |
| SH_AMENDSLIST_RR | OCASIONFLGNM | 発生部署    | （なし）                                    |
| SH_AMENDSLIST_RR | PROCESS      | 工程        | （なし）                                    |
| SH_AMENDSLIST_RR | TERMINAL     | 端末ID      | （なし）                                    |
| SH_AMENDSLIST_RR | VENDOR       | 仕入先      | （なし）                                    |
| SH_AMENDSLIST_RR | WKRATE       | 進度(%)     | （なし）                                    |

## テーブル: SH_CHKREPORTPLAN

| テーブル名       | 列ID         | 列名        | 備考           |
|:-----------------|:-------------|:------------|:---------------|
| SH_CHKREPORTPLAN | CUSTOM       | 得意先      | （なし）       |
| SH_CHKREPORTPLAN | DELIDATE     | 顧客納期    | （なし）       |
| SH_CHKREPORTPLAN | DRWNO        | 部品番号    | （なし）       |
| SH_CHKREPORTPLAN | IMNM         | 品名        | （なし）       |
| SH_CHKREPORTPLAN | ITEM         | 品目        | （なし）       |
| SH_CHKREPORTPLAN | LOCT         | 納入場所    | （なし）       |
| SH_CHKREPORTPLAN | LOCTNM       | 場所名      | （なし）       |
| SH_CHKREPORTPLAN | OFFCLF       | 確定/内示Ｆ | （なし）       |
| SH_CHKREPORTPLAN | ORDERQTY     | 受注数      | （なし）       |
| SH_CHKREPORTPLAN | PROCESS      | 工程        | （なし）       |
| SH_CHKREPORTPLAN | RCORDERNO    | 受注No      | （なし）       |
| SH_CHKREPORTPLAN | TERMINAL     | 端末ID      | （なし）       |
| SH_CHKREPORTPLAN | TRANSACTORNM | 得意先名    | （なし）       |
| SH_CHKREPORTPLAN | VENDOR       | 仕入先      | 「NONE」に固定 |

## テーブル: SH_CREDITCOMP

| テーブル名    | 列ID         | 列名       | 備考           |
|:--------------|:-------------|:-----------|:---------------|
| SH_CREDITCOMP | AMTMNY       | 納入金額   | （なし）       |
| SH_CREDITCOMP | COUNTER      | 内部登録No | （なし）       |
| SH_CREDITCOMP | CUSTOM       | 顧客       | （なし）       |
| SH_CREDITCOMP | CUSTOMNO     | 顧客注番   | （なし）       |
| SH_CREDITCOMP | DELIDATE     | 顧客納期   | （なし）       |
| SH_CREDITCOMP | DIFCOMMENT   | 差異内容   | （なし）       |
| SH_CREDITCOMP | DRWNO        | 部品番号   | （なし）       |
| SH_CREDITCOMP | IMNM         | 品名       | （なし）       |
| SH_CREDITCOMP | ITEM         | 品目       | （なし）       |
| SH_CREDITCOMP | LOCT         | 納入場所   | （なし）       |
| SH_CREDITCOMP | LOCTNM       | 場所名     | （なし）       |
| SH_CREDITCOMP | ORDERQTY     | 納入数     | （なし）       |
| SH_CREDITCOMP | PRICE        | 納入単価   | （なし）       |
| SH_CREDITCOMP | PROCESS      | 工程       | （なし）       |
| SH_CREDITCOMP | RCORDERNO    | 受注No     | （なし）       |
| SH_CREDITCOMP | RCVDAMTMNY   | 支払金額   | （なし）       |
| SH_CREDITCOMP | RCVDSHIPQTY  | 支払案内数 | （なし）       |
| SH_CREDITCOMP | RCVDUNTPRC   | 支払単価   | （なし）       |
| SH_CREDITCOMP | RECEIVE_DATE | 受入日     | （なし）       |
| SH_CREDITCOMP | TERMINAL     | 端末ID     | （なし）       |
| SH_CREDITCOMP | TRANSACTORNM | 請求先名   | （なし）       |
| SH_CREDITCOMP | VENDOR       | 仕入先     | 「NONE」に固定 |

## テーブル: SH_INVOICE

| テーブル名   | 列ID         | 列名       | 備考                   |
|:-------------|:-------------|:-----------|:-----------------------|
| SH_INVOICE   | ACCNM        | 口座番号   | （なし）               |
| SH_INVOICE   | ACCTYP       | 口座種別   | 0;当座;1;普通;3;その他 |
| SH_INVOICE   | ADR          | 住所       | （なし）               |
| SH_INVOICE   | ADR2         | 住所2      | （なし）               |
| SH_INVOICE   | AMTMNY       | 請求金額   | （なし）               |
| SH_INVOICE   | AMTTAX       | 税額       | （なし）               |
| SH_INVOICE   | BANKCD       | 銀行コード | （なし）               |
| SH_INVOICE   | BANKNM       | 銀行名     | （なし）               |
| SH_INVOICE   | CCNO         | 請求連番   | （なし）               |
| SH_INVOICE   | CLAIMNO      | 請求№      | （なし）               |
| SH_INVOICE   | CLMCD        | 請求先     | （なし）               |
| SH_INVOICE   | CLWSTD_MONTH | 請求締日月 | （なし）               |
| SH_INVOICE   | CLWSTD_YEAR  | 請求締日年 | （なし）               |
| SH_INVOICE   | CUSTOMNO     | 顧客注番   | （なし）               |
| SH_INVOICE   | DETAIL_F     | 詳細区分   | 0;明細;1;合計データ    |
| SH_INVOICE   | DRWNO        | 部品番号   | （なし）               |
| SH_INVOICE   | IMNM         | 品名       | （なし）               |
| SH_INVOICE   | ITEM         | 品目       | （なし）               |
| SH_INVOICE   | POSTCD       | 郵便番号   | （なし）               |
| SH_INVOICE   | PROCESS      | 工程       | （なし）               |
| SH_INVOICE   | REMARK       | 備考       | （なし）               |
| SH_INVOICE   | SHIPQTY      | 出荷数     | （なし）               |
| SH_INVOICE   | SHPMNTD      | 納品日     | （なし）               |
| SH_INVOICE   | TERMINAL     | 端末ID     | （なし）               |
| SH_INVOICE   | TOAMTMNY     | 税抜金額   | （なし）               |
| SH_INVOICE   | TRANSACTORNM | 請求先名   | （なし）               |
| SH_INVOICE   | UNTPRC       | 単価       | （なし）               |
| SH_INVOICE   | VENDOR       | 仕入先     | 「NONE」に固定         |

## テーブル: SH_INVSTOCK_TMP

| テーブル名      | 列ID        | 列名       | 備考     |
|:----------------|:------------|:-----------|:---------|
| SH_INVSTOCK_TMP | CARDNO      | 伝票No     | （なし） |
| SH_INVSTOCK_TMP | COUNTER     | 内部登録No | （なし） |
| SH_INVSTOCK_TMP | DRWNO       | 部品番号   | （なし） |
| SH_INVSTOCK_TMP | EREACD      | エリア担当 | （なし） |
| SH_INVSTOCK_TMP | IMNM        | 品名       | （なし） |
| SH_INVSTOCK_TMP | INVDATE     | 棚卸日     | （なし） |
| SH_INVSTOCK_TMP | INVQTY      | 棚卸数     | （なし） |
| SH_INVSTOCK_TMP | INVSTOCK_NO | 棚番       | （なし） |
| SH_INVSTOCK_TMP | ITEM        | 品目       | （なし） |
| SH_INVSTOCK_TMP | PROCESS     | 工程       | （なし） |
| SH_INVSTOCK_TMP | RGSTD       | 登録日     | （なし） |
| SH_INVSTOCK_TMP | TERMINAL    | 端末情報   | （なし） |
| SH_INVSTOCK_TMP | VENDOR      | 仕入先     | （なし） |

## テーブル: SH_ISOMOVE

| テーブル名   | 列ID     | 列名         | 備考                       |
|:-------------|:---------|:-------------|:---------------------------|
| SH_ISOMOVE   | COUNTER  | 内部登録No   | 帳票に不使用               |
| SH_ISOMOVE   | DELIDATE | 予定日       | （なし）                   |
| SH_ISOMOVE   | DRWNO    | 部品番号     | （なし）                   |
| SH_ISOMOVE   | IMNM     | 品名         | （なし）                   |
| SH_ISOMOVE   | ITEM     | 品目         | （なし）                   |
| SH_ISOMOVE   | ORDERNO  | オーダーNo   | （なし）                   |
| SH_ISOMOVE   | PACKQTY  | 入数         | （なし）                   |
| SH_ISOMOVE   | PAGEDENO | ページ数分母 | 帳票データ作成時のみに使用 |
| SH_ISOMOVE   | PAGENO   | ページNo     | （なし）                   |
| SH_ISOMOVE   | PAGENUME | ページ数分子 | 帳票データ作成時のみに使用 |
| SH_ISOMOVE   | PROCESS  | 工程         | （なし）                   |
| SH_ISOMOVE   | RCISQTY  | 指示数       | （なし）                   |
| SH_ISOMOVE   | TERMINAL | 端末ID       | （なし）                   |
| SH_ISOMOVE   | VENDOR   | 仕入先       | （なし）                   |

## テーブル: SH_ISSUEREQ

| テーブル名   | 列ID      | 列名         | 備考                              |
|:-------------|:----------|:-------------|:----------------------------------|
| SH_ISSUEREQ  | DRWNO     | 部品番号     | （なし）                          |
| SH_ISSUEREQ  | IMNM      | 品名         | （なし）                          |
| SH_ISSUEREQ  | IMTYPE    | 品目分類     | （なし）                          |
| SH_ISSUEREQ  | ITEM      | 品目         | （なし）                          |
| SH_ISSUEREQ  | LINED     | 指示ライン   | （なし）                          |
| SH_ISSUEREQ  | LINENM    | ライン名     | （なし）                          |
| SH_ISSUEREQ  | LOCTNM    | 場所名       | 保管場所名                        |
| SH_ISSUEREQ  | OBITEM    | 対象品目     | （なし）                          |
| SH_ISSUEREQ  | OBPROCESS | 対象品目工程 | （なし）                          |
| SH_ISSUEREQ  | ORDER_F   | 指示F        | 0;生産指示データ;1;出庫指示データ |
| SH_ISSUEREQ  | PLANDATE  | 指示日       | （なし）                          |
| SH_ISSUEREQ  | PROCESS   | 工程         | （なし）                          |
| SH_ISSUEREQ  | REQQTY    | 必要数       | （なし）                          |
| SH_ISSUEREQ  | SECT      | 担当部門     | （なし）                          |
| SH_ISSUEREQ  | SECTNM    | 部門名       | （なし）                          |
| SH_ISSUEREQ  | STLOC     | 保管場所     | （なし）                          |
| SH_ISSUEREQ  | TERMINAL  | 端末ID       | （なし）                          |
| SH_ISSUEREQ  | VENDOR    | 仕入先       | （なし）                          |

## テーブル: SH_PAYMENT

| テーブル名   | 列ID           | 列名           | 備考                                        |
|:-------------|:---------------|:---------------|:--------------------------------------------|
| SH_PAYMENT   | A_FPLACE1      | 受入場所       | （なし）                                    |
| SH_PAYMENT   | A_FPTYPE       | 購入区分       | R;固定自給;Y;有償支給;N;無償支給;G;変動自給 |
| SH_PAYMENT   | ADR            | 住所           | （なし）                                    |
| SH_PAYMENT   | ADR2           | 住所2          | （なし）                                    |
| SH_PAYMENT   | AMTMNY         | 受入金額       | （なし）                                    |
| SH_PAYMENT   | AMTTAX         | 税額           | （なし）                                    |
| SH_PAYMENT   | DETAIL_F       | 詳細区分       | 0;明細;1;合計データ                         |
| SH_PAYMENT   | DRWNO          | 部品番号       | （なし）                                    |
| SH_PAYMENT   | IMNM           | 品名           | （なし）                                    |
| SH_PAYMENT   | ITEM           | 品目           | （なし）                                    |
| SH_PAYMENT   | LOCTNM         | 場所名         | （なし）                                    |
| SH_PAYMENT   | NONO           | 計上通知連番   | （なし）                                    |
| SH_PAYMENT   | NOTICENO       | 計上通知No     | （なし）                                    |
| SH_PAYMENT   | PMTWSTD_MONTH  | 支払締日月     | （なし）                                    |
| SH_PAYMENT   | PMTWSTD_YEAR   | 支払締日年     | （なし）                                    |
| SH_PAYMENT   | POSTCD         | 郵便番号       | （なし）                                    |
| SH_PAYMENT   | PROCESS        | 工程           | （なし）                                    |
| SH_PAYMENT   | PYECD          | 支払先         | （なし）                                    |
| SH_PAYMENT   | REGISTRATIONNO | 適格事業者番号 | （なし）                                    |
| SH_PAYMENT   | REMARK         | 備考           | （なし）                                    |
| SH_PAYMENT   | SBORDERNO      | オーダーNo     | （なし）                                    |
| SH_PAYMENT   | SP_F           | 単価区分       | 0;単価マスタより;1;特別単価                 |
| SH_PAYMENT   | SPLYQTY        | 受入数量       | （なし）                                    |
| SH_PAYMENT   | SPYSMUPD       | 受入日         | （なし）                                    |
| SH_PAYMENT   | TERMINAL       | 端末ID         | （なし）                                    |
| SH_PAYMENT   | TOAMTMNY       | 税抜金額       | （なし）                                    |
| SH_PAYMENT   | TRANSACTORNM   | 支払先名       | （なし）                                    |
| SH_PAYMENT   | UNIT           | 単位           | （なし）                                    |
| SH_PAYMENT   | UNTPRC         | 単価           | （なし）                                    |
| SH_PAYMENT   | VENDOR         | 仕入先         | 「NONE」に固定                              |
| SH_PAYMENT   | WKRATE         | 進度(%)        | （なし）                                    |

## テーブル: SH_PRDCTINST

| テーブル名   | 列ID        | 列名               | 備考     |
|:-------------|:------------|:-------------------|:---------|
| SH_PRDCTINST | A_ITMSTATUS | ステータス         | （なし） |
| SH_PRDCTINST | DRWNO       | 部品番号           | （なし） |
| SH_PRDCTINST | IMNM        | 品名               | （なし） |
| SH_PRDCTINST | ITEM        | 品目               | （なし） |
| SH_PRDCTINST | LINED       | 指示ライン         | （なし） |
| SH_PRDCTINST | LINENM      | ライン名           | （なし） |
| SH_PRDCTINST | LOCTNM      | 場所名             | （なし） |
| SH_PRDCTINST | PA_DRWNO    | 親部品番号         | （なし） |
| SH_PRDCTINST | PA_ITEM     | 親品目             | （なし） |
| SH_PRDCTINST | PA_LINED    | 親ライン           | （なし） |
| SH_PRDCTINST | PA_LINENM   | 親ライン名         | （なし） |
| SH_PRDCTINST | PA_PROCESS  | 親工程             | （なし） |
| SH_PRDCTINST | PA_SECT     | 親ライン担当部門   | （なし） |
| SH_PRDCTINST | PA_SECTNM   | 親ライン担当部門名 | （なし） |
| SH_PRDCTINST | PA_VENDOR   | 親仕入先           | （なし） |
| SH_PRDCTINST | PLANDATE    | 指示日             | （なし） |
| SH_PRDCTINST | PRDCTQTY    | 指示数             | （なし） |
| SH_PRDCTINST | PROCESS     | 工程               | （なし） |
| SH_PRDCTINST | PRORDERNO   | オーダNo           | （なし） |
| SH_PRDCTINST | SECT        | 担当部門           | （なし） |
| SH_PRDCTINST | SECTNM      | 部門名             | （なし） |
| SH_PRDCTINST | STLOC       | 保管場所           | （なし） |
| SH_PRDCTINST | TERMINAL    | 端末ID             | （なし） |
| SH_PRDCTINST | VENDOR      | 仕入先             | （なし） |

## テーブル: SH_PRDCTPLAN

| テーブル名   | 列ID      | 列名       | 備考                               |
|:-------------|:----------|:-----------|:-----------------------------------|
| SH_PRDCTPLAN | DRWNO     | 部品番号   | （なし）                           |
| SH_PRDCTPLAN | IMNM      | 品名       | （なし）                           |
| SH_PRDCTPLAN | ITEM      | 品目       | （なし）                           |
| SH_PRDCTPLAN | LINED     | 指示ライン | （なし）                           |
| SH_PRDCTPLAN | LINENM    | ライン名   | （なし）                           |
| SH_PRDCTPLAN | PLANDATE  | 指示日     | （なし）                           |
| SH_PRDCTPLAN | PRDCTQTY  | 指示数     | （なし）                           |
| SH_PRDCTPLAN | PROCESS   | 工程       | （なし）                           |
| SH_PRDCTPLAN | PRORDERNO | オーダNo   | （なし）                           |
| SH_PRDCTPLAN | SECT      | 担当部門   | （なし）                           |
| SH_PRDCTPLAN | SECTNM    | 部門名     | （なし）                           |
| SH_PRDCTPLAN | SUM_FLG   | 集計F      | 0;確定明細;1;過去発注残;2;未来集計 |
| SH_PRDCTPLAN | TERMINAL  | 端末ID     | （なし）                           |
| SH_PRDCTPLAN | VENDOR    | 仕入先     | （なし）                           |

## テーブル: SH_PRICENOTICE

| テーブル名     | 列ID         | 列名           | 備考          |
|:---------------|:-------------|:---------------|:--------------|
| SH_PRICENOTICE | ADR          | 住所           | 住所（1段目） |
| SH_PRICENOTICE | ADR2         | 住所2          | 住所（2段目） |
| SH_PRICENOTICE | APPLYDATE    | 発効日         | （なし）      |
| SH_PRICENOTICE | COUNTER      | 内部登録No     | （なし）      |
| SH_PRICENOTICE | DRWNO        | 部品番号       | （なし）      |
| SH_PRICENOTICE | IMNM         | 品名           | （なし）      |
| SH_PRICENOTICE | ITEM         | 品目           | （なし）      |
| SH_PRICENOTICE | LIMNM        | 原材料名       | （なし）      |
| SH_PRICENOTICE | LITEM        | 原材料品目     | （なし）      |
| SH_PRICENOTICE | LPROCESS     | 原材料工程     | （なし）      |
| SH_PRICENOTICE | LVENDOR      | 原材料仕入先   | （なし）      |
| SH_PRICENOTICE | MAT_PRICE    | 材料費         | （なし）      |
| SH_PRICENOTICE | PHUNIT       | 投入重量       | （なし）      |
| SH_PRICENOTICE | POSTCD       | 郵便番号       | 郵便番号      |
| SH_PRICENOTICE | PRICE        | 単価           | （なし）      |
| SH_PRICENOTICE | PRICE_INPUT  | 投入単価       | （なし）      |
| SH_PRICENOTICE | PROC_CHARGE  | 加工費         | （なし）      |
| SH_PRICENOTICE | PROCESS      | 工程           | （なし）      |
| SH_PRICENOTICE | REASONCD     | 原因CD         | （なし）      |
| SH_PRICENOTICE | SCR_PHUNIT   | スクラップ重量 | （なし）      |
| SH_PRICENOTICE | SCR_PRICE    | スクラップ単価 | （なし）      |
| SH_PRICENOTICE | TERMINAL     | 端末ID         | （なし）      |
| SH_PRICENOTICE | TRANSACTOR   | 取引先         | （なし）      |
| SH_PRICENOTICE | TRANSACTORNM | 取引先名       | 取引先名      |
| SH_PRICENOTICE | VENDOR       | 仕入先         | （なし）      |

## テーブル: SH_PROVIDEINV

| テーブル名    | 列ID          | 列名           | 備考                                                                      |
|:--------------|:--------------|:---------------|:--------------------------------------------------------------------------|
| SH_PROVIDEINV | A_ITMSTATUS   | ステータス     | 1;試作;2;生試;3;初品;4;量産;6;製品打切;7;サービスパーツ;8;削除;9;製作不可 |
| SH_PROVIDEINV | COUNTER       | 内部登録No     | （なし）                                                                  |
| SH_PROVIDEINV | DRWNO         | 部品番号       | （なし）                                                                  |
| SH_PROVIDEINV | HDRWNO        | 親部品番号     | （なし）                                                                  |
| SH_PROVIDEINV | HITEM         | 親品目         | （なし）                                                                  |
| SH_PROVIDEINV | HPROCESS      | 親工程         | （なし）                                                                  |
| SH_PROVIDEINV | IMNM          | 品名           | （なし）                                                                  |
| SH_PROVIDEINV | ITEM          | 品目           | （なし）                                                                  |
| SH_PROVIDEINV | LTRANSACTOR   | 子品目取引先   | （なし）                                                                  |
| SH_PROVIDEINV | LTRANSACTORNM | 子品目取引先名 | （なし）                                                                  |
| SH_PROVIDEINV | PROCESS       | 工程           | （なし）                                                                  |
| SH_PROVIDEINV | PRVDDATE      | 支給日         | （なし）                                                                  |
| SH_PROVIDEINV | PRVDQTY       | 支給数         | （なし）                                                                  |
| SH_PROVIDEINV | REMARK        | 備考           | （なし）                                                                  |
| SH_PROVIDEINV | TERMINAL      | 端末ID         | （なし）                                                                  |
| SH_PROVIDEINV | TRANSACTOR    | 取引先         | （なし）                                                                  |
| SH_PROVIDEINV | TRANSACTORNM  | 取引先名       | （なし）                                                                  |
| SH_PROVIDEINV | VENDOR        | 仕入先         | （なし）                                                                  |

## テーブル: SH_PROVIDEINV_EX

| テーブル名       | 列ID          | 列名           | 備考                                                                      |
|:-----------------|:--------------|:---------------|:--------------------------------------------------------------------------|
| SH_PROVIDEINV_EX | A_FPLACE1     | 場所1          | （なし）                                                                  |
| SH_PROVIDEINV_EX | A_ITMSTATUS   | ステータス     | 1;試作;2;生試;3;初品;4;量産;6;製品打切;7;サービスパーツ;8;削除;9;製作不可 |
| SH_PROVIDEINV_EX | COUNTER       | 内部登録No     | （なし）                                                                  |
| SH_PROVIDEINV_EX | DRWNO         | 部品番号       | （なし）                                                                  |
| SH_PROVIDEINV_EX | HDRWNO        | 親部品番号     | （なし）                                                                  |
| SH_PROVIDEINV_EX | HITEM         | 親品目         | （なし）                                                                  |
| SH_PROVIDEINV_EX | HPROCESS      | 親工程         | （なし）                                                                  |
| SH_PROVIDEINV_EX | IMNM          | 品名           | （なし）                                                                  |
| SH_PROVIDEINV_EX | ITEM          | 品目           | （なし）                                                                  |
| SH_PROVIDEINV_EX | LTRANSACTOR   | 子品目取引先   | （なし）                                                                  |
| SH_PROVIDEINV_EX | LTRANSACTORNM | 子品目取引先名 | （なし）                                                                  |
| SH_PROVIDEINV_EX | PROCESS       | 工程           | （なし）                                                                  |
| SH_PROVIDEINV_EX | PRVD_PLACE    | 支給先場所     | （なし）                                                                  |
| SH_PROVIDEINV_EX | PRVDDATE      | 支給日         | （なし）                                                                  |
| SH_PROVIDEINV_EX | PRVDQTY       | 支給数         | （なし）                                                                  |
| SH_PROVIDEINV_EX | REMARK        | 備考           | 0;受注;1;支給                                                             |
| SH_PROVIDEINV_EX | TRANSACTOR    | 取引先         | （なし）                                                                  |
| SH_PROVIDEINV_EX | TRANSACTORNM  | 取引先名       | （なし）                                                                  |
| SH_PROVIDEINV_EX | VENDOR        | 仕入先         | （なし）                                                                  |

## テーブル: SH_PROVIDEPLAN

| テーブル名     | 列ID           | 列名           | 備考                                            |
|:---------------|:---------------|:---------------|:------------------------------------------------|
| SH_PROVIDEPLAN | ADR            | 住所           | （なし）                                        |
| SH_PROVIDEPLAN | ADR2           | 住所2          | （なし）                                        |
| SH_PROVIDEPLAN | DELIDATE       | 顧客納期       | （なし）                                        |
| SH_PROVIDEPLAN | DRWNO          | 部品番号       | （なし）                                        |
| SH_PROVIDEPLAN | IMNM           | 品名           | （なし）                                        |
| SH_PROVIDEPLAN | ITEM           | 品目           | （なし）                                        |
| SH_PROVIDEPLAN | OBTRANSACTOR   | 対象取引先     | （なし）                                        |
| SH_PROVIDEPLAN | OFFCLF         | 確定/内示Ｆ    | 0;内示;1;確定                                   |
| SH_PROVIDEPLAN | ORDERQTY       | オーダ数       | （なし）                                        |
| SH_PROVIDEPLAN | POSTCD         | 郵便番号       | （なし）                                        |
| SH_PROVIDEPLAN | PROCESS        | 工程           | （なし）                                        |
| SH_PROVIDEPLAN | SHARE_TXT      | 共用部品       | （なし）                                        |
| SH_PROVIDEPLAN | T_ADR          | 取引先住所     | （なし）                                        |
| SH_PROVIDEPLAN | T_ADR2         | 取引先住所2    | （なし）                                        |
| SH_PROVIDEPLAN | T_POSTCD       | 取引先郵便番号 | （なし）                                        |
| SH_PROVIDEPLAN | TERMINAL       | 端末ID         | （なし）                                        |
| SH_PROVIDEPLAN | TRANSACTOR     | 取引先         | キー追加　2010/04/14 同一日・品目で異取引先対応 |
| SH_PROVIDEPLAN | TRANSACTOR_CNT | 対象取引先数   | （なし）                                        |
| SH_PROVIDEPLAN | TRANSACTORNM   | 取引先名       | （なし）                                        |
| SH_PROVIDEPLAN | VENDOR         | 仕入先         | 「NONE」に固定                                  |

## テーブル: SH_PURCHASE

| テーブル名   | 列ID         | 列名               | 備考     |
|:-------------|:-------------|:-------------------|:---------|
| SH_PURCHASE  | A_ITMSTATUS  | ステータス         | （なし） |
| SH_PURCHASE  | DELIDATE     | 指示日             | （なし） |
| SH_PURCHASE  | DRWNO        | 部品番号           | （なし） |
| SH_PURCHASE  | IMNM         | 品名               | （なし） |
| SH_PURCHASE  | ITEM         | 品目               | （なし） |
| SH_PURCHASE  | LOCTNM       | 場所名             | （なし） |
| SH_PURCHASE  | ORDERQTY     | オーダ数           | （なし） |
| SH_PURCHASE  | PA_DRWNO     | 親部品番号         | （なし） |
| SH_PURCHASE  | PA_ITEM      | 親品目             | （なし） |
| SH_PURCHASE  | PA_LINED     | 親ライン           | （なし） |
| SH_PURCHASE  | PA_LINENM    | 親ライン名         | （なし） |
| SH_PURCHASE  | PA_PROCESS   | 親工程             | （なし） |
| SH_PURCHASE  | PA_SECT      | 親ライン担当部門   | （なし） |
| SH_PURCHASE  | PA_SECTNM    | 親ライン担当部門名 | （なし） |
| SH_PURCHASE  | PA_VENDOR    | 親仕入先           | （なし） |
| SH_PURCHASE  | PROCESS      | 工程               | （なし） |
| SH_PURCHASE  | PUORDERNO    | 発注番号           | （なし） |
| SH_PURCHASE  | STLOC        | 保管場所           | （なし） |
| SH_PURCHASE  | TERMINAL     | 端末ID             | （なし） |
| SH_PURCHASE  | TRANSACTOR   | 取引先             | （なし） |
| SH_PURCHASE  | TRANSACTORNM | 取引先名           | （なし） |
| SH_PURCHASE  | VENDOR       | 仕入先             | （なし） |

## テーブル: SH_PURCHPLAN

| テーブル名   | 列ID         | 列名           | 備考                               |
|:-------------|:-------------|:---------------|:-----------------------------------|
| SH_PURCHPLAN | ADR          | 住所           | （なし）                           |
| SH_PURCHPLAN | ADR2         | 住所2          | （なし）                           |
| SH_PURCHPLAN | DELIDATE     | 指示日         | （なし）                           |
| SH_PURCHPLAN | DRWNO        | 部品番号       | （なし）                           |
| SH_PURCHPLAN | IMNM         | 品名           | （なし）                           |
| SH_PURCHPLAN | ITEM         | 品目           | （なし）                           |
| SH_PURCHPLAN | OFFCLF       | 確定/内示Ｆ    | 0;内示;1;確定                      |
| SH_PURCHPLAN | ORDERQTY     | オーダ数       | （なし）                           |
| SH_PURCHPLAN | POSTCD       | 郵便番号       | （なし）                           |
| SH_PURCHPLAN | PROCESS      | 工程           | （なし）                           |
| SH_PURCHPLAN | PUORDERNO    | 発注番号       | （なし）                           |
| SH_PURCHPLAN | SUM_FLG      | 集計F          | 0;確定明細;1;過去発注残;2;未来集計 |
| SH_PURCHPLAN | T_ADR        | 取引先住所     | （なし）                           |
| SH_PURCHPLAN | T_ADR2       | 取引先住所2    | （なし）                           |
| SH_PURCHPLAN | T_POSTCD     | 取引先郵便番号 | （なし）                           |
| SH_PURCHPLAN | TERMINAL     | 端末ID         | （なし）                           |
| SH_PURCHPLAN | TRANSACTOR   | 取引先         | （なし）                           |
| SH_PURCHPLAN | TRANSACTORNM | 取引先名       | （なし）                           |
| SH_PURCHPLAN | VENDOR       | 仕入先         | （なし）                           |

## テーブル: SH_RECEIVECHKPLAN

| テーブル名        | 列ID         | 列名       | 備考     |
|:------------------|:-------------|:-----------|:---------|
| SH_RECEIVECHKPLAN | DELIDATE     | 指示日     | （なし） |
| SH_RECEIVECHKPLAN | DRWNO        | 部品番号   | （なし） |
| SH_RECEIVECHKPLAN | IMNM         | 品名       | （なし） |
| SH_RECEIVECHKPLAN | ITEM         | 品目       | （なし） |
| SH_RECEIVECHKPLAN | OFFCLF       | 確定/内示F | （なし） |
| SH_RECEIVECHKPLAN | ORDERNO      | 発注番号   | （なし） |
| SH_RECEIVECHKPLAN | ORDERQTY     | オーダ数   | （なし） |
| SH_RECEIVECHKPLAN | PROCESS      | 工程       | （なし） |
| SH_RECEIVECHKPLAN | TERMINAL     | 端末ID     | （なし） |
| SH_RECEIVECHKPLAN | TRANSACTOR   | 取引先     | （なし） |
| SH_RECEIVECHKPLAN | TRANSACTORNM | 取引先名   | （なし） |
| SH_RECEIVECHKPLAN | VENDOR       | 仕入先     | （なし） |

## テーブル: SH_SHIPINST

| テーブル名   | 列ID         | 列名                 | 備考           |
|:-------------|:-------------|:---------------------|:---------------|
| SH_SHIPINST  | A_FGROUP     | 商品分類             | （なし）       |
| SH_SHIPINST  | A_SHIPSECT   | 出荷担当部門         | （なし）       |
| SH_SHIPINST  | A_STATUS     | 生試区分             | （なし）       |
| SH_SHIPINST  | CASECD       | 容器                 | （なし）       |
| SH_SHIPINST  | CASENM       | 容器名称             | （なし）       |
| SH_SHIPINST  | CLLCTYPE     | 集荷タイプ           | （なし）       |
| SH_SHIPINST  | CLLCTYPENM   | 集荷タイプ名         | （なし）       |
| SH_SHIPINST  | CUSTOM       | 顧客                 | （なし）       |
| SH_SHIPINST  | CUSTOMNO     | 顧客注番             | （なし）       |
| SH_SHIPINST  | DELIDATE     | 顧客納期             | （なし）       |
| SH_SHIPINST  | DELITIME     | 納入時間(時)         | （なし）       |
| SH_SHIPINST  | DLVLT        | 納入L/T（日）        | （なし）       |
| SH_SHIPINST  | DRWNO        | 部品番号             | （なし）       |
| SH_SHIPINST  | IMNM         | 品名                 | （なし）       |
| SH_SHIPINST  | ITEM         | 品目                 | （なし）       |
| SH_SHIPINST  | LOCT         | 納入プラットフォーム | （なし）       |
| SH_SHIPINST  | LOCTNM       | 場所名               | （なし）       |
| SH_SHIPINST  | ORDERQTY     | 受注数               | （なし）       |
| SH_SHIPINST  | PROCESS      | 工程                 | （なし）       |
| SH_SHIPINST  | RCORDERNO    | 受注No               | （なし）       |
| SH_SHIPINST  | SCHCOMPDATE  | 出荷予定日           | （なし）       |
| SH_SHIPINST  | SECTNM       | 部門名               | 出荷担当部門名 |
| SH_SHIPINST  | TERMINAL     | 端末ID               | （なし）       |
| SH_SHIPINST  | TRANSACTORNM | 取引先名             | （なし）       |
| SH_SHIPINST  | VENDOR       | 仕入先               | 「NONE」に固定 |

## テーブル: SH_SHIPPLAN

| テーブル名   | 列ID         | 列名                 | 備考                               |
|:-------------|:-------------|:---------------------|:-----------------------------------|
| SH_SHIPPLAN  | AM_FLG       | 午前午後F            | 0;AM;1;PM                          |
| SH_SHIPPLAN  | CLNDDATE     | 日付                 | （なし）                           |
| SH_SHIPPLAN  | CUSTOM       | 顧客                 | （なし）                           |
| SH_SHIPPLAN  | DELITIME     | 納入時間(時)         | （なし）                           |
| SH_SHIPPLAN  | DRWNO        | 部品番号             | （なし）                           |
| SH_SHIPPLAN  | IMNM         | 品名                 | （なし）                           |
| SH_SHIPPLAN  | ITEM         | 品目                 | （なし）                           |
| SH_SHIPPLAN  | LOCT         | 納入プラットフォーム | （なし）                           |
| SH_SHIPPLAN  | LOCTNM       | 場所名               | （なし）                           |
| SH_SHIPPLAN  | OFFCLF       | 確定/内示Ｆ          | （なし）                           |
| SH_SHIPPLAN  | ORDERQTY     | 受注数               | （なし）                           |
| SH_SHIPPLAN  | PROCESS      | 工程                 | （なし）                           |
| SH_SHIPPLAN  | RCORDERNO    | 受注No               | （なし）                           |
| SH_SHIPPLAN  | SCHCOMPDATE  | 出荷予定日           | （なし）                           |
| SH_SHIPPLAN  | SUM_FLG      | 集計F                | 0;確定明細;1;過去発注残;2;未来集計 |
| SH_SHIPPLAN  | TERMINAL     | 端末ID               | （なし）                           |
| SH_SHIPPLAN  | TRANSACTORNM | 取引先名             | （なし）                           |
| SH_SHIPPLAN  | VENDOR       | 仕入先               | 「NONE」に固定                     |

## テーブル: SH_SUBCONT

| テーブル名   | 列ID         | 列名               | 備考     |
|:-------------|:-------------|:-------------------|:---------|
| SH_SUBCONT   | A_ITMSTATUS  | ステータス         | （なし） |
| SH_SUBCONT   | DELIDATE     | 指示日             | （なし） |
| SH_SUBCONT   | DRWNO        | 部品番号           | （なし） |
| SH_SUBCONT   | IMNM         | 品名               | （なし） |
| SH_SUBCONT   | ITEM         | 品目               | （なし） |
| SH_SUBCONT   | LOCTNM       | 場所名             | （なし） |
| SH_SUBCONT   | ORDERQTY     | オーダ数           | （なし） |
| SH_SUBCONT   | PA_DRWNO     | 親部品番号         | （なし） |
| SH_SUBCONT   | PA_ITEM      | 親品目             | （なし） |
| SH_SUBCONT   | PA_LINED     | 親ライン           | （なし） |
| SH_SUBCONT   | PA_LINENM    | 親ライン名         | （なし） |
| SH_SUBCONT   | PA_PROCESS   | 親工程             | （なし） |
| SH_SUBCONT   | PA_SECT      | 親ライン担当部門   | （なし） |
| SH_SUBCONT   | PA_SECTNM    | 親ライン担当部門名 | （なし） |
| SH_SUBCONT   | PA_VENDOR    | 親仕入先           | （なし） |
| SH_SUBCONT   | PROCESS      | 工程               | （なし） |
| SH_SUBCONT   | SBORDERNO    | 発注番号           | （なし） |
| SH_SUBCONT   | STLOC        | 保管場所           | （なし） |
| SH_SUBCONT   | TERMINAL     | 端末ID             | （なし） |
| SH_SUBCONT   | TRANSACTOR   | 取引先             | （なし） |
| SH_SUBCONT   | TRANSACTORNM | 取引先名           | （なし） |
| SH_SUBCONT   | VENDOR       | 仕入先             | （なし） |

## テーブル: SH_SUBCONTPLAN

| テーブル名     | 列ID         | 列名           | 備考                               |
|:---------------|:-------------|:---------------|:-----------------------------------|
| SH_SUBCONTPLAN | ADR          | 住所           | （なし）                           |
| SH_SUBCONTPLAN | ADR2         | 住所2          | （なし）                           |
| SH_SUBCONTPLAN | DELIDATE     | 指示日         | （なし）                           |
| SH_SUBCONTPLAN | DRWNO        | 部品番号       | （なし）                           |
| SH_SUBCONTPLAN | IMNM         | 品名           | （なし）                           |
| SH_SUBCONTPLAN | ITEM         | 品目           | （なし）                           |
| SH_SUBCONTPLAN | ORDERQTY     | オーダ数       | （なし）                           |
| SH_SUBCONTPLAN | POSTCD       | 郵便番号       | （なし）                           |
| SH_SUBCONTPLAN | PROCESS      | 工程           | （なし）                           |
| SH_SUBCONTPLAN | SBORDERNO    | オーダNo       | （なし）                           |
| SH_SUBCONTPLAN | SUM_FLG      | 集計F          | 0;確定明細;1;過去発注残;2;未来集計 |
| SH_SUBCONTPLAN | T_ADR        | 取引先住所     | （なし）                           |
| SH_SUBCONTPLAN | T_ADR2       | 取引先住所2    | （なし）                           |
| SH_SUBCONTPLAN | T_POSTCD     | 取引先郵便番号 | （なし）                           |
| SH_SUBCONTPLAN | TERMINAL     | 端末ID         | （なし）                           |
| SH_SUBCONTPLAN | TRANSACTOR   | 取引先         | （なし）                           |
| SH_SUBCONTPLAN | TRANSACTORNM | 取引先名       | （なし）                           |
| SH_SUBCONTPLAN | VENDOR       | 仕入先         | （なし）                           |

## テーブル: SH_VENDOREVALUE

| テーブル名      | 列ID          | 列名         | 備考                                                     |
|:----------------|:--------------|:-------------|:---------------------------------------------------------|
| SH_VENDOREVALUE | DEFECT_FT     | 年間不適合数 | （なし）                                                 |
| SH_VENDOREVALUE | DEFECT1       | 1月不適合数  | 当該取引先・年の仕損数または返品数（1月発生）            |
| SH_VENDOREVALUE | DEFECT10      | 10月不適合数 | 当該取引先・年の仕損数または返品数（10月発生）           |
| SH_VENDOREVALUE | DEFECT11      | 11月不適合数 | 当該取引先・年の仕損数または返品数（11月発生）           |
| SH_VENDOREVALUE | DEFECT12      | 12月不適合数 | 当該取引先・年の仕損数または返品数（12月発生）           |
| SH_VENDOREVALUE | DEFECT2       | 2月不適合数  | 当該取引先・年の仕損数または返品数（2月発生）            |
| SH_VENDOREVALUE | DEFECT3       | 3月不適合数  | 当該取引先・年の仕損数または返品数（3月発生）            |
| SH_VENDOREVALUE | DEFECT4       | 4月不適合数  | 当該取引先・年の仕損数または返品数（4月発生）            |
| SH_VENDOREVALUE | DEFECT5       | 5月不適合数  | 当該取引先・年の仕損数または返品数（5月発生）            |
| SH_VENDOREVALUE | DEFECT6       | 6月不適合数  | 当該取引先・年の仕損数または返品数（6月発生）            |
| SH_VENDOREVALUE | DEFECT7       | 7月不適合数  | 当該取引先・年の仕損数または返品数（7月発生）            |
| SH_VENDOREVALUE | DEFECT8       | 8月不適合数  | 当該取引先・年の仕損数または返品数（8発生）              |
| SH_VENDOREVALUE | DEFECT9       | 9月不適合数  | 当該取引先・年の仕損数または返品数（9月発生）            |
| SH_VENDOREVALUE | DELAYCOUNT_FT | 年間遅延件数 | （なし）                                                 |
| SH_VENDOREVALUE | DELAYCOUNT1   | 1月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対1月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT10  | 10月遅延件数 | 当該取引先・年の購入品・外注品納期遅延件数（対10月納期） |
| SH_VENDOREVALUE | DELAYCOUNT11  | 11月遅延件数 | 当該取引先・年の購入品・外注品納期遅延件数（対11月納期） |
| SH_VENDOREVALUE | DELAYCOUNT12  | 12月遅延件数 | 当該取引先・年の購入品・外注品納期遅延件数（対12月納期） |
| SH_VENDOREVALUE | DELAYCOUNT2   | 2月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対2月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT3   | 3月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対2月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT4   | 4月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対4月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT5   | 5月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対5月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT6   | 6月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対6月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT7   | 7月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対7月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT8   | 8月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対8月納期）  |
| SH_VENDOREVALUE | DELAYCOUNT9   | 9月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対9月納期）  |
| SH_VENDOREVALUE | EVAL_YEAR     | 年           | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT_FT    | 年間発生率   | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT1      | 1月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT10     | 10月発生率   | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT11     | 11月発生率   | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT12     | 12月発生率   | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT2      | 2月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT3      | 3月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT4      | 4月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT5      | 5月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT6      | 6月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT7      | 7月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT8      | 8月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATECNT9      | 9月発生率    | （なし）                                                 |
| SH_VENDOREVALUE | RATEQTY_FT    | 年間発生率   | （なし）                                                 |
| SH_VENDOREVALUE | RATEQTY1      | 1月発生率    | 1月不適合数÷1月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY10     | 10月発生率   | 10月不適合数÷10月受入数×100(%)                           |
| SH_VENDOREVALUE | RATEQTY11     | 11月発生率   | 11月不適合数÷11月受入数×100(%)                           |
| SH_VENDOREVALUE | RATEQTY12     | 12月発生率   | 12月不適合数÷12月受入数×100(%)                           |
| SH_VENDOREVALUE | RATEQTY2      | 2月発生率    | 2月不適合数÷2月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY3      | 3月発生率    | 3月不適合数÷3月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY4      | 4月発生率    | 4月不適合数÷4月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY5      | 5月発生率    | 5月不適合数÷5月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY6      | 6月発生率    | 6月不適合数÷6月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY7      | 7月発生率    | 7月不適合数÷7月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY8      | 8月発生率    | 8月不適合数÷8月受入数×100(%)                             |
| SH_VENDOREVALUE | RATEQTY9      | 9月発生率    | 9月不適合数÷9月受入数×100(%)                             |
| SH_VENDOREVALUE | RCVCOUNT_FT   | 年間受入件数 | （なし）                                                 |
| SH_VENDOREVALUE | RCVCOUNT1     | 1月受入件数  | 当該取引先・年の購入品・外注品発注件数（1月納期）        |
| SH_VENDOREVALUE | RCVCOUNT10    | 10月受入件数 | 当該取引先・年の購入品・外注品発注件数（10月納期）       |
| SH_VENDOREVALUE | RCVCOUNT11    | 11月受入件数 | 当該取引先・年の購入品・外注品発注件数（11月納期）       |
| SH_VENDOREVALUE | RCVCOUNT12    | 12月受入件数 | 当該取引先・年の購入品・外注品発注件数（12月納期）       |
| SH_VENDOREVALUE | RCVCOUNT2     | 2月受入件数  | 当該取引先・年の購入品・外注品発注件数（2月納期）        |
| SH_VENDOREVALUE | RCVCOUNT3     | 3月受入件数  | 当該取引先・年の購入品・外注品発注件数（3月納期）        |
| SH_VENDOREVALUE | RCVCOUNT4     | 4月受入件数  | 当該取引先・年の購入品・外注品発注件数（4月納期）        |
| SH_VENDOREVALUE | RCVCOUNT5     | 5月受入件数  | 当該取引先・年の購入品・外注品発注件数（5月納期）        |
| SH_VENDOREVALUE | RCVCOUNT6     | 6月受入件数  | 当該取引先・年の購入品・外注品発注件数（6月納期）        |
| SH_VENDOREVALUE | RCVCOUNT7     | 7月受入件数  | 当該取引先・年の購入品・外注品発注件数（7月納期）        |
| SH_VENDOREVALUE | RCVCOUNT8     | 8月受入件数  | 当該取引先・年の購入品・外注品発注件数（8月納期）        |
| SH_VENDOREVALUE | RCVCOUNT9     | 9月受入件数  | 当該取引先・年の購入品・外注品発注件数（9月納期）        |
| SH_VENDOREVALUE | RECEIVE_FT    | 年間受入数   | （なし）                                                 |
| SH_VENDOREVALUE | RECEIVE1      | 1月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（1月受入）  |
| SH_VENDOREVALUE | RECEIVE10     | 10月受入件数 | 当該取引先・年の購入品・外注品・支給品受入数（10月受入） |
| SH_VENDOREVALUE | RECEIVE11     | 11月受入件数 | 当該取引先・年の購入品・外注品・支給品受入数（11月受入） |
| SH_VENDOREVALUE | RECEIVE12     | 12月受入件数 | 当該取引先・年の購入品・外注品・支給品受入数（12月受入） |
| SH_VENDOREVALUE | RECEIVE2      | 2月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（2月受入）  |
| SH_VENDOREVALUE | RECEIVE3      | 3月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（3月受入）  |
| SH_VENDOREVALUE | RECEIVE4      | 4月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（4月受入）  |
| SH_VENDOREVALUE | RECEIVE5      | 5月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（5月受入）  |
| SH_VENDOREVALUE | RECEIVE6      | 6月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（6月受入）  |
| SH_VENDOREVALUE | RECEIVE7      | 7月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（7月受入）  |
| SH_VENDOREVALUE | RECEIVE8      | 8月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（8月受入）  |
| SH_VENDOREVALUE | RECEIVE9      | 9月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（9月受入）  |
| SH_VENDOREVALUE | TERMINAL      | 端末ID       | （なし）                                                 |
| SH_VENDOREVALUE | TRANSACTOR    | 取引先       | （なし）                                                 |
| SH_VENDOREVALUE | TRANSACTORNM  | 取引先名     | （なし）                                                 |

## テーブル: STOCK_INVSTOCK_TXT_EXP

| テーブル名             | 列ID      | 列名       | 備考     |
|:-----------------------|:----------|:-----------|:---------|
| STOCK_INVSTOCK_TXT_EXP | FILE_NAME | ファイル名 | （なし） |
| STOCK_INVSTOCK_TXT_EXP | INV_DATE  | 棚卸日     | （なし） |
| STOCK_INVSTOCK_TXT_EXP | LOCT      | 場所       | （なし） |

## テーブル: STOCK_INVSTOCK_TXT_IMP

| テーブル名             | 列ID      | 列名       | 備考     |
|:-----------------------|:----------|:-----------|:---------|
| STOCK_INVSTOCK_TXT_IMP | FILE_NAME | ファイル名 | （なし） |

## テーブル: STOCK_REALCAL_DATA

| テーブル名         | 列ID    | 列名          | 備考                       |
|:-------------------|:--------|:--------------|:---------------------------|
| STOCK_REALCAL_DATA | CLNM_NM | 画面表示列名  | （なし）                   |
| STOCK_REALCAL_DATA | IMTYP   | 製品区分      | 0;製造品､1;購入品､2;外注品 |
| STOCK_REALCAL_DATA | ITEM    | 品目          | （なし）                   |
| STOCK_REALCAL_DATA | KEY_NO  | 画面表示列    | （なし）                   |
| STOCK_REALCAL_DATA | LEVELD  | レベル        | （なし）                   |
| STOCK_REALCAL_DATA | PRLT    | 自工程L/T(日) | （なし）                   |
| STOCK_REALCAL_DATA | PROCESS | 工程          | （なし）                   |
| STOCK_REALCAL_DATA | VENDOR  | 仕入先        | （なし）                   |

## テーブル: S_ACTSTOCK

| テーブル名   | 列ID        | 列名             | 備考     |
|:-------------|:------------|:-----------------|:---------|
| S_ACTSTOCK   | ACTSTOCK    | 実際在庫数       | （なし） |
| S_ACTSTOCK   | ALLOCQTY    | 完成品引当在庫数 | （なし） |
| S_ACTSTOCK   | CALCDATE    | 計算日           | （なし） |
| S_ACTSTOCK   | COST        | 標準原価         | （なし） |
| S_ACTSTOCK   | EFCTSTOCK   | 有効在庫数       | （なし） |
| S_ACTSTOCK   | ESTISSUEQTY | 消費予定数       | （なし） |
| S_ACTSTOCK   | ESTMRCVQTY  | 入庫予定数       | （なし） |
| S_ACTSTOCK   | ITEM        | 品目             | （なし） |
| S_ACTSTOCK   | PROCESS     | 工程             | （なし） |
| S_ACTSTOCK   | RGSTD       | 登録日           | （なし） |
| S_ACTSTOCK   | SINVCOST    | 標準在庫費       | （なし） |
| S_ACTSTOCK   | UPDTD       | 更新日           | （なし） |
| S_ACTSTOCK   | UPDTWKCD    | 更新担当者       | （なし） |
| S_ACTSTOCK   | VENDOR      | 仕入先           | （なし） |
| S_ACTSTOCK   | WHSTOCK     | 倉庫在庫数       | （なし） |

## テーブル: S_ACTSTOCKFLUCTU

| テーブル名       | 列ID        | 列名       | 備考     |
|:-----------------|:------------|:-----------|:---------|
| S_ACTSTOCKFLUCTU | ACCOUNTDATE | 計算日     | （なし） |
| S_ACTSTOCKFLUCTU | CMPQTY      | 生産数     | （なし） |
| S_ACTSTOCKFLUCTU | CONSUMP     | 消費数     | （なし） |
| S_ACTSTOCKFLUCTU | DATED       | 変動日     | （なし） |
| S_ACTSTOCKFLUCTU | INVDATE     | 棚卸日     | （なし） |
| S_ACTSTOCKFLUCTU | INVQTY      | 棚卸数     | （なし） |
| S_ACTSTOCKFLUCTU | ISSUEQTY    | 出庫数     | （なし） |
| S_ACTSTOCKFLUCTU | ITEM        | 品目       | （なし） |
| S_ACTSTOCKFLUCTU | PROCESS     | 工程       | （なし） |
| S_ACTSTOCKFLUCTU | RECEIVEQTY  | 入庫数     | （なし） |
| S_ACTSTOCKFLUCTU | RGSTD       | 登録日     | （なし） |
| S_ACTSTOCKFLUCTU | STOCK       | 在庫数     | （なし） |
| S_ACTSTOCKFLUCTU | UPDTD       | 更新日     | （なし） |
| S_ACTSTOCKFLUCTU | UPDTWKCD    | 更新担当者 | （なし） |
| S_ACTSTOCKFLUCTU | VENDOR      | 仕入先     | （なし） |

## テーブル: S_ACTSTOCKFLUCTU_A

| テーブル名         | 列ID        | 列名       | 備考     |
|:-------------------|:------------|:-----------|:---------|
| S_ACTSTOCKFLUCTU_A | ACCOUNTDATE | 計算日     | （なし） |
| S_ACTSTOCKFLUCTU_A | CMPQTY      | 生産数     | （なし） |
| S_ACTSTOCKFLUCTU_A | CONSUMP     | 消費数     | （なし） |
| S_ACTSTOCKFLUCTU_A | DATED       | 変動日     | （なし） |
| S_ACTSTOCKFLUCTU_A | INVDATE     | 棚卸日     | （なし） |
| S_ACTSTOCKFLUCTU_A | INVQTY      | 棚卸数     | （なし） |
| S_ACTSTOCKFLUCTU_A | ISSUEQTY    | 出庫数     | （なし） |
| S_ACTSTOCKFLUCTU_A | ITEM        | 品目       | （なし） |
| S_ACTSTOCKFLUCTU_A | PROCESS     | 工程       | （なし） |
| S_ACTSTOCKFLUCTU_A | RECEIVEQTY  | 入庫数     | （なし） |
| S_ACTSTOCKFLUCTU_A | RGSTD       | 登録日     | （なし） |
| S_ACTSTOCKFLUCTU_A | STOCK       | 在庫数     | （なし） |
| S_ACTSTOCKFLUCTU_A | UPDTD       | 更新日     | （なし） |
| S_ACTSTOCKFLUCTU_A | UPDTWKCD    | 更新担当者 | （なし） |
| S_ACTSTOCKFLUCTU_A | VENDOR      | 仕入先     | （なし） |

## テーブル: S_ACTSTOCKFLUCTU_LOCT

| テーブル名            | 列ID       | 列名   | 備考     |
|:----------------------|:-----------|:-------|:---------|
| S_ACTSTOCKFLUCTU_LOCT | CMPQTY     | 生産数 | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | CONSUMP    | 消費数 | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | DATED      | 変動日 | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | ISSUEQTY   | 出庫数 | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | ITEM       | 品目   | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | LOCT       | 場所   | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | PROCESS    | 工程   | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | RECEIVEQTY | 入庫数 | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | STOCK      | 在庫数 | （なし） |
| S_ACTSTOCKFLUCTU_LOCT | VENDOR     | 仕入先 | （なし） |

## テーブル: S_ACTSTOCK_A

| テーブル名   | 列ID        | 列名             | 備考     |
|:-------------|:------------|:-----------------|:---------|
| S_ACTSTOCK_A | ACTSTOCK    | 実際在庫数       | （なし） |
| S_ACTSTOCK_A | ALLOCQTY    | 完成品引当在庫数 | （なし） |
| S_ACTSTOCK_A | CALCDATE    | 計算日           | （なし） |
| S_ACTSTOCK_A | COST        | 標準原価         | （なし） |
| S_ACTSTOCK_A | EFCTSTOCK   | 有効在庫数       | （なし） |
| S_ACTSTOCK_A | ESTISSUEQTY | 消費予定数       | （なし） |
| S_ACTSTOCK_A | ESTMRCVQTY  | 入庫予定数       | （なし） |
| S_ACTSTOCK_A | ITEM        | 品目             | （なし） |
| S_ACTSTOCK_A | PROCESS     | 工程             | （なし） |
| S_ACTSTOCK_A | RGSTD       | 登録日           | （なし） |
| S_ACTSTOCK_A | SINVCOST    | 標準在庫費       | （なし） |
| S_ACTSTOCK_A | UPDTD       | 更新日           | （なし） |
| S_ACTSTOCK_A | UPDTWKCD    | 更新担当者       | （なし） |
| S_ACTSTOCK_A | VENDOR      | 仕入先           | （なし） |
| S_ACTSTOCK_A | WHSTOCK     | 倉庫在庫数       | （なし） |

## テーブル: S_ACTSTOCK_LOCT

| テーブル名      | 列ID      | 列名       | 備考     |
|:----------------|:----------|:-----------|:---------|
| S_ACTSTOCK_LOCT | ACTSTOCK  | 実際在庫数 | （なし） |
| S_ACTSTOCK_LOCT | CALCDATE  | 計算日     | （なし） |
| S_ACTSTOCK_LOCT | DIFFER    | 差         | （なし） |
| S_ACTSTOCK_LOCT | INVDATE   | 棚卸日     | （なし） |
| S_ACTSTOCK_LOCT | INVQTY    | 棚卸数     | （なし） |
| S_ACTSTOCK_LOCT | ITEM      | 品目       | （なし） |
| S_ACTSTOCK_LOCT | LOCT      | 場所       | （なし） |
| S_ACTSTOCK_LOCT | PROCESS   | 工程       | （なし） |
| S_ACTSTOCK_LOCT | RGSTD     | 登録日     | （なし） |
| S_ACTSTOCK_LOCT | SHPMNTQTY | 出荷数     | （なし） |
| S_ACTSTOCK_LOCT | UPDTWKCD  | 更新担当者 | （なし） |
| S_ACTSTOCK_LOCT | VENDOR    | 仕入先     | （なし） |

## テーブル: S_BATCH_ENTRY

| テーブル名    | 列ID       | 列名           | 備考                                                                                                                                                       |
|:--------------|:-----------|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| S_BATCH_ENTRY | COUNTER    | 内部登録No     | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | DRWNO      | 部品番号       | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | ENTRY_DEF  | エントリー区分 | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | ERRMSG     | 登録エラー     | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | FORCE_F    | 強制F          | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | IMTYP      | 製品区分       | 0;製造品1;購入品2;外注品                                                                                                                                   |
| S_BATCH_ENTRY | ISSUEFLG   | データ区分     | 0;製造品オーダーより;1;購入品オーダーより;2;外注品オーダーより;3;外注支給（在庫移動）;4;受注出荷;10;製造品消費品目;12;外注品消費品目;19;例外入出庫消費品目 |
| S_BATCH_ENTRY | ISSUEQTY   | 出庫数         | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | ITEM       | 品目           | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | LINED      | ライン         | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | LOCT       | 入出庫場所     | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | ORDERNO    | オーダNo       | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | PROCESS    | 工程           | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | RCISCD     | 入出庫区分     | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | RCISDATE   | 入出庫日       | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | RCISF      | 入庫・出庫区分 | 0;入庫;1;出庫                                                                                                                                              |
| S_BATCH_ENTRY | RCISQTY    | 入出庫数       | 非表示項目（入庫数を正、出庫数を負で保存）                                                                                                                 |
| S_BATCH_ENTRY | RCISTIME   | 入出庫時間     | 非表示                                                                                                                                                     |
| S_BATCH_ENTRY | RECEIVEQTY | 入庫数         | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | RGSTD      | 登録日         | YYYY/MM/DD HH;MM;SS                                                                                                                                        |
| S_BATCH_ENTRY | RGSTTM     | 登録時刻       | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | SUB_NO     | 件数           | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | TERMINAL   | 端末情報       | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | TRANSACTOR | 取引先         | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | UPDTD      | 更新日         | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | UPDTWKCD   | 更新担当者     | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | VENDOR     | 仕入先         | （なし）                                                                                                                                                   |
| S_BATCH_ENTRY | WORKERCD   | 担当者         | （なし）                                                                                                                                                   |

## テーブル: S_BOOKSTOCK

| テーブル名   | 列ID        | 列名       | 備考     |
|:-------------|:------------|:-----------|:---------|
| S_BOOKSTOCK  | ACCOUNTDATE | 在庫計算日 | （なし） |
| S_BOOKSTOCK  | INVQTY      | 在庫数     | （なし） |
| S_BOOKSTOCK  | ITEM        | 品目       | （なし） |
| S_BOOKSTOCK  | LOCT        | 場所       | （なし） |
| S_BOOKSTOCK  | PROCESS     | 工程       | （なし） |
| S_BOOKSTOCK  | RGSTD       | 登録日     | （なし） |
| S_BOOKSTOCK  | UPDTD       | 更新日     | （なし） |
| S_BOOKSTOCK  | UPDTWKCD    | 更新担当者 | （なし） |
| S_BOOKSTOCK  | VENDOR      | 仕入先     | （なし） |

## テーブル: S_CONSUME_CHK

| テーブル名    | 列ID       | 列名             | 備考            |
|:--------------|:-----------|:-----------------|:----------------|
| S_CONSUME_CHK | ACTFNDATE  | 生産日           | （なし）        |
| S_CONSUME_CHK | CMPFLG     | 完了Ｆ           | 0;未完了;1;完了 |
| S_CONSUME_CHK | CMPQTY     | 完成数           | （なし）        |
| S_CONSUME_CHK | CONSUMEQTY | 子品目消費数     | （なし）        |
| S_CONSUME_CHK | COUNTER    | 内部番号         | （なし）        |
| S_CONSUME_CHK | HCOUNTER   | 親内部登録No     | （なし）        |
| S_CONSUME_CHK | HITEM      | 親品目           | （なし）        |
| S_CONSUME_CHK | HPROCESS   | 親工程           | （なし）        |
| S_CONSUME_CHK | HVENDOR    | 親仕入先         | （なし）        |
| S_CONSUME_CHK | ISSUEQTY   | 子品目出庫予定数 | （なし）        |
| S_CONSUME_CHK | LITEM      | 子品目           | （なし）        |
| S_CONSUME_CHK | LPROCESS   | 子工程           | （なし）        |
| S_CONSUME_CHK | LVENDOR    | 子仕入先         | （なし）        |
| S_CONSUME_CHK | ORDERNO    | オーダNo         | （なし）        |
| S_CONSUME_CHK | PHUNIT     | 員数             | （なし）        |
| S_CONSUME_CHK | SGFLAG     | 実績             | （なし）        |

## テーブル: S_CREDITDIF

| テーブル名   | 列ID        | 列名       | 備考     |
|:-------------|:------------|:-----------|:---------|
| S_CREDITDIF  | AMTMNY      | 金額       | （なし） |
| S_CREDITDIF  | CCNO        | 請求連番   | （なし） |
| S_CREDITDIF  | CLAIMNO     | 請求No     | （なし） |
| S_CREDITDIF  | CLMCD       | 請求先     | （なし） |
| S_CREDITDIF  | CUSTOMNO    | 顧客注番   | （なし） |
| S_CREDITDIF  | DIFCOMMENT  | 差異内容   | （なし） |
| S_CREDITDIF  | ITEM        | 品目       | （なし） |
| S_CREDITDIF  | LOCT        | 場所       | （なし） |
| S_CREDITDIF  | PROCESS     | 工程       | （なし） |
| S_CREDITDIF  | RCORDERNO   | 受注No     | （なし） |
| S_CREDITDIF  | RCVDAMTMNY  | 納入金額   | （なし） |
| S_CREDITDIF  | RCVDSHIPQTY | 支払案内数 | （なし） |
| S_CREDITDIF  | RCVDUNTPRC  | 納入単価   | （なし） |
| S_CREDITDIF  | SHIPQTY     | 出荷数     | （なし） |
| S_CREDITDIF  | SHPMNTD     | 出荷日     | （なし） |
| S_CREDITDIF  | UNTPRC      | 単価       | （なし） |
| S_CREDITDIF  | VENDOR      | 仕入先     | （なし） |

## テーブル: S_DEFECT

| テーブル名   | 列ID            | 列名                 | 備考                                                         |
|:-------------|:----------------|:---------------------|:-------------------------------------------------------------|
| S_DEFECT     | A_FPTYPE        | 購入区分             | R：固定自給 Y：有償支給 N：無償支給　G：変動自給             |
| S_DEFECT     | ASSYNO          | Assy子部品№          | 0:本体、1-9:Assy子部品                                       |
| S_DEFECT     | BACOFALOF       | 責任区分             | （なし）                                                     |
| S_DEFECT     | COMPENSF        | 補填要否             | 0;不要;1;要                                                  |
| S_DEFECT     | COMPENSLSTF     | 補填リスト出力日     | （なし）                                                     |
| S_DEFECT     | COUNTER         | 内部登録No           | （なし）                                                     |
| S_DEFECT     | CUST_ISSUENO    | 得意先伝票No         | （なし）                                                     |
| S_DEFECT     | DEFECT_F        | 仕損返品F            | （なし）                                                     |
| S_DEFECT     | DEFECT_PRNDATE1 | 仕損伝票印刷日付     | （なし）                                                     |
| S_DEFECT     | DEFECT_PRNDATE2 | 返品伝票印刷日付     | （なし）                                                     |
| S_DEFECT     | DEFECT_PRNDATE3 | 自給伝票印刷日付     | （なし）                                                     |
| S_DEFECT     | DEFECT_PRNDATE4 | 支給伝票印刷日付     | （なし）                                                     |
| S_DEFECT     | DEFECT_PRNDATE5 | 無償支給伝票印刷日付 | （なし）                                                     |
| S_DEFECT     | DEFECT_PRNF1    | 仕損伝票印刷F        | 0;未発行;1;発行済、2:組付け印刷済み                          |
| S_DEFECT     | DEFECT_PRNF2    | 返品伝票印刷F        | 0;未発行;1;発行済、2:組付け印刷済み                          |
| S_DEFECT     | DEFECT_PRNF3    | 自給伝票印刷F        | 0;未発行;1;発行済、2:組付け印刷済み                          |
| S_DEFECT     | DEFECT_PRNF4    | 支給伝票印刷F        | 0;未発行;1;発行済、2:組付け印刷済み                          |
| S_DEFECT     | DEFECT_PRNF5    | 無償支給伝票印刷F    | 0;未発行;1;発行済、2:組付け印刷済み                          |
| S_DEFECT     | DEL_F           | 廃棄F                | 0;未廃棄;1;破棄済                                            |
| S_DEFECT     | DITEM           | 入力品目             | （なし）                                                     |
| S_DEFECT     | DPROCESS        | 入力工程             | （なし）                                                     |
| S_DEFECT     | EDIT_CHK        | 選択                 | （なし）                                                     |
| S_DEFECT     | FCDTY           | 理由タイプ           | （なし）                                                     |
| S_DEFECT     | FCODE           | 理由コード           | （なし）                                                     |
| S_DEFECT     | FIND_SECT       | 発生部門             | （なし）                                                     |
| S_DEFECT     | HAPPENDATE      | 発生日               | （なし）                                                     |
| S_DEFECT     | HIMTYP          | 親製品区分           | 0;製造品1;購入品2;外注品                                     |
| S_DEFECT     | HITEM           | 親品目               | （なし）                                                     |
| S_DEFECT     | HPROCESS        | 親工程               | （なし）                                                     |
| S_DEFECT     | IMTYP           | 製品区分             | 0;製造品1;購入品2;外注品                                     |
| S_DEFECT     | ISSUEFLG        | データ区分           | 0;生産指示ｵｰﾀﾞより1;外注品ｵｰﾀﾞより;2;受注出荷時、倉庫出庫    |
| S_DEFECT     | ISSUENO         | 伝票No               | （なし）                                                     |
| S_DEFECT     | ISSUEQTY        | 出庫数               | （なし）                                                     |
| S_DEFECT     | ITEM            | 品目                 | （なし）                                                     |
| S_DEFECT     | LOCT            | 場所                 | （なし）                                                     |
| S_DEFECT     | MEMO            | メモ欄               | 仕損返品承認処理にて、S_DEFECT_INPUT_TABLET.MEMOをセットする |
| S_DEFECT     | OCASIONFLG      | 発生部署区分         | （なし）                                                     |
| S_DEFECT     | ORDERNO         | オーダNo             | （なし）                                                     |
| S_DEFECT     | PROC_CHARGE     | 単価                 | （なし）                                                     |
| S_DEFECT     | PROCESS         | 工程                 | （なし）                                                     |
| S_DEFECT     | RCISCD          | 入出庫区分           | （なし）                                                     |
| S_DEFECT     | RCISDATE        | 入出庫日             | （なし）                                                     |
| S_DEFECT     | RCISF           | 入庫・出庫区分       | 0;入庫;1;出庫                                                |
| S_DEFECT     | RCISQTY         | 入出庫数             | （なし）                                                     |
| S_DEFECT     | RCISTIME        | 入出庫時間           | （なし）                                                     |
| S_DEFECT     | RECEIPT_DATE    | 受領日               | （なし）                                                     |
| S_DEFECT     | RECEIVEQTY      | 入庫数               | （なし）                                                     |
| S_DEFECT     | REMARK          | 備考                 | （なし）                                                     |
| S_DEFECT     | RESP_SECT       | 責任部門             | （なし）                                                     |
| S_DEFECT     | RGSTD           | 登録日               | （なし）                                                     |
| S_DEFECT     | RGSTTM          | 登録時刻             | （なし）                                                     |
| S_DEFECT     | RSPNSBLF        | 発生責任             | （なし）                                                     |
| S_DEFECT     | SECT            | 担当部門             | （なし）                                                     |
| S_DEFECT     | SLIPF           | 伝票発行済F          | 0;未発行;1;発行済                                            |
| S_DEFECT     | SUBCONTRACT     | 外注先               | （なし）                                                     |
| S_DEFECT     | TERMID          | 端末ID               | （なし）                                                     |
| S_DEFECT     | TERMINAL        | 端末情報             | （なし）                                                     |
| S_DEFECT     | TRANSACTOR      | 取引先               | （なし）                                                     |
| S_DEFECT     | UPDTD           | 更新日               | （なし）                                                     |
| S_DEFECT     | UPDTWKCD        | 更新担当者           | （なし）                                                     |
| S_DEFECT     | VENDOR          | 仕入先               | （なし）                                                     |
| S_DEFECT     | WKRATE          | 進度(%)              | （なし）                                                     |
| S_DEFECT     | WORKERCD        | 担当者               | （なし）                                                     |

## テーブル: S_DEFECTNO

| テーブル名   | 列ID     | 列名           | 備考     |
|:-------------|:---------|:---------------|:---------|
| S_DEFECTNO   | K_NO     | キー項目       | （なし） |
| S_DEFECTNO   | LAST_OD1 | 最終内部登録No | （なし） |
| S_DEFECTNO   | NEXT_OD1 | 次回内部登録No | （なし） |

## テーブル: S_DEFECTNO_TABLET

| テーブル名        | 列ID     | 列名           | 備考     |
|:------------------|:---------|:---------------|:---------|
| S_DEFECTNO_TABLET | K_NO     | キー項目       | （なし） |
| S_DEFECTNO_TABLET | LAST_OD1 | 最終内部登録No | （なし） |
| S_DEFECTNO_TABLET | NEXT_OD1 | 次回内部登録No | （なし） |

## テーブル: S_DEFECT_INPUT

| テーブル名     | 列ID         | 列名              | 備考                   |
|:---------------|:-------------|:------------------|:-----------------------|
| S_DEFECT_INPUT | A_ITEM1      | 組立済部品1品目   | （なし）               |
| S_DEFECT_INPUT | A_ITEM2      | 組立済部品2品目   | （なし）               |
| S_DEFECT_INPUT | A_ITEM3      | 組立済部品3品目   | （なし）               |
| S_DEFECT_INPUT | A_ITEM4      | 組立済部品4品目   | （なし）               |
| S_DEFECT_INPUT | A_PROCESS1   | 組立済部品1工程   | （なし）               |
| S_DEFECT_INPUT | A_PROCESS2   | 組立済部品2工程   | （なし）               |
| S_DEFECT_INPUT | A_PROCESS3   | 組立済部品3工程   | （なし）               |
| S_DEFECT_INPUT | A_PROCESS4   | 組立済部品4工程   | （なし）               |
| S_DEFECT_INPUT | A_QTY1       | 組立済部品1仕損数 | （なし）               |
| S_DEFECT_INPUT | A_QTY2       | 組立済部品2仕損数 | （なし）               |
| S_DEFECT_INPUT | A_QTY3       | 組立済部品3仕損数 | （なし）               |
| S_DEFECT_INPUT | A_QTY4       | 組立済部品4仕損数 | （なし）               |
| S_DEFECT_INPUT | A_VENDOR     | 発注先            | 購入品、外注品の発注先 |
| S_DEFECT_INPUT | A_VENDOR_RTN | 責任部署          | （なし）               |
| S_DEFECT_INPUT | A_VENDOR1    | 組立済部品1仕入先 | （なし）               |
| S_DEFECT_INPUT | A_VENDOR2    | 組立済部品2仕入先 | （なし）               |
| S_DEFECT_INPUT | A_VENDOR3    | 組立済部品3仕入先 | （なし）               |
| S_DEFECT_INPUT | A_VENDOR4    | 組立済部品4仕入先 | （なし）               |
| S_DEFECT_INPUT | COUNTER      | 内部登録No        | （なし）               |
| S_DEFECT_INPUT | DEFECT_F     | 仕損返品F         | （なし）               |
| S_DEFECT_INPUT | DEFECTQTY    | 返品数            | （なし）               |
| S_DEFECT_INPUT | ERRMSG       | 登録エラー        | （なし）               |
| S_DEFECT_INPUT | FCDTY        | 理由タイプ        | （なし）               |
| S_DEFECT_INPUT | FCODE        | 理由コード        | （なし）               |
| S_DEFECT_INPUT | HAPPENDATE   | 発生日            | （なし）               |
| S_DEFECT_INPUT | ISSUENO      | 伝票No            | （なし）               |
| S_DEFECT_INPUT | ITEM         | 品目              | （なし）               |
| S_DEFECT_INPUT | OCASIONFLG   | 発生部署区分      | （なし）               |
| S_DEFECT_INPUT | PROCESS      | 工程              | （なし）               |
| S_DEFECT_INPUT | REMARK       | 備考              | （なし）               |
| S_DEFECT_INPUT | RGSTD        | 登録日            | （なし）               |
| S_DEFECT_INPUT | RGSTTM       | 登録時刻          | （なし）               |
| S_DEFECT_INPUT | TERMINAL     | 端末情報          | （なし）               |
| S_DEFECT_INPUT | VENDOR       | 仕入先            | （なし）               |
| S_DEFECT_INPUT | WKRATE       | 進度(%)           | （なし）               |
| S_DEFECT_INPUT | WORKERCD     | 担当者            | （なし）               |

## テーブル: S_DEFECT_INPUT_DETAIL_TABLET

| テーブル名                   | 列ID      | 列名             | 備考     |
|:-----------------------------|:----------|:-----------------|:---------|
| S_DEFECT_INPUT_DETAIL_TABLET | A_ITEM    | 組立済部品品目   | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | A_PROCESS | 組立済部品工程   | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | A_QTY     | 組立済部品仕損数 | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | A_VENDOR  | 組立済部品仕入先 | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | COUNTER   | 内部登録No       | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | REMARK    | 備考             | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | RGSTD     | 登録日           | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | RGSTTM    | 登録時刻         | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | SUB_NO    | 件数             | （なし） |
| S_DEFECT_INPUT_DETAIL_TABLET | WORKERCD  | 担当者           | （なし） |

## テーブル: S_DEFECT_INPUT_TABLET

| テーブル名            | 列ID         | 列名         | 備考                                   |
|:----------------------|:-------------|:-------------|:---------------------------------------|
| S_DEFECT_INPUT_TABLET | A_VENDOR     | 発注先       | 購入品、外注品の発注先                 |
| S_DEFECT_INPUT_TABLET | A_VENDOR_RTN | 責任部署     | （なし）                               |
| S_DEFECT_INPUT_TABLET | ACTSTDATE    | 生産日       | （なし）                               |
| S_DEFECT_INPUT_TABLET | COUNTER      | 内部登録No   | （なし）                               |
| S_DEFECT_INPUT_TABLET | DEFECT_F     | 仕損返品F    | '0;仕損;1;返品                         |
| S_DEFECT_INPUT_TABLET | DEFECTQTY    | 返品数       | （なし）                               |
| S_DEFECT_INPUT_TABLET | ERRMSG       | 登録エラー   | （なし）                               |
| S_DEFECT_INPUT_TABLET | FCDTY        | 理由タイプ   | （なし）                               |
| S_DEFECT_INPUT_TABLET | FCODE        | 理由コード   | （なし）                               |
| S_DEFECT_INPUT_TABLET | FIX_FLG      | 承認F        | （なし）                               |
| S_DEFECT_INPUT_TABLET | HAPPENDATE   | 発生日       | （なし）                               |
| S_DEFECT_INPUT_TABLET | ISSUENO      | 伝票No       | （なし）                               |
| S_DEFECT_INPUT_TABLET | ITEM         | 品目         | （なし）                               |
| S_DEFECT_INPUT_TABLET | MEMO         | メモ欄       | （なし）                               |
| S_DEFECT_INPUT_TABLET | NNL_FLG      | NNL区分      | 0：既存TABLET、1:設備連動TABLET        |
| S_DEFECT_INPUT_TABLET | OCASIONFLG   | 発生部署区分 | 1;組立;2;検査;3;加工;4;外注;5;受入倉庫 |
| S_DEFECT_INPUT_TABLET | OEE_LINED    | 実績ライン   | （なし）                               |
| S_DEFECT_INPUT_TABLET | PRNFLG       | 印刷完了F    | （なし）                               |
| S_DEFECT_INPUT_TABLET | PROCESS      | 工程         | （なし）                               |
| S_DEFECT_INPUT_TABLET | REMARK       | 備考         | （なし）                               |
| S_DEFECT_INPUT_TABLET | RGSTD        | 登録日       | （なし）                               |
| S_DEFECT_INPUT_TABLET | RGSTTM       | 登録時刻     | （なし）                               |
| S_DEFECT_INPUT_TABLET | SHIFTF       | 直区分       | 1;1直;2;2直;3;3直                      |
| S_DEFECT_INPUT_TABLET | TERMINAL     | 端末情報     | （なし）                               |
| S_DEFECT_INPUT_TABLET | UPDTD        | 更新日       | （なし）                               |
| S_DEFECT_INPUT_TABLET | UPDTFLG      | 更新F        | （なし）                               |
| S_DEFECT_INPUT_TABLET | UPDTWKCD     | 更新担当者   | （なし）                               |
| S_DEFECT_INPUT_TABLET | VENDOR       | 仕入先       | （なし）                               |
| S_DEFECT_INPUT_TABLET | WKRATE       | 進度(%)      | （なし）                               |
| S_DEFECT_INPUT_TABLET | WORKERCD     | 担当者       | （なし）                               |

## テーブル: S_DEFECT_RCNO

| テーブル名    | 列ID     | 列名           | 備考     |
|:--------------|:---------|:---------------|:---------|
| S_DEFECT_RCNO | K_NO     | キー項目       | （なし） |
| S_DEFECT_RCNO | LAST_OD1 | 最終内部登録No | （なし） |
| S_DEFECT_RCNO | NEXT_OD1 | 次回内部登録No | （なし） |

## テーブル: S_DEFECT_RCNO_TABLET

| テーブル名           | 列ID     | 列名           | 備考     |
|:---------------------|:---------|:---------------|:---------|
| S_DEFECT_RCNO_TABLET | K_NO     | キー項目       | （なし） |
| S_DEFECT_RCNO_TABLET | LAST_OD1 | 最終内部登録No | （なし） |
| S_DEFECT_RCNO_TABLET | NEXT_OD1 | 次回内部登録No | （なし） |

## テーブル: S_DELAYEVALUE

| テーブル名    | 列ID          | 列名         | 備考                                                     |
|:--------------|:--------------|:-------------|:---------------------------------------------------------|
| S_DELAYEVALUE | DELAYCOUNT_FT | 年間遅延件数 | （なし）                                                 |
| S_DELAYEVALUE | DELAYCOUNT1   | 1月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対1月納期）  |
| S_DELAYEVALUE | DELAYCOUNT10  | 10月遅延件数 | 当該取引先・年の購入品・外注品納期遅延件数（対10月納期） |
| S_DELAYEVALUE | DELAYCOUNT11  | 11月遅延件数 | 当該取引先・年の購入品・外注品納期遅延件数（対11月納期） |
| S_DELAYEVALUE | DELAYCOUNT12  | 12月遅延件数 | 当該取引先・年の購入品・外注品納期遅延件数（対12月納期） |
| S_DELAYEVALUE | DELAYCOUNT2   | 2月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対2月納期）  |
| S_DELAYEVALUE | DELAYCOUNT3   | 3月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対2月納期）  |
| S_DELAYEVALUE | DELAYCOUNT4   | 4月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対4月納期）  |
| S_DELAYEVALUE | DELAYCOUNT5   | 5月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対5月納期）  |
| S_DELAYEVALUE | DELAYCOUNT6   | 6月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対6月納期）  |
| S_DELAYEVALUE | DELAYCOUNT7   | 7月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対7月納期）  |
| S_DELAYEVALUE | DELAYCOUNT8   | 8月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対8月納期）  |
| S_DELAYEVALUE | DELAYCOUNT9   | 9月遅延件数  | 当該取引先・年の購入品・外注品納期遅延件数（対9月納期）  |
| S_DELAYEVALUE | EVAL_YEAR     | 評価年度     | （なし）                                                 |
| S_DELAYEVALUE | RATE_FT       | 年間発生率   | （なし）                                                 |
| S_DELAYEVALUE | RATE1         | 1月発生率    | 1月遅延件数÷1月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE10        | 10月発生率   | 10月遅延件数÷10月納期件数×100(%)                         |
| S_DELAYEVALUE | RATE11        | 11月発生率   | 11月遅延件数÷11月納期件数×100(%)                         |
| S_DELAYEVALUE | RATE12        | 12月発生率   | 12月遅延件数÷12月納期件数×100(%)                         |
| S_DELAYEVALUE | RATE2         | 2月発生率    | 2月遅延件数÷2月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE3         | 3月発生率    | 3月遅延件数÷3月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE4         | 4月発生率    | 4月遅延件数÷4月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE5         | 5月発生率    | 5月遅延件数÷5月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE6         | 6月発生率    | 6月遅延件数÷6月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE7         | 7月発生率    | 7月遅延件数÷7月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE8         | 8月発生率    | 8月遅延件数÷8月納期件数×100(%)                           |
| S_DELAYEVALUE | RATE9         | 9月発生率    | 9月遅延件数÷9月納期件数×100(%)                           |
| S_DELAYEVALUE | RCVCOUNT_FT   | 年間受入件数 | （なし）                                                 |
| S_DELAYEVALUE | RCVCOUNT1     | 1月受入件数  | 当該取引先・年の購入品・外注品発注件数（1月納期）        |
| S_DELAYEVALUE | RCVCOUNT10    | 10月受入件数 | 当該取引先・年の購入品・外注品発注件数（10月納期）       |
| S_DELAYEVALUE | RCVCOUNT11    | 11月受入件数 | 当該取引先・年の購入品・外注品発注件数（11月納期）       |
| S_DELAYEVALUE | RCVCOUNT12    | 12月受入件数 | 当該取引先・年の購入品・外注品発注件数（12月納期）       |
| S_DELAYEVALUE | RCVCOUNT2     | 2月受入件数  | 当該取引先・年の購入品・外注品発注件数（2月納期）        |
| S_DELAYEVALUE | RCVCOUNT3     | 3月受入件数  | 当該取引先・年の購入品・外注品発注件数（3月納期）        |
| S_DELAYEVALUE | RCVCOUNT4     | 4月受入件数  | 当該取引先・年の購入品・外注品発注件数（4月納期）        |
| S_DELAYEVALUE | RCVCOUNT5     | 5月受入件数  | 当該取引先・年の購入品・外注品発注件数（5月納期）        |
| S_DELAYEVALUE | RCVCOUNT6     | 6月受入件数  | 当該取引先・年の購入品・外注品発注件数（6月納期）        |
| S_DELAYEVALUE | RCVCOUNT7     | 7月受入件数  | 当該取引先・年の購入品・外注品発注件数（7月納期）        |
| S_DELAYEVALUE | RCVCOUNT8     | 8月受入件数  | 当該取引先・年の購入品・外注品発注件数（8月納期）        |
| S_DELAYEVALUE | RCVCOUNT9     | 9月受入件数  | 当該取引先・年の購入品・外注品発注件数（9月納期）        |
| S_DELAYEVALUE | RGSTD         | 登録日       | （なし）                                                 |
| S_DELAYEVALUE | TRANSACTOR    | 取引先       | （なし）                                                 |
| S_DELAYEVALUE | UPDTD         | 更新日       | （なし）                                                 |
| S_DELAYEVALUE | UPDTWKCD      | 更新担当者   | （なし）                                                 |

## テーブル: S_GROSSSTOCK

| テーブル名   | 列ID     | 列名           | 備考     |
|:-------------|:---------|:---------------|:---------|
| S_GROSSSTOCK | COST     | 実際単価       | （なし） |
| S_GROSSSTOCK | GRSQTY   | グロス在庫数   | （なし） |
| S_GROSSSTOCK | INVDATE  | 棚卸日         | （なし） |
| S_GROSSSTOCK | INVQTY   | 棚卸在庫数     | （なし） |
| S_GROSSSTOCK | ITEM     | 品目           | （なし） |
| S_GROSSSTOCK | PROCESS  | 工程           | （なし） |
| S_GROSSSTOCK | RGSTD    | 登録日         | （なし） |
| S_GROSSSTOCK | SINVCOST | グロス在庫金額 | （なし） |
| S_GROSSSTOCK | UPDTD    | 更新日         | （なし） |
| S_GROSSSTOCK | UPDTWKCD | 更新担当者     | （なし） |
| S_GROSSSTOCK | VENDOR   | 仕入先         | （なし） |

## テーブル: S_GROSSSTOCK_MONTH

| テーブル名         | 列ID      | 列名           | 備考     |
|:-------------------|:----------|:---------------|:---------|
| S_GROSSSTOCK_MONTH | COST      | 実際単価       | （なし） |
| S_GROSSSTOCK_MONTH | GRSQTY    | グロス在庫数   | （なし） |
| S_GROSSSTOCK_MONTH | INVDATE   | 月末日         | （なし） |
| S_GROSSSTOCK_MONTH | INVQTY    | 月次在庫数     | （なし） |
| S_GROSSSTOCK_MONTH | ITEM      | 品目           | （なし） |
| S_GROSSSTOCK_MONTH | PROCESS   | 工程           | （なし） |
| S_GROSSSTOCK_MONTH | RGSTD     | 登録日         | （なし） |
| S_GROSSSTOCK_MONTH | SINVCOST  | グロス在庫金額 | （なし） |
| S_GROSSSTOCK_MONTH | UPDTD     | 更新日         | （なし） |
| S_GROSSSTOCK_MONTH | UPDTWKCD  | 更新担当者     | （なし） |
| S_GROSSSTOCK_MONTH | VENDOR    | 仕入先         | （なし） |
| S_GROSSSTOCK_MONTH | YEARMONTH | 年月度         | （なし） |

## テーブル: S_INVENTORYPRICE

| テーブル名       | 列ID         | 列名         | 備考            |
|:-----------------|:-------------|:-------------|:----------------|
| S_INVENTORYPRICE | A_FMCUS      | 代表得意先   | （なし）        |
| S_INVENTORYPRICE | A_FPCLASS    | クラス       | （なし）        |
| S_INVENTORYPRICE | ACT_AMOUNT   | 実際在庫金額 | （なし）        |
| S_INVENTORYPRICE | ACT_PS_TTL   | 実際積上合計 | （なし）        |
| S_INVENTORYPRICE | CLASSNM      | クラス名     | （なし）        |
| S_INVENTORYPRICE | DRWNO        | 部品番号     | （なし）        |
| S_INVENTORYPRICE | ITEM         | 品目         | （なし）        |
| S_INVENTORYPRICE | LOCT         | 入出庫場所   | （なし）        |
| S_INVENTORYPRICE | PROCESS      | 工程         | （なし）        |
| S_INVENTORYPRICE | QTY          | 棚卸在庫数   | （なし）        |
| S_INVENTORYPRICE | STD_AMOUNT   | 標準在庫金額 | （なし）        |
| S_INVENTORYPRICE | STD_PS_TTL   | 標準積上合計 | （なし）        |
| S_INVENTORYPRICE | TRANSACTORNM | 取引先名     | 0;顧客;1;仕入先 |
| S_INVENTORYPRICE | VENDOR       | 仕入先       | （なし）        |
| S_INVENTORYPRICE | YEARMONTH    | 年月度       | （なし）        |

## テーブル: S_INVFLUCTU

| テーブル名   | 列ID        | 列名       | 備考     |
|:-------------|:------------|:-----------|:---------|
| S_INVFLUCTU  | ACCOUNTDATE | 計算日     | （なし） |
| S_INVFLUCTU  | CMPQTY      | 生産数     | （なし） |
| S_INVFLUCTU  | CONSUMP     | 消費数     | （なし） |
| S_INVFLUCTU  | DATED       | 変動日     | （なし） |
| S_INVFLUCTU  | INVDATE     | 棚卸日     | （なし） |
| S_INVFLUCTU  | INVQTY      | 棚卸数     | （なし） |
| S_INVFLUCTU  | ISSUEQTY    | 出庫数     | （なし） |
| S_INVFLUCTU  | ITEM        | 品目       | （なし） |
| S_INVFLUCTU  | PROCESS     | 工程       | （なし） |
| S_INVFLUCTU  | RECEIVEQTY  | 入庫数     | （なし） |
| S_INVFLUCTU  | RGSTD       | 登録日     | （なし） |
| S_INVFLUCTU  | STOCK       | 在庫数     | （なし） |
| S_INVFLUCTU  | UPDTD       | 更新日     | （なし） |
| S_INVFLUCTU  | UPDTWKCD    | 更新担当者 | （なし） |
| S_INVFLUCTU  | VENDOR      | 仕入先     | （なし） |

## テーブル: S_INVMVRESULT

| テーブル名    | 列ID         | 列名              | 備考                                                                                                                                                       |
|:--------------|:-------------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| S_INVMVRESULT | AODEN_FLG    | 青伝区分          | （なし）                                                                                                                                                   |
| S_INVMVRESULT | CMPFLG       | 完了Ｆ            | 0;未完了;1;完了                                                                                                                                            |
| S_INVMVRESULT | COMPENSF     | 補填要否          | 0;不要;1;要                                                                                                                                                |
| S_INVMVRESULT | COST         | 単価              | （なし）                                                                                                                                                   |
| S_INVMVRESULT | COUNTER      | 内部登録No        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | HCOUNTER     | 親内部登録No      | （なし）                                                                                                                                                   |
| S_INVMVRESULT | IMTYP        | 製品区分          | 0;製造品1;購入品2;外注品                                                                                                                                   |
| S_INVMVRESULT | IMTYP2       | 製品区分          | 0;製造品1;購入品2;外注品                                                                                                                                   |
| S_INVMVRESULT | INPUTLOTNO   | 投入ロット        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | ISO_PRNT_F   | ISO移動票印刷F    | 0;未完了;1;完了                                                                                                                                            |
| S_INVMVRESULT | ISSORDERNO   | 出庫元オーダNo    | S*****;生産指示オーダ;G*****;外注品オーダ;J*****;受注オーダ                                                                                                |
| S_INVMVRESULT | ISSUEFLG     | データ区分        | 0;製造品オーダーより;1;購入品オーダーより;2;外注品オーダーより;3;外注支給（在庫移動）;4;受注出荷;10;製造品消費品目;12;外注品消費品目;19;例外入出庫消費品目 |
| S_INVMVRESULT | ISSUEFLG_G   | データ区分G       | （なし）                                                                                                                                                   |
| S_INVMVRESULT | ISSUEQTY     | 出庫数            | （なし）                                                                                                                                                   |
| S_INVMVRESULT | ITEM         | 品目              | （なし）                                                                                                                                                   |
| S_INVMVRESULT | ITEM_T       | 移動先品目        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | LOCT         | 入出庫場所        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | LOCT2        | 入出庫場所        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | ORDERNO      | オーダNo          | （なし）                                                                                                                                                   |
| S_INVMVRESULT | PRNT_F       | 支給伝票印刷F     | 0;未完了;1;完了                                                                                                                                            |
| S_INVMVRESULT | PRNT_REF_F   | 支給伝票印刷参照F | 0;印刷対象外;1;印刷対象                                                                                                                                    |
| S_INVMVRESULT | PRNTDATE     | 印刷日付          | （なし）                                                                                                                                                   |
| S_INVMVRESULT | PROCESS      | 工程              | （なし）                                                                                                                                                   |
| S_INVMVRESULT | PROCESS_T    | 移動先工程        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | RCISCD       | 入出庫区分        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | RCISCD2      | 入出庫区分        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | RCISDATE     | 入出庫日          | （なし）                                                                                                                                                   |
| S_INVMVRESULT | RCISF        | 入庫・出庫区分    | 0;入庫;1;出庫                                                                                                                                              |
| S_INVMVRESULT | RCISQTY      | 入出庫数          | 非表示項目（入庫数を正、出庫数を負で保存）                                                                                                                 |
| S_INVMVRESULT | RCISTIME     | 入出庫時間        | 非表示                                                                                                                                                     |
| S_INVMVRESULT | RECEIVEQTY   | 入庫数            | （なし）                                                                                                                                                   |
| S_INVMVRESULT | REMARK       | 備考              | （なし）                                                                                                                                                   |
| S_INVMVRESULT | RESULT_REG_F | 実績登録済みF     | （なし）                                                                                                                                                   |
| S_INVMVRESULT | RGSTD        | 登録日            | YYYY/MM/DD HH;MM;SS                                                                                                                                        |
| S_INVMVRESULT | RGSTTM       | 登録時刻          | （なし）                                                                                                                                                   |
| S_INVMVRESULT | SUBCONTRACT  | 外注先            | （なし）                                                                                                                                                   |
| S_INVMVRESULT | TANKA_FLG    | 単価決定区分      | （なし）                                                                                                                                                   |
| S_INVMVRESULT | TERMID       | 端末ID            | （なし）                                                                                                                                                   |
| S_INVMVRESULT | TRANSACTOR   | 入出庫取引先      | （なし）                                                                                                                                                   |
| S_INVMVRESULT | UPDTD        | 更新日            | （なし）                                                                                                                                                   |
| S_INVMVRESULT | UPDTWKCD     | 更新担当者        | （なし）                                                                                                                                                   |
| S_INVMVRESULT | VENDOR       | 仕入先            | （なし）                                                                                                                                                   |
| S_INVMVRESULT | VENDOR_T     | 移動先仕入先      | （なし）                                                                                                                                                   |
| S_INVMVRESULT | VENDOR2      | 外注ｺｰﾄﾞ          | （なし）                                                                                                                                                   |
| S_INVMVRESULT | WKRATE       | 進度(%)           | （なし）                                                                                                                                                   |
| S_INVMVRESULT | WORKERCD     | 担当者            | （なし）                                                                                                                                                   |

## テーブル: S_INVMVRESULT_TMP

| テーブル名        | 列ID         | 列名              | 備考                                                                                             |
|:------------------|:-------------|:------------------|:-------------------------------------------------------------------------------------------------|
| S_INVMVRESULT_TMP | COMPENSF     | 補填要否          | 0;不要;1;要                                                                                      |
| S_INVMVRESULT_TMP | COST         | 単価              | （なし）                                                                                         |
| S_INVMVRESULT_TMP | COUNTER      | 内部登録No        | （なし）                                                                                         |
| S_INVMVRESULT_TMP | IMTYP        | 製品区分          | 0;製造品1;購入品2;外注品                                                                         |
| S_INVMVRESULT_TMP | ISO_PRNT_F   | ISO移動票印刷F    | 0;未完了;1;完了                                                                                  |
| S_INVMVRESULT_TMP | ISSORDERNO   | 出庫元オーダNo    | S*****;生産指示オーダ;G*****;外注品オーダ;J*****;受注オーダ                                      |
| S_INVMVRESULT_TMP | ISSUEFLG     | 出庫区分          | 0;製造品オーダーより;1;購入品オーダーより;2;外注品オーダーより;3;外注支給（在庫移動）;4;受注出荷 |
| S_INVMVRESULT_TMP | ISSUEQTY     | 出庫数            | （なし）                                                                                         |
| S_INVMVRESULT_TMP | ITEM         | 品目              | （なし）                                                                                         |
| S_INVMVRESULT_TMP | LOCT         | 入出庫場所        | （なし）                                                                                         |
| S_INVMVRESULT_TMP | LOCT2        | 入出庫場所        | （なし）                                                                                         |
| S_INVMVRESULT_TMP | ORDERNO      | オーダNo          | （なし）                                                                                         |
| S_INVMVRESULT_TMP | PRNT_F       | 支給伝票印刷F     | 0;未完了;1;完了                                                                                  |
| S_INVMVRESULT_TMP | PRNT_REF_F   | 支給伝票印刷参照F | 0;印刷対象外;1;印刷対象                                                                          |
| S_INVMVRESULT_TMP | PRNTDATE     | 印刷日付          | （なし）                                                                                         |
| S_INVMVRESULT_TMP | PROCESS      | 工程              | （なし）                                                                                         |
| S_INVMVRESULT_TMP | RCISCD       | 入出庫区分        | （なし）                                                                                         |
| S_INVMVRESULT_TMP | RCISCD2      | 入出庫区分        | （なし）                                                                                         |
| S_INVMVRESULT_TMP | RCISDATE     | 入出庫日          | （なし）                                                                                         |
| S_INVMVRESULT_TMP | RCISF        | 入庫・出庫区分    | 0;入庫;1;出庫                                                                                    |
| S_INVMVRESULT_TMP | RCISQTY      | 入出庫数          | 非表示項目（入庫数を正、出庫数を負で保存）                                                       |
| S_INVMVRESULT_TMP | RCISTIME     | 入出庫時間        | 非表示                                                                                           |
| S_INVMVRESULT_TMP | RECEIVEQTY   | 入庫数            | （なし）                                                                                         |
| S_INVMVRESULT_TMP | REMARK       | 備考              | （なし）                                                                                         |
| S_INVMVRESULT_TMP | RESULT_REG_F | 実績登録済みF     | （なし）                                                                                         |
| S_INVMVRESULT_TMP | RGSTD        | 登録日            | YYYY/MM/DD HH;MM;SS                                                                              |
| S_INVMVRESULT_TMP | RGSTTM       | 登録時刻          | （なし）                                                                                         |
| S_INVMVRESULT_TMP | SUBCONTRACT  | 外注先            | （なし）                                                                                         |
| S_INVMVRESULT_TMP | TERMID       | 端末ID            | （なし）                                                                                         |
| S_INVMVRESULT_TMP | TRANSACTOR   | 入出庫取引先      | （なし）                                                                                         |
| S_INVMVRESULT_TMP | UPDTD        | 更新日            | （なし）                                                                                         |
| S_INVMVRESULT_TMP | UPDTWKCD     | 更新担当者        | （なし）                                                                                         |
| S_INVMVRESULT_TMP | VENDOR       | 仕入先            | （なし）                                                                                         |
| S_INVMVRESULT_TMP | VENDOR2      | 外注ｺｰﾄﾞ          | （なし）                                                                                         |
| S_INVMVRESULT_TMP | WORKERCD     | 担当者            | （なし）                                                                                         |

## テーブル: S_INVSTOCK

| テーブル名   | 列ID          | 列名               | 備考     |
|:-------------|:--------------|:-------------------|:---------|
| S_INVSTOCK   | ACCOUNTDATE   | 在庫計算日         | （なし） |
| S_INVSTOCK   | BOOKINVQTY    | 帳簿在庫数         | （なし） |
| S_INVSTOCK   | COST          | 標準原価           | （なし） |
| S_INVSTOCK   | DIFFQTY       | 差異               | （なし） |
| S_INVSTOCK   | INVDATE       | 棚卸日             | （なし） |
| S_INVSTOCK   | INVQTY        | 棚卸在庫数         | （なし） |
| S_INVSTOCK   | ITEM          | 品目               | （なし） |
| S_INVSTOCK   | LASTBOOKIVQTY | 前回帳簿在庫数     | （なし） |
| S_INVSTOCK   | LASTDIFFQTY   | 前回差異           | （なし） |
| S_INVSTOCK   | LASTISDATE    | 最終出庫日         | （なし） |
| S_INVSTOCK   | LASTIVDATE    | 前回棚卸日         | （なし） |
| S_INVSTOCK   | LASTIVQTY     | 前回棚卸在庫数     | （なし） |
| S_INVSTOCK   | LASTRCDATE    | 最終入庫日         | （なし） |
| S_INVSTOCK   | LASTUPDATE    | 最終入出庫日更新日 | （なし） |
| S_INVSTOCK   | PROCESS       | 工程               | （なし） |
| S_INVSTOCK   | RGSTD         | 登録日             | （なし） |
| S_INVSTOCK   | SINVCOST      | 標準在庫費         | （なし） |
| S_INVSTOCK   | UPDTD         | 更新日             | （なし） |
| S_INVSTOCK   | UPDTWKCD      | 更新担当者         | （なし） |
| S_INVSTOCK   | VENDOR        | 仕入先             | （なし） |

## テーブル: S_INVSTOCK_LOCT

| テーブル名      | 列ID        | 列名                    | 備考     |
|:----------------|:------------|:------------------------|:---------|
| S_INVSTOCK_LOCT | COST        | 標準原価                | （なし） |
| S_INVSTOCK_LOCT | DIFFQTY     | 在庫数差異（棚卸-現在） | （なし） |
| S_INVSTOCK_LOCT | EVALDATE    | 在庫評価日              | （なし） |
| S_INVSTOCK_LOCT | INVDATE     | 棚卸日                  | （なし） |
| S_INVSTOCK_LOCT | INVQTY      | 棚卸在庫数              | （なし） |
| S_INVSTOCK_LOCT | ITEM        | 品目                    | （なし） |
| S_INVSTOCK_LOCT | LASTDIFFQTY | 前回差異                | （なし） |
| S_INVSTOCK_LOCT | LASTISDATE  | 最終出庫日              | （なし） |
| S_INVSTOCK_LOCT | LASTIVDATE  | 前回棚卸日              | （なし） |
| S_INVSTOCK_LOCT | LASTIVQTY   | 前回棚卸在庫数          | （なし） |
| S_INVSTOCK_LOCT | LASTRCDATE  | 最終入庫日              | （なし） |
| S_INVSTOCK_LOCT | LASTUPDATE  | 最終入出庫日更新日      | （なし） |
| S_INVSTOCK_LOCT | LOCT        | 場所                    | （なし） |
| S_INVSTOCK_LOCT | PROCESS     | 工程                    | （なし） |
| S_INVSTOCK_LOCT | RGSTD       | 登録日                  | （なし） |
| S_INVSTOCK_LOCT | SINVCOST    | 標準在庫費              | （なし） |
| S_INVSTOCK_LOCT | UPDTD       | 更新日                  | （なし） |
| S_INVSTOCK_LOCT | UPDTWKCD    | 更新担当者              | （なし） |
| S_INVSTOCK_LOCT | VENDOR      | 仕入先                  | （なし） |

## テーブル: S_INVSTOCK_LOCT_DIF

| テーブル名          | 列ID         | 列名                      | 備考     |
|:--------------------|:-------------|:--------------------------|:---------|
| S_INVSTOCK_LOCT_DIF | ACCOUNTDATE  | 棚卸月月末日              | （なし） |
| S_INVSTOCK_LOCT_DIF | BOOKSTOCK_A  | 月末在庫                  | （なし） |
| S_INVSTOCK_LOCT_DIF | BOOKSTOCK_B  | 月末理論                  | （なし） |
| S_INVSTOCK_LOCT_DIF | DIFFQTY      | 差異（月末在庫-月末理論） | （なし） |
| S_INVSTOCK_LOCT_DIF | INVDATE      | 今回棚卸日                | （なし） |
| S_INVSTOCK_LOCT_DIF | INVQTY       | 今回棚卸在庫              | （なし） |
| S_INVSTOCK_LOCT_DIF | ITEM         | 品目                      | （なし） |
| S_INVSTOCK_LOCT_DIF | LAST_INVDATE | 前回棚卸日                | （なし） |
| S_INVSTOCK_LOCT_DIF | LAST_INVQTY  | 前回棚卸在庫              | （なし） |
| S_INVSTOCK_LOCT_DIF | LOCT         | 在庫場所                  | （なし） |
| S_INVSTOCK_LOCT_DIF | PROCESS      | 工程                      | （なし） |
| S_INVSTOCK_LOCT_DIF | RGSTD        | 登録日                    | （なし） |
| S_INVSTOCK_LOCT_DIF | UPDTD        | 更新日                    | （なし） |
| S_INVSTOCK_LOCT_DIF | UPDTWKCD     | 更新担当者                | （なし） |
| S_INVSTOCK_LOCT_DIF | VENDOR       | 仕入先                    | （なし） |

## テーブル: S_INVSTOCK_LOCT_TMP

| テーブル名          | 列ID        | 列名           | 備考     |
|:--------------------|:------------|:---------------|:---------|
| S_INVSTOCK_LOCT_TMP | BOOKGROSQTY | 帳簿グロス在庫 | （なし） |
| S_INVSTOCK_LOCT_TMP | BOOKQTY     | 帳簿在庫数     | （なし） |
| S_INVSTOCK_LOCT_TMP | BOOKS1      | 帳簿1          | （なし） |
| S_INVSTOCK_LOCT_TMP | BOOKS2      | 帳簿2          | （なし） |
| S_INVSTOCK_LOCT_TMP | BOOKS3      | 帳簿3          | （なし） |
| S_INVSTOCK_LOCT_TMP | BOOKS4      | 帳簿4          | （なし） |
| S_INVSTOCK_LOCT_TMP | BOOKS5      | 帳簿5          | （なし） |
| S_INVSTOCK_LOCT_TMP | DIFFER1     | 差異1          | （なし） |
| S_INVSTOCK_LOCT_TMP | DIFFER2     | 差異2          | （なし） |
| S_INVSTOCK_LOCT_TMP | DIFFER3     | 差異3          | （なし） |
| S_INVSTOCK_LOCT_TMP | DIFFER4     | 差異4          | （なし） |
| S_INVSTOCK_LOCT_TMP | DIFFER5     | 差異5          | （なし） |
| S_INVSTOCK_LOCT_TMP | GROSQTY     | グロス在庫     | （なし） |
| S_INVSTOCK_LOCT_TMP | INVDATE     | 棚卸日         | （なし） |
| S_INVSTOCK_LOCT_TMP | INVQTY      | 棚卸在庫数     | （なし） |
| S_INVSTOCK_LOCT_TMP | ITEM        | 品目           | （なし） |
| S_INVSTOCK_LOCT_TMP | PLACE1      | 場所1          | （なし） |
| S_INVSTOCK_LOCT_TMP | PLACE2      | 場所2          | （なし） |
| S_INVSTOCK_LOCT_TMP | PLACE3      | 場所3          | （なし） |
| S_INVSTOCK_LOCT_TMP | PLACE4      | 場所4          | （なし） |
| S_INVSTOCK_LOCT_TMP | PLACE5      | 場所5          | （なし） |
| S_INVSTOCK_LOCT_TMP | PROCESS     | 工程           | （なし） |
| S_INVSTOCK_LOCT_TMP | QTYDIFFER   | グロス在庫差異 | （なし） |
| S_INVSTOCK_LOCT_TMP | RGSTD       | 登録日         | （なし） |
| S_INVSTOCK_LOCT_TMP | STOCK1      | 棚番1          | （なし） |
| S_INVSTOCK_LOCT_TMP | STOCK2      | 棚番2          | （なし） |
| S_INVSTOCK_LOCT_TMP | STOCK3      | 棚番3          | （なし） |
| S_INVSTOCK_LOCT_TMP | STOCK4      | 棚番4          | （なし） |
| S_INVSTOCK_LOCT_TMP | STOCK5      | 棚番5          | （なし） |
| S_INVSTOCK_LOCT_TMP | VENDOR      | 仕入先         | （なし） |

## テーブル: S_INVSTOCK_LOCT_TXT

| テーブル名          | 列ID     | 列名           | 備考     |
|:--------------------|:---------|:---------------|:---------|
| S_INVSTOCK_LOCT_TXT | ACTSTOCK | 実際在庫数     | （なし） |
| S_INVSTOCK_LOCT_TXT | DRWNO    | 部品番号       | （なし） |
| S_INVSTOCK_LOCT_TXT | INVDATE  | 棚卸日         | （なし） |
| S_INVSTOCK_LOCT_TXT | INVQTY   | 棚卸在庫数     | （なし） |
| S_INVSTOCK_LOCT_TXT | ITEM     | 品目           | （なし） |
| S_INVSTOCK_LOCT_TXT | LOCT     | 棚卸在庫場所   | （なし） |
| S_INVSTOCK_LOCT_TXT | PROCESS  | 工程           | （なし） |
| S_INVSTOCK_LOCT_TXT | STLOC    | 保管場所       | （なし） |
| S_INVSTOCK_LOCT_TXT | UPDT_F   | 棚卸更新フラグ | （なし） |

## テーブル: S_INVSTOCK_LOCT_TXT_CHK

| テーブル名              | 列ID     | 列名                             | 備考     |
|:------------------------|:---------|:---------------------------------|:---------|
| S_INVSTOCK_LOCT_TXT_CHK | CITEM    | 品目無                           | YES/NO   |
| S_INVSTOCK_LOCT_TXT_CHK | CLOCT    | 棚卸在庫場所無                   | YES/NO   |
| S_INVSTOCK_LOCT_TXT_CHK | INVDATE  | 同一品目が場所違いで棚卸日が違う | YES/NO   |
| S_INVSTOCK_LOCT_TXT_CHK | INVDATE2 | 棚卸日未設定                     | YES/NO   |
| S_INVSTOCK_LOCT_TXT_CHK | ITEM     | 品目                             | （なし） |
| S_INVSTOCK_LOCT_TXT_CHK | LOCT     | 棚卸在庫場所                     | （なし） |
| S_INVSTOCK_LOCT_TXT_CHK | PROCESS  | 工程                             | （なし） |
| S_INVSTOCK_LOCT_TXT_CHK | UPDT_F   | 棚卸更新フラグ未設定             | YES/NO   |
| S_INVSTOCK_LOCT_TXT_CHK | VENDOR   | 仕入先                           | （なし） |

## テーブル: S_INVSTOCK_NOLST

| テーブル名       | 列ID        | 列名     | 備考     |
|:-----------------|:------------|:---------|:---------|
| S_INVSTOCK_NOLST | INVDATE     | 棚卸日   | （なし） |
| S_INVSTOCK_NOLST | INVSTOCK_NO | 棚番     | （なし） |
| S_INVSTOCK_NOLST | ITEM        | 品目     | （なし） |
| S_INVSTOCK_NOLST | LINED       | ライン   | （なし） |
| S_INVSTOCK_NOLST | LOCT        | 場所     | （なし） |
| S_INVSTOCK_NOLST | PROCESS     | 工程     | （なし） |
| S_INVSTOCK_NOLST | SECT        | 担当部門 | （なし） |
| S_INVSTOCK_NOLST | VENDOR      | 仕入先   | （なし） |

## テーブル: S_INVSTOCK_TMP

| テーブル名     | 列ID        | 列名       | 備考     |
|:---------------|:------------|:-----------|:---------|
| S_INVSTOCK_TMP | CARDNO      | 伝票No     | （なし） |
| S_INVSTOCK_TMP | COUNTER     | 内部登録No | （なし） |
| S_INVSTOCK_TMP | DRWNO       | 部品番号   | （なし） |
| S_INVSTOCK_TMP | EREACD      | エリア担当 | （なし） |
| S_INVSTOCK_TMP | IMNM        | 品名       | （なし） |
| S_INVSTOCK_TMP | INVDATE     | 棚卸日     | （なし） |
| S_INVSTOCK_TMP | INVQTY      | 棚卸数     | （なし） |
| S_INVSTOCK_TMP | INVSTOCK_NO | 棚番       | （なし） |
| S_INVSTOCK_TMP | ITEM        | 品目       | （なし） |
| S_INVSTOCK_TMP | PROCESS     | 工程       | （なし） |
| S_INVSTOCK_TMP | RGSTD       | 登録日     | （なし） |
| S_INVSTOCK_TMP | TERMINAL    | 端末情報   | （なし） |
| S_INVSTOCK_TMP | VENDOR      | 仕入先     | （なし） |

## テーブル: S_INVSTOCK_TXT

| テーブル名     | 列ID    | 列名           | 備考     |
|:---------------|:--------|:---------------|:---------|
| S_INVSTOCK_TXT | IMNM    | 品名           | （なし） |
| S_INVSTOCK_TXT | INVDATE | 棚卸日         | （なし） |
| S_INVSTOCK_TXT | INVQTY  | 棚卸在庫数     | （なし） |
| S_INVSTOCK_TXT | ITEM    | 品目           | （なし） |
| S_INVSTOCK_TXT | PROCESS | 工程           | （なし） |
| S_INVSTOCK_TXT | STGSECT | 保管部門       | （なし） |
| S_INVSTOCK_TXT | UPDT_F  | 棚卸更新フラグ | （なし） |
| S_INVSTOCK_TXT | VENDOR  | 仕入先         | （なし） |

## テーブル: S_INVSTOCK_TXT_CHK

| テーブル名         | 列ID    | 列名                 | 備考     |
|:-------------------|:--------|:---------------------|:---------|
| S_INVSTOCK_TXT_CHK | CITEM   | 品目無               | YES/NO   |
| S_INVSTOCK_TXT_CHK | INVDATE | 棚卸日未設定         | YES/NO   |
| S_INVSTOCK_TXT_CHK | ITEM    | 品目                 | （なし） |
| S_INVSTOCK_TXT_CHK | PROCESS | 工程                 | （なし） |
| S_INVSTOCK_TXT_CHK | UPDT_F  | 棚卸更新フラグ未設定 | YES/NO   |
| S_INVSTOCK_TXT_CHK | VENDOR  | 仕入先               | （なし） |

## テーブル: S_ITEM_INVSTOCKNO

| テーブル名        | 列ID    | 列名   | 備考     |
|:------------------|:--------|:-------|:---------|
| S_ITEM_INVSTOCKNO | INVDATE | 棚卸日 | （なし） |
| S_ITEM_INVSTOCKNO | INVNO1  | 棚番   | （なし） |
| S_ITEM_INVSTOCKNO | INVNO2  | 棚番2  | （なし） |
| S_ITEM_INVSTOCKNO | INVNO3  | 棚番3  | （なし） |
| S_ITEM_INVSTOCKNO | INVNO4  | 棚番4  | （なし） |
| S_ITEM_INVSTOCKNO | INVNO5  | 棚番5  | （なし） |
| S_ITEM_INVSTOCKNO | ITEM    | 品目   | （なし） |
| S_ITEM_INVSTOCKNO | PLACE1  | 場所   | （なし） |
| S_ITEM_INVSTOCKNO | PLACE2  | 場所2  | （なし） |
| S_ITEM_INVSTOCKNO | PLACE3  | 場所3  | （なし） |
| S_ITEM_INVSTOCKNO | PLACE4  | 場所4  | （なし） |
| S_ITEM_INVSTOCKNO | PLACE5  | 場所5  | （なし） |
| S_ITEM_INVSTOCKNO | PROCESS | 工程   | （なし） |
| S_ITEM_INVSTOCKNO | VENDOR  | 仕入先 | （なし） |

## テーブル: S_MONTH

| テーブル名   | 列ID      | 列名       | 備考     |
|:-------------|:----------|:-----------|:---------|
| S_MONTH      | DATE1     | 締め日１   | （なし） |
| S_MONTH      | DATE10    | 締め日10   | （なし） |
| S_MONTH      | DATE11    | 締め日11   | （なし） |
| S_MONTH      | DATE12    | 締め日12   | （なし） |
| S_MONTH      | DATE2     | 締め日２   | （なし） |
| S_MONTH      | DATE3     | 締め日３   | （なし） |
| S_MONTH      | DATE4     | 締め日４   | （なし） |
| S_MONTH      | DATE5     | 締め日５   | （なし） |
| S_MONTH      | DATE6     | 締め日６   | （なし） |
| S_MONTH      | DATE7     | 締め日７   | （なし） |
| S_MONTH      | DATE8     | 締め日８   | （なし） |
| S_MONTH      | DATE9     | 締め日９   | （なし） |
| S_MONTH      | INVDATE1  | 棚卸年月１ | （なし） |
| S_MONTH      | INVDATE10 | 棚卸年月10 | （なし） |
| S_MONTH      | INVDATE11 | 棚卸年月11 | （なし） |
| S_MONTH      | INVDATE12 | 棚卸年月12 | （なし） |
| S_MONTH      | INVDATE2  | 棚卸年月２ | （なし） |
| S_MONTH      | INVDATE3  | 棚卸年月３ | （なし） |
| S_MONTH      | INVDATE4  | 棚卸年月４ | （なし） |
| S_MONTH      | INVDATE5  | 棚卸年月５ | （なし） |
| S_MONTH      | INVDATE6  | 棚卸年月６ | （なし） |
| S_MONTH      | INVDATE7  | 棚卸年月７ | （なし） |
| S_MONTH      | INVDATE8  | 棚卸年月８ | （なし） |
| S_MONTH      | INVDATE9  | 棚卸年月９ | （なし） |
| S_MONTH      | ITEM      | 品目       | （なし） |
| S_MONTH      | PROCESS   | 工程       | （なし） |
| S_MONTH      | RGSTD     | 登録日     | （なし） |
| S_MONTH      | STOCK1    | 棚卸在庫１ | （なし） |
| S_MONTH      | STOCK10   | 棚卸在庫10 | （なし） |
| S_MONTH      | STOCK11   | 棚卸在庫11 | （なし） |
| S_MONTH      | STOCK12   | 棚卸在庫12 | （なし） |
| S_MONTH      | STOCK2    | 棚卸在庫２ | （なし） |
| S_MONTH      | STOCK3    | 棚卸在庫３ | （なし） |
| S_MONTH      | STOCK4    | 棚卸在庫４ | （なし） |
| S_MONTH      | STOCK5    | 棚卸在庫５ | （なし） |
| S_MONTH      | STOCK6    | 棚卸在庫６ | （なし） |
| S_MONTH      | STOCK7    | 棚卸在庫７ | （なし） |
| S_MONTH      | STOCK8    | 棚卸在庫８ | （なし） |
| S_MONTH      | STOCK9    | 棚卸在庫９ | （なし） |
| S_MONTH      | UPDTD     | 更新日     | （なし） |
| S_MONTH      | UPDTWKCD  | 更新担当者 | （なし） |
| S_MONTH      | VENDOR    | 仕入先     | （なし） |

## テーブル: S_MONTHSTOCK

| テーブル名   | 列ID        | 列名       | 備考     |
|:-------------|:------------|:-----------|:---------|
| S_MONTHSTOCK | ACCOUNTDATE | 在庫計算日 | （なし） |
| S_MONTHSTOCK | COST        | 標準原価   | （なし） |
| S_MONTHSTOCK | INVQTY      | 棚卸在庫数 | （なし） |
| S_MONTHSTOCK | ITEM        | 品目       | （なし） |
| S_MONTHSTOCK | LOCT        | 場所       | （なし） |
| S_MONTHSTOCK | PROCESS     | 工程       | （なし） |
| S_MONTHSTOCK | RGSTD       | 登録日     | （なし） |
| S_MONTHSTOCK | SINVCOST    | 標準在庫費 | （なし） |
| S_MONTHSTOCK | UPDTD       | 更新日     | （なし） |
| S_MONTHSTOCK | UPDTWKCD    | 更新担当者 | （なし） |
| S_MONTHSTOCK | VENDOR      | 仕入先     | （なし） |
| S_MONTHSTOCK | YEARMONTH   | 年月度     | （なし） |

## テーブル: S_MRPSTOCK

| テーブル名   | 列ID        | 列名             | 備考     |
|:-------------|:------------|:-----------------|:---------|
| S_MRPSTOCK   | ACTSTOCK    | 実際在庫数       | （なし） |
| S_MRPSTOCK   | ALLOCQTY    | 完成品引当在庫数 | （なし） |
| S_MRPSTOCK   | CALCDATE    | 計算日           | （なし） |
| S_MRPSTOCK   | COST        | 標準原価         | （なし） |
| S_MRPSTOCK   | EFCTSTOCK   | 有効在庫数       | （なし） |
| S_MRPSTOCK   | ESTISSUEQTY | 消費予定数       | （なし） |
| S_MRPSTOCK   | ESTMRCVQTY  | 入庫予定数       | （なし） |
| S_MRPSTOCK   | ITEM        | 品目             | （なし） |
| S_MRPSTOCK   | PROCESS     | 工程             | （なし） |
| S_MRPSTOCK   | RGSTD       | 登録日           | （なし） |
| S_MRPSTOCK   | SINVCOST    | 標準在庫費       | （なし） |
| S_MRPSTOCK   | UPDTD       | 更新日           | （なし） |
| S_MRPSTOCK   | UPDTWKCD    | 更新担当者       | （なし） |
| S_MRPSTOCK   | VENDOR      | 仕入先           | （なし） |
| S_MRPSTOCK   | WHSTOCK     | 倉庫在庫数       | （なし） |

## テーブル: S_PRDCTNOSTOCK

| テーブル名     | 列ID        | 列名       | 備考                                                                                         |
|:---------------|:------------|:-----------|:---------------------------------------------------------------------------------------------|
| S_PRDCTNOSTOCK | BKTNO       | バケットNo | （なし）                                                                                     |
| S_PRDCTNOSTOCK | BKTYEAR     | バケット年 | （なし）                                                                                     |
| S_PRDCTNOSTOCK | CMPFLG      | 完了Ｆ     | -2;内示分引当残在庫;-1;内示分引当在庫;0;生産途中;1;生産完了、消費未完了;2;生産完了、消費完了 |
| S_PRDCTNOSTOCK | CMPQTY      | 完成数     | （なし）                                                                                     |
| S_PRDCTNOSTOCK | CONSUMP     | 消費数     | （なし）                                                                                     |
| S_PRDCTNOSTOCK | ITEM        | 品目       | （なし）                                                                                     |
| S_PRDCTNOSTOCK | LINED       | ライン     | （なし）                                                                                     |
| S_PRDCTNOSTOCK | PRDCTBNO    | 枝番       | （なし）                                                                                     |
| S_PRDCTNOSTOCK | PRDCTNO     | 製番       | （なし）                                                                                     |
| S_PRDCTNOSTOCK | PRDCTQTY    | 指示数     | （なし）                                                                                     |
| S_PRDCTNOSTOCK | PROCESS     | 工程       | （なし）                                                                                     |
| S_PRDCTNOSTOCK | RGSTD       | 登録日     | （なし）                                                                                     |
| S_PRDCTNOSTOCK | SUSPENDTERM | 可能時間   | （なし）                                                                                     |
| S_PRDCTNOSTOCK | UPDTD       | 更新日     | （なし）                                                                                     |
| S_PRDCTNOSTOCK | UPDTWKCD    | 更新担当者 | （なし）                                                                                     |
| S_PRDCTNOSTOCK | VENDOR      | 仕入先     | （なし）                                                                                     |

## テーブル: S_PRODUCT_ENTRY

| テーブル名      | 列ID     | 列名       | 備考     |
|:----------------|:---------|:-----------|:---------|
| S_PRODUCT_ENTRY | COUNTER  | 内部登録No | （なし） |
| S_PRODUCT_ENTRY | ITEM     | 品目       | （なし） |
| S_PRODUCT_ENTRY | LINED    | 指示ライン | （なし） |
| S_PRODUCT_ENTRY | PLANDATE | 生産日     | （なし） |
| S_PRODUCT_ENTRY | PLANTIME | 生産時間   | （なし） |
| S_PRODUCT_ENTRY | PRDCTQTY | 生産数     | （なし） |
| S_PRODUCT_ENTRY | PROCESS  | 工程       | （なし） |
| S_PRODUCT_ENTRY | RGSTD    | 登録日     | （なし） |
| S_PRODUCT_ENTRY | RGSTTM   | 登録時刻   | （なし） |
| S_PRODUCT_ENTRY | SUB_NO   | 件数       | （なし） |
| S_PRODUCT_ENTRY | TERMINAL | 端末ID     | （なし） |
| S_PRODUCT_ENTRY | VENDOR   | 仕入先     | （なし） |
| S_PRODUCT_ENTRY | WORKERCD | 担当者     | （なし） |

## テーブル: S_QUALITYEVALUE

| テーブル名      | 列ID       | 列名         | 備考                                                     |
|:----------------|:-----------|:-------------|:---------------------------------------------------------|
| S_QUALITYEVALUE | DEFECT_FT  | 年間不適合数 | （なし）                                                 |
| S_QUALITYEVALUE | DEFECT1    | 1月不適合数  | 当該取引先・年の仕損数または返品数（1月発生）            |
| S_QUALITYEVALUE | DEFECT10   | 10月不適合数 | 当該取引先・年の仕損数または返品数（10月発生）           |
| S_QUALITYEVALUE | DEFECT11   | 11月不適合数 | 当該取引先・年の仕損数または返品数（11月発生）           |
| S_QUALITYEVALUE | DEFECT12   | 12月不適合数 | 当該取引先・年の仕損数または返品数（12月発生）           |
| S_QUALITYEVALUE | DEFECT2    | 2月不適合数  | 当該取引先・年の仕損数または返品数（2月発生）            |
| S_QUALITYEVALUE | DEFECT3    | 3月不適合数  | 当該取引先・年の仕損数または返品数（3月発生）            |
| S_QUALITYEVALUE | DEFECT4    | 4月不適合数  | 当該取引先・年の仕損数または返品数（4月発生）            |
| S_QUALITYEVALUE | DEFECT5    | 5月不適合数  | 当該取引先・年の仕損数または返品数（5月発生）            |
| S_QUALITYEVALUE | DEFECT6    | 6月不適合数  | 当該取引先・年の仕損数または返品数（6月発生）            |
| S_QUALITYEVALUE | DEFECT7    | 7月不適合数  | 当該取引先・年の仕損数または返品数（7月発生）            |
| S_QUALITYEVALUE | DEFECT8    | 8月不適合数  | 当該取引先・年の仕損数または返品数（8発生）              |
| S_QUALITYEVALUE | DEFECT9    | 9月不適合数  | 当該取引先・年の仕損数または返品数（9月発生）            |
| S_QUALITYEVALUE | EVAL_YEAR  | 評価年度     | （なし）                                                 |
| S_QUALITYEVALUE | RATE_FT    | 年間発生率   | （なし）                                                 |
| S_QUALITYEVALUE | RATE1      | 1月発生率    | 1月不適合数÷1月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE10     | 10月発生率   | 10月不適合数÷10月受入数×100(%)                           |
| S_QUALITYEVALUE | RATE11     | 11月発生率   | 11月不適合数÷11月受入数×100(%)                           |
| S_QUALITYEVALUE | RATE12     | 12月発生率   | 12月不適合数÷12月受入数×100(%)                           |
| S_QUALITYEVALUE | RATE2      | 2月発生率    | 2月不適合数÷2月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE3      | 3月発生率    | 3月不適合数÷3月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE4      | 4月発生率    | 4月不適合数÷4月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE5      | 5月発生率    | 5月不適合数÷5月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE6      | 6月発生率    | 6月不適合数÷6月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE7      | 7月発生率    | 7月不適合数÷7月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE8      | 8月発生率    | 8月不適合数÷8月受入数×100(%)                             |
| S_QUALITYEVALUE | RATE9      | 9月発生率    | 9月不適合数÷9月受入数×100(%)                             |
| S_QUALITYEVALUE | RECEIVE_FT | 年間受入数   | （なし）                                                 |
| S_QUALITYEVALUE | RECEIVE1   | 1月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（1月受入）  |
| S_QUALITYEVALUE | RECEIVE10  | 10月受入件数 | 当該取引先・年の購入品・外注品・支給品受入数（10月受入） |
| S_QUALITYEVALUE | RECEIVE11  | 11月受入件数 | 当該取引先・年の購入品・外注品・支給品受入数（11月受入） |
| S_QUALITYEVALUE | RECEIVE12  | 12月受入件数 | 当該取引先・年の購入品・外注品・支給品受入数（12月受入） |
| S_QUALITYEVALUE | RECEIVE2   | 2月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（2月受入）  |
| S_QUALITYEVALUE | RECEIVE3   | 3月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（3月受入）  |
| S_QUALITYEVALUE | RECEIVE4   | 4月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（4月受入）  |
| S_QUALITYEVALUE | RECEIVE5   | 5月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（5月受入）  |
| S_QUALITYEVALUE | RECEIVE6   | 6月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（6月受入）  |
| S_QUALITYEVALUE | RECEIVE7   | 7月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（7月受入）  |
| S_QUALITYEVALUE | RECEIVE8   | 8月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（8月受入）  |
| S_QUALITYEVALUE | RECEIVE9   | 9月受入件数  | 当該取引先・年の購入品・外注品・支給品受入数（9月受入）  |
| S_QUALITYEVALUE | RGSTD      | 登録日       | （なし）                                                 |
| S_QUALITYEVALUE | TRANSACTOR | 取引先       | （なし）                                                 |
| S_QUALITYEVALUE | UPDTD      | 更新日       | （なし）                                                 |
| S_QUALITYEVALUE | UPDTWKCD   | 更新担当者   | （なし）                                                 |

## テーブル: S_SIRODEN_ENTRY

| テーブル名      | 列ID       | 列名           | 備考                                                                                             |
|:----------------|:-----------|:---------------|:-------------------------------------------------------------------------------------------------|
| S_SIRODEN_ENTRY | COUNTER    | 内部登録No     | （なし）                                                                                         |
| S_SIRODEN_ENTRY | IMTYP      | 製品区分       | 0;製造品1;購入品2;外注品                                                                         |
| S_SIRODEN_ENTRY | ISSUEFLG   | 出庫区分       | 0;製造品オーダーより;1;購入品オーダーより;2;外注品オーダーより;3;外注支給（在庫移動）;4;受注出荷 |
| S_SIRODEN_ENTRY | ITEM       | 品目           | （なし）                                                                                         |
| S_SIRODEN_ENTRY | LOCT       | 入出庫場所     | （なし）                                                                                         |
| S_SIRODEN_ENTRY | PROCESS    | 工程           | （なし）                                                                                         |
| S_SIRODEN_ENTRY | RCISCD     | 入出庫区分     | （なし）                                                                                         |
| S_SIRODEN_ENTRY | RCISDATE   | 入出庫日       | （なし）                                                                                         |
| S_SIRODEN_ENTRY | RCISF      | 入庫・出庫区分 | 0;入庫;1;出庫                                                                                    |
| S_SIRODEN_ENTRY | RCISTIME   | 入出庫時間     | 非表示                                                                                           |
| S_SIRODEN_ENTRY | RECEIVEQTY | 入庫数         | （なし）                                                                                         |
| S_SIRODEN_ENTRY | RGSTD      | 登録日         | YYYY/MM/DD HH;MM;SS                                                                              |
| S_SIRODEN_ENTRY | RGSTTM     | 登録時刻       | （なし）                                                                                         |
| S_SIRODEN_ENTRY | SP_F       | 単価参照F      | 0;単価マスタより;1;特別単価                                                                      |
| S_SIRODEN_ENTRY | TERMINAL   | 端末情報       | （なし）                                                                                         |
| S_SIRODEN_ENTRY | TRANSACTOR | 取引先         | （なし）                                                                                         |
| S_SIRODEN_ENTRY | UNTPRC     | 単価           | （なし）                                                                                         |
| S_SIRODEN_ENTRY | UPDTD      | 更新日         | （なし）                                                                                         |
| S_SIRODEN_ENTRY | UPDTWKCD   | 更新担当者     | （なし）                                                                                         |
| S_SIRODEN_ENTRY | VENDOR     | 仕入先         | （なし）                                                                                         |
| S_SIRODEN_ENTRY | WKRATE     | 進度(%)        | （なし）                                                                                         |
| S_SIRODEN_ENTRY | WORKERCD   | 担当者         | （なし）                                                                                         |

## テーブル: S_SUSPENDSTOCK

| テーブル名     | 列ID         | 列名       | 備考     |
|:---------------|:-------------|:-----------|:---------|
| S_SUSPENDSTOCK | BKTNO        | バケットNo | （なし） |
| S_SUSPENDSTOCK | BKTYEAR      | バケット年 | （なし） |
| S_SUSPENDSTOCK | ITEM         | 品目       | （なし） |
| S_SUSPENDSTOCK | PROCESS      | 工程       | （なし） |
| S_SUSPENDSTOCK | RGSTD        | 登録日     | （なし） |
| S_SUSPENDSTOCK | SUSPENDDATE  | 保留解除日 | （なし） |
| S_SUSPENDSTOCK | SUSPENDSTOCK | 保留在庫数 | （なし） |
| S_SUSPENDSTOCK | UPDTD        | 更新日     | （なし） |
| S_SUSPENDSTOCK | UPDTWKCD     | 更新担当者 | （なし） |
| S_SUSPENDSTOCK | VENDOR       | 仕入先     | （なし） |

## テーブル: S_THEOSTOCK

| テーブル名   | 列ID        | 列名       | 備考     |
|:-------------|:------------|:-----------|:---------|
| S_THEOSTOCK  | ACCOUNTDATE | 計算日     | （なし） |
| S_THEOSTOCK  | BKTNO       | バケットNo | （なし） |
| S_THEOSTOCK  | BKTYEAR     | バケット年 | （なし） |
| S_THEOSTOCK  | ITEM        | 品目       | （なし） |
| S_THEOSTOCK  | PROCESS     | 工程       | （なし） |
| S_THEOSTOCK  | RGSTD       | 登録日     | （なし） |
| S_THEOSTOCK  | THEOSTOCK   | 理論在庫数 | （なし） |
| S_THEOSTOCK  | THEOSTOCK2  | 理論在庫数 | （なし） |
| S_THEOSTOCK  | UPDTD       | 更新日     | （なし） |
| S_THEOSTOCK  | UPDTWKCD    | 更新担当者 | （なし） |
| S_THEOSTOCK  | VENDOR      | 仕入先     | （なし） |

## テーブル: S_THEOSTOCKFLUCTU

| テーブル名        | 列ID        | 列名             | 備考     |
|:------------------|:------------|:-----------------|:---------|
| S_THEOSTOCKFLUCTU | ACCOUNTDATE | 計算日           | （なし） |
| S_THEOSTOCKFLUCTU | CMPQTY      | 生産数           | （なし） |
| S_THEOSTOCKFLUCTU | CONSUMP     | 消費数           | （なし） |
| S_THEOSTOCKFLUCTU | DATED       | 変動日           | （なし） |
| S_THEOSTOCKFLUCTU | H_CNT       | カウント         | （なし） |
| S_THEOSTOCKFLUCTU | HITEM       | 親品目           | （なし） |
| S_THEOSTOCKFLUCTU | INVDATE     | 棚卸日           | （なし） |
| S_THEOSTOCKFLUCTU | INVQTY      | 棚卸数           | （なし） |
| S_THEOSTOCKFLUCTU | ISSUEQTY    | 出庫数           | （なし） |
| S_THEOSTOCKFLUCTU | ITEM        | 品目             | （なし） |
| S_THEOSTOCKFLUCTU | PROCESS     | 工程             | （なし） |
| S_THEOSTOCKFLUCTU | PRORDERNO   | 生産指示オーダNo | （なし） |
| S_THEOSTOCKFLUCTU | PUORDERNO   | 購入オーダNo     | （なし） |
| S_THEOSTOCKFLUCTU | RCORDERNO   | 受注No           | （なし） |
| S_THEOSTOCKFLUCTU | RECEIVEQTY  | 入庫数           | （なし） |
| S_THEOSTOCKFLUCTU | RGSTD       | 登録日           | （なし） |
| S_THEOSTOCKFLUCTU | SBORDERNO   | 外注オーダNo     | （なし） |
| S_THEOSTOCKFLUCTU | STATUS      | 状態             | （なし） |
| S_THEOSTOCKFLUCTU | STOCK       | 在庫数           | （なし） |
| S_THEOSTOCKFLUCTU | UPDTD       | 更新日           | （なし） |
| S_THEOSTOCKFLUCTU | UPDTWKCD    | 更新担当者       | （なし） |
| S_THEOSTOCKFLUCTU | VENDOR      | 仕入先           | （なし） |

## テーブル: S_TRIALITM_LIST

| テーブル名      | 列ID         | 列名                 | 備考     |
|:----------------|:-------------|:---------------------|:---------|
| S_TRIALITM_LIST | A_CARD_FLG   | カード区分           | （なし） |
| S_TRIALITM_LIST | A_COLOR      | 色指示コード         | （なし） |
| S_TRIALITM_LIST | A_ODRCD      | 発注方針コード       | （なし） |
| S_TRIALITM_LIST | A_PACKCD     | 荷姿コード           | （なし） |
| S_TRIALITM_LIST | A_PACKNM     | 荷姿名称             | （なし） |
| S_TRIALITM_LIST | A_PACKQTY    | 荷姿収容数           | （なし） |
| S_TRIALITM_LIST | A_PROCESS    | 工程番号             | （なし） |
| S_TRIALITM_LIST | A_SUPPLIER   | 供給者               | （なし） |
| S_TRIALITM_LIST | A_SUPPLIERNM | 供給者名称           | （なし） |
| S_TRIALITM_LIST | A_USER       | 使用者               | （なし） |
| S_TRIALITM_LIST | A_USERNM     | 使用者名称           | （なし） |
| S_TRIALITM_LIST | CHG_FLG      | 変更区分             | （なし） |
| S_TRIALITM_LIST | CUSTOM       | 取引先コード         | （なし） |
| S_TRIALITM_LIST | CUSTOMNO     | オーダ識別番号       | （なし） |
| S_TRIALITM_LIST | DATA_FLG     | データ区分           | （なし） |
| S_TRIALITM_LIST | DELIDTTM     | 納入指示日/納入時刻  | （なし） |
| S_TRIALITM_LIST | IMNM         | 品目名称             | （なし） |
| S_TRIALITM_LIST | INVOICENO    | 納品書番号           | （なし） |
| S_TRIALITM_LIST | ITEM         | 品目番号             | （なし） |
| S_TRIALITM_LIST | LOCT         | 納入プラットフォーム | （なし） |
| S_TRIALITM_LIST | NEW_PRODUC   | 新規区分             | （なし） |
| S_TRIALITM_LIST | OFFCLF       | 内示区分             | （なし） |
| S_TRIALITM_LIST | OLD_ITEM     | 旧体系部品番号       | （なし） |
| S_TRIALITM_LIST | ORDERQTY     | 納入指示数           | （なし） |
| S_TRIALITM_LIST | PROCESS      | 工程                 | （なし） |
| S_TRIALITM_LIST | RECORDNO     | 受注No               | （なし） |
| S_TRIALITM_LIST | RORDERDATE   | 受注日               | （なし） |
| S_TRIALITM_LIST | STATUS       | 生試区分             | （なし） |
| S_TRIALITM_LIST | VENDOR       | 仕入先               | （なし） |

## テーブル: TMP_LOSS

| テーブル名   | 列ID      | 列名           | 備考                            |
|:-------------|:----------|:---------------|:--------------------------------|
| TMP_LOSS     | ACTFNTIME | 生産終了日時   | 'YYYY/MM/DD HH:MM               |
| TMP_LOSS     | ACTSTDATE | 生産日         | '生産日　YYYY/MM/DD             |
| TMP_LOSS     | ACTSTTIME | 生産開始日時   | 'YYYY/MM/DD HH:MM               |
| TMP_LOSS     | COUNTER   | 内部登録No     | '１からの連番                   |
| TMP_LOSS     | END_FLG   | 稼働終了フラグ | '0:稼働中、2：直終了            |
| TMP_LOSS     | FCDTY     | タイプ         | （なし）                        |
| TMP_LOSS     | FCODE     | コード         | （なし）                        |
| TMP_LOSS     | ITEM      | 品目           | 'OEE能力マスタの品目            |
| TMP_LOSS     | LINED     | ライン         | 'OEE能力マスタのライン          |
| TMP_LOSS     | LOSS3_FLG | 計画停止フラグ | 1:計画停止ロス、0：運用停止ロス |
| TMP_LOSS     | PROCESS   | 工程           | 'OEE能力マスタの工程            |
| TMP_LOSS     | RGSTD     | 登録日         | （なし）                        |
| TMP_LOSS     | RGSTWKCD  | 登録担当者     | （なし）                        |
| TMP_LOSS     | SHIFTF    | 直区分         | 1;1直;2;2直                     |
| TMP_LOSS     | UPDTD     | 更新日         | （なし）                        |
| TMP_LOSS     | UPDTWKCD  | 更新担当者     | （なし）                        |
| TMP_LOSS     | VENDOR    | 仕入先         | 'OEE能力マスタの仕入先          |

## テーブル: TMP_SHIFT

| テーブル名   | 列ID      | 列名           | 備考                                     |
|:-------------|:----------|:---------------|:-----------------------------------------|
| TMP_SHIFT    | ACTFNTIME | 生産終了日時   | 'HHMM                                    |
| TMP_SHIFT    | ACTSTDATE | 生産日         | '生産日　YYYY/MM/DD                      |
| TMP_SHIFT    | ACTSTTIME | 生産開始日時   | 'HHMM                                    |
| TMP_SHIFT    | END_FLG   | 稼働終了フラグ | '0:稼働中、2：直終了                     |
| TMP_SHIFT    | ITEM      | 品目           | 'OEE能力マスタの品目                     |
| TMP_SHIFT    | LINED     | ライン         | 'OEE能力マスタのライン                   |
| TMP_SHIFT    | PROCESS   | 工程           | 'OEE能力マスタの工程                     |
| TMP_SHIFT    | RGSTD     | 登録日         | （なし）                                 |
| TMP_SHIFT    | RGSTWKCD  | 登録担当者     | （なし）                                 |
| TMP_SHIFT    | SECT      | 部門           | （なし）                                 |
| TMP_SHIFT    | SHIFTF    | 直区分         | 1;1直;2;2直                              |
| TMP_SHIFT    | SUB_NO    | 件数           | '同一品目・ライン・直場合に＋１（1より） |
| TMP_SHIFT    | UPDTD     | 更新日         | （なし）                                 |
| TMP_SHIFT    | UPDTWKCD  | 更新担当者     | （なし）                                 |
| TMP_SHIFT    | VENDOR    | 仕入先         | 'OEE能力マスタの仕入先                   |
| TMP_SHIFT    | WORKER    | 作業者コード   | （なし）                                 |

## テーブル: TRY_ORDERNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| TRY_ORDERNO  | K_NO     | キー項目     | （なし） |
| TRY_ORDERNO  | LAST_OD1 | 最終オーダNo | （なし） |
| TRY_ORDERNO  | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: T_BUCKET

| テーブル名   | 列ID     | 列名                     | 備考              |
|:-------------|:---------|:-------------------------|:------------------|
| T_BUCKET     | BKTEDD   | ﾊﾞｹｯﾄ最終日              | （なし）          |
| T_BUCKET     | BKTNO    | バケットNo               | （なし）          |
| T_BUCKET     | BKTSTD   | バケット開始日           | （なし）          |
| T_BUCKET     | BKTYEAR  | バケット年               | （なし）          |
| T_BUCKET     | MRPEDD   | 所要量計算最終日         | （なし）          |
| T_BUCKET     | ODEDD    | 所要量計算出荷取込最終日 | （なし）          |
| T_BUCKET     | ODRDEDD  | 受注取込最終日           | （なし）          |
| T_BUCKET     | PODEDD   | 購入品確定最終日         | （なし）          |
| T_BUCKET     | PRDCTODF | 作業指示確定F            | 0;未完了1;完了    |
| T_BUCKET     | RGSTD    | 登録日                   | （なし）          |
| T_BUCKET     | SCH_F    | スケジューラ転送Ｆ       | 0;未転送;1;転送済 |
| T_BUCKET     | SCHEDD   | スケジュール最終日       | （なし）          |
| T_BUCKET     | UPDTD    | 更新日                   | （なし）          |
| T_BUCKET     | UPDTWKCD | 更新担当者               | （なし）          |

## テーブル: T_CUSTOMORDERNO

| テーブル名      | 列ID     | 列名         | 備考     |
|:----------------|:---------|:-------------|:---------|
| T_CUSTOMORDERNO | K_NO     | キー項目     | （なし） |
| T_CUSTOMORDERNO | LAST_OD1 | 最終オーダNo | （なし） |
| T_CUSTOMORDERNO | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: T_EQUIPMENTCLN

| テーブル名     | 列ID       | 列名            | 備考                                |
|:---------------|:-----------|:----------------|:------------------------------------|
| T_EQUIPMENTCLN | BKTNO      | バケットＮｏ    | （なし）                            |
| T_EQUIPMENTCLN | BKTYEAR    | バケット年      | （なし）                            |
| T_EQUIPMENTCLN | DATED      | 日付            | （なし）                            |
| T_EQUIPMENTCLN | EFFTMRATIO | 有効時間比率(%) | （なし）                            |
| T_EQUIPMENTCLN | LINED      | ライン          | （なし）                            |
| T_EQUIPMENTCLN | OPMODE     | 操業モード      | 0;定時;1;定時＋残業;2;休日出勤      |
| T_EQUIPMENTCLN | OPOPTIMIZ  | 操業最適化      | 0;しない;1;する                     |
| T_EQUIPMENTCLN | OVWORKFLG  | 残業Ｆ          | 0;残業・休出しない;1;残業・休出する |
| T_EQUIPMENTCLN | PROCESS    | 工程            | （なし）                            |
| T_EQUIPMENTCLN | RGSTD      | 登録日          | （なし）                            |
| T_EQUIPMENTCLN | TMTBL      | 稼働時間帯      | （なし）                            |
| T_EQUIPMENTCLN | UPDTD      | 更新日          | （なし）                            |
| T_EQUIPMENTCLN | UPDTWKCD   | 更新担当者      | （なし）                            |

## テーブル: T_EXCHANGE

| テーブル名   | 列ID     | 列名       | 備考     |
|:-------------|:---------|:-----------|:---------|
| T_EXCHANGE   | DATED    | 日付       | （なし） |
| T_EXCHANGE   | EXCHANGE | 為替レート | （なし） |
| T_EXCHANGE   | K_NO     | キーNo     | （なし） |

## テーブル: T_GANTFIXDATA

| テーブル名    | 列ID      | 列名       | 備考            |
|:--------------|:----------|:-----------|:----------------|
| T_GANTFIXDATA | BKTNO     | バケットNo | （なし）        |
| T_GANTFIXDATA | BKTYEAR   | バケット年 | （なし）        |
| T_GANTFIXDATA | CMPFLG    | 完了Ｆ     | 0;未完了;1;完了 |
| T_GANTFIXDATA | CMPQTY    | 完成数     | （なし）        |
| T_GANTFIXDATA | FIXDATE   | 固定日     | （なし）        |
| T_GANTFIXDATA | FIXQTY    | 固定個数   | （なし）        |
| T_GANTFIXDATA | FIXSTTIME | 開始時間   | （なし）        |
| T_GANTFIXDATA | ITEM      | 品目       | （なし）        |
| T_GANTFIXDATA | LINED     | ライン     | （なし）        |
| T_GANTFIXDATA | PRDCTBNO  | 枝番       | （なし）        |
| T_GANTFIXDATA | PRDCTNO   | 製番       | （なし）        |
| T_GANTFIXDATA | PROCESS   | 工程       | （なし）        |
| T_GANTFIXDATA | RGSTD     | 登録日     | （なし）        |
| T_GANTFIXDATA | UPDTD     | 更新日     | （なし）        |
| T_GANTFIXDATA | UPDTWKCD  | 更新担当者 | （なし）        |
| T_GANTFIXDATA | VENDOR    | 仕入先     | （なし）        |

## テーブル: T_GENKA

| テーブル名   | 列ID         | 列名                                 | 備考                       |
|:-------------|:-------------|:-------------------------------------|:---------------------------|
| T_GENKA      | COST         | 標準原価                             | （なし）                   |
| T_GENKA      | HBFURYOSU    | 標準後工程戻り不良数                 | （なし）                   |
| T_GENKA      | HFURYOSU     | 標準不良数                           | （なし）                   |
| T_GENKA      | HGAICHUHI    | 標準外注加工費                       | （なし）                   |
| T_GENKA      | HHENDOUHI    | 標準変動費                           | （なし）                   |
| T_GENKA      | HJ_KIKAN     | 標準原価  取込み期間                 | YYYY/MM〜YYYY/MM           |
| T_GENKA      | HKAKOUHI     | 標準加工費                           | （なし）                   |
| T_GENKA      | HKANSETUHI   | 標準間接経費                         | （なし）                   |
| T_GENKA      | HKOTEIHI     | 標準固定費                           | （なし）                   |
| T_GENKA      | HKOUNYUHI    | 標準購入品費（補助材）               | （なし）                   |
| T_GENKA      | HRUIKEI      | 累計標準原価                         | （なし）                   |
| T_GENKA      | HSEISANSU    | 標準生産数または購入数               | （なし）                   |
| T_GENKA      | HSHISONHI    | 標準仕損費                           | （なし）                   |
| T_GENKA      | HSHUKKASU    | 標準出荷数                           | （なし）                   |
| T_GENKA      | IMNM         | 品名                                 | （なし）                   |
| T_GENKA      | IMTYP        | 製品区分                             | 0;製造品､1;購入品､2;外注品 |
| T_GENKA      | ITEM         | 品目                                 | （なし）                   |
| T_GENKA      | JBFURYOSU    | 実際後工程戻り不良数                 | （なし）                   |
| T_GENKA      | JED_BZAIKOSU | 月末戻り在庫数                       | （なし）                   |
| T_GENKA      | JED_ZAIKOHI  | 負荷時間からの月末在庫費             | （なし）                   |
| T_GENKA      | JED_ZAIKOHI2 | 生産能力からの月末在庫費             | （なし）                   |
| T_GENKA      | JED_ZAIKOSU  | 月末在庫数                           | （なし）                   |
| T_GENKA      | JED_ZTANKA   | 負荷時間からの月末在庫単価           | （なし）                   |
| T_GENKA      | JED_ZTANKA2  | 生産能力からの月末在庫単価           | （なし）                   |
| T_GENKA      | JFURYOSU     | 実際不良数                           | （なし）                   |
| T_GENKA      | JGAICHUHI    | 負荷時間からの実際外注加工費         | （なし）                   |
| T_GENKA      | JGAICHUHI2   | 生産能力からの実際外注加工費         | （なし）                   |
| T_GENKA      | JHENDOUHI    | 負荷時間からの変動費                 | （なし）                   |
| T_GENKA      | JHENDOUHI2   | 生産能力からの変動費                 | （なし）                   |
| T_GENKA      | JINOUTHI     | 負荷時間からの入出庫経費             | （なし）                   |
| T_GENKA      | JINOUTHI2    | 生産能力からの入出庫経費             | （なし）                   |
| T_GENKA      | JKAKOUHI     | 負荷時間からの実際加工費             | （なし）                   |
| T_GENKA      | JKAKOUHI2    | 生産能力からの実際加工費             | （なし）                   |
| T_GENKA      | JKANSEIHI    | 負荷時間からの                       | （なし）                   |
| T_GENKA      | JKANSEIHI2   | 生産能力からの                       | （なし）                   |
| T_GENKA      | JKANSETUHI   | 負荷時間からの間接経費               | （なし）                   |
| T_GENKA      | JKANSETUHI2  | 生産能力からの間接経費               | （なし）                   |
| T_GENKA      | JKOTEIHI     | 負荷時間からの固定費                 | （なし）                   |
| T_GENKA      | JKOTEIHI2    | 生産能力からの固定費                 | （なし）                   |
| T_GENKA      | JKOUNYUHI    | 負荷時間からの実際購入品費（補助材） | （なし）                   |
| T_GENKA      | JKOUNYUHI2   | 生産能力からの実際購入品費（補助材） | （なし）                   |
| T_GENKA      | JRUIKEI      | 負荷時間からの累計実際原価           | （なし）                   |
| T_GENKA      | JRUIKEI2     | 生産能力からの累計実際原価           | （なし）                   |
| T_GENKA      | JS_KIKAN     | 実績ﾃﾞｰﾀ　取込み期間                 | YYYY/MM/DD〜YYYY/MM/DD     |
| T_GENKA      | JSEISANSU    | 実際生産数または購入数               | （なし）                   |
| T_GENKA      | JSHISONHI    | 負荷時間からの仕損費                 | （なし）                   |
| T_GENKA      | JSHISONHI2   | 生産能力からの仕損費                 | （なし）                   |
| T_GENKA      | JSHUKKASU    | 実際出荷数                           | （なし）                   |
| T_GENKA      | JST_BZAIKOSU | 月初戻り在庫数                       | （なし）                   |
| T_GENKA      | JST_ZAIKOHI  | 負荷時間からの月初在庫費             | （なし）                   |
| T_GENKA      | JST_ZAIKOHI2 | 生産能力からの月初在庫費             | （なし）                   |
| T_GENKA      | JST_ZAIKOSU  | 月初在庫数                           | （なし）                   |
| T_GENKA      | JST_ZTANKA   | 負荷時間からの月初在庫単価           | （なし）                   |
| T_GENKA      | JST_ZTANKA2  | 生産能力からの月初在庫単価           | （なし）                   |
| T_GENKA      | JTANKA       | 負荷時間からの実際原価               | （なし）                   |
| T_GENKA      | JTANKA2      | 生産能力からの実際原価               | （なし）                   |
| T_GENKA      | JZIN         | 未使用                               | （なし）                   |
| T_GENKA      | JZOUT        | 未使用                               | （なし）                   |
| T_GENKA      | MONTH        | 原価計算月                           | （なし）                   |
| T_GENKA      | PROCESS      | 工程                                 | （なし）                   |
| T_GENKA      | UPDTD        | 更新日                               | （なし）                   |
| T_GENKA      | UPDTWKCD     | 更新担当者                           | （なし）                   |
| T_GENKA      | VENDOR       | 仕入先                               | （なし）                   |
| T_GENKA      | YEAR         | 原価計算年                           | （なし）                   |

## テーブル: T_HISEQUIPMENT

| テーブル名     | 列ID      | 列名          | 備考     |
|:---------------|:----------|:--------------|:---------|
| T_HISEQUIPMENT | BKTNO     | バケットNo    | （なし） |
| T_HISEQUIPMENT | BKTYEAR   | バケット年    | （なし） |
| T_HISEQUIPMENT | LINED     | ライン        | （なし） |
| T_HISEQUIPMENT | OPRTRATIO | 計画稼働率(%) | （なし） |
| T_HISEQUIPMENT | PROCESS   | 工程          | （なし） |
| T_HISEQUIPMENT | RGSTD     | 登録日        | （なし） |
| T_HISEQUIPMENT | UPDTD     | 更新日        | （なし） |
| T_HISEQUIPMENT | UPDTWKCD  | 更新担当者    | （なし） |

## テーブル: T_ISSUENO_TABLET

| テーブル名       | 列ID     | 列名           | 備考     |
|:-----------------|:---------|:---------------|:---------|
| T_ISSUENO_TABLET | K_NO     | キー項目       | （なし） |
| T_ISSUENO_TABLET | LAST_OD1 | 最終内部登録No | （なし） |
| T_ISSUENO_TABLET | NEXT_OD1 | 次回内部登録No | （なし） |

## テーブル: T_KEIHI

| テーブル名   | 列ID          | 列名                  | 備考     |
|:-------------|:--------------|:----------------------|:---------|
| T_KEIHI      | H_HENDOUHI1   | 標準変動費1(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI10  | 標準変動費10(円/月)   | （なし） |
| T_KEIHI      | H_HENDOUHI11  | 標準変動費11(円/月)   | （なし） |
| T_KEIHI      | H_HENDOUHI12  | 標準変動費12(円/月)   | （なし） |
| T_KEIHI      | H_HENDOUHI2   | 標準変動費2(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI3   | 標準変動費3(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI4   | 標準変動費4(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI5   | 標準変動費5(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI6   | 標準変動費6(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI7   | 標準変動費7(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI8   | 標準変動費8(円/月)    | （なし） |
| T_KEIHI      | H_HENDOUHI9   | 標準変動費9(円/月)    | （なし） |
| T_KEIHI      | H_KANSETUHI1  | 標準間接経費1(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI10 | 標準間接経費10(円/月) | （なし） |
| T_KEIHI      | H_KANSETUHI11 | 標準間接経費11(円/月) | （なし） |
| T_KEIHI      | H_KANSETUHI12 | 標準間接経費12(円/月) | （なし） |
| T_KEIHI      | H_KANSETUHI2  | 標準間接経費2(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI3  | 標準間接経費3(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI4  | 標準間接経費4(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI5  | 標準間接経費5(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI6  | 標準間接経費6(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI7  | 標準間接経費7(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI8  | 標準間接経費8(円/月)  | （なし） |
| T_KEIHI      | H_KANSETUHI9  | 標準間接経費9(円/月)  | （なし） |
| T_KEIHI      | H_KOTEIHI1    | 標準固定費1(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI10   | 標準固定費10(円/月)   | （なし） |
| T_KEIHI      | H_KOTEIHI11   | 標準固定費11(円/月)   | （なし） |
| T_KEIHI      | H_KOTEIHI12   | 標準固定費12(円/月)   | （なし） |
| T_KEIHI      | H_KOTEIHI2    | 標準固定費2(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI3    | 標準固定費3(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI4    | 標準固定費4(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI5    | 標準固定費5(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI6    | 標準固定費6(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI7    | 標準固定費7(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI8    | 標準固定費8(円/月)    | （なし） |
| T_KEIHI      | H_KOTEIHI9    | 標準固定費9(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI1   | 実際変動費1(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI10  | 実際変動費10(円/月)   | （なし） |
| T_KEIHI      | J_HENDOUHI11  | 実際変動費11(円/月)   | （なし） |
| T_KEIHI      | J_HENDOUHI12  | 実際変動費12(円/月)   | （なし） |
| T_KEIHI      | J_HENDOUHI2   | 実際変動費2(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI3   | 実際変動費3(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI4   | 実際変動費4(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI5   | 実際変動費5(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI6   | 実際変動費6(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI7   | 実際変動費7(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI8   | 実際変動費8(円/月)    | （なし） |
| T_KEIHI      | J_HENDOUHI9   | 実際変動費9(円/月)    | （なし） |
| T_KEIHI      | J_KANSETUHI1  | 実際間接経費1(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI10 | 実際間接経費10(円/月) | （なし） |
| T_KEIHI      | J_KANSETUHI11 | 実際間接経費11(円/月) | （なし） |
| T_KEIHI      | J_KANSETUHI12 | 実際間接経費12(円/月) | （なし） |
| T_KEIHI      | J_KANSETUHI2  | 実際間接経費2(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI3  | 実際間接経費3(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI4  | 実際間接経費4(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI5  | 実際間接経費5(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI6  | 実際間接経費6(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI7  | 実際間接経費7(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI8  | 実際間接経費8(円/月)  | （なし） |
| T_KEIHI      | J_KANSETUHI9  | 実際間接経費9(円/月)  | （なし） |
| T_KEIHI      | J_KOTEIHI1    | 実際固定費1(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI10   | 実際固定費10(円/月)   | （なし） |
| T_KEIHI      | J_KOTEIHI11   | 実際固定費11(円/月)   | （なし） |
| T_KEIHI      | J_KOTEIHI12   | 実際固定費12(円/月)   | （なし） |
| T_KEIHI      | J_KOTEIHI2    | 実際固定費2(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI3    | 実際固定費3(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI4    | 実際固定費4(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI5    | 実際固定費5(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI6    | 実際固定費6(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI7    | 実際固定費7(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI8    | 実際固定費8(円/月)    | （なし） |
| T_KEIHI      | J_KOTEIHI9    | 実際固定費9(円/月)    | （なし） |
| T_KEIHI      | MONTH1        | 年月１                | （なし） |
| T_KEIHI      | MONTH10       | 年月10                | （なし） |
| T_KEIHI      | MONTH11       | 年月11                | （なし） |
| T_KEIHI      | MONTH12       | 年月12                | （なし） |
| T_KEIHI      | MONTH2        | 年月2                 | （なし） |
| T_KEIHI      | MONTH3        | 年月3                 | （なし） |
| T_KEIHI      | MONTH4        | 年月4                 | （なし） |
| T_KEIHI      | MONTH5        | 年月5                 | （なし） |
| T_KEIHI      | MONTH6        | 年月6                 | （なし） |
| T_KEIHI      | MONTH7        | 年月7                 | （なし） |
| T_KEIHI      | MONTH8        | 年月8                 | （なし） |
| T_KEIHI      | MONTH9        | 年月9                 | （なし） |
| T_KEIHI      | PROCESS       | 工程                  | （なし） |
| T_KEIHI      | RGSTD         | 登録日                | （なし） |
| T_KEIHI      | UPDTD         | 更新日                | （なし） |
| T_KEIHI      | UPDTWKCD      | 更新担当者            | （なし） |

## テーブル: T_MRPRESULT

| テーブル名   | 列ID         | 列名           | 備考     |
|:-------------|:-------------|:---------------|:---------|
| T_MRPRESULT  | BKTNO        | バケットNo     | （なし） |
| T_MRPRESULT  | BKTYEAR      | バケット年     | （なし） |
| T_MRPRESULT  | DATED        | 日付           | （なし） |
| T_MRPRESULT  | ITEM         | 品目           | （なし） |
| T_MRPRESULT  | OD           | オーダ数       | （なし） |
| T_MRPRESULT  | OFFICIALOD   | 確定オーダ数   | （なし） |
| T_MRPRESULT  | OFFICIALODNO | 確定オーダNo   | （なし） |
| T_MRPRESULT  | PROCESS      | 工程           | （なし） |
| T_MRPRESULT  | PRODUCTTIME  | 生産時間(時間) | （なし） |
| T_MRPRESULT  | RD           | 必要数         | （なし） |
| T_MRPRESULT  | RGSTD        | 登録日         | （なし） |
| T_MRPRESULT  | STOCK        | 在庫数         | （なし） |
| T_MRPRESULT  | UPDTD        | 更新日         | （なし） |
| T_MRPRESULT  | UPDTWKCD     | 更新担当者     | （なし） |
| T_MRPRESULT  | VENDOR       | 仕入先         | （なし） |

## テーブル: T_MRPRESULT2

| テーブル名   | 列ID         | 列名         | 備考     |
|:-------------|:-------------|:-------------|:---------|
| T_MRPRESULT2 | BKTNO        | バケットNo   | （なし） |
| T_MRPRESULT2 | BKTYEAR      | バケット年   | （なし） |
| T_MRPRESULT2 | DATED        | 日付         | （なし） |
| T_MRPRESULT2 | ITEM         | 品目         | （なし） |
| T_MRPRESULT2 | OD           | オーダ数     | （なし） |
| T_MRPRESULT2 | OFFICIALOD   | 確定オーダ数 | （なし） |
| T_MRPRESULT2 | OFFICIALODNO | 確定オーダNo | （なし） |
| T_MRPRESULT2 | PROCESS      | 工程         | （なし） |
| T_MRPRESULT2 | RD           | 必要数       | （なし） |
| T_MRPRESULT2 | RGSTD        | 登録日       | （なし） |
| T_MRPRESULT2 | STOCK        | 在庫数       | （なし） |
| T_MRPRESULT2 | UPDTD        | 更新日       | （なし） |
| T_MRPRESULT2 | UPDTWKCD     | 更新担当者   | （なし） |
| T_MRPRESULT2 | VENDOR       | 仕入先       | （なし） |

## テーブル: T_OVSPROCURE

| テーブル名   | 列ID             | 列名                | 備考                                           |
|:-------------|:-----------------|:--------------------|:-----------------------------------------------|
| T_OVSPROCURE | ALLOCD           | 引当期限日          | （なし）                                       |
| T_OVSPROCURE | CALDATE          | 計算日              | （なし）                                       |
| T_OVSPROCURE | COUNTER          | 内部番号            | （なし）                                       |
| T_OVSPROCURE | ESTARV           | 到着予定日          | （なし）                                       |
| T_OVSPROCURE | ESTDEP           | 出港予定日          | IMI, IMT⇒null、YMSC⇒出ETD1（第1木曜, 第3木曜） |
| T_OVSPROCURE | GROSSTOCK        | ロス在庫            | （なし）                                       |
| T_OVSPROCURE | GROSSTOCK_DIFF   | 棚卸グロス在庫差異  | （なし）                                       |
| T_OVSPROCURE | INI_GROSSTOCK    | 初期グロス在庫      | 「計算日」時点のグロス在庫                     |
| T_OVSPROCURE | ITEM             | 品目                | （なし）                                       |
| T_OVSPROCURE | LIMIT_ALLOCD     | 引当限界日          | （なし）                                       |
| T_OVSPROCURE | LIMIT_ALLOCD_CHK | 引当限界日(CHK)     | （なし）                                       |
| T_OVSPROCURE | LIMIT_STOCK      | 引当限界日在庫      | （なし）                                       |
| T_OVSPROCURE | LIMIT_STOCK_CHK  | 引当限界日在庫(CHK) | （なし）                                       |
| T_OVSPROCURE | MINILOT          | 最小発注ロット      | （なし）                                       |
| T_OVSPROCURE | OD               | OD                  | （なし）                                       |
| T_OVSPROCURE | OFFCL_ORDER      | 発注済確定PO        | 発注済オーダー数合計                           |
| T_OVSPROCURE | OFFCL_ORDERNO    | 発注済確定PO_No     | 発注済オーダーNo  【例】K0016073他             |
| T_OVSPROCURE | ORDEREDF         | 確定F               | 0;内示予定;1;確定予定2;既存確定                |
| T_OVSPROCURE | PROCESS          | 工程                | （なし）                                       |
| T_OVSPROCURE | PROCURE_BKTNO    | 調達BKTNo           | （なし）                                       |
| T_OVSPROCURE | PROCURE_YM       | 調達年月            | （なし）                                       |
| T_OVSPROCURE | RD               | RD                  | （なし）                                       |
| T_OVSPROCURE | RMN_ORDER        | 未受入発注残        | 「計算日」以前の未受入発注残合計               |
| T_OVSPROCURE | SFTYSTCK         | 安全在庫            | （なし）                                       |
| T_OVSPROCURE | TRANSACTOR       | 発注先              | 海外工場（IMI, IMT, YMSC etc.)⇒取引先Mから選択 |
| T_OVSPROCURE | VENDOR           | 仕入先              | （なし）                                       |
| T_OVSPROCURE | WARNING          | 予定割警告          | （なし）                                       |

## テーブル: T_OVSSHIPITEM

| テーブル名    | 列ID       | 列名         | 備考              |
|:--------------|:-----------|:-------------|:------------------|
| T_OVSSHIPITEM | DEMANDFLG  | 需要有無F    | 0;需要無;1;需要有 |
| T_OVSSHIPITEM | HAFMCUS    | 代表得意先   | （なし）          |
| T_OVSSHIPITEM | HITEM      | 親品目       | （なし）          |
| T_OVSSHIPITEM | HPROCESS   | 親工程       | （なし）          |
| T_OVSSHIPITEM | HVENDOR    | 親仕入先     | （なし）          |
| T_OVSSHIPITEM | ITEM       | 品目         | （なし）          |
| T_OVSSHIPITEM | MONTH1     | 第1月        | （なし）          |
| T_OVSSHIPITEM | MONTH10    | 第10月       | （なし）          |
| T_OVSSHIPITEM | MONTH11    | 第11月       | （なし）          |
| T_OVSSHIPITEM | MONTH12    | 第12月       | （なし）          |
| T_OVSSHIPITEM | MONTH2     | 第2月        | （なし）          |
| T_OVSSHIPITEM | MONTH3     | 第3月        | （なし）          |
| T_OVSSHIPITEM | MONTH4     | 第4月        | （なし）          |
| T_OVSSHIPITEM | MONTH5     | 第5月        | （なし）          |
| T_OVSSHIPITEM | MONTH6     | 第6月        | （なし）          |
| T_OVSSHIPITEM | MONTH7     | 第7月        | （なし）          |
| T_OVSSHIPITEM | MONTH8     | 第8月        | （なし）          |
| T_OVSSHIPITEM | MONTH9     | 第9月        | （なし）          |
| T_OVSSHIPITEM | PHUNIT     | 構成数       | （なし）          |
| T_OVSSHIPITEM | PROCESS    | 工程         | （なし）          |
| T_OVSSHIPITEM | QTY1       | 第1月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY10      | 第10月出荷数 | （なし）          |
| T_OVSSHIPITEM | QTY11      | 第11月出荷数 | （なし）          |
| T_OVSSHIPITEM | QTY12      | 第12月出荷数 | （なし）          |
| T_OVSSHIPITEM | QTY2       | 第2月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY3       | 第3月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY4       | 第4月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY5       | 第5月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY6       | 第6月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY7       | 第7月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY8       | 第8月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTY9       | 第9月出荷数  | （なし）          |
| T_OVSSHIPITEM | QTYSUM     | 受注数合計   | （なし）          |
| T_OVSSHIPITEM | TMONTH1    | 第1月        | （なし）          |
| T_OVSSHIPITEM | TMONTH10   | 第10月       | （なし）          |
| T_OVSSHIPITEM | TMONTH11   | 第11月       | （なし）          |
| T_OVSSHIPITEM | TMONTH12   | 第12月       | （なし）          |
| T_OVSSHIPITEM | TMONTH2    | 第2月        | （なし）          |
| T_OVSSHIPITEM | TMONTH3    | 第3月        | （なし）          |
| T_OVSSHIPITEM | TMONTH4    | 第4月        | （なし）          |
| T_OVSSHIPITEM | TMONTH5    | 第5月        | （なし）          |
| T_OVSSHIPITEM | TMONTH6    | 第6月        | （なし）          |
| T_OVSSHIPITEM | TMONTH7    | 第7月        | （なし）          |
| T_OVSSHIPITEM | TMONTH8    | 第8月        | （なし）          |
| T_OVSSHIPITEM | TMONTH9    | 第9月        | （なし）          |
| T_OVSSHIPITEM | TRANSACTOR | 発注先       | （なし）          |
| T_OVSSHIPITEM | VENDOR     | 仕入先       | （なし）          |

## テーブル: T_OVSSHIPPLAN

| テーブル名    | 列ID       | 列名         | 備考     |
|:--------------|:-----------|:-------------|:---------|
| T_OVSSHIPPLAN | ITEM       | 品目         | （なし） |
| T_OVSSHIPPLAN | MONTH1     | 第1月        | （なし） |
| T_OVSSHIPPLAN | MONTH10    | 第10月       | （なし） |
| T_OVSSHIPPLAN | MONTH11    | 第11月       | （なし） |
| T_OVSSHIPPLAN | MONTH12    | 第12月       | （なし） |
| T_OVSSHIPPLAN | MONTH2     | 第2月        | （なし） |
| T_OVSSHIPPLAN | MONTH3     | 第3月        | （なし） |
| T_OVSSHIPPLAN | MONTH4     | 第4月        | （なし） |
| T_OVSSHIPPLAN | MONTH5     | 第5月        | （なし） |
| T_OVSSHIPPLAN | MONTH6     | 第6月        | （なし） |
| T_OVSSHIPPLAN | MONTH7     | 第7月        | （なし） |
| T_OVSSHIPPLAN | MONTH8     | 第8月        | （なし） |
| T_OVSSHIPPLAN | MONTH9     | 第9月        | （なし） |
| T_OVSSHIPPLAN | PROCESS    | 工程         | （なし） |
| T_OVSSHIPPLAN | QTY1       | 第1月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY10      | 第10月出荷数 | （なし） |
| T_OVSSHIPPLAN | QTY11      | 第11月出荷数 | （なし） |
| T_OVSSHIPPLAN | QTY12      | 第12月出荷数 | （なし） |
| T_OVSSHIPPLAN | QTY2       | 第2月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY3       | 第3月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY4       | 第4月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY5       | 第5月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY6       | 第6月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY7       | 第7月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY8       | 第8月出荷数  | （なし） |
| T_OVSSHIPPLAN | QTY9       | 第9月出荷数  | （なし） |
| T_OVSSHIPPLAN | TMONTH1    | 第1月        | （なし） |
| T_OVSSHIPPLAN | TMONTH10   | 第10月       | （なし） |
| T_OVSSHIPPLAN | TMONTH11   | 第11月       | （なし） |
| T_OVSSHIPPLAN | TMONTH12   | 第12月       | （なし） |
| T_OVSSHIPPLAN | TMONTH2    | 第2月        | （なし） |
| T_OVSSHIPPLAN | TMONTH3    | 第3月        | （なし） |
| T_OVSSHIPPLAN | TMONTH4    | 第4月        | （なし） |
| T_OVSSHIPPLAN | TMONTH5    | 第5月        | （なし） |
| T_OVSSHIPPLAN | TMONTH6    | 第6月        | （なし） |
| T_OVSSHIPPLAN | TMONTH7    | 第7月        | （なし） |
| T_OVSSHIPPLAN | TMONTH8    | 第8月        | （なし） |
| T_OVSSHIPPLAN | TMONTH9    | 第9月        | （なし） |
| T_OVSSHIPPLAN | TRANSACTOR | 発注先       | （なし） |
| T_OVSSHIPPLAN | VENDOR     | 仕入先       | （なし） |

## テーブル: T_PRDODUCT

| テーブル名   | 列ID       | 列名     | 備考     |
|:-------------|:-----------|:---------|:---------|
| T_PRDODUCT   | EDIT_CHK   | チェック | （なし） |
| T_PRDODUCT   | ITEM       | 品目     | （なし） |
| T_PRDODUCT   | LINED      | ライン   | （なし） |
| T_PRDODUCT   | LINED_EDT  | ライン   | （なし） |
| T_PRDODUCT   | NOUKI      | 納期     | （なし） |
| T_PRDODUCT   | NOUKI_EDT  | 納期     | （なし） |
| T_PRDODUCT   | PROCESS    | 工程     | （なし） |
| T_PRDODUCT   | REQQTY     | 指示数   | （なし） |
| T_PRDODUCT   | TRANSACTOR | 取引先   | （なし） |
| T_PRDODUCT   | VENDOR     | 仕入先   | （なし） |

## テーブル: T_RCISNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| T_RCISNO     | K_NO     | キー項目     | （なし） |
| T_RCISNO     | LAST_OD1 | 最終オーダNo | （なし） |
| T_RCISNO     | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: T_TASK

| テーブル名   | 列ID      | 列名         | 備考     |
|:-------------|:----------|:-------------|:---------|
| T_TASK       | BKTNO     | バケットNo   | （なし） |
| T_TASK       | BKTYEAR   | バケット年   | （なし） |
| T_TASK       | SMODE     | 処理モード   | （なし） |
| T_TASK       | SYORIDATE | 最終処理日時 | （なし） |
| T_TASK       | TASK      | タスクコード | （なし） |
| T_TASK       | TASKMEI   | タスク名     | （なし） |

## テーブル: T_TMPNO

| テーブル名   | 列ID     | 列名         | 備考     |
|:-------------|:---------|:-------------|:---------|
| T_TMPNO      | K_NO     | キー項目     | （なし） |
| T_TMPNO      | LAST_OD1 | 最終オーダNo | （なし） |
| T_TMPNO      | NEXT_OD1 | 次回オーダNo | （なし） |

## テーブル: YCOM_PAYMENT

| テーブル名   | 列ID          | 列名           | 備考     |
|:-------------|:--------------|:---------------|:---------|
| YCOM_PAYMENT | A_FGROUP      | 商品分類       | （なし） |
| YCOM_PAYMENT | A_FPTYPE      | 受入有支区分   | （なし） |
| YCOM_PAYMENT | A_SUPPLIER    | 供給者         | （なし） |
| YCOM_PAYMENT | A_USER        | 使用者         | （なし） |
| YCOM_PAYMENT | AMOUNT        | 受入金額       | （なし） |
| YCOM_PAYMENT | BATCH_NO      | バッチＮｏ     | （なし） |
| YCOM_PAYMENT | COUNTER       | 内部登録No     | （なし） |
| YCOM_PAYMENT | DELIVERY_DATE | 納入指示日     | （なし） |
| YCOM_PAYMENT | DRWNO         | 部品番号       | （なし） |
| YCOM_PAYMENT | IDENTIFY_CD   | 識別コード     | （なし） |
| YCOM_PAYMENT | INVOICE_CD    | 伝票コード     | （なし） |
| YCOM_PAYMENT | INVOICENO     | 納品書番号     | （なし） |
| YCOM_PAYMENT | ISSUE_DATE    | 発行日         | （なし） |
| YCOM_PAYMENT | ITEM          | 品目           | （なし） |
| YCOM_PAYMENT | ITEM_CD       | 旧部品番号     | （なし） |
| YCOM_PAYMENT | ITMNM         | 品名           | （なし） |
| YCOM_PAYMENT | MAKER_CD      | メーカーコード | （なし） |
| YCOM_PAYMENT | PERSON_CD     | 購買担当       | （なし） |
| YCOM_PAYMENT | PLATFORM      | 納入場所       | （なし） |
| YCOM_PAYMENT | PRCS_CD       | 工程番号       | （なし） |
| YCOM_PAYMENT | PRICE         | 受入単価       | （なし） |
| YCOM_PAYMENT | PROCESS       | 工程           | （なし） |
| YCOM_PAYMENT | QTY           | 受入数         | （なし） |
| YCOM_PAYMENT | RECEIVE_DATE  | 受入日         | （なし） |
| YCOM_PAYMENT | RECEPT_LOCT   | 受渡場所       | （なし） |
| YCOM_PAYMENT | RECORD_TYPE   | レコードタイプ | （なし） |
| YCOM_PAYMENT | REFER_NO      | 照合Ｎｏ       | （なし） |
| YCOM_PAYMENT | TRANSACTOR    | 取引先         | （なし） |
| YCOM_PAYMENT | VENDOR        | 仕入先         | （なし） |
| YCOM_PAYMENT | YM_TERM       | 年月           | （なし） |

## テーブル: YCOM_PROVISION

| テーブル名     | 列ID          | 列名           | 備考     |
|:---------------|:--------------|:---------------|:---------|
| YCOM_PROVISION | A_FGROUP      | 商品分類       | （なし） |
| YCOM_PROVISION | A_FPTYPE      | 受入有支区分   | （なし） |
| YCOM_PROVISION | A_SUPPLIER    | 供給者         | （なし） |
| YCOM_PROVISION | A_USER        | 使用者         | （なし） |
| YCOM_PROVISION | AMOUNT        | 有支金額       | （なし） |
| YCOM_PROVISION | BATCH_NO      | バッチＮｏ     | （なし） |
| YCOM_PROVISION | COUNTER       | 内部登録No     | （なし） |
| YCOM_PROVISION | DELIVERY_DATE | 納入指示日     | （なし） |
| YCOM_PROVISION | DRWNO         | 部品番号       | （なし） |
| YCOM_PROVISION | IDENTIFY_CD   | 識別コード     | （なし） |
| YCOM_PROVISION | INVOICE_CD    | 伝票コード     | （なし） |
| YCOM_PROVISION | INVOICENO     | 納品書番号     | （なし） |
| YCOM_PROVISION | ISSUE_DATE    | 発行日         | （なし） |
| YCOM_PROVISION | ITEM          | 品目           | （なし） |
| YCOM_PROVISION | ITEM_CD       | 旧部品番号     | （なし） |
| YCOM_PROVISION | ITMNM         | 品名           | （なし） |
| YCOM_PROVISION | PERSON_CD     | 購買担当       | （なし） |
| YCOM_PROVISION | PRCS_CD       | 工程番号       | （なし） |
| YCOM_PROVISION | PRICE         | 有支単価       | （なし） |
| YCOM_PROVISION | PROCESS       | 工程           | （なし） |
| YCOM_PROVISION | PROVIDE_DATE  | 支給日         | （なし） |
| YCOM_PROVISION | QTY           | 支給数         | （なし） |
| YCOM_PROVISION | RECORD_TYPE   | レコードタイプ | （なし） |
| YCOM_PROVISION | REFER_NO      | 照合No         | （なし） |
| YCOM_PROVISION | TRANSACTOR    | 取引先         | （なし） |
| YCOM_PROVISION | VENDOR        | 仕入先         | （なし） |

## テーブル: YCOM_TOOLCHARGE

| テーブル名      | 列ID        | 列名           | 備考     |
|:----------------|:------------|:---------------|:---------|
| YCOM_TOOLCHARGE | A_FGROUP    | 商品分類       | （なし） |
| YCOM_TOOLCHARGE | A_FPTYPE    | 受入有支区分   | （なし） |
| YCOM_TOOLCHARGE | AMOUNT      | 型総額         | （なし） |
| YCOM_TOOLCHARGE | COUNTER     | 内部登録No     | （なし） |
| YCOM_TOOLCHARGE | DRWNO       | 部品番号       | （なし） |
| YCOM_TOOLCHARGE | ISSUE_DATE  | 発行日         | （なし） |
| YCOM_TOOLCHARGE | ITEM        | 品目           | （なし） |
| YCOM_TOOLCHARGE | ITEM_CD     | 旧部品番号     | （なし） |
| YCOM_TOOLCHARGE | ITMNM       | 品名           | （なし） |
| YCOM_TOOLCHARGE | MAKER_CD    | メーカーコード | （なし） |
| YCOM_TOOLCHARGE | PAYMENT_CNT | 累計支払回数   | （なし） |
| YCOM_TOOLCHARGE | PERSON_CD   | 購買担当       | （なし） |
| YCOM_TOOLCHARGE | PRCS_CD     | 工程番号       | （なし） |
| YCOM_TOOLCHARGE | PRICE       | 型支払金額     | （なし） |
| YCOM_TOOLCHARGE | PROCESS     | 工程           | （なし） |
| YCOM_TOOLCHARGE | RECORD_TYPE | レコードタイプ | （なし） |
| YCOM_TOOLCHARGE | SUBNUMBER   | 型追番         | （なし） |
| YCOM_TOOLCHARGE | TRANSACTOR  | 取引先         | （なし） |
| YCOM_TOOLCHARGE | VENDOR      | 仕入先         | （なし） |
| YCOM_TOOLCHARGE | YEARMONTH   | 支払月度       | （なし） |

## テーブル: YCOM_XDLPUR

| テーブル名   | 列ID          | 列名                 | 備考     |
|:-------------|:--------------|:---------------------|:---------|
| YCOM_XDLPUR  | A_FGROUP      | 商品分類             | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH1  | 1年目_第1月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH10 | 1年目_第10月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH11 | 1年目_第11月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH12 | 1年目_第12月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH13 | 2年目_第1月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH14 | 2年目_第2月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH15 | 2年目_第3月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH16 | 2年目_第4月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH17 | 2年目_第5月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH18 | 2年目_第6月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH19 | 2年目_第7月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH2  | 1年目_第2月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH20 | 2年目_第8月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH21 | 2年目_第9月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH22 | 2年目_第10月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH23 | 2年目_第11月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH24 | 2年目_第12月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH25 | 3年目_第1月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH26 | 3年目_第2月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH27 | 3年目_第3月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH28 | 3年目_第4月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH29 | 3年目_第5月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH3  | 1年目_第3月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH30 | 3年目_第6月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH31 | 3年目_第7月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH32 | 3年目_第8月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH33 | 3年目_第9月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH34 | 3年目_第10月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH35 | 3年目_第11月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH36 | 3年目_第12月実際合計 | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH4  | 1年目_第4月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH5  | 1年目_第5月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH6  | 1年目_第6月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH7  | 1年目_第7月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH8  | 1年目_第8月実際合計  | （なし） |
| YCOM_XDLPUR  | AAMNT_MONTH9  | 1年目_第9月実際合計  | （なし） |
| YCOM_XDLPUR  | ACT_PRICE     | 実際単価             | （なし） |
| YCOM_XDLPUR  | COUNTER       | 内部登録No           | （なし） |
| YCOM_XDLPUR  | DRWNO         | 部品番号             | （なし） |
| YCOM_XDLPUR  | IMNM          | 品名                 | （なし） |
| YCOM_XDLPUR  | ITEM          | 品目                 | （なし） |
| YCOM_XDLPUR  | ITEM_CD       | 旧部品番号           | （なし） |
| YCOM_XDLPUR  | MAX_UPDTD     | 最新更新日           | （なし） |
| YCOM_XDLPUR  | MTRL_COST     | 材料単価             | （なし） |
| YCOM_XDLPUR  | PRCS_COST     | 加工単価             | （なし） |
| YCOM_XDLPUR  | PROCESS       | 工程                 | （なし） |
| YCOM_XDLPUR  | QTY_MONTH1    | 1年目_第1月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH10   | 1年目_第10月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH11   | 1年目_第11月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH12   | 1年目_第12月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH13   | 2年目_第1月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH14   | 2年目_第2月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH15   | 2年目_第3月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH16   | 2年目_第4月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH17   | 2年目_第5月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH18   | 2年目_第6月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH19   | 2年目_第7月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH2    | 1年目_第2月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH20   | 2年目_第8月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH21   | 2年目_第9月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH22   | 2年目_第10月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH23   | 2年目_第11月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH24   | 2年目_第12月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH25   | 3年目_第1月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH26   | 3年目_第2月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH27   | 3年目_第3月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH28   | 3年目_第4月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH29   | 3年目_第5月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH3    | 1年目_第3月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH30   | 3年目_第6月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH31   | 3年目_第7月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH32   | 3年目_第8月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH33   | 3年目_第9月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH34   | 3年目_第10月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH35   | 3年目_第11月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH36   | 3年目_第12月数量     | （なし） |
| YCOM_XDLPUR  | QTY_MONTH4    | 1年目_第4月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH5    | 1年目_第5月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH6    | 1年目_第6月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH7    | 1年目_第7月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH8    | 1年目_第8月数量      | （なし） |
| YCOM_XDLPUR  | QTY_MONTH9    | 1年目_第9月数量      | （なし） |
| YCOM_XDLPUR  | QTY_YEAR1     | 1年目数量集計        | （なし） |
| YCOM_XDLPUR  | QTY_YEAR2     | 2年目数量集計        | （なし） |
| YCOM_XDLPUR  | QTY_YEAR3     | 3年目数量集計        | （なし） |
| YCOM_XDLPUR  | RGSTD         | 登録日               | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH1  | 1年目_第1月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH10 | 1年目_第10月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH11 | 1年目_第11月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH12 | 1年目_第12月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH13 | 2年目_第1月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH14 | 2年目_第2月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH15 | 2年目_第3月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH16 | 2年目_第4月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH17 | 2年目_第5月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH18 | 2年目_第6月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH19 | 2年目_第7月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH2  | 1年目_第2月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH20 | 2年目_第8月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH21 | 2年目_第9月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH22 | 2年目_第10月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH23 | 2年目_第11月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH24 | 2年目_第12月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH25 | 3年目_第1月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH26 | 3年目_第2月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH27 | 3年目_第3月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH28 | 3年目_第4月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH29 | 3年目_第5月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH3  | 1年目_第3月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH30 | 3年目_第6月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH31 | 3年目_第7月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH32 | 3年目_第8月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH33 | 3年目_第9月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH34 | 3年目_第10月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH35 | 3年目_第11月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH36 | 3年目_第12月標準合計 | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH4  | 1年目_第4月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH5  | 1年目_第5月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH6  | 1年目_第6月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH7  | 1年目_第7月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH8  | 1年目_第8月標準合計  | （なし） |
| YCOM_XDLPUR  | SAMNT_MONTH9  | 1年目_第9月標準合計  | （なし） |
| YCOM_XDLPUR  | STD_PRICE     | 標準単価             | （なし） |
| YCOM_XDLPUR  | SU_CODE       | S/Uコード            | （なし） |
| YCOM_XDLPUR  | TOOL_COST     | 型単価               | （なし） |
| YCOM_XDLPUR  | TRANSACTOR    | 取引先               | （なし） |
| YCOM_XDLPUR  | UPDTD         | 更新日               | （なし） |
| YCOM_XDLPUR  | UPDTWKCD      | 更新担当者           | （なし） |
| YCOM_XDLPUR  | VENDOR        | 仕入先               | （なし） |
| YCOM_XDLPUR  | XDLPUR_DT     | 発行日               | （なし） |
| YCOM_XDLPUR  | XDLPUR_FILE   | 能力検討ファイル名   | （なし） |
| YCOM_XDLPUR  | YYY_MONTH1    | 1年目_第1月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH10   | 1年目_第10月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH11   | 1年目_第11月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH12   | 1年目_第12月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH13   | 2年目_第1月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH14   | 2年目_第2月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH15   | 2年目_第3月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH16   | 2年目_第4月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH17   | 2年目_第5月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH18   | 2年目_第6月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH19   | 2年目_第7月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH2    | 1年目_第2月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH20   | 2年目_第8月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH21   | 2年目_第9月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH22   | 2年目_第10月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH23   | 2年目_第11月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH24   | 2年目_第12月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH25   | 3年目_第1月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH26   | 3年目_第2月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH27   | 3年目_第3月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH28   | 3年目_第4月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH29   | 3年目_第5月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH3    | 1年目_第3月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH30   | 3年目_第6月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH31   | 3年目_第7月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH32   | 3年目_第8月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH33   | 3年目_第9月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH34   | 3年目_第10月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH35   | 3年目_第11月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH36   | 3年目_第12月         | （なし） |
| YCOM_XDLPUR  | YYY_MONTH4    | 1年目_第4月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH5    | 1年目_第5月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH6    | 1年目_第6月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH7    | 1年目_第7月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH8    | 1年目_第8月          | （なし） |
| YCOM_XDLPUR  | YYY_MONTH9    | 1年目_第9月          | （なし） |

## テーブル: YCOM_XDLPUR_ERR

| テーブル名      | 列ID        | 列名                   | 備考     |
|:----------------|:------------|:-----------------------|:---------|
| YCOM_XDLPUR_ERR | A_FGROUP    | 商品分類               | （なし） |
| YCOM_XDLPUR_ERR | ERR_REMARKS | エラー内容             | （なし） |
| YCOM_XDLPUR_ERR | ITEM_CD     | 旧部品番号             | （なし） |
| YCOM_XDLPUR_ERR | SU_CODE     | S/U ｺｰﾄﾞ               | （なし） |
| YCOM_XDLPUR_ERR | TRANSACTOR  | 取引先                 | （なし） |
| YCOM_XDLPUR_ERR | XDLPUR_DT   | 能力検討ファイル更新日 | （なし） |
| YCOM_XDLPUR_ERR | XDLPUR_FILE | 能力検討ファイル名     | （なし） |

## テーブル: YCOM_XDLPUR_EXPL

| テーブル名       | 列ID          | 列名                   | 備考                                        |
|:-----------------|:--------------|:-----------------------|:--------------------------------------------|
| YCOM_XDLPUR_EXPL | A_FGROUP      | 商品分類               | （なし）                                    |
| YCOM_XDLPUR_EXPL | A_FMCUS       | 代表得意先             | （なし）                                    |
| YCOM_XDLPUR_EXPL | A_FPTYPE      | 購入区分               | R;固定自給;Y;有償支給;N;無償支給;G;変動自給 |
| YCOM_XDLPUR_EXPL | A_SUPPLIER    | 供給者                 | 有償支給の供給者                            |
| YCOM_XDLPUR_EXPL | A_USER        | 使用者                 | 有償支給の供給者                            |
| YCOM_XDLPUR_EXPL | A_VENDOR      | 発注先                 | 購入品、外注品の発注先                      |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH1  | 1年目_第1月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH10 | 1年目_第10月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH11 | 1年目_第11月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH12 | 1年目_第12月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH13 | 2年目_第1月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH14 | 2年目_第2月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH15 | 2年目_第3月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH16 | 2年目_第4月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH17 | 2年目_第5月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH18 | 2年目_第6月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH19 | 2年目_第7月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH2  | 1年目_第2月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH20 | 2年目_第8月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH21 | 2年目_第9月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH22 | 2年目_第10月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH23 | 2年目_第11月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH24 | 2年目_第12月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH25 | 3年目_第1月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH26 | 3年目_第2月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH27 | 3年目_第3月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH28 | 3年目_第4月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH29 | 3年目_第5月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH3  | 1年目_第3月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH30 | 3年目_第6月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH31 | 3年目_第7月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH32 | 3年目_第8月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH33 | 3年目_第9月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH34 | 3年目_第10月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH35 | 3年目_第11月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH36 | 3年目_第12月非選択合計 | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH4  | 1年目_第4月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH5  | 1年目_第5月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH6  | 1年目_第6月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH7  | 1年目_第7月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH8  | 1年目_第8月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | AAMNT_MONTH9  | 1年目_第9月非選択合計  | （なし）                                    |
| YCOM_XDLPUR_EXPL | ACT_PRICE     | 実際単価               | （なし）                                    |
| YCOM_XDLPUR_EXPL | DRWNO         | 部品番号               | （なし）                                    |
| YCOM_XDLPUR_EXPL | IMNM          | 品名                   | （なし）                                    |
| YCOM_XDLPUR_EXPL | ITEM          | 品目                   | （なし）                                    |
| YCOM_XDLPUR_EXPL | LINED         | ライン                 | （なし）                                    |
| YCOM_XDLPUR_EXPL | PROCESS       | 工程                   | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH1    | 第1月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH10   | 第10月数量             | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH11   | 第11月数量             | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH12   | 第12月数量             | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH13   | 2年目_第1月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH14   | 2年目_第2月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH15   | 2年目_第3月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH16   | 2年目_第4月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH17   | 2年目_第5月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH18   | 2年目_第6月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH19   | 2年目_第7月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH2    | 第2月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH20   | 2年目_第8月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH21   | 2年目_第9月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH22   | 2年目_第10月数量       | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH23   | 2年目_第11月数量       | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH24   | 2年目_第12月数量       | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH25   | 3年目_第1月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH26   | 3年目_第2月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH27   | 3年目_第3月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH28   | 3年目_第4月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH29   | 3年目_第5月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH3    | 第3月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH30   | 3年目_第6月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH31   | 3年目_第7月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH32   | 3年目_第8月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH33   | 3年目_第9月数量        | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH34   | 3年目_第10月数量       | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH35   | 3年目_第11月数量       | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH36   | 3年目_第12月数量       | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH4    | 第4月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH5    | 第5月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH6    | 第6月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH7    | 第7月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH8    | 第8月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | QTY_MONTH9    | 第9月数量              | （なし）                                    |
| YCOM_XDLPUR_EXPL | RGSTD         | 登録日                 | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH1  | 1年目_第1月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH10 | 1年目_第10月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH11 | 1年目_第11月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH12 | 1年目_第12月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH13 | 2年目_第1月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH14 | 2年目_第2月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH15 | 2年目_第3月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH16 | 2年目_第4月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH17 | 2年目_第5月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH18 | 2年目_第6月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH19 | 2年目_第7月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH2  | 1年目_第2月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH20 | 2年目_第8月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH21 | 2年目_第9月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH22 | 2年目_第10月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH23 | 2年目_第11月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH24 | 2年目_第12月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH25 | 3年目_第1月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH26 | 3年目_第2月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH27 | 3年目_第3月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH28 | 3年目_第4月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH29 | 3年目_第5月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH3  | 1年目_第3月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH30 | 3年目_第6月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH31 | 3年目_第7月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH32 | 3年目_第8月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH33 | 3年目_第9月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH34 | 3年目_第10月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH35 | 3年目_第11月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH36 | 3年目_第12月選択合計   | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH4  | 1年目_第4月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH5  | 1年目_第5月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH6  | 1年目_第6月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH7  | 1年目_第7月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH8  | 1年目_第8月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | SAMNT_MONTH9  | 1年目_第9月選択合計    | （なし）                                    |
| YCOM_XDLPUR_EXPL | STD_PRICE     | 標準単価               | （なし）                                    |
| YCOM_XDLPUR_EXPL | TRANSACTOR    | 取引先                 | （なし）                                    |
| YCOM_XDLPUR_EXPL | VENDOR        | 仕入先                 | （なし）                                    |
| YCOM_XDLPUR_EXPL | XDLPUR_DT     | 発行日                 | （なし）                                    |
| YCOM_XDLPUR_EXPL | XDLPUR_FILE   | 能力検討ファイル名     | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH1    | 1年目_第1月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH10   | 1年目_第10月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH11   | 1年目_第11月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH12   | 1年目_第12月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH13   | 2年目_第1月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH14   | 2年目_第2月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH15   | 2年目_第3月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH16   | 2年目_第4月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH17   | 2年目_第5月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH18   | 2年目_第6月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH19   | 2年目_第7月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH2    | 1年目_第2月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH20   | 2年目_第8月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH21   | 2年目_第9月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH22   | 2年目_第10月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH23   | 2年目_第11月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH24   | 2年目_第12月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH25   | 3年目_第1月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH26   | 3年目_第2月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH27   | 3年目_第3月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH28   | 3年目_第4月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH29   | 3年目_第5月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH3    | 1年目_第3月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH30   | 3年目_第6月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH31   | 3年目_第7月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH32   | 3年目_第8月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH33   | 3年目_第9月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH34   | 3年目_第10月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH35   | 3年目_第11月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH36   | 3年目_第12月           | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH4    | 1年目_第4月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH5    | 1年目_第5月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH6    | 1年目_第6月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH7    | 1年目_第7月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH8    | 1年目_第8月            | （なし）                                    |
| YCOM_XDLPUR_EXPL | YYY_MONTH9    | 1年目_第9月            | （なし）                                    |

## テーブル: YCOM_XDLPUR_SET

| テーブル名      | 列ID   | 列名     | 備考            |
|:----------------|:-------|:---------|:----------------|
| YCOM_XDLPUR_SET | GAICU  | 外注費F  | 0;選択;1;非選択 |
| YCOM_XDLPUR_SET | K_NO   | キー項目 | （なし）        |
| YCOM_XDLPUR_SET | KAKOU  | 加工費F  | 0;選択;1;非選択 |
| YCOM_XDLPUR_SET | KANRI  | 管理費F  | 0;選択;1;非選択 |
| YCOM_XDLPUR_SET | KONYU  | 購入費F  | 0;選択;1;非選択 |
| YCOM_XDLPUR_SET | SIKYU  | 支給費F  | 0;選択;1;非選択 |
| YCOM_XDLPUR_SET | SOZAI  | 素材費F  | 0;選択;1;非選択 |

## テーブル: Y_BFMSALES

| テーブル名   | 列ID         | 列名       | 備考            |
|:-------------|:-------------|:-----------|:----------------|
| Y_BFMSALES   | A_FGROUP     | 商品分類   | （なし）        |
| Y_BFMSALES   | A_FPCLASS    | クラス     | （なし）        |
| Y_BFMSALES   | AMOUNT       | 受注金額   | （なし）        |
| Y_BFMSALES   | CLASSNM      | クラス名   | （なし）        |
| Y_BFMSALES   | CUSTOMNO     | 顧客注番   | （なし）        |
| Y_BFMSALES   | DELIDATE     | 納入日     | （なし）        |
| Y_BFMSALES   | DRWNO        | 部品番号   | （なし）        |
| Y_BFMSALES   | IMNM         | 品名       | （なし）        |
| Y_BFMSALES   | ITEM         | 品目       | （なし）        |
| Y_BFMSALES   | LOCT         | 入出庫場所 | （なし）        |
| Y_BFMSALES   | PRICE        | 単価       | （なし）        |
| Y_BFMSALES   | PROCESS      | 工程       | （なし）        |
| Y_BFMSALES   | QTY          | 納入数     | （なし）        |
| Y_BFMSALES   | RECORDNO     | 受注No     | （なし）        |
| Y_BFMSALES   | RGSTD        | 作成日     | （なし）        |
| Y_BFMSALES   | SHPMNTNO     | 出荷No     | （なし）        |
| Y_BFMSALES   | TRANSACTOR   | 取引先     | （なし）        |
| Y_BFMSALES   | TRANSACTORNM | 取引先名   | 0;顧客;1;仕入先 |
| Y_BFMSALES   | VENDOR       | 仕入先     | （なし）        |

## テーブル: Y_PRODUCTFORECAST

| テーブル名        | 列ID            | 列名            | 備考            |
|:------------------|:----------------|:----------------|:----------------|
| Y_PRODUCTFORECAST | A_FGROUP        | 商品分類        | （なし）        |
| Y_PRODUCTFORECAST | A_FPCLASS       | クラス          | （なし）        |
| Y_PRODUCTFORECAST | A_FPCLASS2      | クラス２        | （なし）        |
| Y_PRODUCTFORECAST | CLASSNM         | クラス名        | （なし）        |
| Y_PRODUCTFORECAST | DRWNO           | 部品番号        | （なし）        |
| Y_PRODUCTFORECAST | IMNM            | 品名            | （なし）        |
| Y_PRODUCTFORECAST | ITEM            | 品目            | （なし）        |
| Y_PRODUCTFORECAST | LINED           | ライン          | （なし）        |
| Y_PRODUCTFORECAST | MONTH1          | 1ヶ月目         | （なし）        |
| Y_PRODUCTFORECAST | MONTH2          | 2ヶ月目         | （なし）        |
| Y_PRODUCTFORECAST | MONTH3          | 3ヶ月目         | （なし）        |
| Y_PRODUCTFORECAST | MONTH4          | 4ヶ月目         | （なし）        |
| Y_PRODUCTFORECAST | PROCESS         | 工程            | （なし）        |
| Y_PRODUCTFORECAST | PROCESS_CHARGE1 | 第1月社内加工費 | （なし）        |
| Y_PRODUCTFORECAST | PROCESS_CHARGE2 | 第2月社内加工費 | （なし）        |
| Y_PRODUCTFORECAST | PROCESS_CHARGE3 | 第3月社内加工費 | （なし）        |
| Y_PRODUCTFORECAST | PROCESS_CHARGE4 | 第4月社内加工費 | （なし）        |
| Y_PRODUCTFORECAST | QTY1            | 第1月数量       | （なし）        |
| Y_PRODUCTFORECAST | QTY2            | 第2月数量       | （なし）        |
| Y_PRODUCTFORECAST | QTY3            | 第3月数量       | （なし）        |
| Y_PRODUCTFORECAST | QTY4            | 第4月数量       | （なし）        |
| Y_PRODUCTFORECAST | RGSTD           | 作成日          | （なし）        |
| Y_PRODUCTFORECAST | SECT            | 担当部門        | （なし）        |
| Y_PRODUCTFORECAST | TRANSACTOR      | 取引先          | （なし）        |
| Y_PRODUCTFORECAST | TRANSACTORNM    | 取引先名        | 0;顧客;1;仕入先 |
| Y_PRODUCTFORECAST | VENDOR          | 仕入先          | （なし）        |

## テーブル: Y_PURCHASEFORECAST

| テーブル名         | 列ID           | 列名              | 備考                   |
|:-------------------|:---------------|:------------------|:-----------------------|
| Y_PURCHASEFORECAST | A_FGROUP       | 商品分類          | （なし）               |
| Y_PURCHASEFORECAST | A_FPCLASS      | クラス            | （なし）               |
| Y_PURCHASEFORECAST | A_FPCLASS2     | クラス２          | （なし）               |
| Y_PURCHASEFORECAST | A_VENDOR       | 発注先            | 購入品、外注品の発注先 |
| Y_PURCHASEFORECAST | CLASSNM        | クラス名          | （なし）               |
| Y_PURCHASEFORECAST | DRWNO          | 部品番号          | （なし）               |
| Y_PURCHASEFORECAST | IMNM           | 品名              | （なし）               |
| Y_PURCHASEFORECAST | ITEM           | 品目              | （なし）               |
| Y_PURCHASEFORECAST | MONTH1         | 1ヶ月目           | （なし）               |
| Y_PURCHASEFORECAST | MONTH2         | 2ヶ月目           | （なし）               |
| Y_PURCHASEFORECAST | MONTH3         | 3ヶ月目           | （なし）               |
| Y_PURCHASEFORECAST | MONTH4         | 4ヶ月目           | （なし）               |
| Y_PURCHASEFORECAST | PROCESS        | 工程              | （なし）               |
| Y_PURCHASEFORECAST | PURCHASE_COST1 | 第1月仕入・材料費 | （なし）               |
| Y_PURCHASEFORECAST | PURCHASE_COST2 | 第2月仕入・材料費 | （なし）               |
| Y_PURCHASEFORECAST | PURCHASE_COST3 | 第3月仕入・材料費 | （なし）               |
| Y_PURCHASEFORECAST | PURCHASE_COST4 | 第4月仕入・材料費 | （なし）               |
| Y_PURCHASEFORECAST | QTY1           | 第1月数量         | （なし）               |
| Y_PURCHASEFORECAST | QTY2           | 第2月数量         | （なし）               |
| Y_PURCHASEFORECAST | QTY3           | 第3月数量         | （なし）               |
| Y_PURCHASEFORECAST | QTY4           | 第4月数量         | （なし）               |
| Y_PURCHASEFORECAST | RGSTD          | 登録日            | （なし）               |
| Y_PURCHASEFORECAST | TRANSACTOR     | 取引先            | （なし）               |
| Y_PURCHASEFORECAST | TRANSACTORNM   | 取引先名          | 0;顧客;1;仕入先        |
| Y_PURCHASEFORECAST | VENDOR         | 仕入先            | （なし）               |

## テーブル: Y_SALESFORECAST

| テーブル名      | 列ID            | 列名            | 備考            |
|:----------------|:----------------|:----------------|:----------------|
| Y_SALESFORECAST | A_FGROUP        | 商品分類        | （なし）        |
| Y_SALESFORECAST | A_FPCLASS       | クラス          | （なし）        |
| Y_SALESFORECAST | A_FPCLASS2      | クラス２        | （なし）        |
| Y_SALESFORECAST | CLASSNM         | クラス名        | （なし）        |
| Y_SALESFORECAST | DRWNO           | 部品番号        | （なし）        |
| Y_SALESFORECAST | IMNM            | 品名            | （なし）        |
| Y_SALESFORECAST | ITEM            | 品目            | （なし）        |
| Y_SALESFORECAST | LINED           | ライン          | （なし）        |
| Y_SALESFORECAST | MONTH1          | 1ヶ月目         | （なし）        |
| Y_SALESFORECAST | MONTH2          | 2ヶ月目         | （なし）        |
| Y_SALESFORECAST | MONTH3          | 3ヶ月目         | （なし）        |
| Y_SALESFORECAST | MONTH4          | 4ヶ月目         | （なし）        |
| Y_SALESFORECAST | PROCESS         | 工程            | （なし）        |
| Y_SALESFORECAST | PROCESS_CHARGE1 | 第1月社内加工費 | （なし）        |
| Y_SALESFORECAST | PROCESS_CHARGE2 | 第2月社内加工費 | （なし）        |
| Y_SALESFORECAST | PROCESS_CHARGE3 | 第3月社内加工費 | （なし）        |
| Y_SALESFORECAST | PROCESS_CHARGE4 | 第4月社内加工費 | （なし）        |
| Y_SALESFORECAST | QTY1            | 第1月数量       | （なし）        |
| Y_SALESFORECAST | QTY2            | 第2月数量       | （なし）        |
| Y_SALESFORECAST | QTY3            | 第3月数量       | （なし）        |
| Y_SALESFORECAST | QTY4            | 第4月数量       | （なし）        |
| Y_SALESFORECAST | RGSTD           | 作成日          | （なし）        |
| Y_SALESFORECAST | SECT            | 担当部門        | （なし）        |
| Y_SALESFORECAST | TRANSACTOR      | 取引先          | （なし）        |
| Y_SALESFORECAST | TRANSACTORNM    | 取引先名        | 0;顧客;1;仕入先 |
| Y_SALESFORECAST | VENDOR          | 仕入先          | （なし）        |

## テーブル: Y_SALESFORECASTD

| テーブル名       | 列ID             | 列名              | 備考            |
|:-----------------|:-----------------|:------------------|:----------------|
| Y_SALESFORECASTD | A_FGROUP         | 商品分類          | （なし）        |
| Y_SALESFORECASTD | A_FPCLASS        | クラス            | （なし）        |
| Y_SALESFORECASTD | A_FPCLASS2       | クラス２          | （なし）        |
| Y_SALESFORECASTD | AMOUNT1          | 第1月売上高       | （なし）        |
| Y_SALESFORECASTD | AMOUNT2          | 第2月売上高       | （なし）        |
| Y_SALESFORECASTD | AMOUNT3          | 第3月売上高       | （なし）        |
| Y_SALESFORECASTD | AMOUNT4          | 第4月売上高       | （なし）        |
| Y_SALESFORECASTD | CLASSNM          | クラス名          | （なし）        |
| Y_SALESFORECASTD | COUNT1           | 第1月件数         | （なし）        |
| Y_SALESFORECASTD | COUNT2           | 第2月件数         | （なし）        |
| Y_SALESFORECASTD | COUNT3           | 第3月件数         | （なし）        |
| Y_SALESFORECASTD | COUNT4           | 第4月件数         | （なし）        |
| Y_SALESFORECASTD | COUNTER          | ﾚｺｰﾄﾞNo           | （なし）        |
| Y_SALESFORECASTD | DATATYPE         | データ区分        | （なし）        |
| Y_SALESFORECASTD | DRWNO            | 部品番号          | （なし）        |
| Y_SALESFORECASTD | IMNM             | 品名              | （なし）        |
| Y_SALESFORECASTD | ITEM             | 品目              | （なし）        |
| Y_SALESFORECASTD | MONTH1           | 1ヶ月目           | （なし）        |
| Y_SALESFORECASTD | MONTH2           | 2ヶ月目           | （なし）        |
| Y_SALESFORECASTD | MONTH3           | 3ヶ月目           | （なし）        |
| Y_SALESFORECASTD | MONTH4           | 4ヶ月目           | （なし）        |
| Y_SALESFORECASTD | PROCESS          | 工程              | （なし）        |
| Y_SALESFORECASTD | PROCESS_CHARGE1  | 第1月社内加工費   | （なし）        |
| Y_SALESFORECASTD | PROCESS_CHARGE2  | 第2月社内加工費   | （なし）        |
| Y_SALESFORECASTD | PROCESS_CHARGE3  | 第3月社内加工費   | （なし）        |
| Y_SALESFORECASTD | PROCESS_CHARGE4  | 第4月社内加工費   | （なし）        |
| Y_SALESFORECASTD | PURCHASE_COST1   | 第1月仕入・材料費 | （なし）        |
| Y_SALESFORECASTD | PURCHASE_COST2   | 第2月仕入・材料費 | （なし）        |
| Y_SALESFORECASTD | PURCHASE_COST3   | 第3月仕入・材料費 | （なし）        |
| Y_SALESFORECASTD | PURCHASE_COST4   | 第4月仕入・材料費 | （なし）        |
| Y_SALESFORECASTD | QTY1             | 第1月数量         | （なし）        |
| Y_SALESFORECASTD | QTY2             | 第2月数量         | （なし）        |
| Y_SALESFORECASTD | QTY3             | 第3月数量         | （なし）        |
| Y_SALESFORECASTD | QTY4             | 第4月数量         | （なし）        |
| Y_SALESFORECASTD | RGSTD            | 作成日            | （なし）        |
| Y_SALESFORECASTD | SBCNTRCT_CHARGE1 | 第1月外注加工費   | （なし）        |
| Y_SALESFORECASTD | SBCNTRCT_CHARGE2 | 第2月外注加工費   | （なし）        |
| Y_SALESFORECASTD | SBCNTRCT_CHARGE3 | 第3月外注加工費   | （なし）        |
| Y_SALESFORECASTD | SBCNTRCT_CHARGE4 | 第4月外注加工費   | （なし）        |
| Y_SALESFORECASTD | TRANSACTOR       | 取引先            | （なし）        |
| Y_SALESFORECASTD | TRANSACTORNM     | 取引先名          | 0;顧客;1;仕入先 |
| Y_SALESFORECASTD | VENDOR           | 仕入先            | （なし）        |

## テーブル: Y_SBCNTFORECAST

| テーブル名      | 列ID             | 列名            | 備考                   |
|:----------------|:-----------------|:----------------|:-----------------------|
| Y_SBCNTFORECAST | A_FGROUP         | 商品分類        | （なし）               |
| Y_SBCNTFORECAST | A_FPCLASS        | クラス          | （なし）               |
| Y_SBCNTFORECAST | A_FPCLASS2       | クラス２        | （なし）               |
| Y_SBCNTFORECAST | A_VENDOR         | 発注先          | 購入品、外注品の発注先 |
| Y_SBCNTFORECAST | CLASSNM          | クラス名        | （なし）               |
| Y_SBCNTFORECAST | DRWNO            | 部品番号        | （なし）               |
| Y_SBCNTFORECAST | IMNM             | 品名            | （なし）               |
| Y_SBCNTFORECAST | ITEM             | 品目            | （なし）               |
| Y_SBCNTFORECAST | MONTH1           | 1ヶ月目         | （なし）               |
| Y_SBCNTFORECAST | MONTH2           | 2ヶ月目         | （なし）               |
| Y_SBCNTFORECAST | MONTH3           | 3ヶ月目         | （なし）               |
| Y_SBCNTFORECAST | MONTH4           | 4ヶ月目         | （なし）               |
| Y_SBCNTFORECAST | PROCESS          | 工程            | （なし）               |
| Y_SBCNTFORECAST | QTY1             | 第1月数量       | （なし）               |
| Y_SBCNTFORECAST | QTY2             | 第2月数量       | （なし）               |
| Y_SBCNTFORECAST | QTY3             | 第3月数量       | （なし）               |
| Y_SBCNTFORECAST | QTY4             | 第4月数量       | （なし）               |
| Y_SBCNTFORECAST | RGSTD            | 作成日          | （なし）               |
| Y_SBCNTFORECAST | SBCNTRCT_CHARGE1 | 第1月外注加工費 | （なし）               |
| Y_SBCNTFORECAST | SBCNTRCT_CHARGE2 | 第2月外注加工費 | （なし）               |
| Y_SBCNTFORECAST | SBCNTRCT_CHARGE3 | 第3月外注加工費 | （なし）               |
| Y_SBCNTFORECAST | SBCNTRCT_CHARGE4 | 第4月外注加工費 | （なし）               |
| Y_SBCNTFORECAST | TRANSACTOR       | 取引先          | （なし）               |
| Y_SBCNTFORECAST | TRANSACTORNM     | 取引先名        | 0;顧客;1;仕入先        |
| Y_SBCNTFORECAST | VENDOR           | 仕入先          | （なし）               |

