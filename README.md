# ACCROAD_Subsystems

Oracle データベースと連携し、取引先やオーダー単位での付加価値計算を行う社内向けの分析支援アプリです。  
Streamlit を用いたWebアプリケーションとして提供されます。

---

## 📦 主な機能

- 月次単位での付加価値集計（顧客別／全体）
- オーダー単位での詳細な原価・付加価値表示
- 実績（CMPFLG = 1）＋予測（CMPFLG = 0）の混合集計
- CSV出力対応

---

## 🚀 セットアップ手順

### 1. 必要ライブラリのインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数ファイル `.env` の作成

リポジトリルートに `.env` を作成し、以下の内容を記入してください。

```env
ORACLE_USER=your_user
ORACLE_PASSWORD=your_password
ORACLE_HOST=your_host
ORACLE_PORT=1521
ORACLE_SERVICE=your_service
```

※ `.env.template` を参考にしてください。

---

## ▶️ 実行方法

```bash
streamlit run main.py
```

サイドバーから「付加価値取得」を選択してください。

---

## 📁 ディレクトリ構成

```
.
├── main.py              # トップ画面（リリース履歴など）
├── pages/
│   └── 付加価値取得.py    # 主要機能：付加価値計算
├── docs/
│   ├── table_config.csv
│   └── table_details.csv
├── requirements.txt
├── .env.template
└── README.md
```

---

## 🕒 リリース履歴

- **2025/5/7 v0.0.1**: ベータ版として付加価値計算機能を導入

---

## 📌 注意

- このリポジトリは社内用途向けで、外部公開を想定していません。
- `.env` は絶対にGitに含めないでください。
