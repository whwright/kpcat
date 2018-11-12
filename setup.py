from setuptools import setup


requirements = [
    'click==7.0',
    'construct>=2.9.45',
    'pykeepass'
]

dependency_links = [
    'git+ssh://git@github.com/whwright/pykeepass.git@115-fix-tz-comparison#egg=pykeepass'
]

setup(
    name='kpcat',
    version='0.1.0',
    description='cat a keepass file - with style',
    url='https://github.com/whwright/kpcat',
    author='Harrison Wright',
    author_email='mail@harrisonwright.me',
    py_modules=['kpcat'],
    install_requires=requirements,
    dependency_links=dependency_links,
    entry_points='''
        [console_scripts]
        kpcat=kpcat:main
    '''
)
