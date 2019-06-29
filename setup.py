from setuptools import setup, find_packages

setup(
    name="govini-site-crawler",
    description="Govini assessment script that crawls a specified website",
    version="1",
    packages=find_packages(exclude="tests"),
    author="Christopher Herman",
    author_email="crherman7@gmail.com",
    scripts=['scripts/run_crawler'],
)
