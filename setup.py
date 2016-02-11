from setuptools import setup

# Load the version string
exec(open('hyperop/_version.py').read())

setup(
    name="hyperop",
    packages=['hyperop'],
    version=__version__,
    download_url='https://github.com/thoppe/python-hyperoperators/tarball/1.0',
    author="Travis Hoppe",
    author_email="travis.hoppe+hyperop@gmail.com",
    description=(
        "Hyperoperators (succession, addition, multiplication, exponentiation, tetration and higher) in python."),
    license = "Creative Commons Attribution-ShareAlike 4.0 International License",
    keywords = ["math", "hyperoperators", "uparrow", "large-numbers", ],
    url="https://github.com/thoppe/python-hyperoperators",
    test_suite="tests",
)
