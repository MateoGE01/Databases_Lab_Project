#Script para limpiar el dataset ---- Ya no es necesario, EN REALIDAD SI LO ES, PORQUE EL DATASET ES POCO 
import os
import pandas as pd

data = pd.read_csv('Dataset/colombianos_detenidos_exterior_Clean.csv')

print(len(data))
#data_clean = data.dropna()
#data_clean_unique = data_clean.drop_duplicates()
#data_clean_unique['FECHA_PUBLICACION'] = pd.to_datetime(data_clean_unique['FECHA_PUBLICACION'])
#crea un archivo csv con los datos limpios
#data_clean_unique.to_csv('Dataset/colombianos_detenidos_exterior_Clean.csv', index=False)