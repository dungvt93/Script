# -*- coding: utf-8 -*-
import cv2, os, math
import numpy as np 
from scipy import ndimage

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def rotate_image_without_crop(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """

    height, width = mat.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat

root_dir = "./ダメ/"
result_dir = os.path.abspath(os.path.join(root_dir, os.pardir)) + "/result/"
angel = 10

if not os.path.exists(result_dir):
    os.mkdir(result_dir)
for file_name in os.listdir(root_dir):
    n = np.fromfile(root_dir + file_name, np.uint8)
    img = cv2.imdecode(n, cv2.IMREAD_UNCHANGED)
    #rotation angle in degree
    for i in range(angel,360,angel):
        #debug
        image_center = tuple(np.array(img.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, 10, 1.0)
        result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
        cv2.imshow("dfsd",result)
        cv2.waitKey(0)
        exit()
        #debug
        rotated = rotate_image(img,i)
        file_path =  result_dir + os.path.splitext(file_name)[0]+"_" + str(i)+".png"
        ext = os.path.splitext(file_path)[1]
        result, n = cv2.imencode(ext, rotated, None)
        with open(file_path, mode='w+b') as f:
            n.tofile(f)
