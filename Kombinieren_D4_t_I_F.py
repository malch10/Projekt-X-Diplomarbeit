import os
import pickle


def combine_pkl_files(folder_path, output_file_path):
    # Liste aller .pkl-Dateien im angegebenen Ordner
    pkl_files = [file for file in os.listdir(folder_path) if file.endswith('.pkl')]

    combined_data = []
    for file_name in pkl_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'rb') as file:
            # Lade die Daten aus der .pkl-Datei
            data = pickle.load(file)
            combined_data.append(data)

    # Schreibe die kombinierten Daten in eine neue .pkl-Datei
    with open(output_file_path, 'wb') as output_file:
        pickle.dump(combined_data, output_file)


# Beispielaufruf der Funktion
folder_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_D4_t_I_F_PKL'  # Ersetzen Sie dies mit dem Pfad zu Ihrem Ordner
output_file_path = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_ALL_D4_t_I_F_PKL'  # Name der kombinierten .pkl-Datei
combine_pkl_files(folder_path, output_file_path)
