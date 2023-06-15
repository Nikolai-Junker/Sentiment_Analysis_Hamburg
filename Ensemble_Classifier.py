# Importieren der erforderlichen Bibliotheken
import pandas as pd  # Für Datenmanipulation und -analyse
import re  # Reguläre Ausdrücke für die Stringmanipulation
import nltk  # Natural Language Toolkit für Textanalyse
from nltk.corpus import stopwords  # Für die Entfernung von Stop-Wörtern
from sklearn.feature_extraction.text import TfidfVectorizer  # Für die Textvektorierung
from sklearn.preprocessing import MultiLabelBinarizer  # Zum Umwandeln der Labels in binäre Form
from sklearn.model_selection import train_test_split  # Zum Teilen der Daten in Trainings- und Testset
from sklearn.pipeline import Pipeline  # Zum Erstellen einer Pipeline zur Automatisierung des Modell-Trainingsprozesses
from sklearn.ensemble import RandomForestClassifier  # RandomForest-Klassifikator
from sklearn.linear_model import SGDClassifier  # SGD-Klassifikator
from sklearn.svm import SVC  # SVC-Klassifikator
from sklearn.multiclass import OneVsRestClassifier  # Für die Multilabel-Klassifikation
from sklearn.metrics import classification_report  # Zum Generieren des Klassifikationsberichts
from collections import Counter  # Zum Zählen der Tags
from unidecode import unidecode  # Zum Entfernen von Akzenten

# Daten einlesen
df = pd.read_excel("Overlapping_Tags_and_Comments.xlsx")  # Liest die Excel-Datei in eine DataFrame

# Funktion für Text-Preprocessing
def preprocess_text(text):
    text = unidecode(text)  # Entfernen von Akzenten
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # Entfernen spezieller Zeichen und Nummern
    
    text = text.lower()  # Konvertieren alles zu Kleinbuchstaben
    
    stop_words = set(stopwords.words('german'))  # Setzen der deutschen Stop-Wörter
    words = nltk.word_tokenize(text)  # Aufteilen des Texts in einzelne Wörter
    text = ' '.join([word for word in words if word not in stop_words])  # Entfernen der Stop-Wörter und Verbinden der restlichen Wörter zurück in einen Satz
    
    return text  # Rückgabe des vorverarbeiteten Texts

# Funktion zum Bereinigen und Standardisieren der Tags
def clean_labels(labels):
    cleaned = []  # Initialisierung einer leeren Liste für die gereinigten Tags
    for tag_list in labels:  # Gehe durch jede Tag-Liste
        cleaned_list = [tag.lower().strip() for tag in tag_list]  # Konvertiere jeden Tag zu Kleinbuchstaben und entferne Leerzeichen
        cleaned.append(cleaned_list)  # Füge die gereinigte Liste der Tags zur 'cleaned'-Liste hinzu
    return cleaned  # Rückgabe der Liste mit gereinigten Tags

# Verarbeite die Kommentare mit der Funktion
df['Comment'] = df['Comment'].apply(preprocess_text)  # Anwenden der Preprocessing-Funktion auf jeden Kommentar in der DataFrame

# Spalten der Daten in 70/30 Split
train_df, val_df = train_test_split(df, test_size=0.3, random_state=42)  # Teilen der Daten in ein Trainings- und ein Testset

# Extrahiere die Kommentare und Labels aus den Trainings- und Testdaten
X_train = train_df["Comment"].values  # Extrahieren der Kommentare aus dem Trainingsdatensatz
X_val = val_df["Comment"].values  # Extrahieren der Kommentare aus dem Testdatensatz

# Trennen der Tags mit einem Komma und bereinigen der Tags
y_train = [tags.split(',') for tags in train_df["Overlapping_Tags"].values]
y_val = [tags.split(',') for tags in val_df["Overlapping_Tags"].values]
y_train = clean_labels(y_train)
y_val = clean_labels(y_val)

# Reduziere die Dimensionen der Tags und zähle die Frequenz der einzelnen Tags
all_tags = [tag for tags_list in y_train for tag in tags_list]
tag_counter = Counter(all_tags)

# Finde die n am häufigsten vorkommenden Tags
most_common_tags = tag_counter.most_common(6)

# Extrahiere nur die Tags, nicht ihre Anzahl
most_common_tags = [tag[0] for tag in most_common_tags]

# Umwandeln der Tags in binäre Form
mlb = MultiLabelBinarizer(classes=most_common_tags)
y_train = mlb.fit_transform(y_train)
y_val = mlb.transform(y_val)

# Einstellen der Parameter für die Klassifikatoren
clf1 = SGDClassifier(loss='log_loss', alpha=0.0001)  
clf2 = SVC(C=1, gamma=1, kernel='sigmoid', degree=4, probability=True)
clf3 = RandomForestClassifier(n_estimators=100)

# Konfigurieren des Voting-Klassifikators, der die oben definierten Klassifikatoren verwendet
eclf = VotingClassifier(
    estimators=[('sgd', clf1), ('svc', clf2), ('rf', clf3)],
    voting='soft'
)

# Erstellen der Pipeline, die einen TfidfVectorizer und den Voting-Klassifikator enthält
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_df=0.8, min_df=5, use_idf=False)),
    ("clf", OneVsRestClassifier(eclf))
])

# Trainiere das Modell
pipeline.fit(X_train, y_train)

# Vorhersagen der Labels für die Testdaten
y_pred = pipeline.predict(X_val)

# Ausgabe des Klassifikationsberichts
print(classification_report(y_val, y_pred, target_names=mlb.classes_, zero_division=0))
