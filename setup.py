import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="darkchess",
    version="0.0.1",
    author="Vishal Subbiah",
    author_email="subbiahvishal@gmail.com",
    description="incomplete information chess",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vishalsubbiah/darkchess",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
)
