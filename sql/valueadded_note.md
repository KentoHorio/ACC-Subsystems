# ACCROADについてのメモ

## 付加価値

付加価値 = 売価−原価

## 付加価値計算に使うテーブル情報

- SHIPORDER
- MPS
- COST_TREE
- M_ITEM
- M_TRANSACTOR
- M_PRICE
- M_BOM2

## SHIPORDERとMPSの使い分け

どちらも受注・内示情報が格納されたテーブルですが下記方針で取得します
1. 過去-当月 : SHIPORDER
2. 翌月以降 : M_TRANSACTOR.A_EDIF=1ならばSHIPORDERから、それ以外はMPSから取得する。 SHIPORDER、MPS共にCUSTOMのカラムをM_TRANSACTOR.TRANSACTORを結合して参照する

## 付加価値の計算

SHIPORDERのDELIDATE、MPSのPLANDATEを基準にその時点での売価および仕入価格を利用して付加価値を計算したいです。

## 製品構成の取得

COST_TREEはBOMとしてのみ使い、それ以外の用途で使ってはいけない
PRDCT_PROCESSとPRDCT_ITEMをキーにして検索した情報を元にBOMを取得する
価格の情報があるが、売価や仕入価格はM_PRICEから取得すること
売値はPRICE、買値はACT_PRICEを参照する
PROCESS = 'GEN'だけは特殊で自身のレコードよりも1レコード上位で取得された品目をHPROCESS,HITEM、
自身をLPROCESS,LITEMに指定してM_BOM2からレコードを取得、PRICE*(ACT_PHUNIT+ACT_SCR_PHUNIT)を
材料費として扱う

## 外注・購買費・売価

M_PRICE.SPFLAG="P": 仕入外注費
M_PRICE.SPFLAG="S": 売価

M_PRICE.ACT_PRICE: 外部コスト
M_PRICE.PRICE: イハラがもらうお金

PROCESS = 'GEN'

## 仕入外注費の細分化

1. 有償支給費: M_ITEM.A_FPTYPE = 'Y'
2. 自給素材費: M_ITEM.A_FPTYPE != 'Y' && M_ITEM.IMTYP = '1' && M_ITEM.PROCESS IN ('GEN','SOZ')
3. 購入費: M_ITEM.A_FPTYPE != 'Y' && M_ITEM.IMTYP = '1' && M_ITEM.PROCESS NOT IN ('GEN','SOZ')
4. 外注費: M_ITEM.A_FPTYPE != 'Y' && M_ITEM.IMTYP = '2'
5. 原材料費: PROCESS = 'GEN'はCOST_TREEのRECORD_ID - 1 の品目をHPROCESS,HITEMにLPROCESS,LITEMを自分自身を指定の上、M_BOM2を参照
