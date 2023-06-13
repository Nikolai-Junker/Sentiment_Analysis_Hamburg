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

## Find_Invalid_Tags.py

Dieses Skript dient zur Identifikation von ungültigen oder fehlerhaften Tags in den Bewertungen. Im Detail durchläuft es alle Bewertungen und prüft dabei, ob die von den Ratern angegebenen Tags in der zuvor definierten Tag-Liste vorhanden sind. 

Im Falle, dass ein Tag nicht in der Liste gefunden wird, wird dieser als ungültig eingestuft. Informationen über den jeweiligen Tag, den zugehörigen Rater und die Zeilennummer werden dann in eine separate Excel-Datei geschrieben.

Die Ausgabe dieses Prozesses ermöglicht eine effiziente Fehlerbehebung und trägt zur Qualitätssicherung der Daten bei, da problematische Tags und ihre Quellen leicht identifiziert und adressiert werden können.
