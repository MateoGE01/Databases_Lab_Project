#Limpiando el dataset
import os
import pandas as pd

data = pd.read_csv('Dataset/colombianos_detenidos_exterior.csv')
print(data.info())
data_clean = data.dropna()
data_clean_unique = data_clean.drop_duplicates()
#data_clean_unique['Timestamp'] = pd.to_datetime(data_clean_unique['Timestamp'])
#crea un archivo csv con los datos limpios
#data_clean_unique.to_csv('Dataset/Mental_Health_Dataset_Clean.csv', index=False)