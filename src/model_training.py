import torch
from torch import nn
from torch.utils.data import DataLoader
from transformers import AdamW, get_linear_schedule_with_warmup
from src.data_preprocessing import load_data, preprocess_data
from src.model_evaluation import evaluate_model
from models import MyModel  # Assurez-vous d'importer votre modèle ici

def train_model(model, train_dataset, val_dataset, epochs=3, batch_size=32, learning_rate=5e-5):
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    optimizer = AdamW(model.parameters(), lr=learning_rate)
    total_steps = len(train_loader) * epochs
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

    for epoch in range(epochs):
        model.train()
        total_loss = 0

        for batch in train_loader:
            optimizer.zero_grad()
            inputs, labels = batch
            outputs = model(inputs)
            loss = nn.CrossEntropyLoss()(outputs, labels)
            loss.backward()
            optimizer.step()
            scheduler.step()
            total_loss += loss.item()

        avg_train_loss = total_loss / len(train_loader)
        print(f'Epoch {epoch + 1}/{epochs}, Training Loss: {avg_train_loss}')

        # Évaluation du modèle sur l'ensemble de validation
        val_loss, val_accuracy = evaluate_model(model, val_loader)
        print(f'Epoch {epoch + 1}/{epochs}, Validation Loss: {val_loss}, Validation Accuracy: {val_accuracy}')

if __name__ == "__main__":
    # Charger et prétraiter les données
    train_data, val_data = load_data()
    train_dataset = preprocess_data(train_data)
    val_dataset = preprocess_data(val_data)

    # Initialiser le modèle
    model = MyModel()  # Remplacez par votre classe de modèle

    # Entraîner le modèle
    train_model(model, train_dataset, val_dataset)