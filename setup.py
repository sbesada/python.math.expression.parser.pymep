import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymep",
    version="1.0.4",
    author="Sergio Besada",
    author_email="sergio.besada@gmail.com",
    description="Python Math Expression Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbesada/python.math.expression.parser.pymep",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],

)