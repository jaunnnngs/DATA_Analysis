import random
import numpy as np
import os
import cv2
import glob
from PIL import Image , ImageFilter, ImageEnhance
import PIL.ImageOps


# 새로 만들 이미지 갯수 정하기
num_augmented_images = 50

# 원본 사진 폴더 경로
file_path = './data'

# file_path 폴더 내부에 있는 이미지 이름을 저장
file_name = os.listdir(file_path)
print(file_name)

# file_name 길이 체크
total_origin_image_num = len(file_name)
print('total image number>>', total_origin_image_num)
# total image number >> 3

augment_cnt = 1

for i in range(1, num_augmented_images):
    # image = [image01, image02, image03]
    change_picture_index = random.randint(0, total_origin_image_num-1)
    #print(change_picture_index)
    file_names = file_name[change_picture_index]
    #print(file_names)

    os.makedirs('./custom_data', exist_ok=True)
    orgin_image_path = './data/' + file_names

    image = Image.open(orgin_image_path)
    #print(image)

    # 랜덤값이 1~7 나오도록
    random_augment = random.randrange(1,7)
    print(random_augment)

    if (random_augment == 1):
        # 이미지 좌우 반전
        inverted_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        inverted_image.save("./custom_data/" + "inverted_" +
                            str(augment_cnt) + ".png")
    elif (random_augment == 2):
        # 이미지 기울기
        rotated_image = image.rotate(random.randrange(-20, 20))
        rotated_image.save("./custom_data/" + "rotated_" +
                           str(augment_cnt) + ".png")
    elif (random_augment == 3):
        # 이미지 리사이즈
        resize_image = image.resize(size=(224, 224))
        resize_image.save("./custom_data/" + "resize_" +
                          str(augment_cnt) + ".png")

    elif (random_augment == 4):
        # 이미지 업다운 반전
        inverted_image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
        inverted_image2.save("./custom_data/" + "updown_" +
                           str(augment_cnt) + ".png")

    elif (random_augment == 5):
        # 이미지 밝기 조정
        bright_image = ImageEnhance.Color(image).enhance(2)
        bright_image.save("./custom_data/" + "bright_" +
                          str(augment_cnt) + ".png")

    elif (random_augment == 6):
        # 이미지 블러처리
        filter_image = image.filter(ImageFilter.BLUR)
        filter_image.save("./custom_data/" + "filter_" +
                          str(augment_cnt) + ".png")

    augment_cnt += 1