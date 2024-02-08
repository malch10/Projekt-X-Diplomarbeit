import pandas as pd
import glob
import pickle
import time
start_time = time.time()
Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'

valu_dateien = glob.glob(Pfad + '/*_exportierte_data.pkl')

for datei in valu_dateien:
    data = pd.read_pickle(datei)
    data.columns = ['X-Koordinate','Y-Koordinate','Zeitpunkt','Strom','Kraft','Temperatur']

    # Temperaturen entfernen, welche kleiner als Zimmertemperatur sind
    filtered_values = data.loc[data['Temperatur'] < 290, 'Temperatur']
    pkl_dateiname = datei.replace('_exportierte_data.pkl', '_finish_data.pkl')
    data.to_pickle(pkl_dateiname)
    data = data.drop(filtered_values.index)
    data.reset_index(drop=True, inplace=True)
    print(data)
    print(f' Filtered: {filtered_values.count()}')
end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time

print(f"Die Ausführungszeit betrug {duration} Sekunden.")

