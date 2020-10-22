# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import argparse 


root_folder = "C:/Users/n3724/Desktop/実証実験"
parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('--path', help='画像を持つフォルダパス', required=True)    # 必須の引数を追加
parser.add_argument('--name',default="video", help='出力映像の名前')
parser.add_argument('--fps',default="1", help='Frame per second' ,type=float)
args = parser.parse_args()

img=[]
for filename in os.listdir(args.path):
    # img.append(cv2.imread(args.path + "/" + str(filename)))
    numpy_image = np.fromfile(args.path + "/" + str(filename),dtype=np.uint8)
    img.append(cv2.imdecode(numpy_image,cv2.IMREAD_UNCHANGED))

if len(img[1].shape) > 2:
    height,width,_ =img[1].shape
    video=cv2.VideoWriter(args.name+'.avi',cv2.VideoWriter_fourcc(*'DIVX'),args.fps,(width,height))
else:
    height,width =img[1].shape
    video=cv2.VideoWriter(args.name+'.avi',cv2.VideoWriter_fourcc(*'DIVX'),args.fps,(width,height),0)
    # video=cv2.VideoWriter('video.mp4',cv2.VideoWriter_fourcc(*'MP4V'),1,(width,height))
for frame in img:
    video.write(frame)

cv2.destroyAllWindows()
video.release()
