import pandas as pd

# Pfad zur Excel-Datei, die die Bewertungen und Tags enthält
file_path = "C:\\Users\\Nikol\\.spyder-py3\\Projects\\Hamburg\\Comments_To_Concepts_Final.xlsx"

# Die Excel-Datei wird geladen und die "Kommentarliste" Tabelle wird gelesen
xl = pd.ExcelFile(file_path)
df = xl.parse("Kommentarliste")

# Initialisierung der Ergebnis-DataFrame mit den Spalten 'Comment' und 'Overlapping_Tags'
columns = ['Comment', 'Overlapping_Tags']
result_df = pd.DataFrame(columns=columns)

# Iteration durch die Zeilen der geladenen DataFrame
for index, row in df.iterrows():
    # Die Tags von den drei Bewertern (Amira, Marcel und Alex) werden in separaten Sets gespeichert
    amira_tags = set(str(row[6]).split(','))
    marcel_tags = set(str(row[7]).split(','))
    alex_tags = set(str(row[8]).split(','))

    # Findet die gemeinsamen Tags (Überschneidungen) zwischen den Bewertungen aller Bewerter
    overlapping_tags = amira_tags.intersection(marcel_tags).intersection(alex_tags)

    # Wenn es Überschneidungen gibt, werden diese zusammen mit dem zugehörigen Kommentar zur Ergebnis-DataFrame hinzugefügt
    if overlapping_tags:
        comment = row[3]
        result_df = result_df.append({'Comment': comment, 'Overlapping_Tags': ', '.join(overlapping_tags)}, ignore_index=True)

# Die resultierende DataFrame wird in einer neuen Excel-Datei gespeichert
result_df.to_excel("Overlapping_Tags_and_Comments.xlsx", index=False)
