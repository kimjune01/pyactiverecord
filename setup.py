from setuptools import setup, find_packages
version = '0.1.0'

try:
    import pypandoc
    read_md = lambda f: pypandoc.convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='py-activerecord',
    version=version,
    description="py-activerecord is python activerecord like mysql wrapper.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='db, mysql, activerecord, ORM',
    author="Hiroyuki Nikaido",
    author_email="hiroyuki.nikaido@gmail.com",
    url='https://github.com/nkdn/py-activerecord',
    license='MIT',
    packages=find_packages(exclude=['examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    long_description=read_md('README.md'),
    install_requires=["mysql-connector-python"]
)