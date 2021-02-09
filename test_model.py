import numpy as np
from PIL import ImageGrab
from cv2 import cv2
import time
from grabscreen import grab_screen
from getkeys import key_check
from nn import alexnet
from directkeys import PressKey, ReleaseKey, Z, Q, D
import os

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'pygtasa-car-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCHS)

t_time = 0.09

def straight():    
    ReleaseKey(Q)
    ReleaseKey(D)
    PressKey(Z)

def left():
    ReleaseKey(D)
    #ReleaseKey(Z)
    PressKey(Q)
    PressKey(Z)
    time.sleep(t_time)
    ReleaseKey(Q)

def right():
    ReleaseKey(Q)
    #ReleaseKey(Z)
    PressKey(D)
    PressKey(Z)
    time.sleep(t_time)
    ReleaseKey(D)

def slow_ya_roll():
    ReleaseKey(Z)
    ReleaseKey(Q)
    ReleaseKey(D)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    while(True):
        if not paused: 
            screen = grab_screen(region=(0,40,640,480))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80,60))

            print('Loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
            moves = list(np.around(prediction))
            print(moves, prediction)

            if moves == [1,0,0]:
                left()
            elif moves == [0,1,0]:
                straight()
            elif moves == [0,0,1]:
                right()
        
        keys = key_check()

        if 'P' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(Z)
                ReleaseKey(D)
                ReleaseKey(Q)
                time.sleep(1)

if __name__ == "__main__":
    main()