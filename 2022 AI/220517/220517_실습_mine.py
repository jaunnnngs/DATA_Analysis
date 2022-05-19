import os
import json
import cv2
import numpy as np

image_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220517/automotive_engine/image'
json_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220517/automotive_engine/json'

print(os.listdir(image_root))

for filename in os.listdir(image_root):
    image_path = os.path.join(image_root,filename)

    filename_json = filename.split('.')[0] + '.json'
    json_path = os.path.join(json_root,filename_json)

    with open(json_path, 'r') as j:
        json_data = json.load(j)

    annos = json_data['shapes']
    for anno in annos:
        points = anno['points']
        points = np.array(points,np.int)
        image = cv2.polylines(image,[points],True, (255,255,0), 3)

    cv2.imshow('visual', image)
    if cv2.waitKey(0) & 0xFF ==ord('q'):
        cv2.destroyAllWindows()
        exit()
    #    print(points)
    #    exit()