import pandas as pd

df = pd.read_csv("sample.csv")

#先頭5行
print(df.head())
#行数・列数
# print(df.shape)
#列名
# print(df.columns)
#データの概要
# print(df.info())
#統計量
# print(df.describe())
#単列
# print(df["読書"])
#複数列
# print(df[["読書","コーディング"]])
#0番目の行
# print(df.loc[0])
#行番号で複数行
# print(df.loc[0:3])
#読書が1の行だけ
# print(df[df["読書"] == 1])
# print(df[df["読書"] != 1])
#Not条件(~以外)
# print(df[~(df["読書"] == 1)])
#読書=1勝コーディング=1
# print(df[(df["読書"] == 1) & (df["コーディング"] == 1)])
# print(df[(df["読書"] == 1) | (df["コーディング"] == 1)])
# 列の追加
# df["新しい列"] = 1
# print(df.head())
# #計算で作る列
# df["合計"] = df["読書"] + df["コーディング"]
# 欠損値の有無確認
# print(df["合計"])
# print(df.isna().sum())
#欠損を埋める
# print(df.fillna(0))
# csvに保存
# df.to_csv("output.csv",index=False)
# print(df.sort_values("読書",ascending=False))
# print(df.head(2))
#さらに条件で絞る
# print(df["コーディング"] + df["読書"] > 1)
#group by
# print(df.groupby("読書").mean())
# print(df.groupby("読書")["コーディング"].mean())
# print(df["読書"].sum())
# print(df["読書"].mean())
# print(df["読書"].count())
#重複削除
# print(df["読書"].unique())
# df.drop_duplicates()
#MYSQLのデータ削除
# cursor.execute("TRUNCATE sample")
# conn.commit()


# df[df["点数"].between(60, 80)]
# df[df["A"].isin([1, 5, 9])]
