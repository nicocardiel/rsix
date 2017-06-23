from setuptools import setup
from setuptools import find_packages

def setup_package():

    from rsix import __version__
    REQUIRES = ['numpy >=1.7', 'astropy>=1.0', 'scipy', 'matplotlib']
    META_DATA = dict(
        name='rsix',
        version=__version__,
        description='miscelaneous script collection',
        author='Nicolas Cardiel',
        author_email='cardiel@ucm.es',
        packages=find_packages('.'),
        entry_points={
            'console_scripts': [
                'r6-addnf = rsix.addnf:main',
                'r6-insert_keyword_in_FITS = rsix.insert_keyword_in_FITS:main'
            ],
            },
        setup_requires=['rsix'],
        install_requires=REQUIRES,
        zip_safe=False
        )

    setup(**META_DATA)


if __name__ == '__main__':
    setup_package()
