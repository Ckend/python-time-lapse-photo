import os
import moviepy
import moviepy.video.io.ImageSequenceClip
from moviepy.editor import *

def pics2video(frames_dir, video_dst, music, fps=10):
    """
    图片合成MP4

    Args:
        frames_dir (str): 图片目录
        video_dst (str): 目标目录
        fps (int, optional): 帧数. Defaults to 25.
    """
    frames_name = sorted(os.listdir(frames_dir))
    frames_path = [frames_dir+frame_name for frame_name in frames_name]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(frames_path, fps=fps)
    
    audio_clip = AudioFileClip(music).volumex(0.5)
    audio = afx.audio_loop( audio_clip, duration=clip.duration)
    final_video = clip.set_audio(audio)

    final_video.write_videofile(video_dst, codec='libx264')

music = '打上花火.mp3'
frames_dir = './result/'
video_dst = 'screenshots.mp4'
pics2video(frames_dir, video_dst, music)
