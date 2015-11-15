from setuptools import setup, find_packages


setup(
    name='upyflashed',

    version='0.1.0',

    description='A script to watch for new hex files from https://github.com/ntoll/upyed and flash the micro:bit immediately',

    # The project's main homepage.
    url='https://github.com/tomviner/upyflashed',

    # Author details
    author='Tom Viner',
    author_email='upyflashed@viner.tv',

    # Choose your license
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
