# Summary: This script combines all the code cells from the notebook into a single Python script.

import pandas as pd

df = pd.read_csv('googleplaystore.csv')

print(df)

print(df.drop('App',axis=1))

df = pd.read_csv('titanic.csv')

print(df)

df.drop(['Name','Pclass'],inplace=True,axis=1)

print(df)

df.Age.fillna(df.Age.mean(),inplace=True)

print(df)

df.Age.isnull().sum()

df.Age = df.Age.apply(lambda x: round(x,1))

print(df)

df.Embarked = df.Embarked.fillna(df.Embarked.mode().iloc[0])

print(df.Embarked.isnull().sum())

print(df.isnull().sum())

df.dropna()

print(df)

df.Age = df.Age.apply(lambda x: 65 if x>65 else 5 if x<5 else x)

df.loc[df.Age>65] = 60

print(df)

df.Age[df.Age>65]

df = pd.read_csv('titanic.csv')

print(df)

print(df.Age[df.Age>65])

print(df.Age.corr(df.Fare))

print(df.corr(numeric_only=True))

print(df.head())

print(df.Name.str.startswith(('d','D')))

print(df[df.Name.str.lower().str.startswith('d')])

# how many people are doctor
# first name
# last name
# drop name column

print(df)

print(df[df.Name.str.contains('Dr.')])

print(type(df.Name[0]))

df.drop('Name',axis=1)

print(df.Name.apply(lambda f: f.split(',')[0]))

print(df.Name.apply(lambda f: ' '.join(f.split(' ')[2:])))