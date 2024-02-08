import pandas as pd
import glob
import os
import re
import time
import pickle

start_time = time.time()
# Pfad zum Dateiordner
Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'

# Finde alle Dateien, die auf '_valu.txt' enden
valu_dateien = glob.glob(Pfad + '/*_valu.txt')

# Zeile und Spalten festlegen (Nur jede zweite Zeile/Spalte einlesen)
index_names = pd.read_csv(Pfad + '/TPath_coorX.txt', header=None).squeeze()[::4]
column_names = pd.read_csv(Pfad + '/TPath_coorY.txt', header=None).squeeze()[::4]

print(column_names)
print(index_names)


for datei in valu_dateien:
    # Lese die Hauptdaten, nur jede zweite Zeile und Spalte
    #data = pd.read_csv(datei, sep='\s+', header=None, skiprows=lambda x: x % 2 == 1).iloc[:, ::2]

    skiprows = [x for x in range(1, 400) if x % 4 != 0]

    # Lese die Datei, überspringe die bestimmten Zeilen und wähle jede vierte Spalte
    data = pd.read_csv(datei, sep='\s+', header=None, skiprows=skiprows).iloc[:, ::4]

    # Zeige die ersten Zeilen der gefilterten Daten an
    #print(data.head())

    # Zeit extrahieren
    Zeitpunkt = os.path.basename(datei).split('_')[1]
    Zeitpunkt = int(Zeitpunkt)

    # Strom und Kraft aus Ordnernamen extrahieren
    Ordnername = re.findall(r'\d+', Pfad)
    Strom = int(Ordnername[0])
    Kraft = int(Ordnername[1])

    # Setze Spaltennamen und Index
    data.columns = column_names
    data.index = index_names

    # Info_array erstellen um Daten zu speichern
    info_array = pd.DataFrame(columns=['Zeilenname', 'Spaltenname', 'Wert', 'Wert1', 'Wert2', 'Wert3'])

    # Definiere die process_cell-Funktion
    def process_cell(row):
        row_df = pd.DataFrame({
            'Zeilenname': row.name,
            'Spaltenname': row.index,
            'Wert': Zeitpunkt,
            'Wert1': Strom,
            'Wert2': Kraft,
            'Wert3': row.values,
        })
        return row_df

    # Anwenden der Funktion und Konkatenation der Ergebnisse
    info_array = pd.concat([process_cell(data.iloc[i]) for i in range(len(data))]).reset_index(drop=True)
    print(info_array)
    # min_index = info_array["Wert3"].idxmin()
    # print(info_array.loc[min_index])


    # Exportiere den DataFrame in eine PKL-Datei
    pkl_dateiname = datei.replace('_valu.txt', '_exportierte_data_D3.pkl')
    info_array.to_pickle(pkl_dateiname)

    #print(f'Datei {pkl_dateiname} wurde erfolgreich exportiert.')

end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time
print(f"Die Ausführungszeit betrug {duration} Sekunden.")
