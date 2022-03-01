import pandas as pd

df = pd.read_csv("covid_vaccine_statewise.csv")

# print(df.describe())

df1 = df.groupby('State')

