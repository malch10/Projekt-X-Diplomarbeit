import pandas as pd
import glob
import os
import re
import time

# Startzeit der Ausführung aufzeichnen
start_time = time.time()

# Pfad zum Dateiordner
path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Ausgangsdaten/I7000_F9000'

# Finde alle Dateien, die auf '_valu.txt' enden
valu_dateien = glob.glob(path + '/*_valu.txt')

# Zeile und Spalten festlegen
index_names = pd.read_csv(path + '/TPath_coorX.txt', header=None).squeeze()
column_names = pd.read_csv(path + '/TPath_coorY.txt', header=None).squeeze()

# Schleife durch jede Datei in valu_dateien
for datei in valu_dateien:
    # Lese die Hauptdaten
    data = pd.read_csv(datei, sep='\s+', header=None)

    # Zeit extrahieren
    zeitpunkt = os.path.basename(datei).split('_')[1]
    zeitpunkt = int(zeitpunkt)

    # Strom und Kraft aus Ordnernamen extrahieren
    ordnername = re.findall(r'\d+', path)
    strom = int(ordnername[0])
    kraft = int(ordnername[1])

    # Setze Spaltennamen und Index
    data.columns = column_names
    data.index = index_names

    # Info_array erstellen um Daten zu speichern
    info_array = pd.DataFrame(columns=['Zeilenname', 'Spaltenname', 'Wert', 'Wert1', 'Wert2', 'Wert3'])

    # Definieren der process_cell-Funktion
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

    # Ausgabe des info_array
    print(info_array)

    # Exportiere den DataFrame in eine PKL-Datei
    pkl_dateiname = datei.replace('_valu.txt', '_exportierte_data_D1.pkl')
    info_array.to_pickle(pkl_dateiname)

    # Erfolgsmeldung ausgeben
    print(f'Datei {pkl_dateiname} wurde erfolgreich exportiert.')

# Endzeit der Ausführung aufzeichnen
end_time = time.time()

# Berechne die Dauer der Ausführung
duration = end_time - start_time
print(f"Die Ausführungszeit betrug {duration} Sekunden.")
