import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle 

data={
    "age":[22,25,30,18,40],
    "weight":[60,75,80,55,90],
    "height":[170,165,172,168,175],
    "bp_sys":[110,135,140,105,150],
    "bp_dia":[70,85,90,65,95],
    "cholestrol":[180,210,220,160,240],
    "has_disease":[0,1,1,0,1]
}
df=pd.DataFrame(data)
x=df.drop("has_disease",axis=1)
y=df["has_disease"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=RandomForestClassifier()
model.fit (x_train,y_train)

with open ("model.pkl","wb") as f:
    pickle.dump (model,f)
print ("Model da duoc huan luyen va luu thanh cong")    