import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
import time
import os
for dirname, _, filenames in os.walk(''):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# 設置含有 CSV 文件的目錄
directory_path = './'

# 初始化一個空的 DataFrame 列表來存儲每個文件的數據
dataframes = {}
# 遍歷目錄下的每個文件
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):  # 確保只處理 CSV 文件
        file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)  # 讀取 CSV 文件到 DataFrame
        # 將 DataFrame 轉換為元組(tuple)，並去除'machine_fail'列
        tuple_without_machine_fail = tuple(df.drop('Machine failure', axis=1).values[0])
        # 如果這個 tuple 已經存在於字典中，將對應的 'machine_fail' 設置為1
        if tuple_without_machine_fail in dataframes:
            dataframes[tuple_without_machine_fail]['Machine failure'] = 1
        else:
            # 否則，將這個 tuple 設置為這個 DataFrame 的索引，並添加到字典中
            df.set_index(list(df.columns.drop('Machine failure')), inplace=True)
            dataframes[tuple_without_machine_fail] = df

# 使用 concat 合併所有 DataFrame
combined_df = pd.concat(dataframes.values(), ignore_index=False)

# 重設索引
combined_df.reset_index(inplace=True)

# 顯示合併後的 DataFrame
print(combined_df)
df = combined_df.copy()
df.drop(columns = ["Product ID"],inplace =True)

# df.drop(columns = ["id","Product ID"],inplace =True)
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
df["Type"] = label.fit_transform(df["Type"])
print(df.head())
df["Machine failure"].value_counts()
df.corr()
plt.figure(figsize=(12,12))
sns.heatmap(df.corr(),annot=True)

y = df["Machine failure"]
df.drop(columns = "Machine failure",inplace =True)
X = df
from imblearn.over_sampling import SMOTE
sm =SMOTE(sampling_strategy=0.8)
Features,target  = sm.fit_resample(X,y) 
target.value_counts()
df_new = pd.DataFrame
df_new = Features
df_new["Machine failure"] = target
df_new.corr()
plt.figure(figsize=(12,12))
sns.heatmap(df_new.corr(),annot=True)
plt.show()
df_new.drop(columns="RNF",inplace=True)
X_new = df_new.iloc[:,:-1]
Y_new = df_new.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X_new,Y_new,test_size=0.3,random_state=42)
from sklearn.preprocessing import StandardScaler
Scaler = StandardScaler()
x_train = Scaler.fit_transform(x_train)
x_test = Scaler.transform(x_test)
from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier(max_depth = 30)
RF.fit(x_train,y_train)
pred = RF.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,pred))
accuracy_in_name = int(accuracy_score(y_test,pred)*100)
from joblib import dump, load
dump(RF, 'random2.joblib')
import shutil
shutil.copy2('random2.joblib','/result/NCKU_Owen_CnCAbnormalDetect2_'+str(accuracy_in_name)+'.joblib')

RF2 = load('/result/NCKU_Owen_CnCAbnormalDetect2_'+str(accuracy_in_name)+'.joblib')     

from sklearn.metrics import accuracy_score
pred = RF2.predict(x_train)
result2 = accuracy_score(y_train,pred)
print("real predict result")
print(result2)
print("Success")
check_file = os.path.isfile('/result/NCKU_Owen_CnCAbnormalDetect2_'+str(accuracy_in_name)+'.joblib')
print(check_file)


# plt.figure(figsize=(12,12))
# sns.heatmap(df.corr(),annot=True)
