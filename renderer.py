"""
renderer.py
Provide an easy interface for pixel-by-pixel rendering.
"""
import itertools as it
from PIL import Image
from PIL.ImageDraw import ImageDraw

from config import MAX_X, MAX_Y


def display(rgb_from_coords=None):
    """
    Display an image of dimensions MAX_X, MAX_Y, delegating to rgb_from_coords
    to choose the colour for the current pixel.
    :param rgb_from_coords:Function mapping x, y to (r, g, b).
    """

    if rgb_from_coords is None:
        raise ValueError("Pass in a callback function (x, y)->(r,g,b).")
    img = Image.new("RGB", (MAX_X, MAX_Y))
    draw = ImageDraw(img)
    for coords in it.product(range(MAX_X), range(MAX_Y)):
        rgb = rgb_from_coords(*coords)
        draw.point(coords, rgb)
    img.show()


if __name__ == "__main__":
    display(lambda x, y: (x, y, x * y))
