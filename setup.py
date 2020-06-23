#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K pip setup file
Author: TianZerL
Editor: K4YT3X, TianZerL
"""

import platform
import setuptools

system = platform.system()
if system == "Linux":
    lib = {"": ["*.so"]}
if system == "Windows":
    lib = {"": ["*.dll"]}


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyanime4k",
    version="1.0.1",
    author="TianZer",
    description="An easy way to use anime4kcpp in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="anime4k",
    url="https://github.com/TianZerL/pyanime4k",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
    package_data=lib,
    install_requires=["ffmpy3>=0.2.3"],
)
