 from setuptools import setup, find_packages

setup(
    name="nt-telegram-bot-lib",
    version="0.1.0",
    author="otabek",
    description="A simple example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/otabekr-dev/nt-telegram-bot-lib.git",
    packages=find_packages(),
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      ],
    python_requires=">=3.9",
  )