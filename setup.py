from setuptools import setup


setup(
    name="argc",
    version="0.2.1",
    description="A argument parsing module for python 2 and 3",
    author="Javad Shafique",
    author_email="javadshafique@hotmail.com",
    license="MIT",
    packages=["argc"],
    long_description=open("README.md", "r").read(),
    include_package_data=True
)