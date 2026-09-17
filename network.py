import torch.nn as nn
from torch.utils.data import Dataset , DataLoader


class Network(nn.Module):
  def __init__(self,size):
    super().__init__()
    self.linear = nn.Sequential(
        nn.Linear(size,100),
        nn.ReLU(),
        nn.Linear(100,75),
        nn.ReLU(),
        nn.Linear(75,10),
    )

  def forward(self,X):
    out = self.linear(X)
    return out

class Loader(Dataset):
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __len__(self):
    return self.x.size(0)
  def __getitem__(self,item):
    return self.x[item],self.y[item]

