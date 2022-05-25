# 크롤링한 이미지 저장
#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# import pandas as pd
# import os
#
# from urllib.request import (urlopen, urlparse, urlretrieve)
#
#
# # 구글 이미지 URL
# chrome_path = "./chromedriver"
# # window
# # chrome_path = "./chromedriver.exe"
# base_url = "https://www.google.co.kr/imghp"
#
# # 구글 검색 옵션
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("lang=ko_KR") # 한국어
# chrome_options.add_argument("window-size=1920x1080")
#
# def selenium_scroll_option() :
#     SCROLL_PAUSE_SEC = 1
#
#     # 스크롤 높이 가져옴
#     last_height = driver.execute_script(
#         "return document.body.scrollHeight")
#
#     while True :
#         # 끝까지 스크롤 다운
#         driver.execute_script(
#             "window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(SCROLL_PAUSE_SEC)
#         # 스크롤 다운 후 스크롤 높이 다시 가져옴
#         new_height = driver.execute_script(
#             "return document.body.scrollHeight")
#         if new_height == last_height :
#             break
#         last_height = new_height
#
# a = "상어"
# image_name = "shark"
# driver = webdriver.Chrome(chrome_path)
# driver.get("http://www.google.co.kr/imghp?hl=ko")
# browser = driver.find_element_by_name('q')
# browser.send_keys(a)
# browser.send_keys(Keys.RETURN)
#
# # //*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input
# selenium_scroll_option()# 스크롤 하여 이미지 확보
# driver.find_element_by_xpath(
#     '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
# selenium_scroll_option()
#
# # 이미지 저장 src 요소를 리스트업 해서 이미지 url 저장
# image = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# # 클래스 네임에서 공백은 . 을 찍어줌
#
# print(image)
# image_url = []
# for i in image:
#     if i.get_attribute("src") != None :
#         image_url.append(i.get_attribute("src"))
#     else :
#         image_url.append(i.get_attribute("data-src"))
#
# # 전체 이미지 개수
# print(f"전체 다운로드한 이미지 개수 : {len(image_url)}")
# image_url = pd.DataFrame(image_url)[0].unique()
#
# # 해당하는 파일에 이미지 다운로드
# os.makedirs("./shark", exist_ok=True)
# shark = "./shark/"
# if image_name == 'shark' :
#     for t, url in enumerate(image_url, 0) :
#         urlretrieve(url, shark + image_name + "_" + str(t) + ".png")
#
#     driver.close()
#
# print("완료")
#
#

import time

# 자주 쓰는 라이브러리
import torch
import torchvision
import os
import cv2
import numpy as np
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
from matplotlib import pyplot as plt
import albumentations
from albumentations.pytorch import ToTensorV2


class AlbumentationsDataset(Dataset):
    def __init__(self, file_path, labels, transform=None):
        self.file_path = file_path
        self.labels = labels
        self.transform = transform

    def __getitem__(self, index):
        label = self.labels[index]
        file_path = self.file_path[index]

        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        start_t = time.time()
        if self.transform:
            augmented = self.transform(image=image)
            image = augmented['image']

        total_time = (time.time() - start_t)

        return image, label, total_time

    def __len__(self):
        return len(self.file_path)


albumentations_transform = albumentations.Compose([
    albumentations.Resize(256, 256),
    albumentations.RandomCrop(224, 224),
    albumentations.HorizontalFlip(),
    transforms.ToTensor(),
])


image_path = os.listdir('./shark')
albumentations_dataset = AlbumentationsDataset(
    file_path=image_path,
    labels=1,
    transform=albumentations_transform
)
total_time =0
os.makedirs('./shark_transform', exist_ok=True)
for i in range(len(image_path)):
    sample, _, transform_time = albumentations_dataset[i]
    new_image = transforms.ToPILImage()(sample)
    new_image.save(os.path.join('./shark_transform)',f'shark_{i}.png'))
    total_time += transform_time