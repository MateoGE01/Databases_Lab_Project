#Script para limpiar el dataset 
import os
import pandas as pd

#Funcion para limpiar los datos del dataset original
def clean_data(datacsv):
    
    data = pd.read_csv(datacsv)

    print(len(data))
    data_clean = data.dropna(subset=['LoE_DI', 'YoB', 'gender'])
    data_clean_unique = data_clean.drop_duplicates()

    data_clean_unique['start_time_DI'] = pd.to_datetime(data_clean_unique['start_time_DI'], dayfirst=True)
    data_clean_unique['last_event_DI'] = pd.to_datetime(data_clean_unique['last_event_DI'], dayfirst=True)
    data_clean_unique.to_csv('Dataset/CourClean1.csv', index=False)

#clean_data('Dataset/CourClean.csv')

#Funcion para cambiar el tipo de dato de las columnas en el nuevo dataset, porque pandas los pone como float64
def change_datatype(datasetcsv, *args):
    data = pd.read_csv(datasetcsv)
    for key in args:
        data[key] = data[key].astype('Int64')
    data.to_csv(datasetcsv, index=False)
    
#change_datatype('Dataset/CourClean1.csv', 'id', 'registered', 'viewed', 'explored', 'certified', 'YoB', 'nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'incomplete_flag')