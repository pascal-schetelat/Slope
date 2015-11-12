from setuptools import setup
import sys
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        #self.test_args = []
        #self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

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
