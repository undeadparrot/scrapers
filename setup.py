from setuptools import setup, find_packages

setup(
    name="shanes-scrapers",
    version="0.0.2",
    description="Assorted scrapy scrapers (and/or APIs), some for South African sites.",
    author="Shane Matuszek",
    packages=find_packages(),
    install_requires=["scrapy"],
)
