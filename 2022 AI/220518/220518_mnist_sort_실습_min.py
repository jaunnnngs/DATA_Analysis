import os
import shutil
from tqdm import tqdm

def main():
    image_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/mnist'
    save_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/220518/label'
    image_paths = {}
    for (path, dir, files) in os.walk(image_root):
        for file in files:
            image_path = os.path.join(path, file)
            label = file.split('.')[0][-1]
            if label not in image_paths.keys():
                image_paths[label] = []
            image_paths[label].append(image_path)

    for label in image_paths.keys():
        path = os.path.join(save_root, label)
        os.makedirs(path, exist_ok=True)

    for label in image_paths.keys():
        for path in tqdm(image_paths[label], desc=f'{label}: '):
            filename = os.path.basename(path)
            save_path = os.path.join(save_root, label, filename)
            shutil.copy(path, save_path)

if __name__ == '__main__':
    main()