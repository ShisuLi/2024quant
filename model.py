import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
from xgboost import XGBClassifier  
from sklearn.metrics import classification_report, accuracy_score 
import os
import matplotlib.pyplot as plt

file_dir="./data"
sym=0
dates = list(range(156))
data_frames = []
for date in dates:
    if date%2==0:
        file_name=f"snapshot_sym{sym}_date{date//2}_am.csv"
    else:
        file_name=f"snapshot_sym{sym}_date{date//2}_pm.csv"
    try:
        data_frames.append(pd.read_csv(os.path.join(file_dir, file_name)))
    except FileNotFoundError:
        pass
    

df = pd.concat(data_frames)

df.fillna(method='ffill', inplace=True)  

feature_col_names =['n_bid1', 'n_bid2', 'n_bid3', 'n_bid4', 'n_bid5',\
                    'n_ask1', 'n_ask2', 'n_ask3', 'n_ask4', 'n_ask5', ]
label_col_name = ['label_5']

train_sample_nums = 20000
train_data = np.ascontiguousarray(df[feature_col_names][:train_sample_nums].values)
train_label = df[label_col_name][:train_sample_nums].values.reshape(-1)

test_data = np.ascontiguousarray(df[label_col_name][train_sample_nums:40000].values)
test_label = df[label_col_name][train_sample_nums:40000].values.reshape(-1)

model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')  
model.fit(train_data, train_label)  

y_hat = model.predict(train_data)
y=train_label

print("总体正确率：", sum(y_hat == y) / len(y_hat))  
index = y != 1  
print("上涨下跌召回率：", sum(y_hat[index] == y[index]) / sum(index))  
index = y_hat != 1  
print("上涨下跌准确率：", sum(y_hat[index] == y[index]) / sum(index))

