import pandas as pd
import glob
import pickle
import time
start_time = time.time()
Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'

valu_dateien = glob.glob(Pfad + '/*_exportierte_data_D4.pkl')

for datei in valu_dateien:
    data = pd.read_pickle(datei)
    data.columns = ['X-Koordinate','Y-Koordinate','Zeitpunkt','Strom','Kraft','Temperatur']

    # Temperaturen entfernen, welche kleiner als Zimmertemperatur sind
    filtered_values = data.loc[data['Temperatur'] < 290, 'Temperatur']
    data = data.drop(filtered_values.index)
    data.reset_index(drop=True, inplace=True)
    print(data)
    print(f' Filtered: {filtered_values.count()}')
    pkl_dateiname = datei.replace('_exportierte_data_D4.pkl', '_finish_data_D4.pkl')
    data.to_pickle(pkl_dateiname)


end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time

print(f"Die Ausführungszeit betrug {duration} Sekunden.")

