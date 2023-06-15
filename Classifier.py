import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from collections import Counter

# Einlesen der Daten aus einer Excel-Datei
df = pd.read_excel("Overlapping_Tags_and_Comments.xlsx")

# Definieren einer Funktion zur Vorverarbeitung des Textes
def preprocess_text(text):
    # Ersetzen von speziellen Zeichen und Zahlen durch Leerzeichen
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    
    # Konvertieren des gesamten Textes in Kleinbuchstaben
    text = text.lower()
    
    # Entfernen von Stoppwörtern mithilfe der nltk-Bibliothek
    stop_words = set(stopwords.words('german'))
    words = nltk.word_tokenize(text)
    text = ' '.join([word for word in words if word not in stop_words])
    
    return text

# Anwenden der Vorverarbeitungsfunktion auf die Kommentarspalte
df['Comment'] = df['Comment'].apply(preprocess_text)

# Aufteilen der Daten in ein Trainingsset und ein Testset (70:30-Verhältnis)
train_df, val_df = train_test_split(df, test_size=0.3, random_state=42)

# Extrahieren der Kommentare und Labels für das Training und die Validierung
X_train = train_df["Comment"].values
X_val = val_df["Comment"].values

# Funktion zur Bereinigung und Standardisierung der Tags
def clean_labels(labels):
    cleaned = []
    for tag_list in labels:
        cleaned_list = [tag.lower().strip() for tag in tag_list]
        cleaned.append(cleaned_list)
    return cleaned

y_train = [tags.split(',') for tags in train_df["Overlapping_Tags"].values]
y_train = clean_labels(y_train)

y_val = [tags.split(',') for tags in val_df["Overlapping_Tags"].values]
y_val = clean_labels(y_val)

# Sammeln aller Tags aus dem Trainingset und Zählen ihrer Häufigkeiten
all_tags = [tag for tags_list in y_train for tag in tags_list]
tag_counter = Counter(all_tags)

# Bestimmen der n am häufigsten vorkommenden Tags
most_common_tags = tag_counter.most_common(6)  # Anzahl kann je nach Bedarf geändert werden

# Entfernen der Zählungen, um nur die Tags zu erhalten
most_common_tags = [tag[0] for tag in most_common_tags]

# Umwandlung der Tags in eine binäre Form
mlb = MultiLabelBinarizer(classes=most_common_tags)
y_train = mlb.fit_transform(y_train)
y_val = mlb.transform(y_val)

# Erstellen einer Machine-Learning-Pipeline, die einen TF-IDF-Vektorisierer und einen One-vs-Rest-Klassifikator enthält
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_df=0.8, min_df=5)),  # Anpassen der Parameter je nach Bedarf
    ("clf", OneVsRestClassifier(LinearSVC(C=1.5)))  # Anpassen des Regularisierungsparameters C je nach Bedarf
])

# Trainieren des Modells mit den Trainingsdaten
pipeline.fit(X_train, y_train)

# Vorhersagen für das Validierungsset machen
y_pred = pipeline.predict(X_val)

# Ausgabe eines Berichts zur Leistung des Modells auf den Validierungsdaten
print(classification_report(y_val, y_pred, target_names=mlb.classes_, zero_division=0))
