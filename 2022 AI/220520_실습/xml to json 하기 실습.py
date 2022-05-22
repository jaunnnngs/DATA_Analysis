from xml.etree import ElementTree as ET
import json
import os


def main():
    xml_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/' \
               'DATA_Analysis/2022 AI/220520_실습/실습1_파일읽기'
    xml_paths = get_xml_paths(xml_root)

    json_path = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/' \
                'DATA_Analysis/2022 AI/220520_실습/실습1_파일읽기'

    json_data = []
    for xml_path in xml_paths:
        root = ET.parse(xml_path)
        images = root.findall('image')
        for image in images:
            name = image.attrib['name']
            width = int(image.attrib['width'])
            height = int(image.attrib['height'])

            json_annos = {}
            anoos = image.findall('polyline')
            for anno in anoos:
                label = anno.attrib['label']
                points = anno.attrib['points']

                json_points = []
                for xy in points.split(';'):
                    x, y = xy.split(',')
                    x = float(x)
                    y = float(y)

                    json_points.append(x)
                    json_points.append(y)
                json_annos[label] = json_points

            json_image = {
                'filename': name,
                'width': width,
                'height': height,
                'annotations': json_annos
            }
            json_data.append(json_image)

    with open(json_path, 'w') as j:
        json.dump(json_data, j, indent='/t')  # 줄띄우기 용


def get_xml_paths(root):
    paths = []
    for (path, dir, files) in os.walk(root):
        for file in files:
            ext = file.split('.')[-1]
            if ext in ['xml']:
                file_path = os.path.join(path, file)
                paths.append(file_path)
    return paths


if __name__ == '__main__':
    main()
