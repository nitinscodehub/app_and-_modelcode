import torch
import torch.nn as nn

# नाम ध्यान से देखें: ParkinsonGaitLSTM
class ParkinsonGaitLSTM(nn.Module):
    def __init__(self, input_dim=16, hidden_dim1=128, hidden_dim2=64, num_classes=1):
        super(ParkinsonGaitLSTM, self).__init__()
        
        self.lstm1 = nn.LSTM(input_dim, hidden_dim1, batch_first=True)
        self.lstm2 = nn.LSTM(hidden_dim1, hidden_dim2, batch_first=True)
        self.dropout = nn.Dropout(0.3)
        self.fc = nn.Linear(hidden_dim2, num_classes)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        lstm_out1, _ = self.lstm1(x)
        lstm_out1 = self.dropout(lstm_out1)
        
        lstm_out2, (hidden, _) = self.lstm2(lstm_out1)
        last_time_step_output = hidden[-1] 
        
        out = self.fc(last_time_step_output)
        return self.sigmoid(out)