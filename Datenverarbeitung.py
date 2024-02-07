import pandas as pd
import glob
import pickle
import time
start_time = time.time()
Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'

valu_dateien = glob.glob(Pfad + '/*_exportierte_data2.pkl')

for datei in valu_dateien:
    data = pd.read_pickle(datei)
    data.columns = ['X-Koordinate','Y-Koordinate','Zeitpunkt','Strom','Kraft','Temperatur']

    #anzahl_vorkommen = (data['X-Koordinate'] == 0.003).sum()
    #print(f'Die Anzahl an ist {anzahl_vorkommen}')
    #print(data['X-Koordinate'].value_counts())
    #print(data.describe())
    print(data)
    #data = data.drop(0)

    print(data.describe())

    pkl_dateiname = datei.replace('_exportierte_data2.pkl', '_finish_data2.pkl')
    data.to_pickle(pkl_dateiname)

end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time

print(f"Die Ausführungszeit betrug {duration} Sekunden.")

