from setuptools import setup, find_packages

setup(
    name='zalando_spider',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = dirbot.settings']},
)
