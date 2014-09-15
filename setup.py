import os
from setuptools import setup, find_packages

from directional import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = []

setup(
    name = "directionalstatspy",
    version = ".".join(map(str, __version__)),
    description = "Directional Statistics in Python",
    long_description = read('README.rst'),
    url = 'https://github.com/calben/directionalstatspy/',
    license = 'MIT',
    author = 'Calem Bendell',
    author_email = 'calem.j.bendell@gmail.com',
    packages = find_packages(exclude=['tests']),
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    install_requires = requirements,
    tests_require = [],
)
