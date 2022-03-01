""" import pandas as pd
data = pd.read_csv("iris.csv")

print(data)

print('Iris-setosa')
setosa = data['Species'] == 'Iris-setosa'
print(data[setosa].describe())

 """


import pandas as pd
df = pd.read_csv("employee.csv")

print(df)



grpByRes = df.groupby(['EmpDept','EmpSalary'])

print("\n")
print(grpByRes.first())

grpBySalary = df.groupby(['EmpDept'])['EmpSalary']

print("\n")
print("---------------Mean----------------")
print(grpBySalary.mean())

print("\n")
print("---------------Median----------------")
print(grpBySalary.median())

print("\n")
print("---------------Standard Deviation----------------")
print(grpBySalary.std())

print("\n")
print("---------------Minimum----------------")
print(grpBySalary.min())

print("\n")
print("---------------Maximum----------------")
print(grpBySalary.max())