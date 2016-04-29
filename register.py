import os
import pypandoc

f = open('README.txt','w+')

readme = pypandoc.convert('README.md', 'rst')
readme = readme.replace(", see\n`LICENSE.md <./LICENSE.md>`__", "\n\n" + open("LICENSE.md", "r").read())

f.write(readme)
f.close()

os.system("python setup.py sdist upload")
os.remove('README.txt')