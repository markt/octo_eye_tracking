import sys
import os
os.environ["DLClight"] = "True"
vid_list = sys.argv[1:]
import deeplabcut
config_path = '/dartfs-hpc/rc/home/7/f002qw7/thesis/ir_test-markt-2020-02-28/config.yaml' 
os.system('echo analyzing')
deeplabcut.analyze_videos(config_path,vid_list)
deeplabcut.create_labeled_video(config_path,vid_list,save_frames=True)
os.system('echo finished vid!')
