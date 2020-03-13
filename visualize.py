import os
import subprocess
import shutil
import matplotlib
import matplotlib.pyplot as plt

from analyze import *

def visualize_frame(i,pairs,lines,stim_points,vid,show_eyes=True,show_peduncle=True,show_stim_dot=True,show_stim_line=True,show_vis_line=True,show_theta=True,show_vid=True,save=False,save_dir="frame_dir"):
    fig = plt.figure()
    plt.xlim(0, 800)
    plt.ylim(0, 600)
    
    coords = pairs[i]
    left = coords[0]
    right = coords[1]
    
    ped_line = lines[i]
    eye_xs = ped_line[0]
    eye_ys = ped_line[1]
    
    stim_points = stim_points[i]
    stim_x = stim_points[0]
    stim_y = stim_points[1]
    
    # get the line to the stimulus, also returns which eye is closer and the distance from that eye to stimulus
    stim_line, closer, further, d = eye_to_stim(left,right,stim_points) # should also return closer eye
    
    # get the line representing the center of the visual field
    vis_line, eye_vec = vis_field_line(closer,further,d)
    
    # calculate the vector from the closer eye to the stimulus,
    # then the difference between the two vectors
    stim_vec = points_to_vec([(stim_x,stim_y),closer])
    theta = calc_angle(eye_vec,stim_vec)
    
    if show_peduncle:
        plt.plot(eye_xs,eye_ys)
    
    if show_stim_line:
        plt.plot(stim_line[0],stim_line[1])
    
    if show_vis_line:
        plt.plot(vis_line[0],vis_line[1])
    
    if show_eyes:
        plt.plot(left[0],left[1], 'bo')
        plt.plot(right[0],right[1], 'ro')

    if show_stim_dot:
        plt.plot(stim_x,stim_y, 'go')
    
    if show_theta:
        plt.text(100, 640, f"theta = {theta}", fontsize=12)
    
    if show_vid:
        plt.imshow(vid[i],origin='lower')
    if save:
        plt.savefig(f"{os.getcwd()}/{save_dir}/frame{i}.png")
        plt.close()


def create_video(vid,first,last,pairs,lines,stim_points,clean_up=True):
    path = os.path.join(os.getcwd(), "frame_dir")
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
    if os.path.exists("eye_tracking_vid.mp4"):
        os.remove("eye_tracking_vid.mp4")
    os.mkdir(path)
    
    for i in range(first,last):
        visualize_frame(i,pairs,lines,stim_points,vid,save=True)
    
    os.chdir("frame_dir")
    subprocess.call(['ffmpeg', '-r', '10', '-f', 'image2', '-start_number', f'{first}', '-i', 'frame%d.png', '-pix_fmt', 'yuv420p','../eye_tracking_vid.mp4'])
    os.chdir("..")
    
    if clean_up:
        shutil.rmtree(path)