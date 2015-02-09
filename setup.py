# Copyright 2015 Bradley Rowe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name="pyfitnesspal",
    description="Food diary with statistics - budget your nutrition!",
    version='0.1.1',
    author="Brad Rowe",
    author_email="rowebradleyj@gmail.com",
    url="https://gord1anknot.github.io/pyfitnesspal",
    packages=find_packages(),
    test_suite='tests.runtests.runtests',
    license="Apache 2.0",
    install_requires=["Django>=1.7",
                      "wsgiref>=0.1.2",
                      "dj-database-url>=0.3",
                      "django-crispy-forms>=1.4"],
    extras_require={
        'postgres':  ["psycopg2>=2.5.4"]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
    )
