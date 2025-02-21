def evaluate_model(model, test_loader, criterion):
    model.eval()
    total_loss = 0
    correct_predictions = 0
    total_samples = 0

    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            total_loss += loss.item()

            _, predicted = torch.max(outputs, 1)
            correct_predictions += (predicted == labels).sum().item()
            total_samples += labels.size(0)

    average_loss = total_loss / len(test_loader)
    accuracy = correct_predictions / total_samples

    return average_loss, accuracy

def save_evaluation_results(results, filepath):
    with open(filepath, 'w') as f:
        f.write("Average Loss: {}\n".format(results[0]))
        f.write("Accuracy: {}\n".format(results[1]))