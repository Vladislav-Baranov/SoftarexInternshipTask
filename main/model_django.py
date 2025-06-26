import torch
import torch.nn as nn
import torchvision.transforms.v2 as tfs
from PIL import Image
import torch.nn.functional as F
import os
from pathlib import Path


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'model_SMOTE9.tar')
res_context = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}


class MyModel(nn.Module):
    def __init__(self, num_classes=7):
        super(MyModel, self).__init__()
        
        # Block 1
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.bn1 = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.bn2 = nn.BatchNorm2d(64)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.dropout1 = nn.Dropout(0.25)
        
        # Block 2
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3)
        self.bn3 = nn.BatchNorm2d(128)
        self.conv4 = nn.Conv2d(128, 128, kernel_size=3)
        self.bn4 = nn.BatchNorm2d(128)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.dropout2 = nn.Dropout(0.25)
        
        # Block 3
        self.conv5 = nn.Conv2d(128, 256, kernel_size=3)
        self.bn5 = nn.BatchNorm2d(256)
        self.conv6 = nn.Conv2d(256, 256, kernel_size=3)
        self.bn6 = nn.BatchNorm2d(256)
        self.pool3 = nn.MaxPool2d(2, 2)
        self.dropout3 = nn.Dropout(0.25)
        
        # Classifier
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(256 * 2 * 2, 256)  
        self.bn7 = nn.BatchNorm1d(256)
        self.dropout4 = nn.Dropout(0.5)
        self.fc2 = nn.Linear(256, num_classes)

    def forward(self, x):
        # Block 1
        x = F.relu(self.conv1(x))
        x = self.bn1(x)
        x = F.relu(self.conv2(x))
        x = self.bn2(x)
        x = self.pool1(x)
        x = self.dropout1(x)
        
        # Block 2
        x = F.relu(self.conv3(x))
        x = self.bn3(x)
        x = F.relu(self.conv4(x))
        x = self.bn4(x)
        x = self.pool2(x)
        x = self.dropout2(x)
        
        # Block 3
        x = F.relu(self.conv5(x))
        x = self.bn5(x)
        x = F.relu(self.conv6(x))
        x = self.bn6(x)
        x = self.pool3(x)
        x = self.dropout3(x)
        
        # Classifier
        x = self.flatten(x)
        x = F.relu(self.fc1(x))
        x = self.bn7(x)
        x = self.dropout4(x)
        x = self.fc2(x)
        
        return x 


transform = tfs.Compose([
    tfs.Resize((48, 48)),
    tfs.ToImage(),
    tfs.Grayscale(),
    tfs.ToDtype(torch.float32, scale=True),                            
])


model = MyModel()
st = torch.load(file_path, weights_only=False, map_location=torch.device('cpu'))
model.load_state_dict(st)
model.eval()


def calculate(path):
    img = transform(Image.open(path[1:])).unsqueeze_(0)
    predict = torch.argmax(model(img), dim=1).item()
    return res_context[predict]


