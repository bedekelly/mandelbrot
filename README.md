# mandelbrot
A basic greyscale renderer for the Mandelbrot set in Python.

![Mandelbrot Set in Greyscale](http://i.imgur.com/FdpGQMx.png)

Although it's a relatively simple project, I've used this to become more familiar with the PyCharm IDE - hence the ReStructured Text docstrings. Half the complexity actually arises from the decorator-based progress indicator, as the actual algorithm is fairly compact. I've also made especially sure to separate the rendering parts of the code from the calculations, so both can be reused in different scenarios.

To generate and display a mandelbrot set of your own:
  * Change `config.py` to suit your needs
  * Run `python3 mandelbrot.py`
