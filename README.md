# Reduzierung Berechnungszeit von FE-Simulationen durch maschinelles Lernen 

## Beschreibung des Projekts

In diesem Projekt habe ich mich mit maschinellem Lernen und der Anwendung im Bereich von FE-Simulationen beschäftigt.
Die Hauptaufgabe besteht darin, ein ML-Modell zu erstellen, das effizient und genau vorhersagen kann, ob ein Schweißpunkt gelingt oder nicht.

## Ausgangsdaten

Die Ausgangsdaten sind Textdateien, die die Temperaturverteilung in der Fügezone (ROI) beschreiben. Die Daten basieren auf validierten Finite-Element-Simulationen. Eine Ausgangsdatei ist eine TXT-Datei und beschreibt einen Zeitpunkt mit einem Temperaturfeld. 
Mehrere Zeitpunkte ergeben zusammengefasst den Schweißprozess.
## Datenvorverarbeitung 

Für die Datenvorverarbeitung werden die Daten der FE-Simulationen für den jeweiligen Anwendungsfall vorbereitet. Die Programme der 'Datenbeschaffung' befassen sich mit der Vorbereitung. 

Datenbeschaffung_D1-D4:

- erstellt Datenpakete mit absteigender Auflösung der ROI 
- die Textdateien werden als 'exportierte_data' gespeichert
-  Bsp. Syntax: TPath_100_valu.txt

Datenverarbeitung:

- Verarbeitet die Daten weiter von 'exportierte_data' zu 'finish_data'
- Datenpakete sind dann bereit verwendet zu werden

Datenbeschaffung_D1_t-D4_t:

- konkatiniert 'finish_data'- Dateien um eine fortlaufende Datei über die gesamte Schweißzeit eines Schweißprozesses zu erhalten

Export_D1_ALL-D4_ALL:

- durch die Änderung in der Datenbereitstellung musste eine abgewandelte Form von 'Datenbeschaffung' entwicklet werden, um auf Syntax-Änderungen einzugehen
- hat die gleich Aufgabe wie die 'Datenbeschaffung'
- die Textdateien werden als 'exportierte_data' gespeichert
- Bsp. Syntax: TempPSimI7000F6000_4_valu.txt

Kombinieren:

- Kombiniert alle .pkl Dateien eines Ordners zu einer großen .pkl Datei
- Kombination mehrerer Schweißprozesse zu einer Datei 
- Verwendung der Datei in beispielsweise: NeuroNetz_D3_t_9_I_F_1.ipynb

## Erstellung der neuronalen Netze

Für jedes NeuroNetz gibt es drei Varainten. Diese Variante resultieren aus der Durchführung von  Random Search um die Modellarchitektur zu finden.
Random Search wurde immer in der ersten Modellvarainte (Bsp. NeuroNetz_D1_1) durchgeführt, weswegen der Code dafür nur dort vorhanden ist.
Die Varianten unterscheiden sich ansonsten in den Hyperparamtern der neuronalen Netze. 
Die jeweils erste Variante jedes NeuroNetz wird ausführlich auskommentiert.

Kurze Beschreibung der erstellten Netze: (Trainingsdatensatz; Testdatensatz)

NeuroNetz_D1:

- Auflösung D1, X-Koordiante, Y-Koordinate; einzelne Temperaturen in der ROI
- Benutztes Datenpaket: TPath_500_finish_data_D1.pkl

NeuroNetz_D2:

- Auflösung D2, X-Koordiante, Y-Koordinate; einzelne Temperaturen in der ROI
- Benutztes Datenpaket: TPath_500_finish_data_D2.pkl

NeuroNetz_D3:

- Auflösung D3, X-Koordiante, Y-Koordinate; einzelne Temperaturen in der ROI
- Benutztes Datenpaket: TPath_500_finish_data_D3.pkl

NeuroNetz_D4:

- Auflösung D4, X-Koordiante, Y-Koordinate; einzelne Temperaturen in der ROI
- Benutztes Datenpaket: TPath_500_finish_data_D4.pkl

NeuroNetz_D3_I_F (High-1):

- Auflösung D3, X-Koordiante, Y-Koordinate, Strom, Kraft; Temperaturfeld einer unbekannten Simulation zu einem bestimmten Zeitpunkt
- Benutztes Datenpaket: Finish_ALL_D3_500_I_F_PKL.pkl

NeuroNetz_D3_t_9_I_F (High-9):

- Auflösung D3, X-Koordiante, Y-Koordinate, 9 Zeitschritte Strom, Kraft; Temperaturfeld einer unbekannten Simulation zu einem bestimmten Zeitpunkt, Temperaturfelder über die 9 Zeitschritte
- Benutztes Datenpaket: Finish_ALL_D3_t_9_I_F_PKL.pkl

NeuroNetz_D3_t_21_I_F (High-21):

- Auflösung D3, X-Koordiante, Y-Koordinate, 21 Zeitschritte Strom, Kraft; Temperaturfeld einer unbekannten Simulation zu einem bestimmten Zeitpunkt, Temperaturfelder über die 21 Zeitschritte
- Benutztes Datenpaket: Finish_ALL_D3_t_21_I_F_PKL.pkl

NeuroNetz_D4_I_F (Low-1):

- Auflösung D4, X-Koordiante, Y-Koordinate, Kraft; Temperaturfeld einer unbekannten Simulation zu einem bestimmten Zeitpunkt
- Benutztes Datenpaket: Finish_ALL_D4_500_I_F_PKL.pkl

NeuroNetz_D4_t_9_I_F (Low-9):

- Auflösung D4, X-Koordiante, Y-Koordinate, 9 Zeitschritte Strom, Kraft; Temperaturfeld einer unbekannten Simulation zu einem bestimmten Zeitpunkt, Temperaturfelder über die 9 Zeitschritte
- Benutztes Datenpaket: Finish_ALL_D4_t_9_I_F_PKL.pkl

NeuroNetz_D4_t_21_I_F (Low-21):

- Auflösung D4, X-Koordiante, Y-Koordinate, 21 Zeitschritte Strom, Kraft; Temperaturfeld einer unbekannten Simulation zu einem bestimmten Zeitpunkt, Temperaturfelder über die 21 Zeitschritte
- Benutztes Datenpaket: Finish_ALL_D4_t_21_I_F_PKL.pkl

## Plotting und Visualisierung

Diese Programme dienen dazu die Ergebnisse auszugeben. Plotting beschäftigt sich mit der Ausgabe unterschieldicher Plots um Zusammenhänge zu verdeutlichen.
Visualisierung wird genutzt um die Fügezone (ROI) abzubilden und darzustellen.

## Vorgehen bei der Erstellung neuronaler Netze für das jeweilige Datenpaket

- Vorverarbeitung der Daten (Feature Extraction, Feature Scaling, Datenbereinigung usw.)
- Erstellung einfach neuronaler Netze (Shallow Neural Network)
- Daten und Anforderungen verstehen
- Random Search Modellarchitektur finden (Rahmen festlegen in dem Architketur gesucht wird)
- Hyperparameteroptimierung der gefundenen Architekturen durch Grid Search 
- Kreuzvaliderung auf dem Trainingsdatensatz (Vergleich optinmierter Modelle miteinander, Einschätzung der Modellperformance)
- Bewertung und Vergleich der erstellten Netze auf dem Testdatensatz (Testdaten sollten Anwendungsfall widerspiegeln)
- Iterativer Verbesserungsprozess


## Verwendete Versionen 

Python 3.11 Keras 2.15 Keras-Tuner 
1.4.6 Matplotlib 3.8.2 Pandas 2.2.1 
Scikeras 0.12.0 TensorFlow 2.15 
Scikit-learn 1.4.0 Scipy 1.12 H5py 3.10


