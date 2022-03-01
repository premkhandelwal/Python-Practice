import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()


def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['Survived','Dead']
    df.plot(kind='bar',stacked=True, figsize=(10,5))

train = pd.read_csv('input/titanic/train.csv')
test = pd.read_csv('input/titanic/test.csv')
train.head()
print(train.shape)
print(test.shape)
print(train.isnull().sum())
bar_chart('Sex')
bar_chart('Pclass')
bar_chart('Embarked')
bar_chart('Parch')
bar_chart('SibSp')