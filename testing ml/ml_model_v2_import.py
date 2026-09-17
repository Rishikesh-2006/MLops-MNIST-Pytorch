import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets
from sklearn.model_selection import train_test_split
import pickle
import network

data = datasets.MNIST('./Data',train = True , download = True)

X = data.data
y = data.targets

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = 0.2,shuffle = True)
X_train =  X_train.reshape(-1,28*28)

X_train = X_train.float()/255

Y_train = y_train.long()

x_test = X_test.float()
x_test = x_test.reshape(-1,28*28)/255

y_test = y_test.long()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

device

Train_loader = network.Loader(X_train,y_train)
Train_loader = network.DataLoader(Train_loader,batch_size = 32,shuffle = True)


model = network.Network(28*28).to(device)
optimizer = optim.Adam(model.parameters(),lr = 0.001)
criteria = nn.CrossEntropyLoss()

epoch = 20
for e in range(epoch):

  total_loss = 0

  for X,y in Train_loader:

    X = X.to(device)
    y = y.to(device)

    y_pred = model(X)

    loss = criteria(y_pred,y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    total_loss += loss.item()
  print(f"epoch = {e+1} , loss = {total_loss/len(Train_loader)}")


with torch.no_grad():
  # 1. Get model predictions for all test items
  y_out = model(x_test)

  # 2. Get the index of the max value across the 10 outputs (dim=1)
  predictions = torch.argmax(y_out, dim=1)

  # 3. Count how many predictions match the true values
  count = (predictions == y_test).sum().item()

print("correct --> ", count, " accuracy -->", (count / len(y_test)) * 100, "%")

print(torch.argmax(y_out,dim=1))
print(y_test)


#pickle.dump(model,open('modelv2.pkl','wb'))