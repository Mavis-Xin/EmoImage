import pickle

with open('./dataset_balance/scene_norepeat.pkl', 'rb') as file:
    data = pickle.load(file)
    # 在此处可以对读取到的数据进行处理和操作
    print(len(data))