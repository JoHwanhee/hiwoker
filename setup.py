import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="hiworker",
    version="0.0.1",
    author="Jayden",
    author_email="chohh@gabia.com",
    description="A hiworks chatbot API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoHwanhee/hiwoker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)