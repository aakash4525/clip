from distutils.core import setup
#
#try:
#    import pypandoc
#    long_description = pypandoc.convert('README.md', 'rst')
#    long_description = long_description.replace("\r","")
#except:
#    print('Long desc failure')
#    long_description = open('README.md').read()
#
setup(
    name = 'clip', # name of package
    version = '0.1',
    description = 'Python package interact with clipboard',
    long_description=long_description,
    license='MIT',
    author = 'Akash Ahmed',
    author_email = 'aksben65@gmail.com',
    url = 'https://github.com/aakash4525/py_link_preview', # url of git repo
    download_url = 'https://github.com/aakash4525/py_link_preview/archive/v0.1.tar.gz', # git tagged tar.gz
    keywords = ['clipboard', 'clip'],
    platforms='windows',
    classifiers = []
)