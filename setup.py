import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="washington_football",
    include_package_data=True,
    version="0.0.3.1",
    author="Kinnaird McQuade",
    author_email="kinnairdm@gmail.com",
    description="Washington Redskins are god awful",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmcquade/washington_football",
    packages=setuptools.find_packages(),
    install_requires=[
        'click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['washington_football/bin/washington_football'],
)
