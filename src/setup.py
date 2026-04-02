
from setuptools import setup
from Cython.Build import cythonize

setup(name="TensorOrder", ext_modules=cythonize(["contraction_methods/*.pyx", "tensor_network/*.pyx", "decompositions/*.pyx"], language_level=3))
