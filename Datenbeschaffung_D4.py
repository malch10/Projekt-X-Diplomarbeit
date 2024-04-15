import pandas as pd
import glob
import os
import re
import time
import pickle

start_time = time.time()
# Pfad zum Dateiordner
pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Vorhersage/I8000_F5000'

# Finde alle Dateien, die auf '_valu.txt' enden
valu_dateien = glob.glob(pfad + '/*_valu.txt')

# Zeile und Spalten festlegen (Nur jede zweite Zeile/Spalte einlesen)
index_names = pd.read_csv(pfad + '/TPath_coorX.txt', header=None).squeeze()[::12]
column_names = pd.read_csv(pfad + '/TPath_coorY.txt', header=None).squeeze()[::8]

print(column_names)
print(index_names)


for datei in valu_dateien:
    # Lese die Hauptdaten, nur jede zwölfte Zeile

    skiprows = [x for x in range(1, 400) if x % 12 != 0]

    # Lese die Datei, überspringe die bestimmten Zeilen und wähle jede achte Spalte
    data = pd.read_csv(datei, sep='\s+', header=None, skiprows=skiprows).iloc[:, ::8]

    # Zeit extrahieren
    zeitpunkt = os.path.basename(datei).split('_')[1]
    zeitpunkt = int(zeitpunkt)

    # Strom und Kraft aus Ordnernamen extrahieren
    ordnername = re.findall(r'\d+', pfad)
    strom = int(ordnername[0])
    kraft = int(ordnername[1])

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
            'Wert': zeitpunkt,
            'Wert1': strom,
            'Wert2': kraft,
            'Wert3': row.values,
        })
        return row_df

    # Anwenden der Funktion und Konkatenation der Ergebnisse
    info_array = pd.concat([process_cell(data.iloc[i]) for i in range(len(data))]).reset_index(drop=True)

    # Exportiere den DataFrame in eine PKL-Datei
    pkl_dateiname = datei.replace('_valu.txt', '_exportierte_data_D4.pkl')
    info_array.to_pickle(pkl_dateiname)

    print(f'Datei {pkl_dateiname} wurde erfolgreich exportiert.')

end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time
print(f"Die Ausführungszeit betrug {duration} Sekunden.")

