import pandas as pd
import pymysql

conn = pymysql.connect(
    host="localhost",
    user= "root",
    password="1234",
    database="socials_db"
)

quary = "select * from social_network_ads"

df = pd.read_sql(quary,conn)

print(df)
conn.close()







import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib


df =df.drop(columns=['User ID','Gender'])

x = df.drop(columns=['Purchased'])
y = df['Purchased']

x_train ,x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)

joblib.dump(model , 'lr_model.pkl')
