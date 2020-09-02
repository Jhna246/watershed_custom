import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cv2
%matplotlib inline


def create_rgb(i):
    return tuple(np.array(cm.Set1(i)[:3]) * 255)


def mouse_callback(events, x, y, flags, params):
    global markers_updated
    if events == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_marker, center=(x,y), radius=15, color=(current_marker), thickness=-1)
        cv2.circle(img_copy, center=(x,y), radius=15, color=colors[current_marker], thickness=-1)
        markers_updated= True


#global variables
current_marker = 1
markers_updated = False

# read image
img = cv2.imread('image.jpg')
img_copy = img.copy()
img_marker = np.zeros(shape=(img.shape[:2]), dtype=np.int32)
segments = np.zeros(shape=(img.shape), dtype=np.uint8)
    

# set colors
colors = []

for i in range(9):
    colors.append(create_rgb(i))
    
# create window
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

while True:
    cv2.imshow('watershed', segments)
    cv2.imshow('Image', img_copy)
    
    c = cv2.waitKey(1)
    
    if c == 27:
        break
        
    elif c == ord('q'):
        img_copy = img.copy()
        img_marker = np.zeros(img.shape[0:2], dtype=np.int32)
        segments = np.zeros(img.shape,dtype=np.uint8)
        
    elif c > 0 and chr(c).isdigit():
        current_marker = int(chr(c))
    
    if markers_updated:
        img_marker_copy = img_marker.copy()
        cv2.watershed(img, img_marker_copy)
        
        segments = np.zeros(img.shape, dtype=np.uint8)
        
        for i in range(9):
            segments[img_marker_copy == (i)] = colors[i]
    
    
        marks_updated = False

    
cv2.destroyAllWindows()
