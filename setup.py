# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


SRC_DIR = "src"


with open("README.md", mode = 'r', encoding = 'utf-8') as f:
    readme = f.read()

data_files = [
    os.path.join(SRC_DIR, "pyCRGI/data/igrf13coeffs.txt")
]


setup(
    name = "pyCRGI",
    version = "0.4.0",
    author = "pyCRGI authors",
    author_email = "ernst@pleiszenburg.de",
    description = "IGRF-13 Model in Python",
    long_description = readme,
    long_description_content_type = "text/markdown",
    license = "MIT",
    url = "https://github.com/pleiszenburg/pyCRGI",
    packages = find_packages(SRC_DIR),
    package_dir = {"": SRC_DIR},
    include_package_data=True,
    package_data = {"pyCRGI/data": data_files},
    install_requires = [],
    extras_require = {
        "jited": [
            "numba",
            "numpy",
        ],
        "array": [
            "numba",
            "numpy",
        ],
        "dev": [
            "goto-statement",
            "matplotlib",
            "numpy",
            "pexpect",
            "tqdm",
            "typeguard",
            "zarr",
        ],
    },
)
