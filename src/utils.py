def load_json(file_path):
    import json
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    import json
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def create_directory(directory_path):
    import os
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def set_seed(seed):
    import random
    import numpy as np
    import torch
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def print_model_summary(model):
    from torchsummary import summary
    summary(model, input_size=(3, 224, 224))  # Adjust input size as necessary

def get_device():
    import torch
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")