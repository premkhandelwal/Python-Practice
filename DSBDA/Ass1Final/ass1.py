import pandas as pd
import os

df = pd.read_csv('weather.csv')


# ? Fill missing values
print(df.isnull())
df2 = df.fillna(value =0)
print(df2)

# ? Convert categorial values into numerical values

# Convert by using get_dummies method
dummies = pd.get_dummies(df.RainTomorrow)
print(dummies)

merged = pd.concat([df, dummies], axis = 'columns')
merged.drop(columns=['RainTomorrow'], axis = 'columns')

print(merged)


# Convert by using .factorize
df['RainTomorrow'] = pd.factorize(df['RainTomorrow'])[0]
print(df)