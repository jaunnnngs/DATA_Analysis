import json
import os
import cv2
import shutil
from tqdm import tqdm


def main():
    # json 파일 읽어서 bbox 로 가져와서 이미지 crop
    image_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/mnist'
    save_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/mnist'
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    image_paths = {}

    for (path, dir, files) in os.walk(image_root):
        for file in files:
            image_path = os.path.join(path,file)
            label = file.split('.')[0][-1]
            if label not in image_path_keys():
                image_paths[label] = []
            image_paths[label].append(image_path)

    for label in image_paths.keys():
        path = os.path.join(save_root,label)
        os.makedirs(save_forder, exist_ok=True)

    for label in image_paths.keys():
        for path

    exit()


if __name__ == '__main__':
    main()
