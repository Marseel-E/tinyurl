import setuptools

with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tinyurl",
    version="0.1.0",
    author="Marseel Eeso",
    author_email="marseeleeso@gmail.com",
    description="Python API wrapper for tinyurl.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Marseel-E/tinyurl",
    project_urls={
        "Bug Tracker": "https://github.com/Marseel-E/tinyurl/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['tinyurl', 'tinyurl.utils'],
    python_requires=">=3.11",
)