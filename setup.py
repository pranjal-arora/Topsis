from distutils.core import setup

VERSION = '1.0.1'
DESCRIPTION = 'Topsis package- By Pranjal Arora, 102003402'

# Setting up
setup(
    name="Topsis-Pranjal-102003402",
    version='1.0.1',
    license='MIT',
    description='TOPSIS is the Technique for Order of Preference by Similarity to Ideal Solution, and it is a multi-criteria decision analysis method. It is based on the fundamental premise that the best solution has the shortest distance from the positive-ideal solution, and the longest distance from the negative-ideal one. Following is a package, coded in Python, to implement the Topsis Algorithm.',
    author="Pranjal Arora",
    author_email="<prv.gma@gmail.com>",
    url='https://github.com/pranjal-arora/Topsis',
    download_url='https://github.com/pranjal-arora/Topsis/archive/refs/tags/v_01.tar.gz',
    description=DESCRIPTION,
    packages=['Topsis-Pranjal-102003402'],
    install_requires=['numpy', 'pandas', 'logging'],
    keywords=['python', 'topsis', 'machinelearning', 'datascience', 'statistics', 'predictiveanalysis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)