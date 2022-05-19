import json
import cv2
import os

mask_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220516/steel_masking/mask'

json_data = {}

for filename in os.listdir(mask_root):
    mask_path = os.path.join(mask_root, filename)
    mask = cv2.imread(mask_path)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # json annotation file 파일
    #{
    #    filename: {
    #        'filename': 이미지 파일 이름,
    #        'width':    이미지 가로 길이(int),
    #        'height': 이미지 세로 길이(int),
    #        'anno': [
    #            [xmin, ymin, xmax, ymax]
    #            , ...
    #        ]
    #    },...
    #}

    height, width = mask.shape
    annos =[]
    coutours, h = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for coutour in coutours:
        xs, ys = [], []

        for coord in coutour:
            x, y = coord[0]
            xs.append(x)
            ys.append(y)
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        anno = [int(xmin), int(ymin), int(xmax), int(ymax)]
        annos.append(anno)
    json_image ={
        'filename': filename,
        'width': width,
        'height': height,
        'anno': annos
    }
    json_data[filename] = json_image

print(json_data)

save_path='/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220516/steel_masking/annotation.json'
with open(save_path, 'w') as j:
    json.dump(json_data, j, indent='/t')