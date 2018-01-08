from setuptools import setup


setup(
    name="argc",
    version="1.0.1",
    description="A argument parsing module for python 2 and 3",
    author="Javad Shafique",
    author_email="javadshafique@hotmail.com",
    license="MIT",
    packages=["argc"],
    include_package_data=True,
    url="https://github.com/JavadSM/argc",
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md'
)