import os
import json
import cv2

json_path = "./json_data/instances_default.json"

with open(json_path, "r") as f:
    coco_info = json.load(f)

assert len(coco_info) > 0, "파일 읽기 실패"

# 카테고리 정보 수집
categories = dict()
for category in coco_info['categories']:
    categories[category["id"]] = category["name"]

# print("categories info >> ", categories)

# annotaiton 정보
ann_info = dict()
for annotation in coco_info['annotations']:
    print("annotation >> ", annotation)
