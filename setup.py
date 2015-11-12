from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


exec(open('version.py').read())

setup(
    name='slope',
    version=__version__,
    author='',
    author_email='',
    packages=[],
    url='',
    license='See LICENSE.txt',
    description=u"slope graph Tufte style",
    package_data={'slope': ['data/*.csv',], },
    long_description=open('README.md').read(),
    install_requires=[
        "matplotlib",
        "pandas",
        "numpy",],
    classifiers=[
        "Development Status ::  Alpha",
    ],
    tests_require=['pytest', 'pytest-cov'],
    cmdclass={'test': PyTest}
    )
