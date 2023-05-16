import setuptools
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='node-distance-ray',
    version=get_version("node-distance-ray/__init__.py"),
    description='lorem ipsum',
    long_description=read('README.rst'),
    url='http://github.com/satzbeleg/node-distance-ray',
    author='Ulf Hamster',
    author_email='554c46@gmail.com',
    license='Apache License 2.0',
    packages=['node-distance-ray'],
    install_requires=[],
    # scripts=['scripts/examplescript.py'],
    python_requires='>=3.6',
    zip_safe=True
)
