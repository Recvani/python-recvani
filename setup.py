import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recvani",
    version="0.0.1",
    author="Anshuman kumar",
    author_email="anshuman@recvani.com",
    description="The client side python apis for making integration with recvani serveers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Recvani/python-recvani",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
