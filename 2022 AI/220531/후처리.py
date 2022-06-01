# 후처리 시작.
from h11 import Data
import cv2
import torch
import glob
from PIL import Image
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import os


class MyCustomDatasetImage(Dataset):
    def __init__(self, path):
        # 정의
        self.all_data = sorted(glob.glob(os.path.join(path, '*', '*.png')))

    def __getitem__(self, index):
        data_path = self.all_data[index]
        image = Image.open(data_path)

        data_split = data_path.split('/')
        data_labels = data_split[1]
        print(data_labels)
        # windows
        # data_split = data_path.split('\\')
        labels = 0
        if data_labels == '망고':
            labels = 0
        elif data_labels == '용과':
            labels = 1
        elif data_labels == '리치':
            labels = 2
        elif data_labels == '두리안':
            labels = 3

        print(data_labels, labels)
        # cv2 PIL 이용해서 이미지 변경 하면됨.
        return image, data_path, labels
        # 정의 작성된 내용을 구현

    def __len__(self):
        # 전체 길이를 반환 -> 리스트 [] len()
        return len(self.all_data)

save_list = ['mango', 'Dragon_fruit', 'lychee', 'durian']
# 2가지 구성 필요 -> dataset dataloader
for i in range(len(save_list)):
    dataset = MyCustomDatasetImage(path=f"{save_list[i]}")
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)

    for path, label in dataloader:
        print(path, label)

