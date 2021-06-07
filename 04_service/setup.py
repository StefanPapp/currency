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
    name="currency_converter_service",
    version=0.02,
    author="sp",
    author_email="stefan.papp@data-wizard.net",
    description="sp",
    keywords="sp ",
    packages=["currency_converter_service"],
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
