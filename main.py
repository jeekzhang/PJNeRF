import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from torch.autograd import Variable
from torchvision.datasets import ImageFolder


def generate_loader():
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.RandomRotation(10),
        transforms.ToTensor(),  # 将图片转换为Tensor,归一化至[0,1]
    ])
    train_set = ImageFolder('./data/train', transform=transform)
    test_set = ImageFolder('./data/test', transform=transform)

    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)  # 转变为dataloader形式，方便载入模型
    test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader


class CNN_Net(nn.Module):  # 构建卷积神经网络模型
    def __init__(self):
        super(CNN_Net, self).__init__()
        self.conv1 = nn.Sequential(nn.Conv2d(1, 10, 5), nn.ReLU(), nn.MaxPool2d(2))  # 卷积
        self.conv2 = nn.Sequential(nn.Conv2d(10, 20, 5), nn.ReLU(), nn.MaxPool2d(2))  # 卷积
        self.conv3 = nn.Sequential(nn.Conv2d(20, 40, 3), nn.ReLU(), nn.MaxPool2d(2))  # 卷积
        self.fc = nn.Sequential(nn.Linear(40, 128), nn.ReLU(), nn.Linear(128, 2))  # 全连接层

    def forward(self, x):  # 重写基础函数forward
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        res = x.view(x.size(0), -1)
        out = self.fc(res)
        return nn.functional.log_softmax(out, dim=1)


def Train():  # 训练
    for batch_idx, (data, label) in enumerate(train_loader):
        output = model(data)
        loss = nn.functional.nll_loss(output, label)
        optimizer.zero_grad()  # 优化器作用
        loss.backward()  # 反向传播
        optimizer.step()


def Test(epoch):  # 测试
    cnt = 0
    for batch_idx, (data, target) in enumerate(test_loader):
        with torch.no_grad():
            data = Variable(data)
            target = Variable(target)
        output = model(data)
        prediction = output.data.max(1, keepdim=True)[1]
        cnt += prediction.eq(target.data.view_as(prediction)).cpu().sum()
    total = batch_idx * batch_size + len(data)
    acc = 100. * cnt / total
    print('Epoch: {} Accuracy: {}/{} ({:.1f}%) '.format(epoch, cnt, total, acc))  # 输出测试精度


if __name__ == "__main__":
    batch_size = 8  # 批处理记录数量
    epoch_num = 60  # 训练次数(轮数)

    train_loader, test_loader = generate_loader()  # 载入数据加载器

    model = CNN_Net()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5, weight_decay=1e-5)  # 定义优化器
    for epoch in range(epoch_num):  # 训练，每训练一轮后测试
        Train()
        Test(epoch)
