import cv2 as cv
import sys

# print('version =',cv.__version__)

img = cv.imread('deer.jpg')

if img is None:
    print('No found Image')
    sys.exit('could not read the image')
    
cv.imshow('image',img)

k = cv.waitKey(0)   

if k == ord('s'):
    # cv.imwrite('deer_copy.jpg',img)
    print('Image saved')
    
                        