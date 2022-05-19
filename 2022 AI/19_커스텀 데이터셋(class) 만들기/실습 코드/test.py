import torch
from torchvision import transforms
from torch.utils.data import DataLoader
import cv2
import os
import shutil

from cnn_model import ConvNet
from custom_dataset import CustomDataset
# from custom_dataset import CLASS_NAME


def main():
    dataset = CustomDataset(
        image_root='/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/19_커스텀 데이터셋(class) 만들기/mnist_dataset/train',
        transform=transforms.ToTensor())
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
    for item in dataloader:
        print(item['label'])
        print(item['image'])
        exit()

if __name__ == '__main__':
    main()