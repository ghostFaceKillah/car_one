from moviepy.editor import VideoFileClip
import numpy as np


vid_fname = 'challenge.mp4'
clip = VideoFileClip(vid_fname)

snap_times = np.linspace(start=0, stop=clip.duration, num=12)

for idx, snap_t in enumerate(snap_times):
    clip.to_ImageClip(snap_t).save_frame('challange_snaps/img_{}.png'.format(idx))
