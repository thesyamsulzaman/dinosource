import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dinosource",
    version="0.0.1",
    author="Syamsul Zaman",
    author_email="thesyamsulzaman@gmail.com",
    description="A small package that extracts Dinosaurs data from dinosaurpictures.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thesyamsulzaman/dinosource",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

