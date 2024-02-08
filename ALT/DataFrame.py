import pandas as pd
import os

# Pfad zum Ordner setzen, der die Textdateien enthält
ordner_pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/DatenSimulation'  # Ersetzen Sie dies mit dem tatsächlichen Pfad

# Liste, um die DataFrames zu speichern
df_list = pd.DataFrame()

df_x = []
df_y = []
df_t = []


df_x = pd.read_csv("C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/DatenSimulation/Skalen/TPath_coorX.txt",delimiter='  ', engine='python' )
df_y = pd.read_csv("C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/DatenSimulation/Skalen/TPath_coorY.txt",delimiter='  ', engine='python' )
df_t = pd.read_csv("C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/DatenSimulation/Skalen/TPath_time.txt",delimiter='  ', engine='python' )
df_x_list = df_x.iloc[:, 0].tolist()
df_y_list = df_y.iloc[:, 0].tolist()
df_t_list = df_t.iloc[:, 0].tolist()


df_list = pd.DataFrame(columns=df_x_list)


#print(df_list)






# Durchlaufen aller Dateien im Ordner
for dateiname in os.listdir(ordner_pfad):
    if dateiname.startswith('TPath'):
        datei_pfad = os.path.join(ordner_pfad, dateiname)

        # Laden der Datei als DataFrame
        # Angenommen, Ihre Textdateien sind durch Kommas getrennt (CSV)
        # Für andere Trennzeichen, ändern Sie das 'sep' Argument entsprechend
        df = pd.read_csv(datei_pfad, delimiter='  ', engine='python')
        # Fügen Sie den DataFrame zur Liste hinzu
        df = pd.DataFrame(columns=df_y_list)

        print (df)

        melted_df = df.reset_index().melt(id_vars='index')

        print(melted_df)



#         df_list.append(df)
#
# # Kombinieren aller DataFrames in der Liste zu einem einzelnen DataFrame
# kombinierter_df = pd.concat(df_list, ignore_index=True)

# Zeigen Sie das resultierende DataFrame an

