import pandas as pd
import glob
import os
import re
import time
import pickle

start_time = time.time()
# Pfad zum Dateiordner

basis_pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Ausgangsdaten'

# Durchlaufe alle Unterordner in 'Daten'
for root, dirs, files in os.walk(basis_pfad):
    for dir in dirs:
        pfad = os.path.join(root, dir)
        pfad = pfad.replace('\\', '/')
        print(pfad)
        print("Versuche, die Datei zu öffnen:", pfad + '/TempPSim' + dir + '_coorX.txt')

        dir_wo = dir.replace('_', '')

        #Einlesen der richtigen Zeilen- und Spaltenabstände für die Koordinaten
        index_names = pd.read_csv(pfad + '/TempPSim' + dir_wo + '_coorX.txt', header=None).squeeze()[::4]
        column_names = pd.read_csv(pfad + '/TempPSim' + dir_wo + '_coorY.txt', header=None).squeeze()[::4]

        print(column_names)
        print(index_names)

        valu_dateien = glob.glob(pfad + '/*_valu.txt')

        for datei in valu_dateien:
            # Einlesen der richtigen Zeilen- und Spaltenabstände für die Temperaturen
            skiprows = [x for x in range(1, 400) if x % 4 != 0]
            data = pd.read_csv(datei, sep='\s+', header=None, skiprows=skiprows).iloc[:, ::4]


            Zeitpunkt = os.path.basename(datei).split('_')[1]
            Zeitpunkt = int(Zeitpunkt)
            print(Zeitpunkt)
            # Strom und Kraft aus Ordnernamen extrahieren
            Ordnername = re.findall(r'\d+', pfad)
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
            #counter = (info_array["Spaltenname"] == 0.002).sum()
            #print(info_array)
            #print(counter)
            # min_index = info_array["Wert3"].idxmin()
            # print(info_array.loc[min_index])


            # Exportiere den DataFrame in eine PKL-Datei
            pkl_dateiname = datei.replace('_valu.txt', '_exportierte_data_D3.pkl')
            pkl_dateiname = pkl_dateiname.replace('TempPSim'+dir_wo, 'TPath'+dir_wo)

            info_array.to_pickle(pkl_dateiname)

            print(f'Datei {pkl_dateiname} wurde erfolgreich exportiert.')

end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time
print(f"Die Ausführungszeit betrug {duration} Sekunden.")

