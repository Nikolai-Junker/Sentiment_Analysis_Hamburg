# Sentiment_Analysis_Hamburg
Meine Arbeit für das IT-Studienprojekt in Kooperation mit der Stadt Hamburg. In dieser Repository befinden sich eine Reihe von Pyhton-Files aus diesem Projekt.

## Fleiss_Kappa_Calculation.py
Dieses Python-Skript berechnet den Fleiss-Kappa-Wert für eine gegebene Excel-Tabelle, die Bewertungen von mehreren Bewertern enthält. Es ist entworfen, um zu messen, wie konsistent die Bewertungen zwischen den verschiedenen Bewertern sind.

Die Bewertungen sind in Form von Tags, die jedem Subjekt in der Tabelle zugeordnet sind. Diese Tags repräsentieren verschiedene Kategorien wie Standort, Straße, Zone, Stadt und andere. 

Das Skript führt die folgenden Schritte aus:

1. Es liest eine Excel-Datei ein, in der die Bewertungen der Bewerter gespeichert sind.
2. Es erstellt für jeden Bewerter eine binäre Matrix, die angibt, ob ein bestimmtes Subjekt getaggt wurde oder nicht.
3. Es aggregiert die Bewertungen der Bewerter in einer einzigen Matrix.
4. Es berechnet den Fleiss-Kappa-Wert für jede Zeile in der Matrix.
5. Es fügt den berechneten Fleiss-Kappa-Wert als neue Spalte zur ursprünglichen Tabelle hinzu.
6. Es speichert die aktualisierte Tabelle in einer neuen Excel-Datei.

Der Fleiss-Kappa-Wert ist ein Maß für die Übereinstimmung der Bewertungen zwischen den Bewertern. Werte nahe bei 1 deuten auf eine hohe Übereinstimmung hin, während Werte nahe bei 0 eine geringe Übereinstimmung anzeigen.

**Bitte beachten:** Der Pfad zur Excel-Datei muss ggf. im Skript angepasst werden.

## Find_Invalid_Tags.py

Dieses Skript dient zur Identifikation von ungültigen oder fehlerhaften Tags in den Bewertungen. Im Detail durchläuft es alle Bewertungen und prüft dabei, ob die von den Ratern angegebenen Tags in der zuvor definierten Tag-Liste vorhanden sind. 

Im Falle, dass ein Tag nicht in der Liste gefunden wird, wird dieser als ungültig eingestuft. Informationen über den jeweiligen Tag, den zugehörigen Rater und die Zeilennummer werden dann in eine separate Excel-Datei geschrieben.

Die Ausgabe dieses Prozesses ermöglicht eine effiziente Fehlerbehebung und trägt zur Qualitätssicherung der Daten bei, da problematische Tags und ihre Quellen leicht identifiziert und adressiert werden können.

## Find_Overlapping_Tags.py

Das Python-Skript "Find_Overlapping_Tags.py" ist dazu gedacht, Überschneidungen in den Tags zu identifizieren, die von verschiedenen Bewertern in einer Textanalyse vergeben wurden.

### Funktionsweise

Das Skript lädt eine Excel-Datei, die die Bewertungen und Tags enthält. Anschließend wird eine leere DataFrame initialisiert, in die die Kommentare und die Überschneidungen der Tags eingetragen werden.

Das Skript geht dann zeilenweise durch die geladene DataFrame und speichert die Tags von jedem Bewerter in separaten Sets. Durch die Verwendung von Sets wird jedes Tag nur einmal gespeichert, auch wenn es mehrfach im Originaldatensatz vorkommt. Anschließend berechnet das Skript die Schnittmenge der drei Sets, um die Überschneidungen in den Tags zu finden.

Falls Überschneidungen existieren, fügt das Skript den Kommentar und die Überschneidungen der Tags zur zuvor erstellten Ergebnis-DataFrame hinzu. Am Ende des Skripts wird die resultierende DataFrame in einer neuen Excel-Datei gespeichert.

### Nutzung

Das Skript benötigt eine Excel-Datei als Eingabe, die eine Tabelle namens "Kommentarliste" enthalten muss. Diese Tabelle sollte Spalten für die Kommentare und die Tags von jedem Bewerter enthalten. Das Skript erstellt dann eine neue Excel-Datei, die die Kommentare und die Überschneidungen der Tags enthält.

## Classifier.py
Das Python-Skript "Classifier" dient zur Kommentarklassifizierung mit mehreren Labels, welche aus einem Datensatz von Kommentaren und zugehörigen Tags abgeleitet werden.

### Funktionsweise

Das Skript lädt zunächst eine Excel-Datei mit den Kommentaren und den zugeordneten Tags. Nachdem die Daten eingelesen wurden, durchläuft jeder Kommentar einen Preprocessing-Prozess, bei dem spezielle Zeichen, Zahlen und Stopwörter entfernt und alle Buchstaben in Kleinbuchstaben umgewandelt werden.

Danach wird der Datensatz in ein Trainings- und ein Testset aufgeteilt. Für jedes Set werden die Kommentare und die zugehörigen Tags extrahiert. Die Tags werden bereinigt, standardisiert und schließlich in eine binäre Form umgewandelt, sodass sie von dem Modell verarbeitet werden können.

Anschließend wird eine Pipeline erstellt, die einen TfidfVectorizer zur Textvektorierung und einen OneVsRestClassifier mit einem LinearSVC-Klassifikator enthält. Mit dieser Pipeline wird das Modell auf den Trainingsdaten trainiert.

Abschließend wird das trainierte Modell auf dem Testset validiert und die Leistung des Modells wird mit einem Klassifikationsbericht bewertet.

### Nutzung

Das Skript benötigt eine Excel-Datei mit den Kommentaren und zugehörigen Tags als Eingabe. Die Kommentare sollten bereits vorverarbeitet sein und die Tags sollten in einer kommagetrennten Liste vorliegen. Das Skript liefert als Ausgabe die Leistungsbeurteilung des trainierten Modells auf dem Testdatensatz.

## Ensemble_Classifier.py
Dieses Skript stellt einen fortschrittlichen Kommentarklassifizierer dar, welcher maschinelles Lernen einsetzt, um mehrere passende Tags für gegebene Kommentare vorherzusagen.
Aufgrund von Feedback wurde ein Ansatz basierend auf ensemble classification mit random forst gewählt, um die geringe Datenmenge zu kompensieren. 

## Funktionsweise

Zunächst lädt das Skript eine Excel-Datei, die eine Reihe von Kommentaren und die dazugehörigen Tags enthält. Jeder dieser Kommentare durchläuft dann einen ausführlichen Preprocessing-Prozess. Dieser beinhaltet die Entfernung von speziellen Zeichen, Zahlen und Stoppwörtern sowie die Konvertierung aller Buchstaben in Kleinbuchstaben. Darüber hinaus werden sämtliche Akzente und diakritische Zeichen aus dem Text entfernt, um die Textdaten zu standardisieren.

Im nächsten Schritt teilt das Skript die eingelesenen Daten in Trainings- und Validierungssets. Es extrahiert Kommentare und die jeweiligen Tags, reinigt und normalisiert diese Tags und wandelt sie in eine binäre Form um.

Anschließend werden die sechs häufigsten Tags aus dem Trainingsset ermittelt und zur Modellierung verwendet. Diese Selektion ermöglicht es, die Komplexität des Modells zu reduzieren und die Rechenleistung zu optimieren.

Das Skript stellt dann ein Ensemble von Klassifikatoren zusammen (einschließlich SGD, SVC und RandomForest), die durch eine Abstimmungsstrategie kombiniert werden. Mit Hilfe einer Pipeline wird die Textvektorierung durchgeführt und das Ensemblemodell auf den Trainingsdaten trainiert.

Am Ende wird das trainierte Modell auf den Validierungsdaten getestet, um seine Fähigkeit zur Vorhersage von Tags auf neuen, unbekannten Daten zu beurteilen. Die Leistung des Modells wird dann durch einen detaillierten Klassifikationsbericht dargestellt.

### Nutzung

Das Skript erfordert eine Excel-Datei als Input, welche eine Tabelle mit den Spalten "Comment" und "Overlapping_Tags" enthält. Die Spalte "Comment" sollte die zu klassifizierenden Textkommentare und die Spalte "Overlapping_Tags" die zugehörigen Tags enthalten. Das Skript nutzt diese Informationen, um ein maschinelles Lernmodell zu trainieren und zu validieren, das die Tags für die Kommentare vorhersagt. Am Ende der Ausführung gibt das Skript einen detaillierten Klassifikationsbericht aus, der die Vorhersageleistung des Modells bewertet.

