import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, Z, Q, S, D
from grabscreen import grab_screen

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

def process_img(original_image):
    # Convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # Edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
    vertices = np.array([[10, 400], [10, 300], [250, 150], [450, 150], [640, 300], [640, 400]], np.int32)
    processed_img = roi(processed_img, [vertices])

    #                       edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 80, 5)
    if lines is not None:
        draw_lines(processed_img, lines)

    return processed_img

def main():
    last_time = time.time()
    while(True):
        screen = grab_screen(region=(0,40,640,480))
        new_screen = process_img(screen)
        print('Loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        # Showing output
        cv2.imshow('window', new_screen)
        #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        # Quitting opencv
        if cv2.waitKey(25) & 0xFF == ord('q'):
            # Destroy
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()