from datetime import datetime
import pickle

import os
os.chdir(os.path.dirname(__file__))

import cv2
from moviepy.editor import *
from moviepy.editor import VideoFileClip

# stepstr = '1234567890'
# print(stepstr.index('8', 6, 9))
'''
dday = datetime.now().day
numbe = 149
print("9-" + str(dday - 1 - numbe//75))

with open('../dat/webnum.pkl', 'rb') as f:
    yiiy = pickle.load(f)
    f.close()

print(yiiy)
'''

cap = cv2.VideoCapture('E:\B_DDLUKKFA\Matlab\project/2.图窗/ved_at_bgm/ved_09_27/n27vedio_1.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()
print(width, height)

video_clip = VideoFileClip('E:\B_DDLUKKFA\Matlab\project/2.图窗/ved_at_bgm/ved_09_27/n27vedio_1.mp4')
print(video_clip.size)

cap = cv2.VideoCapture('E:\B_DDLUKKFA\Matlab\project/2.图窗/ved_at_bgm/ved_09_27/n27vedio_6.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()
print(width, height)

video_clip = VideoFileClip('E:\B_DDLUKKFA\Matlab\project/2.图窗/ved_at_bgm/ved_09_27/n27vedio_6.mp4')
print(video_clip.size)