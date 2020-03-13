import numpy
import pandas as pd
import imageio

# converts a csv file of annotations into a pandas DataFrame
def load_csv(filename):
    df = pd.read_csv(filename,header=2)
    df = df.set_index('coords')
    df = df.rename(columns={"x": "left_x", "y": "left_y","x.1": "right_x", "y.1": "right_y","likelihood": "left_likelihood", "likelihood.1": "right_likelihood"})
    return df

# packages the data from each frame into a list of coordinate tuples for each eye
def package_points(df):
    pairs = []
    for index, row in df.iterrows():
        pairs.append([(row['left_x'],row['left_y']),(row['right_x'],row['right_y'])])
    return pairs

def package_lines(df):
    pairs = []
    for index, row in df.iterrows():
        pairs.append([(row['left_x'],row['right_x']),(row['left_y'],row['right_y'])])
    return pairs

def package_stim_points(df):
    pairs = []
    for index, row in df.iterrows():
        pairs.append([row['x'],row['y']])
    return pairs

# converts a .MP4 video into imageio frames so they can be displayed
def load_video(filename):
    reader = imageio.get_reader(filename)
    frames = []
    for i, im in enumerate(reader):
        frames.append(im)
    return frames