from setuptools import setup, find_packages

setup(
    name='pyri-example-plugin',
    version='0.1.0',
    description='PyRI Teach Pendant Example Plugin',
    author='John Wason',
    author_email='wason@wasontech.com',
    url='http://pyri.tech',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyri-core'
    ],
    tests_require=['pytest','pytest-asyncio'],
    extras_require={
        'test': ['pytest','pytest-asyncio']
    },
    entry_points = {
        'pyri.plugins.factory': ['pyri-example-plugin=pyri_example_plugin.factory:get_factory']
    }
)