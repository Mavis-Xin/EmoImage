import json
import os
import pickle
from tqdm import tqdm
import shutil

property = "scene"  # "object"
raw_dataset_path = '/Users/magic_minmin/202406/data/EmoSet-118K-box/raw'
annotation_path = os.path.join(raw_dataset_path, 'annotation')
image_path = os.path.join(raw_dataset_path, 'image')
re_org_path = os.path.join('/Users/magic_minmin/202406/data/EmoSet-118K-box', property)


'''
property_map = {}

for root, dirs, files in tqdm(os.walk(annotation_path)):
    print('root', root)
    print(dirs)
    print('file', len(files))

    for file in files:
        if file == '.DS_Store':
            continue
        file_path = os.path.join(root, file)
        # print(file_path)
        with open(file_path, 'r') as file:
            anno_data = json.load(file)
        
        if 'scene' in anno_data:
            s_scene = anno_data['scene']
            # print('sssss', s_scene)
            image_file = anno_data['image_id']
            if s_scene not in property_map:
                property_map[s_scene] = [image_file]
            else:
                property_map[s_scene].append(image_file)
    
    # print('ssssss')
print(property_map)

path_w = f'./dataset_balance/mine/{property}_map.json'
with open(path_w, 'w') as file:
    file.write(json.dumps(property_map, ensure_ascii=False))

'''

with open(f'./dataset_balance/mine/{property}_map.json', 'r') as file:
    property_map = json.load(file)

for key, value in property_map .items():
    pro_key = f'({len(value)}) {key}'
    new_folder = os.path.join(re_org_path, pro_key)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    for img in tqdm(value):
        emotion = img.split('_')[0]
        img_path = os.path.join(image_path, emotion, f'{img}.jpg')
        new_img_path = os.path.join(new_folder, f'{img}.jpg')
        # print(img, img_path, new_img_path)
        shutil.copy(img_path, new_img_path)
