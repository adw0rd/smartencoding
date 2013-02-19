from setuptools import setup, find_packages
from smartencoding import __version__

long_description = ""
try:
    readme = open("README.rst")
    long_description = str(readme.read())
    readme.close()
except:
    pass

setup(
    name='smartencoding',
    version=__version__,
    description="Python smart encoding (smart_unicode and other functions)",
    long_description=long_description,
    keywords='smart_unicode, smart_text, smart_encode, smart, encoding, unicode',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    url='http://github.com/adw0rd/smartencoding',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools', ],
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
