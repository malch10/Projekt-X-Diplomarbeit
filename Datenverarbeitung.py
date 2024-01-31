import pandas as pd

Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'

data = pd.read_csv(Pfad + '/exportierte_data.txt', sep=',', header=None)

print(data)