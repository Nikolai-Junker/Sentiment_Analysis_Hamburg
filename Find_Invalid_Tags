import pandas as pd

# Liste der anerkannten Subjekte
subjects = [
    "location", "street", "zone", "city", "store", "river", "lake", "person", "resident",
    "politican", "tourist", "pedestrian", "traffic", "sign", "vehicle", "bicycle", "transport",
    "train", "plane", "time", "date", "period", "day", "night", "year", "mood", "positive",
    "negative", "neutral", "type", "suggestion", "experience", "money", "link", "noise", "ticket",
    "construction", "trafficlight", "parking", "speedcam", "misc"
]

# Lade die Excel-Datei
# Aktualisieren Sie den Pfad zur Excel-Datei entsprechend, falls das Script extern ausgeführt wird
file_path = "C:\\Users\\Nikol\\.spyder-py3\\Projects\\Hamburg\\Comments_To_Concepts(3).xlsx"
xl = pd.ExcelFile(file_path)
df = xl.parse("Kommentarliste")

# Initialisiere die Ergebnis DataFrame
# Diese enthält die Spalten 'Row', 'Rater' und 'Invalid_Tag'
columns = ['Row', 'Rater', 'Invalid_Tag']
result_df = pd.DataFrame(columns=columns)

# Iteriere durch die Reihen der DataFrame
# In jeder Reihe werden die Tags der Bewerter 'Amira', 'Marcel' und 'Alex' gelesen
# und mit den anerkannten Subjekten verglichen
for index, row in df.iterrows():
    amira_tags = str(row[6]).split(',')
    marcel_tags = str(row[7]).split(',')
    alex_tags = str(row[8]).split(',')

    for rater, tags in zip(['Amira', 'Marcel', 'Alex'], [amira_tags, marcel_tags, alex_tags]):
        for tag in tags:
            tag = tag.strip() # Entferne mögliche Leerzeichen vor/nach dem Tag
            if tag not in subjects:
                # Wenn das Tag nicht in den anerkannten Subjekten ist, füge es zur Ergebnis DataFrame hinzu
                result_df = result_df.append({'Row': index + 2, 'Rater': rater, 'Invalid_Tag': tag}, ignore_index=True)

# Speichere die Ergebnis DataFrame in einer neuen Excel-Datei
result_df.to_excel("Invalid_Tags.xlsx", index=False)
