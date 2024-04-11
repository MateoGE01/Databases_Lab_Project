#Limpiando el dataset
import os
import pandas as pd

data = pd.read_csv('Dataset/Mental_Health_Dataset.csv')
#print(data.info())
data_clean = data.dropna()
data_clean_unique = data_clean.drop_duplicates()
print(data_clean_unique.info())
