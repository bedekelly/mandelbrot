"""
utils.py
Provide some general utilities for working with numbers and functions.
"""

from functools import wraps


def scaled_dimension(y1, x1, x2, min_x, max_x, min_y, max_y):
    """
    Given a point y1, return its corresponding point y2 such that the lengths
    of lines (x1, x2) and (y1, y2) are equivalent to each other relative to
    the possible ranges of X and Y.
    :param y1:The first point on the line to draw.
    :param x1:The first point on the corresponding X line.
    :param x2:The second point on the corresponding X line.
    :param min_x:The minimum possible X value.
    :param max_x:The maximum possible X value.
    :param min_y:The minimum possible Y value.
    :param max_y:The maximum possible Y value.
    :return:
    """
    x_range = max_x - min_x
    y_range = max_y - min_y
    x_line_mag = x2 - x1
    line_proportion = x_line_mag / x_range
    y_line_mag = line_proportion * y_range
    y2 = y1 + y_line_mag
    return y2


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


def progress(iterations=0):
    """
    Display the progress of a task that involves calling a function multiple
    times.
    :param iterations:The number of times the decorator function will be called.
    :return:The decorator function, with count initialised to 0.
    """
    count = 0

    def decorator(fn):
        """
        Decorate a function with `count` iterations to display task progress.
        :param fn:The original function to be decorated.
        :return:The decorated function, with added calls to print(percentage).
        """

        percentages = list(range(100, 0, -1))

        def maybe_print_progress():
            """Print progress if we're at a significant threshold."""
            next_perc = percentages[-1]
            if 100*count // iterations >= next_perc:
                print(next_perc, "% complete", sep='')
                percentages.pop()

        @wraps(fn)  # Use the docstring of the function we're wrapping.
        def decorated_func(*args, **kwargs):
            nonlocal count
            count += 1
            maybe_print_progress()
            return fn(*args, **kwargs)

        return decorated_func

    return decorator
