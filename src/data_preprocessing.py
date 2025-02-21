import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
import re

def load_data(file_path):
    """Charge les données à partir d'un fichier CSV."""
    data = pd.read_csv(file_path)
    return data

def clean_text(text):
    """Nettoie le texte en supprimant les caractères spéciaux et en normalisant."""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    return text

def preprocess_data(data):
    """Prétraite les données en nettoyant le texte et en encodant les étiquettes."""
    data['cleaned_text'] = data['text'].apply(clean_text)
    
    label_encoder = LabelEncoder()
    data['encoded_labels'] = label_encoder.fit_transform(data['label'])
    
    return data

def split_data(data, test_size=0.2, random_state=42):
    """Divise les données en ensembles d'entraînement et de test."""
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, test_data

def save_processed_data(data, file_path):
    """Sauvegarde les données prétraitées dans un fichier CSV."""
    data.to_csv(file_path, index=False)