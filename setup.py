from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(name="shaker_calibration",
      version="1.2.1",
      packages=["shaker_calibration"],
      install_requires=requirements)
