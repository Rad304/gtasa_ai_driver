import numpy as np
from PIL import ImageGrab
from cv2 import cv2
import time
from directkeys import PressKey, ReleaseKey, Z, Q, S, D
from grabscreen import grab_screen
from draw_lanes import draw_lanes

def draw_lines(image, lines):
    for line in lines:
        coords = line[0]
        cv2.line(image, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 5)


def roi(image, vertices):
    # Blank mask
    mask = np.zeros_like(image)
    
    # Fill the pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, 255)

    # Extract pixels from image only where mask pixels are nonzero
    masked = cv2.bitwise_and(image, mask)


    return masked 

def process_img(image):
    original_image = image
    # Convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Edge detection
    processed_img = cv2.Canny(processed_img, threshold1=120, threshold2=160)
    processed_img = cv2.GaussianBlur(processed_img, (5,5),0)
    #vertices = np.array([[10, 400], [10, 300], [250, 100], [450, 100], [640, 300], [640, 400]], np.int32)
    vertices = np.array([[10, 350], [10, 300], [320, 210], [325, 210], [640, 300], [640, 350]])
    processed_img = roi(processed_img, [vertices])

    #                       edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 20, 10)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1,m2 = draw_lanes(original_image,lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 5)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 5)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0,0], 5)
                
                
            except Exception as e:
                print(str(e))
    except Exception as e:
        pass

    return processed_img, original_image, m1, m2

def straight():
    ReleaseKey(Q)
    ReleaseKey(D)
    PressKey(Z)

def left():
    ReleaseKey(Z)
    ReleaseKey(D)
    PressKey(Q)
    
def right():
    ReleaseKey(Z)
    ReleaseKey(Q)
    PressKey(D)
    
def slow_down():
    ReleaseKey(Z)
    ReleaseKey(Q)
    ReleaseKey(D)

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

PressKey(Z)
time.sleep(3)
ReleaseKey(Z)

def main():
    last_time = time.time()
    while(True):
        screen = grab_screen(region=(0,40,640,480))
        new_screen, original_image, m1, m2  = process_img(screen)
        print('Loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        # Showing output
        cv2.imshow('window', new_screen)
        cv2.imshow('window2', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

        if m1 < 0 and m2 < 0: 
            right()
        elif m1 > 0 and m2 > 0:
            left()
        else:
            straight()

        # Quitting opencv
        if cv2.waitKey(25) & 0xFF == ord('q'):
            # Destroy
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()