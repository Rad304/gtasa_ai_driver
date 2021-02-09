import numpy as np
from PIL import ImageGrab
from cv2 import cv2
import time
from grabscreen import grab_screen
from getkeys import key_check
import os

def keys_to_output(keys):
    #[Q, Z, D]
    output = [0, 0, 0]

    if 'Q' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1

    return output

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exists, starting fresh!')
    training_data = []

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while(True):
        screen = grab_screen(region=(0,40,640,480))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (80,60))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen, output])
        print('Loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)
        if len(training_data) % 105000 == 0:
            break

if __name__ == "__main__":
    main()