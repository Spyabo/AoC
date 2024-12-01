from setuptools import setup
from Cython.Build import cythonize

setup(
    name='funnybug',
    ext_modules=cythonize("/home/spy/dev/AoC/2021/Day03/funnybug.pyx"),
)