import os
import pandas as pd

def combine_pandas_pkl_files(folder_path, output_file_path):
    # Erstellt eine Liste aller .pkl Dateien im angegebenen Ordner
    pkl_files = [file for file in os.listdir(folder_path) if file.endswith('.pkl')]

    # Initialisiert einen leeren DataFrame, der zum Kombinieren aller Daten verwendet wird
    combined_df = pd.DataFrame()
    first_file = True  # Variable, um zu überprüfen, ob die Datei die erste in der Liste ist

    # Durchläuft alle gefundenen .pkl Dateien
    for file_name in pkl_files:
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_pickle(file_path)  # Lädt jeden DataFrame aus der .pkl Datei

        if first_file:
            # Speichere die Spaltennamen der ersten Datei, um Konsistenz zu gewährleisten
            column_names = df.columns
            first_file = False
        else:
            # Setze die Spaltennamen in allen folgenden DataFrames auf die der ersten Datei
            df = df.reindex(columns=column_names)

        # Fügt den aktuellen DataFrame zum kombinierten DataFrame hinzu
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Speichere den kombinierten DataFrame als .pkl-Datei im angegebenen Ausgabepfad
    combined_df.to_pickle(output_file_path)

# Beispielaufruf der Funktion
folder_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_D4_t_I_F_PKL'  # Ordnerpfad
output_file_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_ALL_D4_t_I_F_PKL.pkl'  # Name der kombinierten .pkl-Datei
combine_pandas_pkl_files(folder_path, output_file_path)
