import pandas as pd

df=pd.read_csv('coaches.csv')
print(df.columns)
df.columns=df.columns.str.strip().str.lower().str.replace(' ', '_')
df['name'] = df['name'].str.strip()
df['nationality'] = df['nationality'].str.strip().str.title()

print(df.columns)
df.dropna(inplace=True)

df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print(df.head())
print(df.dtypes)
print(df['nationality'].value_counts().head())
