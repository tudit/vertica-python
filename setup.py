# Copyright (c) 2013-2017 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#!/usr/bin/env python
import collections
from setuptools import setup, find_packages


ReqOpts = collections.namedtuple('ReqOpts', ['skip_requirements_regex', 'default_vcs'])

opts = ReqOpts(None, 'git')

# version should use the format 'x.x.x' (instead of 'vx.x.x')
setup(
    name='vertica-python',
    version='0.7.3',
    description='A native Python client for the Vertica database.',
    author='Justin Berka, Alex Kim',
    author_email='justin.berka@gmail.com, alex.kim@uber.com',
    url='https://github.com/uber/vertica-python/',
    keywords="database vertica",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        'python-dateutil>=1.5',
        'pytz',
        'future',
        'six>=1.10.0'
    ],
    extras_require={'namedparams': ['psycopg2>=2.5.1']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Operating System :: OS Independent"
    ]
)
