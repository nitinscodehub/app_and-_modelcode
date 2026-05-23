import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split
from sklearn.preprocessing import StandardScaler
from model import ParkinsonGaitLSTM

def load_real_data(data_dir, window_size=200, step_size=50):
    X, y = [], []
    scaler = StandardScaler()
    
    print("Files ko read aur preprocess kiya ja raha hai...")
    for file_name in os.listdir(data_dir):
        if not file_name.endswith('.txt'):
            continue
            
        file_path = os.path.join(data_dir, file_name)
        data = np.loadtxt(file_path)
        sensor_data = data[:, 2:18] # 16 sensor columns
        
        if len(sensor_data) < window_size:
            continue
            
        sensor_data = scaler.fit_transform(sensor_data)
        label = 1 if "GaPt" in file_name else 0
        
        for i in range(0, len(sensor_data) - window_size, step_size):
            window = sensor_data[i : i + window_size]
            X.append(window)
            y.append([label])
            
    return np.array(X), np.array(y)

# 1. Data load karna
data_folder = "gait_dataset"
X_real, y_real = load_real_data(data_folder)

# Tensors me badalna
X_tensor = torch.tensor(X_real, dtype=torch.float32)
y_tensor = torch.tensor(y_real, dtype=torch.float32)
dataset = TensorDataset(X_tensor, y_tensor)

# 2. Train-Validation Split (80% Train, 20% Val) -> Overfitting check karne ke liye
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# 3. Model aur Optimizer setup (Weight Decay joda gaya hai overfitting rokne ke liye)
model = ParkinsonGaitLSTM()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)

# Early Stopping ke liye variables
best_val_loss = float('inf')
patience = 3  # Agar 3 epoch tak val_loss nahi sudhra, toh ruk jao
patience_counter = 0

print("\n--- Best Fit Model Training Shuru (With Overfitting Checks) ---")

for epoch in range(15):
    # --- TRAINING PHASE ---
    model.train()
    train_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        
    avg_train_loss = train_loss / len(train_loader)
    
    # --- VALIDATION PHASE ---
    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
            
            # Accuracy calculate karna
            predictions = (outputs >= 0.5).float()
            correct += (predictions == labels).sum().item()
            total += labels.size(0)
            
    avg_val_loss = val_loss / len(val_loader)
    val_accuracy = (correct / total) * 100
    
    print(f"Epoch {epoch+1:02d} -> Train Loss: {avg_train_loss:.4f} | Val Loss: {avg_val_loss:.4f} | Val Accuracy: {val_accuracy:.2f}%")
    
    # Early Stopping & Best Model Saving Logic
    if avg_val_loss < best_val_loss:
        best_val_loss = avg_val_loss
        torch.save(model.state_dict(), "parkinson_gait_best_model.pth")
        patience_counter = 0  # Reset karein kyunki sudhaar hua hai
    else:
        patience_counter += 1
        
    if patience_counter >= patience:
        print(f"\n[Early Stopping] Overfitting rokne ke liye training ko yahin roka ja raha hai.")
        break

print("\nSabse best model 'parkinson_gait_best_model.pth' naam se safe save kar diya gaya hai.")