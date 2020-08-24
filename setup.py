from setuptools import setup, find_packages

d = {}
exec(open("roiextractors_gpl/version.py").read(), None, d)
version = d['version']
pkg_name = "roiextractors_gpl"

with open('README.md') as rd:
    long_description = rd.read()

setup(
    name=pkg_name,
    version=version,
    author="Alessio Buccino, Saksham Sharda, Ben Dichter",
    author_email="alessiop.buccino@gmail.com",
    description="Python module for extracting optical physiology ROIs and traces for various file types and formats. "
                "GPL License",
    url="https://github.com/catalystneuro/roiextractors-gpl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={},
    install_requires=[
        'numpy'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research"
    )
)
