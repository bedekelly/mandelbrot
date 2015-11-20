from distutils.core import setup, Extension

setup(name="iterations", version="0.0.0",
      ext_modules=[Extension("iterations", ["iterations.c"])])
