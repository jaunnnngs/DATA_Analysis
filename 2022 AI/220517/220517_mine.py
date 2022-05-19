import json

json_path = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220517/17_test/test.json'
with open(json_path, 'r') as j:

    json_data = json.load(j)

for filename in json_data.keys():
    for anno in json_data[filename]:
        label = anno['label']
        bbox = anno['points']
        exit()



import  xml.etree.ElementTree as ET

xml_path = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220517/17_test/test.xml'
annotation = ET.parse(xml_path)
size_node = annotation.find('size')
width = size_node.attrib['width']
height = size_node.attrib['height']
print(annotation)
print(width, height)

object_node = annotation.find('object')
name_node = object_node.find('name')
print(name_node.text)

bndbox_node = object_node.find('bndbox')
xmin = bndbox_node.find('xmin').text
ymin = bndbox_node.find('ymin').text
xmax = bndbox_node.find('xmax').text
ymax = bndbox_node.find('ymax').text
print(xmin,ymin,xmax,ymax)