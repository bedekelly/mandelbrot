from renderer import display
from config import MAX_X, MAX_Y, MAX_ITERATION, X1, X2, Y1, Y2
from utils import progress, scaled


def color(it):
    """
    Arbitrarily maps the number of iterations to an RGB colour.
    :param it:The number of iterations for this value.
    :return:A tuple (R, G, B) of color values to paint this pixel.
    """
    return it % 256, it % 256, it % 256


@progress(iterations=MAX_X * MAX_Y)
def basic_mandelbrot(x, y):
    """
    Calculate and return the RGB colour for a given (x, y) pixel.
    :param x: The X coordinate of the pixel.
    :param y: The Y coordinate of the pixel.
    :return: A tuple (R,G,B) of values 0-255.
    """
    # Scale X and Y to the viewport bounded by (X1, Y1) and (X2, Y2).
    x = scaled(x, 0, MAX_Y, X1, X2)
    y = scaled(y, 0, MAX_Y, Y1, Y2)

    # Calculate the number of iterations it takes z to 'escape'.
    z = 0j
    for i in range(MAX_ITERATION):
        z = z * z + complex(x, y)
        if abs(z) > 4:
            break

    # Return a color based on this escape time.
    return color(i)


if __name__ == "__main__":
    display(basic_mandelbrot)
