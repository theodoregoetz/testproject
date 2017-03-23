import os
from codecs import open
from os import path
from subprocess import Popen, PIPE

VERSION = 1,0,0

def setup_opts():
    opts = dict(
        name='module',
        version='.'.join(str(x) for x in VERSION),
        description='Test module',
        long_description='Test module for testing.',
        url='https://github.com/theodoregoetz/testproject',
        author='Johann T. Goetz',
        author_email='theodore.goetz+testproject@gmail.com',
        license='GPLv3',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Operating System :: OS Independent',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3.5',
        ],
        packages=['module'],
        setup_requires=['numpy'],
        install_requires=['numpy'],
    )
    return opts

if __name__ == '__main__':
    from setuptools import setup
    setup(**setup_opts())
