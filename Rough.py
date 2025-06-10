import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set_theme()
import warnings
warnings.filterwarnings('ignore')

import gdown
file_id = "1Yy6m97BjIzXBPJ7RFogtNpZFu3S4ulyL"
gdown.download(f"https://drive.google.com/uc?id={file_id}", "Finance_dept.zip", quiet=False)

import zipfile
with zipfile.ZipFile("Finance_dept.zip", "r") as zip_ref:
    zip_ref.extractall("Finance_dept")

folder_path='Finance_dept'
inner_folder_path = os.path.join(folder_path, 'Capston project finance dept')
files = os.listdir(inner_folder_path)
print(files)

train=pd.read_csv(os.path.join(inner_folder_path,"train.csv"))
train_sorted=train.sort_values('id')
test=pd.read_csv(os.path.join(inner_folder_path,"test_share.csv"))
test_sorted=test.sort_values('id')
geo=pd.read_csv(os.path.join(inner_folder_path,"Geo_scores.csv"))
geo_sorted=geo.sort_values('id')
instance=pd.read_csv(os.path.join(inner_folder_path,"instance_scores.csv"))
instance_sorted=instance.sort_values('id')
qset=pd.read_csv(os.path.join(inner_folder_path,"Qset_tats.csv"))
qset_sorted=qset.sort_values('id')
lambda_wt=pd.read_csv(os.path.join(inner_folder_path,"Lambda_wts.csv"))
lambda_sorted=lambda_wt.sort_values('Group')

m1=pd.merge(geo_sorted,instance_sorted,on='id',how='left')
del geo_sorted,instance_sorted

m2=pd.merge(m1,qset_sorted,on='id',how='left')
del m1,qset_sorted

print(m2.head())
print(m2.info())

m2.isna().sum()

m2['geo_score']=m2['geo_score'].fillna(m2['geo_score'].median())
m2['qsets_normalized_tat']=m2['qsets_normalized_tat'].fillna(m2['qsets_normalized_tat'].median())
m3=pd.merge(test_sorted,lambda_sorted,on='Group',how='left')
del test_sorted
print(m3.info())
m3.isna().sum()

merged_test=pd.merge(m3,m2,on='id',how='left')
del m3
merged_test.isna().sum()

mt3=pd.merge(train_sorted,lambda_sorted,on='Group',how='left')
mt3.info()

mt3.isna().sum()

merged_train=pd.concat([mt3, m2],axis=1,ignore_index=True)