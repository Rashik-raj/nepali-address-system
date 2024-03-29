import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nepali-address-system",
    version="0.0.3",
    author="Rashikraj Shrestha",
    author_email="rashik123.rs@gmail.com",
    description="Package to work with nepali address system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rashik-raj/nepali-address-system",
    project_urls={
        "Bug Tracker": "https://github.com/Rashik-raj/nepali-address-system/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)