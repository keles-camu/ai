# Import libraries 

import pandas as pd
  
# Import dataset
df = pd.read_csv('iris.csv')

print(df.head())

print(df.dtypes)

print(df["Species"].unique())

print(df["Species"].value_counts())

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

print(label_encoder)

df['Species'] = label_encoder.fit_transform(df['Species'])

print(df.head())

print(df.dtypes)

print(df["Species"].unique())

print(df["Species"].value_counts())