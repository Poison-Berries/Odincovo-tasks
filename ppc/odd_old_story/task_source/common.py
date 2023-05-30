from PIL import Image
import numpy as np


def invert_vertical(img):
    arr = np.array(img)
    arr[:, 1::2] = arr[:, 1::2][::-1, :]
    return Image.fromarray(arr)

def invert_horizontal(img):
    arr = np.array(img)
    arr[0::2, :] = arr[0::2, :][:, ::-1]
    return Image.fromarray(arr)
