print(df.describe())

# Grouping dataset state wise
df1 = df.groupby('State')
#Take user input as state from user
state = input("Enter the state name you want to search for first dose: ")
print("\n")

if (state in df['State'].values):

    # Printing total first doses in user entered state
    firstSum = df1.get_group(state)['First Dose Administered'].sum()
    print("Total first doses in state " + state +  " are" , firstSum, "\n")

    # Printing total second doses in user entered state
    secondSum = df1.get_group(state)['Second Dose Administered'].sum()
    print("Total second doses in state " + state +  " are" , secondSum, "\n")

else:
    print("Invalid State Name")        

# Printing total male doses administered 
malesDoses = df['Male (Doses Administered)'].sum()
print("Total male doses are:" , malesDoses, "\n")

# Printing total female doses administered 
femaleDoses = df['Female (Doses Administered)'].sum()
print("Total female doses are:" , femaleDoses)