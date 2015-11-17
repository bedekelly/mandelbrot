from renderer import display
from config import MAX_X, MAX_Y, MAX_ITERATION, X1, Y1, X2, Y2
from utils import progress


def scaled(value, orig_lower, orig_upper, new_lower, new_upper):
    """
    Scale a value from one range to another.
    :param value: The value to be scaled.
    :param orig_lower: The lower bound on the range of possible input values.
    :param orig_upper: The upper bound on the range of possible input values.
    :param new_lower: The lower bound on the new range of output values.
    :param new_upper: The upper bound on the new range of output values.
    :return:
    """
    orig_range = orig_upper - orig_lower
    mag = value / orig_range
    new_range = new_upper - new_lower
    scaled_value = new_lower + mag*new_range
    return scaled_value


@progress(iterations=MAX_X*MAX_Y)
def basic_mandelbrot(x, y):
    """
    Calculate and return the RGB colour for a given (x, y) pixel.
    :param x: The X coordinate of the pixel.
    :param y: The Y coordinate of the pixel.
    :return: A tuple (R,G,B) of values 0-255.
    """
    # Calculate x0 and y0 by scaling our values to the Mandelbrot scale.
    zoomed_x = scaled(x, 0, MAX_X, X1, X2)
    zoomed_y = scaled(y, 0, MAX_Y, Y1, Y2)
    x0 = scaled(zoomed_x, X1, X2, -2.5, 1)
    y0 = scaled(zoomed_y, Y1, Y2, -1, 1)

    # Calculate the max iterations by using the Escape Time Algorithm.
    it = x = y = 0
    for _ in range(MAX_ITERATION):
        it += 1
        if x*x + y*y > 4:
            break
        x, y = x*x - y*y + x0, 2*x*y + y0

    # Scale the max iterations into a value from 0 to 255.
    grey = int(scaled(it, 0, MAX_ITERATION, 0, 255))

    # Return this value for red, green and blue to achieve greyscale colouring.
    return grey, grey, grey


if __name__ == "__main__":
    display(basic_mandelbrot)
