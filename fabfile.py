from fabric.api import local

def test():
    local("nosetests -v")
    local("flake8 hyperop tests")

def cleanup():
    local("autopep8 hyperop/*.py tests/*.py --in-place")

