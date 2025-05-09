import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

# SQLAlchemyの接続設定（.env から取得）
user = os.getenv('ORACLE_USER')
password = os.getenv('ORACLE_PASSWORD')
host = os.getenv('ORACLE_HOST')
port = os.getenv('ORACLE_PORT')
service_name = os.getenv('ORACLE_SERVICE')

DATABASE_URL = f'oracle+cx_oracle://{user}:{password}@{host}:{port}/?service_name={service_name}'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Streamlitのタイトル設定
st.title("付加価値高データ取得")

# 期間選択 初期値は今月の1日と月末
today = pd.to_datetime("today")
start_date = st.date_input("開始日", today.replace(day=1))
end_date = st.date_input("終了日", start_date.replace(day=1) + pd.offsets.MonthEnd(1))

# 集計モード選択
mode = st.radio("集計モードを選択", ["月次集計（顧客別）", "月次集計（全体）", "オーダー単位"])

# クエリ生成関数（月次集計：顧客別）
def fetch_value_added_summary(start_date, end_date):
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
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)

# クエリ生成関数（月次集計：全体）
def fetch_value_added_summary_total(start_date, end_date):
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
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)

# クエリ生成関数（オーダー単位）
def fetch_value_added_orders(start_date, end_date):
    query = f"""
    SELECT
        s.PROCESS AS 工程,
        s.ITEM AS 品目,
        s.CUSTOM AS 顧客CD,
        s.DELIDATE AS 納期,
        s.ORDERQTY AS 受注数,
        s.SHIPQTY AS 納品数,
        p.PRICE AS 単価,
        p.APPLYDATE AS 単価適用日,
        ct.ACT_PS1 AS 素材,
        ct.ACT_PS6 AS 支給,
        ct.ACT_PS2 AS 購買,
        ct.ACT_PS3 AS 外注,
        p.PRICE 
            - COALESCE(ct.ACT_PS1, 0) 
            - COALESCE(ct.ACT_PS2, 0) 
            - COALESCE(ct.ACT_PS3, 0) 
            - COALESCE(ct.ACT_PS6, 0) AS 付加価値,
        CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END * p.PRICE AS 受注額,    
        CASE WHEN s.CMPFLG = 1 THEN s.SHIPQTY ELSE s.ORDERQTY END * (p.PRICE - COALESCE(ct.ACT_PS1, 0) - COALESCE(ct.ACT_PS2, 0) - COALESCE(ct.ACT_PS3, 0) - COALESCE(ct.ACT_PS6, 0)) AS 付加価値計
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
        ON s.PROCESS = ct.PRDCT_PROCESS AND s.ITEM = ct.PRDCT_ITEM AND ct.LEVELD = 'o1'
    WHERE 
        s.DELIDATE BETWEEN TO_DATE('{start_date}', 'YYYY-MM-DD') AND TO_DATE('{end_date}', 'YYYY-MM-DD')
    ORDER BY s.ITEM, s.DELIDATE
    """
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)

# データ取得ボタン
if st.button("データ取得"):
    if mode == "月次集計（顧客別）":
        df = fetch_value_added_summary(start_date, end_date)
    elif mode == "月次集計（全体）":
        df = fetch_value_added_summary_total(start_date, end_date)
    else:
        df = fetch_value_added_orders(start_date, end_date)

    st.dataframe(df)
    st.download_button(
        label="CSVでダウンロード",
        data=df.to_csv(index=False).encode('utf-8-sig'),
        file_name='value_added.csv',
        mime='text/csv',
    )
