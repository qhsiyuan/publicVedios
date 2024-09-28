
import os
os.chdir(os.path.dirname(__file__))

import VideoMergeAudio

for ioi in range(70-28):
    # 路径加载
    vedpath = "E:/B_DDLUKKFA/Matlab/project/2.图窗/ved_at_bgm/ved_09_27/n27vedio_" + str(ioi + 1+28) + ".mp4"
    sndpath = "E:/B_DDLUKKFA/Matlab/project/2.图窗/ved_at_bgm/n27snd/n27sound_" + str(ioi + 1+28) + ".mp3"
    nvedpath = "../n27ved/new_vedio_" + str(ioi + 1+28) + ".mp4"

    print(ioi+1)
    vma = VideoMergeAudio.VideoMergeAudio(vedpath, sndpath, nvedpath, duration_flag=0,)
    vma.merge()
