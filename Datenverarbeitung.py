import pandas as pd

Pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/I7000_F9000'

data = pd.read_csv(Pfad + '/exportierte_data.txt', sep=',' , index_col = 0)


data.columns = ['X-Koordinate','Y-Koordinate','Temperatur']


print(data)

anzahl_vorkommen = (data['X-Koordinate'] == 0.003).sum()

#print(f'Die Anzahl an ist {anzahl_vorkommen}')

#print(data['X-Koordinate'].value_counts())

#print(data.describe())

data = data.drop(0)

print(data)