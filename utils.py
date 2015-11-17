from functools import wraps


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

        percentages = list(range(100, 0, -5))

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
