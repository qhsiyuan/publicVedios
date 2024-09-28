#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   video_merge_audio.py
@Time    :   2022/12/27 15:36:57
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   利用moviepy库, 给视频添加一个背景音乐
'''

import cv2
from moviepy.editor import *
from moviepy.editor import VideoFileClip

class VideoMergeAudio(object):
    
    def __init__(self, video_file, audio_file, nvedpath, duration_flag = 0) -> None:
        '''
        @des  :构造函数
        @params  :
                 video_file视频的绝对地址和文件名
                 audio_file音频的绝对地址和文件名
                 dration_flag如果是0, 那么最终视频尝试以video_file长度为准
                             如果是1, 那么最终视频尝试以audio_file长度为准
        @return  : None   
        '''
        self.video_file = video_file
        self.audio_file = audio_file
        self.duration_flag = duration_flag
        self.nvedpath = nvedpath
        pass

    def merge(self):
        '''
        @des  :合并视频和音频
        @params  :
                 video_file视频的绝对地址和文件名
                 audio_file音频的绝对地址和文件名
                 duration_flag如果是0, 那么最终视频尝试以video_file长度为准
                             如果是1, 那么最终视频尝试以audio_file长度为准
        @return  : 返回合并后的视频文件的绝对地址
        '''
        video_clip = VideoFileClip(self.video_file)
        audio_clip = AudioFileClip(self.audio_file)
        cap = cv2.VideoCapture(self.video_file)
        wid = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        hit = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()
        print(wid, hit)

        if self.duration_flag == 0:
            final_clip = video_clip.set_audio(audio_clip).set_duration(video_clip.duration)
        else:
            final_clip = video_clip.set_audio(audio_clip).set_duration(audio_clip.duration)
        
        if wid >= hit:
            final_clip = final_clip.resize((1280, 720))
        else:
            final_clip = final_clip.resize((720, 1280))

        print(final_clip.size)
        final_clip.write_videofile(self.nvedpath)

