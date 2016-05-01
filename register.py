import os

f = open('README.txt', 'w+')
try:
    import pypandoc

    readme = pypandoc.convert('README.md', 'rst')
    readme = readme.replace(", see\n`LICENSE.md <./LICENSE.md>`__", "\n\n" + open("LICENSE.md", "r").read())
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    readme = open('README.md', 'r').read()
f.write(readme)
f.close()

os.system("python setup.py sdist upload")