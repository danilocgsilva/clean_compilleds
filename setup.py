from setuptools import setup

VERSION = '1.0.0'

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="clean_compileds",
    version=VERSION,
    description="Clean files generated by compilation",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="clean compileds",
    url="https://github.com/danilocgsilva/clean_compilleds",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["clean_compileds"],
    entry_points={"console_scripts": ["cleancompileds=clean_compileds.__main__:main"],},
    include_package_data=True
)
