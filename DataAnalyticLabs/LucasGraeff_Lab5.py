from unicodedata import category
import pandas as pd 
import numpy

df = pd.read_csv('items.csv')
print('\nThe first 7 items')
print(df.head(7))
print('\nThe last 7 items')
print(df.tail(7))
print('\nInformation about items DataFrame')
df.info()
print(f'Items DataFrame has {df.shape[0]} rows and {df.shape[1]} columns')
print('\nDescriptive statistics for Bottle_Cost')
print(df['Bottle_Cost'].describe())
print('\nDataFrame After adding bottle_profit_margin column')
df['bottle_profit_margin'] = (df['Bottle_Retail_Price'] - df['Bottle_Cost']) / df['Bottle_Retail_Price']
print(df.iloc[0:5])
df.drop(df.index[5:16], inplace=True)
print('\nRows 5 to 15 are deleted')
print(df.iloc[0:19])
print('\nItems with more than 750 ml, 12 packs, and bottle_profit_margin more than 0.3')
print(df[(df['Bottle_Volume_ml'] > 750) & (df['Pack'] > 12) & (df['bottle_profit_margin'] > 0.3)])
print('\nThe number of energy drink')
print(df[df['Category'] == 'Energy Drink'].shape[0])
items2 = df
print('\nThe new DataFrame')
print(items2[0:16])
items2['Qty'] = numpy.random.randint(0, 999, size=items2.shape[0])
print('\nQty column added to DataFrame')
print(items2.iloc[:5])