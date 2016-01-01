try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ["requests"]
packages = ["pygg"]
version = "1.0.0"

setup(
    name='pygg',
    version=version,
    description='A Python wrapper for the Champion.gg API',
    long_description='This is a python wrapper for interacting with the Champion.gg API. You will need an API key, that you can get at api.champion.gg',
    author='Philip Fugate',
    author_email='phil.fugate@gmail.com',
    url='api.champion.gg',
    packages=packages,
    package_dir={'pygg': 'pygg'},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)