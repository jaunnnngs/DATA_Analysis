import shutil
import os
import random


def main():
    image_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/18_airport/cropped'
    save_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/18_airport/dataset'

    image_paths = {}

    for (path, dir, files) in os.walk(image_root):
        for file in files:
            image_path = os.path.join(path, file)
            label = os.path.basename(path)
            print(image_path)
            if label not in image_paths.keys():
                image_paths[label] = []
            image_paths[label].append(image_path)

    use_type = ['train', 'test']
    for label in image_paths.keys():
        for use in use_type:
            path = os.path.join(save_root, use, label)
            os.makedirs(path, exist_ok=True)

    for label in image_paths.keys():
        path_list = image_paths[label]
        random.shuffle(path_list)

        idx_train = int(len(path_list) * 0.9)
        for path in path_list[:idx_train]:
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, 'train', label, filename)
            shutil.copy(path, save_path)

        for path in path_list[idx_train:]:
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, 'test', label, filename)
            shutil.copy(path, save_path)


if __name__ == '__main__':
    main()
