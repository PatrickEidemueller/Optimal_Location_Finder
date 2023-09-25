import pandas as pd
import numpy as np

for i in range(2010,2022):
    year = str(i)
    print(year)

    #w = pd.read_csv('data/'+year+'_subset.csv', sep=',', header=None)
    w = pd.read_csv('../weather/' + year + '.csv', sep=',', header=None) #Server-Pfad
    w.columns= ['id', 'date', 'element', 'value', 'm-flag', 'q-flag', 's-flag', 'obs']

    # Nach US Stationen filtern
    w_us = w[(w['id'].str[0:2]=='US') | (w['id'].str[0:2]=='CA')]
    w_us = w_us[['id', 'date', 'element','value']]
    print(w_us.head(10))

    # Tabelle umstrukturieren
    w_us = w_us.pivot(index=['id', 'date'], columns='element', values='value')

    # Spalten umbenennen
    w_us = w_us.reset_index()
    #w_us = w_us[['id', 'date', 'TMIN', 'TMAX', 'PRCP', 'SNOW', 'SNWD']]
    #w_us = w_us[['id', 'date', 'TMIN', 'TMAX', 'PRCP', 'SNOW', 'SNWD', 'TAVG', 'AWND', 'ACSC', 'PSUN']]

    elements = ['TMIN', 'TMAX', 'PRCP', 'SNOW', 'SNWD', 'TAVG', 'AWND', 'ACSC', 'PSUN']

    # nicht vorhandene Spalten im Datensatz erstellen und mit NaN füllen
    for element in elements:
        if element not in w_us.columns:
            w_us[element] = np.nan

    w_us = w_us[['id', 'date'] + elements]

    # Datumsformat umwandeln
    w_us['date'] = pd.to_datetime(w_us['date'], format='%Y%m%d')

    # In csv schreiben
    print(w_us.head(10))
    #w_us.to_csv('data/'+year+'_subset_tidy.csv', index=False, sep=';')
    w_us.to_csv('../weather/'+year+'_tidy.csv', index=False, sep=';') #Server-Pfad

    #w_us_1 = w_us[w_us['id']=='USC00407184']
    #print(w_us_1)