import os
import json
import cv2
import numpy as np
import pandas as pd

json_path="./dataset/anno/raccoon_annotations.coco.json"

with open(json_path,"r") as f:
    coco_info=json.load(f)

assert len(coco_info)>0,"파일 읽기 실패"
anno_info=dict()
for annotation in coco_info['annotations']:

    image_id =annotation["image_id"]
    bbox=annotation["bbox"]

    if image_id not in anno_info:
        anno_info[image_id] ={
            "boxes":[bbox]
        }
    else :
        anno_info[image_id]["boxes"].append(bbox)

data={'file_name':[],'box_x':[],'box_y':[],'box_w':[],'box_h':[]}
for image_info in coco_info['images']:
    filename=image_info["file_name"]
    img_id=image_info["id"]
    try:
        annotation = anno_info[img_id]
        print(annotation)
    except KeyError:
        continue

    for bbox in annotation["boxes"]:
        x1, y1, w, h = bbox
        data['file_name'].append(filename)
        data['box_x'].append(x1)
        data['box_y'].append(y1)
        data['box_w'].append(w)
        data['box_h'].append(h)


data=pd.DataFrame(data)
data.to_csv('./img_info.csv',index=False)