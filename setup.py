#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K pip setup file
Author: TianZerL
Editor: K4YT3X, TianZerL
"""

import setuptools, os
from pyanime4k.ac import Version

curr_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(curr_path, "README.md"), "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyanime4k",
    version=Version.pyanime4k,
    author="TianZer",
    description="An easy way to use anime4kcpp in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords=["anime", "anime4k", "anime4kcpp", "upscale"],
    url="https://github.com/TianZerL/pyanime4k",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
    include_package_data=True,
    install_requires=["ffmpeg-python >= 0.2.0", "numpy >= 1.17.3"],
)
