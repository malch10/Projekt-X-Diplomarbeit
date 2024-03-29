import pandas as pd
import os
import re


def sort_files_by_number(files):
    """Sortiere die Dateien basierend auf der ersten gefundenen Zahl im Dateinamen."""

    def extract_number(file_name):
        # Finde alle Zahlen im Dateinamen und gebe die erste gefundene Zahl zurück
        numbers = re.findall(r'\d+', file_name)
        return int(numbers[2]) if numbers else 0

    files.sort(key=extract_number)


def load_and_combine_pkl_files(folder_path):
    # Liste zur Speicherung der DataFrames
    dfs = []

    # Liste aller .pkl-Dateien im Ordner erhalten
    pkl_files = [f for f in os.listdir(folder_path) if f.endswith('.pkl')]

    # Sortiere die Dateien nach Zahlen, die in den Dateinamen enthalten sind
    sort_files_by_number(pkl_files)

    # Berücksichtige nur die hundertste Datei und jede zehnte Datei danach
    relevant_files = pkl_files[99::10]  # Beachte: Die Zählung beginnt bei 0

    # Durchlaufe die ausgewählten Dateien
    for filename in relevant_files:
        file_path = os.path.join(folder_path, filename)

        # Lese die Pickle-Datei und füge den DataFrame zur Liste hinzu
        df = pd.read_pickle(file_path)
        dfs.append(df)

    # Kombiniere alle DataFrames in der Liste untereinander
    combined_df = pd.concat(dfs, ignore_index=True)

    # Setze den Index des kombinierten DataFrames neu
    combined_df.reset_index(drop=True, inplace=True)

    return combined_df


# Pfad zum Ordner mit den .pkl-Dateien (anpassen nach Bedarf)
folder_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_D3_I6000_F5000'
save_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/D3_t_I6000_F5000.pkl'

# Funktion aufrufen und das Ergebnis in 'result_df' speichern
result_df = load_and_combine_pkl_files(folder_path)

# Speichere das kombinierte DataFrame
result_df.to_pickle(save_path)

# Ergebnis anzeigen
print(result_df['Zeitpunkt'].nunique())

# Speichere das kombinierte DataFrame
result_df.to_pickle(save_path)
print(result_df['Zeitpunkt'].min(), result_df['Zeitpunkt'].max())
# Ergebnis anzeigen

