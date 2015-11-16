from setuptools import setup, find_packages


setup(
    name='upyflashed',

    version='0.1.0',

    description='A command to watch for new hex files from https://github.com/ntoll/upyed and flash the micro:bit immediately',

    url='https://github.com/tomviner/upyflashed',

    author='Tom Viner',
    author_email='upyflashed@viner.tv',

    license='Apache',

    packages=find_packages(
        exclude=['tests']
    ),

    install_requires=[
        'psutil',
    ],

    entry_points={
        'console_scripts': [
            'upyflashed = upyflashed:main',
        ],
    }
)
