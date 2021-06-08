"""
Setup
"""

import os
from setuptools import setup


def _read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    setup_requires=['nose2'],
    test_suite='nose2.collector.collector',
    name="currency_converter",
    version=0.1,
    author="sp",
    author_email="info@sp.com",
    description="sp",
    keywords="sp ",
    packages=["currency_converter"],
    long_description=_read('README.md'),
    zip_safe=True,
    license="2021 Stefan",
    classifiers=[
        "Development Status :: Release",
        "Topic :: Adapter",
    ],
    install_requires=[
    ]
)
