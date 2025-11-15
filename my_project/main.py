import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import lightgbm as lgb
import mysql.connector


#データの読み込み
csv_file = "sample.csv"
df = pd.read_csv(csv_file)

# MySQLに接続
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,          # Dockerでマッピングしたポート
    user="root",        # ユーザー名
    password="dgVH61",  # Docker起動時に設定したパスワード
    database="mydb"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sample (
    ブログ更新 INT,
    試験勉強 INT,
    コーディング INT,
    環境構築 INT,
    読書 INT,
    `1日の幸福度` INT
)
""")

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO sample (ブログ更新, 試験勉強, コーディング, 環境構築, 読書, `1日の幸福度`)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

query = "SELECT * FROM sample LIMIT 20"
df_limited = pd.read_sql(query,conn)
print(df_limited)

# #予測ターゲットの格納
target_df = df[["1日の幸福度"]]

# #特徴量の格納（説明変数：B列以降）
train_df = df[["ブログ更新","試験勉強", "コーディング", "環境構築", "読書"]]

# #モデル学習のための、訓練データとテストデータを7:3で分割
X_train, X_test, y_train, y_test = train_test_split(train_df, target_df, test_size=0.3)

# #XGBoostで学習するためのデータ形式に変換
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# ハイパーパラメータ設定
params = {
    'objective': 'binary',
    'metric': 'binary_error',
    'boosting_type': 'gbdt',
    'learning_rate': 0.1,
    'num_leaves': 31,
    'verbose': -1
}

# モデルパラメータ設定
model = lgb.train(params, train_data, valid_sets=[test_data], num_boost_round=100)

# 予測
y_pred_prob = model.predict(X_test)
y_pred = [1 if p > 0.5 else 0 for p in y_pred_prob]

#　予測結果を格納
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# モデルが正しく予測できたデータの割合
print("Accuracy:", accuracy)
#混同行列
print("Confusion Matrix:\n", cm)