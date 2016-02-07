import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "hyperop",
    version = "1.0",
    author = "Travis Hoppe",
    author_email = "travis.hoppe+hyperop@gmail.com",
    description = ("Hyperoperators (succession, addition, multiplication, exponentiation, tetration and more) in python."),
    license = "MIT",
    keywords = "math hyperoperators uparrow large-numbers",
    packages=['hyperop'],
    long_description=read('README.md'),
    test_suite="tests",
)
