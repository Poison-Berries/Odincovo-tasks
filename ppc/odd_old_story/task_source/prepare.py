from PIL import Image

from common import invert_vertical, invert_horizontal


if __name__ == '__main__':
    img = Image.open(input("Image file name: "))
    invert_horizontal(invert_vertical(img)).show()
