#sort_
import shutil

import pandas as pd
import os
image_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/3주차 수업 자료/pocketmon/image'
csv_path = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/3주차 수업 자료/pocketmon/pokemon.csv'
print(os.path.isdir(image_root))

save_root = '/Users/jaunnnngspc/Desktop/Jaunnnng문서/DATA_Analysis/2022 AI School/3주차 수업 자료/pocketmon/sorted'
os.makedirs(save_root,exist_ok=True)

pocketmon_df = pd.read_csv(csv_path)
type_list = pocketmon_df['Type1'].unique()

for t in type_list:
    dir_path = os.path.join(save_root, t)
    os.makedirs(dir_path,exist_ok=True)

    #이미지 폴더 안에서 포켓몬 파일/이름 읽기
filenames = os.listdir(image_root)

for filename in filenames:
    # 읽은 포켓몬 이름을, csv 파일이랑 매장에서 type1 값 찾기
    #print(filename[:-4])
    name = filename.split('.')[0]
    #print(filename.split('.'))
    #exit()
    type_ = pocketmon_df[pocketmon_df['Name'] == name]['Type1'].value[0]
    #print(name, type_)
    #i +=1
    #if i>5:
    #    exit()

    # 만들어 놓은 하위 폴더에 이미지 파일 옮기기
    current_path = os.path.join(image_root,filename)
    move_path = os.path.join(save_root, type_, filename)
    print(move_path)
    #exit()
    #print(current_path)
    #shutil.move(현재파일 위치, 옮길 파일 위치)
    shutil.move(current_path, move_path)

