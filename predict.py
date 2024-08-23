from opcua import Client
import time
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
import time
import os
import socket
import random
def start_client(input_str):
    server_host='192.168.15.110'
    server_port=5555
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_host, server_port))
        print("Connected to the server.")

        client_socket.send(input_str.encode('utf-8'))
    


df = pd.read_csv("train.csv")
df.drop(columns = ["Product ID"],inplace =True)


from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
df["Type"] = label.fit_transform(df["Type"])
print(df.head())
df["Machine failure"].value_counts()
df.corr()
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
df_new.drop(columns="RNF",inplace=True)
X_new = df_new.iloc[:,:-1]
Y_new = df_new.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X_new,Y_new,test_size=0.3,random_state=42)
from sklearn.preprocessing import StandardScaler
Scaler = StandardScaler()
x_train = Scaler.fit_transform(x_train)
x_test = Scaler.transform(x_test)
from joblib import dump, load
# 設定您的目錄路徑
directory_path = './'

# 列出目錄中所有的joblib檔案
joblib_files = [f for f in os.listdir(directory_path) if f.endswith('.joblib')]
print(joblib_files)
RF2 = load(str(joblib_files[0]))


#設定OPCUA伺服器位置
server_url = 'opc.tcp://192.168.15.36:4840/freeopcua/server/' 
#與伺服器建立OPCUA連結
client = Client(server_url)

try:
    client.connect()
    print("Client connected to the server successfully")

    while True:
        try:
            feedback = ""
            Product_ID_ar = list()
            Type_ar= list()
            AirTemperature_ar= list()
            ProcessTemperature_ar= list()
            RationalSpped_ar= list()
            Torque_ar = list()
            ToolWear_ar= list()
            TWF_ar= list()
            HDF_ar= list()
            PWF_ar= list()
            OSF_ar= list()
            RNF_ar = list()
            # 假设我们知道变量的节点ID
            temp_var_node_id = "ns=2;i=2"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            Product_ID = temp_var.get_value()
            print("Current Type:", Product_ID)
            Product_ID_ar.append(Product_ID)
            feedback+=("CnCAbnormalDetect2&cnc2&"+str(Product_ID)+"&")


            # 假设我们知道变量的节点ID
            temp_var_node_id = "ns=2;i=3"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            Type = temp_var.get_value()
            print("Current Type:", Type)
            Type_ar.append(Type)
            feedback+=(str(Type)+"&")

            temp_var_node_id = "ns=2;i=4"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            AirTemperature = temp_var.get_value()
            print("Current AirTemperature:", AirTemperature)
            AirTemperature_ar.append(AirTemperature)
            feedback+=(str(AirTemperature)+"&")

            temp_var_node_id = "ns=2;i=5"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            ProcessTemperature = temp_var.get_value()
            print("Current ProcessTemperature:", ProcessTemperature)
            ProcessTemperature_ar.append(ProcessTemperature)
            feedback+=(str(ProcessTemperature)+"&")


            temp_var_node_id = "ns=2;i=6"
            temp_var = client.get_node(temp_var_node_id) 
            # 读取变量值
            RationalSpped = temp_var.get_value()
            print("Current RationalSpped:", RationalSpped)
            RationalSpped_ar.append(RationalSpped)
            feedback+=(str(RationalSpped)+"&")

            temp_var_node_id = "ns=2;i=7"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            Torque = temp_var.get_value()
            print("Current Torque:", Torque)
            Torque_ar.append(Torque)
            feedback+=(str(Torque)+"&")

            temp_var_node_id = "ns=2;i=8"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            ToolWear = temp_var.get_value()
            print("Current ToolWear:", ToolWear)
            ToolWear_ar.append(ToolWear)
            feedback+=(str(ToolWear)+"&")

            temp_var_node_id = "ns=2;i=9"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            TWF = temp_var.get_value()
            print("Current TWF:", TWF)
            TWF_ar.append(TWF)
            feedback+=(str(TWF)+"&")

            temp_var_node_id = "ns=2;i=10"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            HDF = temp_var.get_value()
            print("Current HDF:", HDF)
            HDF_ar.append(HDF)
            feedback+=(str(HDF)+"&")

            temp_var_node_id = "ns=2;i=11"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            PWF = temp_var.get_value()
            print("Current PWF:", PWF)
            PWF_ar.append(PWF)
            feedback+=(str(PWF)+"&")

            temp_var_node_id = "ns=2;i=12"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            OSF = temp_var.get_value()
            print("Current OSF:", OSF)
            OSF_ar.append(OSF)
            feedback+=(str(OSF)+"&")

            temp_var_node_id = "ns=2;i=13"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            RNF = temp_var.get_value()
            print("Current RNF:", RNF)
            RNF_ar.append(RNF)
            feedback+=(str(RNF)+"$")
            time.sleep(2)

            # 假设我们知道变量的节点ID
            temp_var_node_id = "ns=2;i=2"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            Product_ID = temp_var.get_value()
            print("Current Type:", Product_ID)
            Product_ID_ar.append(Product_ID)
            feedback+=("CnCAbnormalDetect2&cnc2&"+str(Product_ID)+"&")


            # 假设我们知道变量的节点ID
            temp_var_node_id = "ns=2;i=3"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            Type = temp_var.get_value()
            print("Current Type:", Type)
            Type_ar.append(Type)
            feedback+=(str(Type)+"&")

            temp_var_node_id = "ns=2;i=4"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            AirTemperature = temp_var.get_value()
            print("Current AirTemperature:", AirTemperature)
            AirTemperature_ar.append(AirTemperature)
            feedback+=(str(AirTemperature)+"&")

            temp_var_node_id = "ns=2;i=5"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            ProcessTemperature = temp_var.get_value()
            print("Current ProcessTemperature:", ProcessTemperature)
            ProcessTemperature_ar.append(ProcessTemperature)
            feedback+=(str(ProcessTemperature)+"&")


            temp_var_node_id = "ns=2;i=6"
            temp_var = client.get_node(temp_var_node_id) 
            # 读取变量值
            RationalSpped = temp_var.get_value()
            print("Current RationalSpped:", RationalSpped)
            RationalSpped_ar.append(RationalSpped)
            feedback+=(str(RationalSpped)+"&")

            temp_var_node_id = "ns=2;i=7"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            Torque = temp_var.get_value()
            print("Current Torque:", Torque)
            Torque_ar.append(Torque)
            feedback+=(str(Torque)+"&")

            temp_var_node_id = "ns=2;i=8"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            ToolWear = temp_var.get_value()
            print("Current ToolWear:", ToolWear)
            ToolWear_ar.append(ToolWear)
            feedback+=(str(ToolWear)+"&")

            temp_var_node_id = "ns=2;i=9"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            TWF = temp_var.get_value()
            print("Current TWF:", TWF)
            TWF_ar.append(TWF)
            feedback+=(str(TWF)+"&")

            temp_var_node_id = "ns=2;i=10"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            HDF = temp_var.get_value()
            print("Current HDF:", HDF)
            HDF_ar.append(HDF)
            feedback+=(str(HDF)+"&")

            temp_var_node_id = "ns=2;i=11"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            PWF = temp_var.get_value()
            print("Current PWF:", PWF)
            PWF_ar.append(PWF)
            feedback+=(str(PWF)+"&")

            temp_var_node_id = "ns=2;i=12"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            OSF = temp_var.get_value()
            print("Current OSF:", OSF)
            OSF_ar.append(OSF)
            feedback+=(str(OSF)+"&")

            temp_var_node_id = "ns=2;i=13"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            RNF = temp_var.get_value()
            print("Current RNF:", RNF)
            RNF_ar.append(RNF)
            feedback+=(str(RNF)+"$")

            pre_df = pd.DataFrame({'Type': Type_ar, 'Air temperature [K]': AirTemperature_ar,'Process temperature [K]':ProcessTemperature_ar,'Rotational speed [rpm]':RationalSpped_ar,
                                'Torque [Nm]':Torque_ar,'Tool wear [min]':ToolWear_ar,'TWF':TWF_ar,
                                'HDF':HDF_ar,'PWF':PWF_ar,'OSF':OSF_ar,'RNF':RNF_ar})
            #feedback
            pre_df.drop(columns=["RNF"],inplace=True)
            correlation_cal = pre_df.copy()
            #realpredict
            pre_df["Type"] = label.transform(pre_df["Type"])
            pre_df = Scaler.transform(pre_df)
            print(pre_df)
            test_pre = RF2.predict(pre_df[0:1])
            print("Whether Machine Failure or not")
            print(test_pre[0])
            feedback+=(str(test_pre[0])+"$")
            print("Yes")
            correlation_cal.drop(columns=["Type","Air temperature [K]","Process temperature [K]","Tool wear [min]","TWF","HDF","PWF","OSF"],inplace=True)
            correlation_matrix = correlation_cal.corr()
            print("皮爾森係數：")
            print(correlation_matrix)
            machine_corr = correlation_matrix.loc['Rotational speed [rpm]', 'Torque [Nm]']

            feedback+=(str(machine_corr)+'$')
            temp_var_node_id = "ns=2;i=14"
            temp_var = client.get_node(temp_var_node_id)
            # 读取变量值
            OEE = temp_var.get_value()
            print("Current OEE:", OEE)
            feedback+=(str(OEE))
            print(feedback)
            start_client(feedback)
            print()
            time.sleep(3)
        except:
            time.sleep(5)




finally:
    #與伺服器斷開OPCUA連結
    client.disconnect()