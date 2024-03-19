import pandas as pd
import glob
import pickle
import time
start_time = time.time()



pfad = 'C:/Users/erikm/Desktop/Diplomarbeit Erik Marr/Daten/Finish/Finish_D4_t_I_F'

#valu_dateien = glob.glob(Pfad + '/*_exportierte_data_D1.pkl')
#valu_dateien = glob.glob(Pfad + '/*_exportierte_data_D2.pkl')
#valu_dateien = glob.glob(Pfad + '/*_exportierte_data_D3.pkl')
valu_dateien = glob.glob(pfad + '/*_exportierte_data_D4.pkl')


for datei in valu_dateien:
    data = pd.read_pickle(datei)
    data.columns = ['X-Koordinate','Y-Koordinate','Zeitpunkt','Strom','Kraft','Temperatur']



    filtered_Radius = data.loc[data['X-Koordinate'] > 0.0025, 'X-Koordinate']

    data = data.drop(filtered_Radius.index)
    data.reset_index(drop=True, inplace=True)
    print(data)
    print(f' Filtered: {filtered_Radius.count()}')
    #pkl_dateiname = datei.replace('_exportierte_data_D1.pkl', '_finish_data_D1.pkl')
    #pkl_dateiname = datei.replace('_exportierte_data_D2.pkl', '_finish_data_D2.pkl')
    #pkl_dateiname = datei.replace('_exportierte_data_D3.pkl', '_finish_data_D3.pkl')
    pkl_dateiname = datei.replace('_exportierte_data_D4.pkl', '_finish_data_D4.pkl')

    data.to_pickle(pkl_dateiname)

end_time = time.time()

# Berechne die Dauer
duration = end_time - start_time

print(f"Die Ausführungszeit betrug {duration} Sekunden.")

