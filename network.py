import torch.nn as nn
from torch.utils.data import Dataset , DataLoader
import torch



class Network(nn.Module):
  def __init__(self,in_channel):
    super().__init__()

    self.convo = nn.Sequential(
      nn.Conv2d(in_channel,32,3,padding = 'same'),
      nn.ReLU(),
      nn.BatchNorm2d(32),
      nn.MaxPool2d(2,2),       #32,14,14

      nn.Conv2d(32,64,3,padding = 'same'),
      nn.ReLU(),
      nn.BatchNorm2d(64),
      nn.MaxPool2d(2,2)     #64,7,7
    )

    self.linear = nn.Sequential(
        nn.Flatten(),
        nn.Linear(64*7*7,100),
        nn.ReLU(),
        nn.Dropout(p = 0.4),

        nn.Linear(100,75),
        nn.ReLU(),
        nn.Dropout(p = 0.4),

        nn.Linear(75,10)
    )

  def forward(self,X):
    X = self.convo(X)
    X = self.linear(X)
    return X



class Loader(Dataset):
  def __init__(self,x,y):
    self.x = torch.tensor(x,dtype = torch.float32).reshape(-1,1,28,28)
    self.y = torch.tensor(y,dtype = torch.long)
  def __len__(self):
    return len(self.x)
  def __getitem__(self,item):
    return self.x[item],self.y[item]
