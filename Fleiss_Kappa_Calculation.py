import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa

# Pfad zur Excel-Datei - bitte bei Bedarf aktualisieren!
file_path = "C:\\Users\\Nikol\\.spyder-py3\\Projects\\Hamburg\\Comments_To_Concepts.xlsx"

# Excel-Datei laden
xl = pd.ExcelFile(file_path)
df = xl.parse("Kommentarliste")

# Liste der möglichen Subjekte, auf die sich Tags beziehen können
subjects = [
    "location", "street", "zone", "city", "store", "river", "lake", "person", "resident",
    "politican", "tourist", "pedestrian", "traffic", "sign", "vehicle", "bicycle", "transport",
    "train", "plane", "time", "date", "period", "day", "night", "year", "mood", "positive",
    "negative", "neutral", "type", "suggestion", "experience", "money", "link", "noise", "ticket",
    "construction", "trafficlight", "parking", "speedcam"
]

# Funktion, um eine binäre Matrix zu erstellen, die angibt, ob ein Tag in den Tags eines Raters vorkommt
def binary_matrix(tags, subjects):
    binary_tags = [1 if subject in tags else 0 for subject in subjects]
    return binary_tags

# Funktion zum Aggregieren der Bewertungen der Rater in einer Matrix.
# Diese Matrix zeigt für jeden Rater an, ob sie das Subjekt getaggt haben oder nicht.
def aggregate_raters(matrix, num_raters):
    n_subjects = len(matrix)
    aggregated_matrix = np.zeros((n_subjects, num_raters))

    for i in range(n_subjects):
        count_1s = np.sum(matrix[i])
        aggregated_matrix[i, 0] = count_1s
        aggregated_matrix[i, 1] = num_raters - count_1s

    return aggregated_matrix

# Haupt-Loop, der den Fleiss-Kappa-Wert für jede Zeile in der DataFrame berechnet
fleiss_kappas = []
for index, row in df.iterrows():
    # Extrahiere die Tags von jedem Rater
    amira_tags = str(row[6]).split(',')
    marcel_tags = str(row[7]).split(',')
    alex_tags = str(row[8]).split(',')

    # Erstelle binäre Matrizen für die Tags der Rater
    amira_matrix = binary_matrix(amira_tags, subjects)
    marcel_matrix = binary_matrix(marcel_tags, subjects)
    alex_matrix = binary_matrix(alex_tags, subjects)

    # Kombiniere die binären Matrizen der Rater
    combined_matrix = []

    for i in range(len(subjects)):
        combined_matrix.append([amira_matrix[i], marcel_matrix[i], alex_matrix[i]])

    # Aggregiere die Bewertungen der Rater
    aggregated_matrix = aggregate_raters(combined_matrix, 3)
    
    # Berechne den Fleiss-Kappa-Wert und füge ihn zur Liste hinzu
    kappa = fleiss_kappa(aggregated_matrix, method='fleiss')
    fleiss_kappas.append(kappa)

# Füge die berechneten Fleiss-Kappa-Werte als neue Spalte zur DataFrame hinzu
df['Fleiss_Kappa'] = fleiss_kappas

# Speichern Sie die aktualisierte DataFrame in einer neuen Excel-Datei
df.to_excel("Comments_To_Concepts_with_Fleiss_Kappa.xlsx", index=False)
