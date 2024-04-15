import pandas as pd
import glob
import os
import re
import time
import pickle

start_time = time.time()

# Pfad zum Dateiordner
basis_pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Vorhersage'

# Durchlaufe alle Unterordner in 'Daten'
for root, dirs, files in os.walk(basis_pfad):
    for dir in dirs:
        Pfad = os.path.join(root, dir)
        Pfad = Pfad.replace('\\','/')
        print(Pfad)
        print("Versuche, die Datei zu öffnen:", Pfad + '/TempPSim' + dir + '_coorX.txt')

        # Anpassen des Ordnernamens um auf Dateien zugreifen zu können
        dir_ordnername = dir.replace('_', '')

        # Zeile und Spalten festlegen (Nur jede zweite Zeile/Spalte einlesen)
        index_names = pd.read_csv(Pfad + '/TempPSim' + dir_ordnername + '_coorX.txt', header=None).squeeze()[::12]
        column_names = pd.read_csv(Pfad + '/TempPSim' + dir_ordnername + '_coorY.txt', header=None).squeeze()[::8]

        print(column_names)
        print(index_names)

        valu_dateien = glob.glob(Pfad + '/*_valu.txt')

        for datei in valu_dateien:
            # Lese die Hauptdaten ein, Auflösung D4 erschaffen
            # jede zwölfte Zeile
            skiprows = [x for x in range(1, 400) if x % 12 != 0]

            # Lese die Datei, überspringe die bestimmten Zeilen und wähle jede achte Spalte
            data = pd.read_csv(datei, sep='\s+', header=None, skiprows=skiprows).iloc[:, ::8]

            # Zeitpunkt einlesen
            zeitpunkt = os.path.basename(datei).split('_')[1]
            zeitpunkt = int(zeitpunkt)
            print(zeitpunkt)

            # Strom und Kraft aus Ordnernamen extrahieren
            ordnername   = re.findall(r'\d+', Pfad)
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
            #counter = (info_array["Spaltenname"] == 0.002).sum()
            #print(info_array)
            #print(counter)
            # min_index = info_array["Wert3"].idxmin()
            # print(info_array.loc[min_index])


            # Exportiere den DataFrame in eine PKL-Datei
            pkl_dateiname = datei.replace('_valu.txt', '_exportierte_data_D4.pkl')
            pkl_dateiname = pkl_dateiname.replace('TempPSim' + dir_ordnername, 'TPath' + dir_ordnername)

            info_array.to_pickle(pkl_dateiname)

            print(f'Datei {pkl_dateiname} wurde erfolgreich exportiert.')

end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time
print(f"Die Ausführungszeit betrug {duration} Sekunden.")

