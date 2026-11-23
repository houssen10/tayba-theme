from setuptools import setup, find_packages

from tayba_theme import __version__ as version

setup(
    name="tayba_theme",
    version=version,
    description="High-Visibility Modern Slate Theme for ERPNext",
    author="Tayba Theme",
    author_email="info@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)
