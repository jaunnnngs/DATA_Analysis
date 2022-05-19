import xml.etree.ElementTree as ET
import cv2
import os
import numpy as np

image_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220517/automotive_engine/image'
xml_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220517/automotive_engine/xml'

for filename in os.listdir(image_root):
    image_path = os.path.join(image_root, filename)
    image = cv2.imread(image_path)

    filename_xml = filename.split('.')[0] + '.xml'
    xml_path = os.path.join(xml_root, filename_xml)

    annotation = ET.parse(xml_path)
    object_nodes = annotation.findall('object')
    print(object_nodes)
    exit()

    for object_node in object_nodes:
        bnd_node = object_node.find('bnd_box')
        xmin = int(bnd_node.find('xmin').text)
        xmax = int(bnd_node.find('xmax').text)
        ymin = int(bnd_node.find('ymin').text)
        ymax = int(bnd_node.find('ymax').text)

        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255,255,0), 3)

    cv2.imshow('visual', image)
    if cv2.waitKey(0) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        exit()

