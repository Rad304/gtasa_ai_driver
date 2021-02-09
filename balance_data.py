import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

# Balance_data
'''train_data = np.load('training_data_v2.npy', allow_pickle=True)
print(len(train_data))
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [0,1,0]:
        forwards.append([img, choice])
    elif choice == [1,0,0]:
        lefts.append([img, choice])
    elif choice == [0,0,1]:
        rights.append([img, choice])
    else:
        print('No matches!')

length = min(len(forwards), len(lefts), len(rights))
lefts = lefts[:length]
forwards = forwards[:length]
rights = rights[:length]

final_data = forwards + lefts + rights 

shuffle(final_data)
print(len(final_data))
np.save('training_data_v2_balanced.npy', final_data)''''

# data cleaning - conversion
'''
train_data = np.load('training_data_new.npy', allow_pickle=True)
print(len(train_data))
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

new_train_data = []

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1, 0, 0, 0]:
        new_train_data.append([img, [0, 1, 0]])
    elif choice == [0, 1, 0, 0]:
        new_train_data.append([img, [1, 0, 0]])
    elif choice == [0, 0, 0, 1]:
        new_train_data.append([img, [0, 0, 1]])

print(len(new_train_data))
df = pd.DataFrame(new_train_data)
print(df.head())
print(Counter(df[1].apply(str)))
np.save('training_data_v2.npy', new_train_data)'''

'''
lefts = []
rights = []
forwards = []
backwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0,0]:
        forwards.append([img, choice])
    elif choice == [0,1,0,0]:
        lefts.append([img, choice])
    elif choice == [0,0,1,0]:
        backwards.append([img, choice])
    elif choice == [0,0,0,1]:
        rights.append([img, choice])
    else:
        print('No matches!')

length = min(len(forwards), len(lefts), len(backwards), len(rights))
forwards = forwards[:length]
lefts = lefts[:length]
backwards = backwards[:length]
rights = rights[:length]

final_data = forwards + lefts + backwards + rights 

shuffle(final_data)
print(len(final_data))
np.save('training_data_balanced.npy', final_data)
'''
'''for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [0, 0, 0, 0]:
        data[1] = [1, 0, 0, 0]

np.save('training_data_new.npy', train_data)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))'''


'''for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1, 0, 0]:
        lefts.append([img, choice])
    elif choice == [0, 1, 0]:
        forwards.append([img, choice])
    elif choice == [0, 0, 1]:
        rights.append([img, choice])
    else:
        print("No matches!")'''

'''for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test', img)
    print(choice)
    if cv2.waitKey(25) & 0xFF ==  ord('q'):
        cv2.destroyAllWindows()
        break
'''