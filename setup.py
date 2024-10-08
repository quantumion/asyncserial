#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


if sys.version_info[:3] < (3, 5):
    raise SystemExit("You need Python 3.5+")


setup(
    name="asyncserial",
    version="1.0",
    description="asyncio support for pyserial",
    author="Sebastien Bourdeauducq",
    author_email="sb@m-labs.hk",
    url="https://m-labs.hk",
    download_url="https://github.com/m-labs/asyncserial",
    license="BSD",
    packages=find_packages(),
    install_requires=["pyserial"],
    platforms=["Any"]
)
