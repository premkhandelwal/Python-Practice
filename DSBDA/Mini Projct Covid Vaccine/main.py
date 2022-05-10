import pandas as pd

df = pd.read_csv("covid_vaccine_statewise.csv")
print(df.shape)

# Describing the dataset
print("\nThe dataset can be described as\n")
print(df.describe())

# Printing mean of columns
print("\nThe mean of columns of dataset is\n")
print(df.mean(skipna=True, numeric_only=True))

# Printing count of columns
print("\nThe count of columns of dataset is\n")
print(df.count())

#

print("\nThe head of dataset is\n")
print(df.head())
# Grouping dataset state wise
# Take user input as state from user
state = input("Enter the state name you want to search for first dose: ")
print("\n")
df1 = df.groupby('State').get_group(state)
print(df1)
if (state in df['State'].values):

    # Printing total first doses in user entered state
    firstSum = df1['First Dose Administered'].sum()
    print("Total first doses in state " + state + " are", firstSum, "\n")

    # Printing total second doses in user entered state
    secondSum = df1['Second Dose Administered'].sum()
    print("Total second doses in state " + state + " are", secondSum, "\n")

else:
    print("Invalid State Name")

# Printing total male doses administered
malesDoses = df1['Male (Doses Administered)'].sum()
print("Total male doses are:", malesDoses, "\n")

# Printing total female doses administered
femaleDoses = df1['Female (Doses Administered)'].sum()
print("Total female doses are:", femaleDoses)