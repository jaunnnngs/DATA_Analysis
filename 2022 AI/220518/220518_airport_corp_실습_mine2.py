import json
import os
import cv2


def main():
    # json 파일 읽어서 bbox 정보 가져와서 이미지 crop
    image_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/18_airport/image'
    json_path = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/18_airport/annotation.json'
    save_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/18_airport/cropped'
    labels = ['knife', 'gun']

    for label in labels:
        save_forder = os.path.join(save_root, label)
        os.makedirs(save_forder, exist_ok=True)

    with open(json_path, 'r') as j:
        json_data = json.load(j)

    for filename in os.listdir(image_root):
        file_path = os.path.join(image_root, filename)
        image = cv2.imread(file_path)

        json_image = json_data[filename]
        annos = json_image['anno']

        for idx, anno in enumerate(annos):
            lab = anno['label'].lower()
            xmin, ymin, xmax, ymax = anno['bbox']

            image_crop = image[ymin:ymax, xmin:xmax]
            file = filename[:-4]
            filename_new = f'{file}_{idx}.png'

            save_path = os.path.join(save_root, lab, filename_new)
            cv2.imwrite(save_path, image_crop)
            # cv2.imshow('crop', image_crop)
            # if cv2.waitKey(0) & 0xff == ord('q'):
    exit()


if __name__ == '__main__':
    main()
