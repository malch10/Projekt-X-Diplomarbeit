import pandas as pd

Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'


# Setze Optionen, um alle Zeilen und Spalten anzuzeigen
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

# Lese Spaltennamen und Index
index_names = pd.read_csv(Pfad + '/TPath_coorX.txt', header=None).squeeze()
column_names = pd.read_csv(Pfad + '/TPath_coorY.txt', header=None).squeeze()
#print(index_names)
#print(column_names)


# Lese die Hauptdaten
data = pd.read_csv(Pfad + '/TPath_300_valu.txt', sep='  ', header=None)

# Setze Spaltennamen und Index
data.columns = column_names
data.index = index_names

# Zeige die Daten an
print(data)
print(data.iloc[0])
#print("Spaltennamen:", data.columns)
#print("Indexwerte:", data.index)
data = data.reset_index()


# Info_array erstellen um Daten zu speichern
info_array = pd.DataFrame(columns=['Zeilenname', 'Spaltenname', 'Wert'])


# # Schleife durch die Zeilen des DataFrames
# print(data)
# for index, row in data.iterrows():
#     for column in data.columns:
#         zeilenname = row[data.columns[0]]
#         spaltenname = column
#         wert = data.at[index, column]
#
#         # Erstellen eines temporären DataFrames für jede Zelle
#         temp_df = pd.DataFrame({'Zeilenname': [zeilenname], 'Spaltenname': [spaltenname], 'Wert': [wert]})
#         # Verwenden Sie concat, um den temporären DataFrame zum info_array hinzuzufügen
#         info_array = pd.concat([info_array, temp_df], ignore_index=True)

def process_cell(row):
    row_df = pd.DataFrame({
        'Zeilenname': row.name,
        'Spaltenname': row.index,
        'Wert': row.values
    })
    return row_df

# Anwenden der Funktion auf jede Zeile und Konkatenation der Ergebnisse
info_array = pd.concat([process_cell(data.iloc[i]) for i in range(len(data))]).reset_index(drop=True)

# Angenommener Dateiname für die CSV-Datei
csv_dateiname = Pfad + '/exportierte_data1.txt'
# Exportiere den DataFrame in eine CSV-Datei
info_array.to_csv(csv_dateiname, index=True)


print(info_array,info_array.shape)




