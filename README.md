# Sentiment_Analysis_Hamburg
Meine Arbeit für das IT-Studienprojekt in Kooperation mit der Stadt Hamburg. In dieser Repository befinden sich eine Reihe von Pyhton-Files aus diesem Projekt.

## Fleiss_Kappa_Calculation.py
Dieses Python-Script berechnet den Fleiss-Kappa-Wert für eine gegebene Excel-Tabelle, die Bewertungen von mehreren Bewertern enthält. Es ist entworfen, um zu messen, wie konsistent die Bewertungen zwischen den verschiedenen Bewertern sind.

Die Bewertungen sind in Form von Tags, die jedem Subjekt in der Tabelle zugeordnet sind. Diese Tags repräsentieren verschiedene Kategorien wie Standort, Straße, Zone, Stadt und andere. 

Das Script führt die folgenden Schritte aus:

1. Es liest eine Excel-Datei ein, in der die Bewertungen der Bewerter gespeichert sind.
2. Es erstellt für jeden Bewerter eine binäre Matrix, die angibt, ob ein bestimmtes Subjekt getaggt wurde oder nicht.
3. Es aggregiert die Bewertungen der Bewerter in einer einzigen Matrix.
4. Es berechnet den Fleiss-Kappa-Wert für jede Zeile in der Matrix.
5. Es fügt den berechneten Fleiss-Kappa-Wert als neue Spalte zur ursprünglichen Tabelle hinzu.
6. Es speichert die aktualisierte Tabelle in einer neuen Excel-Datei.

Der Fleiss-Kappa-Wert ist ein Maß für die Übereinstimmung der Bewertungen zwischen den Bewertern. Werte nahe bei 1 deuten auf eine hohe Übereinstimmung hin, während Werte nahe bei 0 eine geringe Übereinstimmung anzeigen.

**Bitte beachten Sie:** Der Pfad zur Excel-Datei muss ggf. im Skript angepasst werden.
