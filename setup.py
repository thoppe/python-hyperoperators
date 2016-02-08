import os
from setuptools import setup

setup(
    name="hyperop",
    packages=['hyperop'],
    version="1.0",
    download_url = 'https://github.com/thoppe/python-hyperoperators/tarball/1.0',
    author="Travis Hoppe",
    author_email="travis.hoppe+hyperop@gmail.com",
    description=(
        "Hyperoperators (succession, addition, multiplication, exponentiation, tetration and higher) in python."),
    license = "Creative Commons Attribution-ShareAlike 4.0 International License",
    keywords = ["math","hyperoperators","uparrow","large-numbers",],
    url="https://github.com/thoppe/python-hyperoperators",
    test_suite="tests",
)
