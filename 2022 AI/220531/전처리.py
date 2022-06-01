
# 이미지 패딩 추가 및 리사이즈
import os
from PIL import Image

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        # paste 이미지 붙이기(추가할 이미지 , 붙일 위치(가로, 세로))
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        # 새로운 이미지 생성
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

item_list = ['망고', '용과', '리치', '두리안']
save_list = ['mango', 'Dragon_fruit', 'lychee', 'durian']
print(len(item_list))
for i in range(len(item_list)):
    im_path = f'fruit{i}/'
    save_path = f'{save_list[i]}/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    im_list = os.listdir(im_path) #원본 이미지 경로의 모든 이미지 list 지정
    print(len(im_list))

    for name in im_list:
        im = Image.open(im_path+name)
        new_im = expand2square(im, (0, 0, 0)).resize((225, 225))
        new_im.save(save_path+name, quality=100)
    print('종료')

# 전처리 완료.
