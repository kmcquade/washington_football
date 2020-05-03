import setuptools
import os
import re
HERE = os.path.dirname(__file__)

VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(HERE, 'washington_football/bin/', 'washington_football')).read()
    return VERSION_RE.search(init).group(1)


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="washington_football",
    include_package_data=True,
    version=get_version(),
    author="Kinnaird McQuade",
    author_email="kinnairdm@gmail.com",
    description="Washington Redskins are god awful",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kmcquade/washington_football",
    packages=setuptools.find_packages(),
    install_requires=[
        'click',
        'click_log'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['washington_football/bin/washington_football'],
)
