import random
import numpy as np
import os
import cv2
import glob
from PIL import Image
import PIL.ImageOps
# PIL -> pip install Pillow
# cv2 -> pip install opencv-python

# 새로만들 이미지 갯수를 정합니다.
num_augmented_images = 50

# 원본 사진 폴더 경로
file_path = "./data"

# 위의 폴더 내부에 있는 이미지 이름의 배열이 저장 되는 형태
file_name = os.listdir(file_path)
print(file_name)

# file_name 길이를 가져오겠습니다.
total_origin_image_num = len(file_name)
print("total image number >> ", total_origin_image_num)
# total image number >>  3

augment_cnt = 1

for i in range(1, num_augmented_images):
    # image = [image01 , image02 , image03]
    change_picture_index = random.randint(0, total_origin_image_num-1)
    # print(change_picture_index)
    file_names = file_name[change_picture_index]
    # print(file_names)

    os.makedirs("./custom_data", exist_ok=True)
    origin_image_path = "./data/" + file_names
    # print(origin_image_path)

    image = Image.open(origin_image_path)

    # 랜덤 값이 1~4 사이으 값이 나오도록 1 2 3
    random_augment = random.randrange(1, 4)
    print(random_augment)

    if (random_augment == 1):
        # 이미지 좌우 반전
        inverted_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        inverted_image.save("./custom_data/" + "inverted_" +
                            str(augment_cnt) + ".png")
        pass
    elif (random_augment == 2):
        rotated_image = image.rotate(random.randrange(-20, 20))
        rotated_image.save("./custom_data/" + "rotated_" +
                           str(augment_cnt) + ".png")
        # 이미지 기울기
    elif (random_augment == 3):
        pass
        resize_image = image.resize(size=(224, 224))
        resize_image.save("./custom_data/" + "resize_" +
                          str(augment_cnt) + ".png")
        # 이미지 리사이즈

    augment_cnt += 1
