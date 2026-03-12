import pandas as pd 


df = pd.read_csv("covid_toy.csv")
# print(df.head(3))

# print(df.isnull().sum())

df['fever']=df['fever'].fillna(df['fever'].mean())

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['gender'] = le.fit_transform(df['gender'])
df['cough'] = le.fit_transform(df['cough'])
df['city'] = le.fit_transform(df['city'])
df['has_covid'] = le.fit_transform(df['has_covid'])


x = df.drop(columns=['has_covid'])
y = df['has_covid']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(x_train, y_train)


import joblib

joblib.dump(lr, 'lr.pkl')
print("model is save")


