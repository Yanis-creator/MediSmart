"""Utilities
"""
import re
import base64
import imageio
import numpy as np
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import cv2



def base64_to_pil(img_base64):
    """
    Convert base64 image data to PIL image
    """
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    im = imageio.imread(BytesIO(base64.b64decode(image_data)))
    pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
    return pil_image


def np_to_base64(img_np):
    """
    Convert numpy image (RGB) to base64 string
    """
    img = Image.fromarray(img_np.astype('uint8'), 'RGB')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return u"data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("ascii")


#see the results 
def malign(img_path,save_path):
    im = Image.open(img_path) 
    width, height = im.size 
    left = 1230
    top = 158
    right = 1987
    bottom = 1316
    im1 = im.crop((left, top, right, bottom)) 
    im1.save(save_path)
    return None

def benin(img_path,save_path):
    im = Image.open(img_path) 
    width, height = im.size 
    left = 2413
    top = 158
    right = 3169
    bottom = 1316
    im1 = im.crop((left, top, right, bottom)) 
    im1.save(save_path)
    return None
def patche_map(img_path,save_path):
    im = Image.open(img_path) 
    width, height = im.size 
    left = 3596
    top = 158
    right = 4352
    bottom = 1316
    im1 = im.crop((left, top, right, bottom)) 
    im1.save(save_path)
    return None


