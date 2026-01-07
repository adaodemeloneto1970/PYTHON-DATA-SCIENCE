import pandas as pd
from enum import Flag
import re

dados = pd.read_csv('fifa.csv')
dados.head(2)
dados['total']=dados['Acceleration']+dados['Agility']
print(dados[['Name','Age','total']])


df=pd.read_csv('house.csv')


filter1 = df.loc[(df['Rooms']==3)&(df['Type']=='h')&(df['Price']<=500000)]
print(filter1)

filter2 = df.loc[df['Address'].str.contains('Turner St'or'Turner Rd', flags=re.I)]

print(filter2)

df2=pd.read_csv('house.csv')

df2.loc[df['SellerG']=='Nelson',['SelleG']]='Ronald'

print(df2)

df2=pd.read_csv('house.csv')

print(df2['SellerG'])

df3=pd.read_csv('house.csv')

print(df3[['Suburb']])

