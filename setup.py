import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def _filter_lines(fd, ignore=('-',)):
    """Filter lines out of the open file descriptor that start with all
    characters in *ignore* and any lines containing only whitespace.
    :param fd: An open file descriptor to read from
    :param ignore: A tuple (or other immutable iterable) of characters denoting
        which lines of the provided file to ignore
    """
    return [l.strip() for l in fd
            if l.strip() and all(not l.startswith(char) for char in ignore)]


def requirements(filename='requirements/base.txt'):
    """Return the filtered contents of requirements file"""
    with open(filename) as f:
        return _filter_lines(f)

REQUIREMENTS = requirements()
TEST_REQUIREMENTS = requirements(filename='requirements/test.txt')


setup(
    name='django-optimistic-lock',
    version='0.1.1',
    description='Offline optimistic locking for Django',
    url='https://github.com/gavinwahl/django-optimistic-lock',
    long_description=read('README.rst'),
    license='BSD',
    author='Gavin Wahl',
    author_email='gavinwahl@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests.runtests.runtests',
)
