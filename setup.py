import os
from setuptools import setup

long_desc = '''
`hyperop` is a small library for representing really, really, ridiculously large numbers in pure python. It does so using [hyperoperations](https://en.wikipedia.org/wiki/Hyperoperation).

+ Hyperoperation 0, `H0` is the [successor function](https://en.wikipedia.org/wiki/Successor_function), `H0(None, 4) = 5`
+ `H1` is [addition](https://en.wikipedia.org/wiki/Addition), `H1(2,4) = 2 + (1+1+1+1) = 6`
+ `H2` is [multiplication](https://en.wikipedia.org/wiki/Multiplication) (repeated addition), `H2(2,4) = 2+2+2+2 = 8`
+ `H3` is [exponentiation](https://en.wikipedia.org/wiki/Exponentiation) (repeated multiplication), `H3(2,4) = 2*2*2*2 = 16`
+ `H4` is [tetration](https://en.wikipedia.org/wiki/Tetration) (repeated exponentiation) `H4(2,4) = 2^(2^(2^(2))) = 65536`
+ ...
+ Hyperoperation n is repeated Hyperoperation (n-1)

Fundamentally, hyperop works recursively by applying a [fold-right](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) operation:

    H[n](x,y) = reduce(lambda x,y: H[n-1](y,x), [a,]*b)
'''

setup(
    name="hyperop",
    version="1.0",
    author="Travis Hoppe",
    author_email="travis.hoppe+hyperop@gmail.com",
    description=(
        "Hyperoperators (succession, addition, multiplication, exponentiation, tetration and more) in python."),
    long_description = long_desc,
    license = "MIT",
    keywords = "math hyperoperators uparrow large-numbers",
    packages=['hyperop'],
    # long_description=read('README.md'),
    test_suite="tests",
)
