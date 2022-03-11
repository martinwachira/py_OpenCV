import cv2 as cv
import numpy as np

W=400

def my_ellipse(img, angle):
    thickness = 2
    line_type = 8
    
    cv.ellipse(img,
               (W // 2, W //2),
               (W // 4, W // 16),
               angle,
               0,
               360,
               (255, 255, 0),
               thickness,
               line_type)
    
def my_filled_circle(img, center):
    thickness = -1
    line_type = 8
    
    cv.circle(img,
              center,
              W // 32,
              (255,123,230),
              thickness,
              line_type)
    
    
atom_window = "Atom Ellipse"

size = W, W, 3
atom_image = np.zeros(size, dtype=np.uint8)

my_ellipse(atom_image, 90)
my_ellipse(atom_image, 0)
my_ellipse(atom_image, 45)
my_ellipse(atom_image, -45)

my_filled_circle(atom_image, (W // 2, W // 2))


cv.imshow(atom_window, atom_image)
cv.moveWindow(atom_window, 0, 200)

cv.waitKey(0)

