from setuptools import setup, find_packages

setup(name="census-income", 
      version="1.0.0",
      author="poomagal",
      author_email="ctpoomagal@gmail.com",
      packages=find_packages(),
      install_requires=["pandas", "numpy", "flask"]
      )