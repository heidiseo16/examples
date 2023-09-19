import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import numpy as np
import os, sys
import subprocess
import mediapy as media
from PIL import Image, ImageDraw

def sample_random_points(height, width, num_points):
  """Sample random points with (time, height, width) order."""
  y = np.random.randint(0, height, (num_points, 1))
  x = np.random.randint(0, width, (num_points, 1))
  points = np.concatenate((y, x), axis=-1).astype(np.int32)
  return points

st.set_page_config(layout="wide")

#video_path = 'tapnet/examplar_videos/horsejump-high.mp4'
#video = media.read_video(video_path)

@st.cache_data
def bind_socket():
    process=f""
    subprocess.run(process,shell=True)

input_image_path = '.figure/animals.png'
    
col1, col2 = st.columns(2)

with col1:
    input_img = Image.open(input_image_path)
    st.image(input_img)

with col2:
    if st.button('This image is changing to...'):
        st.write("Inference working.. Please wait moment")
        
        process=f"python edit_cli.py --input figure/animals.png --ckpt v1-5-pruned-emaonly-adaption-task-humanalign.ckpt --edit 'Transform it to van Gogh, starry night style.''

        
        result_image_path = '.figure/output_animals.jpg'
        input_img = Image.open(input_image_path)
        st.image(input_img)
        
    else:
        st.write("Click button to change the image")
