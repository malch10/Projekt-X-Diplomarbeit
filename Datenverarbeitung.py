import pandas as pd
import glob

Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'


valu_dateien = glob.glob(Pfad + '/*_exportierte_data.txt')


for datei in valu_dateien:
    data = pd.read_csv(datei, sep=',')


    data.columns = ['X-Koordinate','Y-Koordinate','Zeitpunkt','Strom','Kraft','Temperatur']


    print(data)

    #anzahl_vorkommen = (data['X-Koordinate'] == 0.003).sum()

    #print(f'Die Anzahl an ist {anzahl_vorkommen}')

    #print(data['X-Koordinate'].value_counts())

    #print(data.describe())

    data = data.drop(0)
    print(data)
    csv_dateiname = datei.replace('_exportierte_data.txt', '_finish_data.txt')
    data.to_csv(csv_dateiname, index=False)


