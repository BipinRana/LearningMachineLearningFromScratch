# Methods of Pandas for indepth knowledge for operations in DataFrame
import pandas as pd

a = pd.Series([True,True,True,False])

df = pd.read_csv("C:/Users/LEGION/Desktop/Data Science/titanic.csv")

print(df)

#find number of females
#find total mnumber of people embarked from S,C,0
#find total number of people who survived and died
#find total number of alive and dead male
#find total number of alive and dead female
#find total number of people whose age is greather than 20 and less than 30
#find max male and femalre fare
#find female max age abd male max age
#convert fare column to int data type permanently
#rename Sex column to gender
#move suvived column to the last index

print((df.Sex=='female').sum())

print((df.Embarked.isin(['S','C','O'])).sum())

print((df.Embarked =='S').sum())

print((df.Survived == 1).sum())

print((df.Survived == 0).sum())

print(((df.Sex == 'male') & (df.Survived == 0)).sum())

print(((df.Sex == 'male') & (df.Survived == 1)).sum())

print(((df.Sex == 'female') & (df.Survived == 0)).sum())

print(((df.Sex == 'female') & (df.Survived == 1)).sum())

print((df.Age.between(20,30)).sum())

print(df[df.Sex=='male'].Fare.max())

print(df[df.Sex=='female'].Fare.max())

print(df[df.Sex=='female'].Age.max())

print(df[df.Sex=='male'].Age.max())

df['Fare'] = df.Fare.astype('int')

print(df)

#pop

df.rename(columns={'Sex':'Gender'})

df['Survived'] =df.pop('Survived')

print(df)



df.Fare =  df.Fare.apply(lambda f:round(f,1))

print(df)

# add a column named is_alived that has either True or False value
# add a column named alive_dead that has either Alive or Dead value
# drop survied column
# rename sex to gender
# add a column named is_male which has either True or False value
# find how many unique values are in Pclass
# change 1-->one and 2-->two and 3-->three

df['is_alive'] = df.Survived.apply(lambda f: f==1)
print(df)

df['alive_dead'] = df.Survived.apply(lambda f:'Alive' if f==1 else 'Dead')
print(df)

df.pop('Survived')

df = df.rename(columns={'Sex':'Gender'})
print(df)

df['is_male'] = df.Gender.apply(lambda f:f=='male')
print(df)

print(df.Pclass.nunique())

def P_class(class_no):
    if class_no == 1:
        return 'one'
    elif class_no == 2:
        return 'two'
    elif class_no == 3:
        return 'three'
    

df['Pclass'] = df.Pclass.apply(P_class)
print(df)

print(a)

print(a.apply(lambda x:x**2))

print(a.map(lambda x:x**2))

print(df.Pclass.apply(lambda f: 'one' if f==1 else 'two' if f==2 else 'three'))

# sort_values
# sort_index
print(df.sort_values(['Pclass','Age','Fare'],ascending=[True,False,False]))

print(df.Name)

print(df.Age.isnull())

print(df.Age.isnull().sum())

a = pd.DataFrame([[10,20],[4,5]],columns=['price','quantity'])

print(a)

a['total'] = a.price * a.quantity

print(a)



