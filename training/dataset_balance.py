import json
import os
import random
import pickle

property = "scene"  # "object"
data_root = f"/Users/magic_minmin/202406/data/EmoSet-118K-box/{property}"
image_paths = []
for root, _, file_path in os.walk(data_root):
    for file in file_path:
        if file.endswith("jpg"):
            flag = False
            path = os.path.join(root, file)
            emotion = path.split('/')[-1].split('_')[0]
            number = path.split('/')[-1].split('.')[0].split('_')[1]
            attribute = path.split('/')[-2].split(')')[-1].lower().replace(' ', '')
            # print(path.split('/')) # ['', 'Users', 'magic_minmin', '202406', 'data', 'EmoSet-118K-box', 'scene', '(1) airfield', 'amusement_11538.jpg']
            # print(emotion, number, attribute)
            annotion_path = f'/Users/magic_minmin/202406/data/EmoSet-118K-box/raw/annotation/{emotion}/{emotion}_{number}.json'
            annotion = json.load(open(annotion_path, 'r'))
            if 'scene' in annotion:
                flag = True
                tmp = annotion['scene'].lower()
                # print(tmp, attribute)
                if tmp == attribute:
                    image_paths.append(path)
            if flag is False:
                try:
                    tmp = annotion['object'][0].lower().replace(' ', '_')
                    if tmp == attribute:
                        image_paths.append(path)
                except:
                    print("annotation is wrong")

# Calculate the number of samples for each emotion label
emotion_counts = {}
for path in image_paths:
    emotion = path.split('/')[-1].split('_')[0]
    # print(path, emotion)
    if emotion not in emotion_counts:
        emotion_counts[emotion] = []
    emotion_counts[emotion].append(path)
# print(emotion_counts)


# Record the maximum number of samples
max_num = max([len(v) for v in emotion_counts.values()])
print(max_num) 

# Generate a random index list for each emotion label
index_lists = {}
for emotion, paths in emotion_counts.items():
    random_indices = list(range(max_num))
    random.shuffle(random_indices)
    indices = [i % (len(paths)) for i in random_indices]
    # print(emotion, len(paths), len(indices)) # amusement 4143 7879
    # print(indices)
    index_lists[emotion] = indices

# Extract images based on index list
image_paths = []
for emo, path in emotion_counts.items():
    # print(emo,  max(index_lists[emo])) # amusement 4142
    list = index_lists[emo]
    for indice in list:
        image_paths.append(path[indice])

# 随机打乱图像列表
random.shuffle(image_paths)

with open(f'dataset_balance/mine/{property}_norepeat.pkl', 'wb') as f:
    pickle.dump(image_paths, f)
