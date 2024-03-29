import os
import pickle

import os
import pandas as pd


def combine_pandas_pkl_files(folder_path, output_file_path):
    pkl_files = [file for file in os.listdir(folder_path) if file.endswith('.pkl')]

    combined_df = pd.DataFrame()
    first_file = True
    for file_name in pkl_files:
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_pickle(file_path)

        if first_file:
            # Speichere die Spaltennamen der ersten Datei
            column_names = df.columns
            first_file = False
        else:
            # Setze die Spaltennamen in allen folgenden DataFrames auf die der ersten Datei
            df = df.reindex(columns=column_names)

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Speichere den kombinierten DataFrame als .pkl-Datei
    combined_df.to_pickle(output_file_path)


# Beispielaufruf der Funktion
folder_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_D3_t_I_F_PKL'  # Ersetzen Sie dies mit dem Pfad zu Ihrem Ordner
output_file_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_ALL_D3_t_I_F_PKL.pkl'  # Name der kombinierten .pkl-Datei
combine_pandas_pkl_files(folder_path, output_file_path)
