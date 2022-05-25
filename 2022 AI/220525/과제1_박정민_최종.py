import os
import json
import cv2
# 사진 정보가 들어 있는 json 파일
json_path = "./dataset/anno/raccoon_annotations.coco.json"


def padding(img, set_size):
    h, w, c = img.shape
    if max(h, w) > set_size:
        return img

    n_w = set_size - w
    n_h = set_size - h
    top, bottom = n_h / 2, n_h - (n_h / 2)
    left, right = n_w / 2, n_w - (n_w / 2)
    new_img = cv2.copyMakeBorder(img, int(top), int(bottom), int(left), int(right), cv2.BORDER_CONSTANT,
                                 value=[0, 0, 0])
    return new_img

with open(json_path, "r") as f:
    coco_info = json.load(f)

assert len(coco_info) > 0, "파일 읽기 실패"

# 카테고리 정보 수집
categories = dict()
for category in coco_info['categories']:
    categories[category["id"]] = category["name"]
    # print(category)
# print("categories info >> ", categories)

# annotaiton 정보
ann_info = dict()
for annotation in coco_info['annotations']:
    # print("annotation >> ", annotation)
    image_id = annotation["image_id"]
    bbox = annotation["bbox"]
    category_id = annotation["category_id"]
    #print(annotation)

    if image_id not in ann_info:
        ann_info[image_id] = {
            "boxes": [bbox], "categories": [category_id]
        }

    else:
        ann_info[image_id]["boxes"].append(bbox)
        ann_info[image_id]["categories"].append(categories[category_id])


for image_info in coco_info['images']:
    filename = image_info["file_name"]
    height = image_info["height"]
    width = image_info["width"]
    img_id = image_info["id"]

    file_path = os.path.join("./dataset/data", filename)
    img = cv2.imread(file_path)

    try:
        annotation = ann_info[img_id]
    except KeyError:
        continue

    for bbox, category in zip(annotation["boxes"], annotation["categories"]):
        x1, y1, w, h = bbox

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2

        org_img = img.copy()

        # print(crop_img.shape)
        data_list = os.listdir('./dataset/data')
        for i in range(len(data_list)):
            crop_img = org_img[int(x1):int(x1 + w), int(y1): int(y1 + h)]
            if max(w,h,x1,y1) >= 255:
                down_size = 0.6
                img = cv2.resize(crop_img, None, fx=down_size, fy=down_size, interpolation=cv2.INTER_LINEAR)
                padding_img = padding(img, 255)
            else:
                img = crop_img
                padding_img = padding(img, 255)
        # print(padding_img.shape)

        save_root = ('./new_img')
        os.makedirs(save_root,exist_ok=True)
        cv2.imwrite(os.path.join(save_root,filename),padding_img)
