import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymep",
    version="1.0.2",
    author="Sergio Besada",
    author_email="sergio.besada@gmail.com",
    description="Python Math Expression Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbesada/MathParserLibrary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)