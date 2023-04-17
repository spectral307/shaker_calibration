from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(name="shaker_calibration",
      version="1.2.2",
      packages=["shaker_calibration", "shaker_calibration.ui"],
      install_requires=requirements)
