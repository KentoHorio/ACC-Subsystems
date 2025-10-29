import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta

import db.database as db

# ページ設定
st.set_page_config(
    page_title="付加価値分析",
    page_icon="📊",
    layout="wide"
)

st.title("📊 付加価値分析")
st.markdown("---")

# 期間選択
st.subheader("📅 期間選択")
col1, col2 = st.columns(2)

today = pd.to_datetime("today")
with col1:
    start_date = st.date_input("開始日", today.replace(day=1))
with col2:
    # 月末を計算
    if today.month == 12:
        next_month = today.replace(year=today.year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
    default_end = (next_month - timedelta(days=1)).date()
    end_date = st.date_input("終了日", default_end)

st.markdown("---")

# 集計モード選択
st.subheader("📋 集計モード")
mode = st.radio(
    "表示する集計形式を選択してください",
    ["① 月次・客先別サマリー", "② 月次・オーダー単位詳細"],
    horizontal=True
)

st.markdown("---")

# データ取得ボタン
if st.button("🔍 データ取得", type="primary", use_container_width=True):
    with st.spinner("データを取得中..."):
        try:
            # データベースマネージャーの初期化
            manager = db.ValueAddedDataManager()

            # v2 SQLでオーダー単位のデータを取得
            df_orders = manager.fetch_value_added_orders_v2(
                start_date.strftime('%Y-%m-%d'),
                end_date.strftime('%Y-%m-%d')
            )

            if len(df_orders) == 0:
                st.warning("⚠️ 指定期間のデータが見つかりませんでした。")
            else:
                st.success(f"✓ データ取得完了: {len(df_orders)} 件")

                # セッションステートにデータを保存
                st.session_state['df_orders'] = df_orders
                st.session_state['start_date'] = start_date
                st.session_state['end_date'] = end_date
                st.session_state['mode'] = mode

        except Exception as e:
            st.error(f"❌ エラーが発生しました: {str(e)}")
            import traceback
            with st.expander("詳細なエラー情報"):
                st.code(traceback.format_exc())

# データが取得済みの場合は表示
if 'df_orders' in st.session_state:
    df_orders = st.session_state['df_orders']
    mode = st.session_state['mode']
    start_date = st.session_state['start_date']
    end_date = st.session_state['end_date']

    st.markdown("---")

    if mode == "① 月次・客先別サマリー":
        st.subheader("📊 月次・客先別サマリー")

        # 月次・顧客別に集計
        df_orders['年月'] = pd.to_datetime(df_orders['納期']).dt.to_period('M').astype(str)

        # 各コストを数量で乗算
        df_orders['仕入材料費_合計'] = df_orders['仕入材料費'].fillna(0) * df_orders['数量']
        df_orders['有償支給費_合計'] = df_orders['有償支給費'].fillna(0) * df_orders['数量']

        df_summary = df_orders.groupby(['年月', '顧客']).agg({
            '数量': 'sum',
            '売価': lambda x: (x * df_orders.loc[x.index, '数量']).sum(),
            '外注費': lambda x: (x.fillna(0) * df_orders.loc[x.index, '数量']).sum(),
            '仕入材料費_合計': 'sum',
            '有償支給費_合計': 'sum',
            '原価合計': lambda x: (x.fillna(0) * df_orders.loc[x.index, '数量']).sum(),
            '付加価値': 'sum',
        }).reset_index()

        # 列名を変更
        df_summary.columns = [
            '年月', '顧客', '数量', '売上高', '外注費',
            '仕入材料費', '有償支給費', '原価合計', '付加価値'
        ]

        # 付加価値率を計算
        df_summary['付加価値率(%)'] = (
            df_summary['付加価値'] / df_summary['売上高'] * 100
        ).round(2)

        # ソート
        df_summary = df_summary.sort_values(['年月', '付加価値'], ascending=[True, False])

        # 表示用にフォーマット
        df_display = df_summary.copy()
        for col in ['数量', '売上高', '外注費', '仕入材料費', '有償支給費', '原価合計', '付加価値']:
            df_display[col] = df_display[col].apply(lambda x: f"{x:,.0f}")

        # データフレーム表示
        st.dataframe(
            df_display,
            width='stretch',
            height=400
        )

        # 統計情報
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("総売上高", f"{df_summary['売上高'].sum():,.0f} 円")
        with col2:
            st.metric("総原価", f"{df_summary['原価合計'].sum():,.0f} 円")
        with col3:
            st.metric("総付加価値", f"{df_summary['付加価値'].sum():,.0f} 円")
        with col4:
            avg_rate = df_summary['付加価値'].sum() / df_summary['売上高'].sum() * 100
            st.metric("平均付加価値率", f"{avg_rate:.2f} %")

        # Excelエクスポート用のデータフレーム（元の数値）
        export_df = df_summary
        sheet_name = "月次_客先別サマリー"

    else:  # ② 月次・オーダー単位詳細
        st.subheader("📋 月次・オーダー単位詳細")

        # 仕入材料費は既にSQLで統合済み
        df_detail = df_orders.copy()

        # 必要な列のみを選択し、並び替え
        detail_cols = [
            'オーダーNO', '品目', '工程', '納期', '顧客', '数量', '売価',
            '外注費', '仕入材料費', '有償支給費', '原価合計', '付加価値'
        ]

        df_detail = df_detail[detail_cols]

        # ソート
        df_detail = df_detail.sort_values(['納期', 'オーダーNO'])

        # 表示用にフォーマット
        df_display = df_detail.copy()
        df_display['納期'] = pd.to_datetime(df_display['納期']).dt.strftime('%Y-%m-%d')

        for col in ['数量', '売価', '外注費', '仕入材料費', '有償支給費', '原価合計', '付加価値']:
            if col == '数量':
                df_display[col] = df_display[col].apply(lambda x: f"{x:,}")
            else:
                df_display[col] = df_display[col].apply(
                    lambda x: f"{x:,.2f}" if pd.notna(x) else "-"
                )

        # データフレーム表示
        st.dataframe(
            df_display,
            width='stretch',
            height=400
        )

        # 統計情報
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_sales = (df_detail['売価'] * df_detail['数量']).sum()
            st.metric("総売上高", f"{total_sales:,.0f} 円")
        with col2:
            total_cost = (df_detail['原価合計'].fillna(0) * df_detail['数量']).sum()
            st.metric("総原価", f"{total_cost:,.0f} 円")
        with col3:
            total_value = df_detail['付加価値'].sum()
            st.metric("総付加価値", f"{total_value:,.0f} 円")
        with col4:
            avg_rate = total_value / total_sales * 100 if total_sales > 0 else 0
            st.metric("平均付加価値率", f"{avg_rate:.2f} %")

        # Excelエクスポート用のデータフレーム
        export_df = df_detail
        sheet_name = "オーダー単位詳細"

    st.markdown("---")

    # Excelエクスポート
    st.subheader("📥 エクスポート")

    # Excelファイルを作成
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        export_df.to_excel(writer, sheet_name=sheet_name, index=False)

        # ワークシートを取得して列幅を調整
        worksheet = writer.sheets[sheet_name]
        for idx, col in enumerate(export_df.columns, 1):
            max_length = max(
                export_df[col].astype(str).map(len).max(),
                len(str(col))
            )
            worksheet.column_dimensions[chr(64 + idx)].width = min(max_length + 2, 50)

    excel_data = output.getvalue()

    # ファイル名を生成
    mode_name = "月次客先別" if mode == "① 月次・客先別サマリー" else "オーダー単位"
    filename = f"付加価値分析_{mode_name}_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.xlsx"

    col1, col2 = st.columns([1, 3])
    with col1:
        st.download_button(
            label="📊 Excelでダウンロード",
            data=excel_data,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
            type="primary"
        )
    with col2:
        st.info(f"ℹ️ ファイル名: {filename}")

else:
    st.info("👆 期間と集計モードを選択して「データ取得」ボタンをクリックしてください。")
