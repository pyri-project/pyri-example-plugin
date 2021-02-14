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
        'pyri.plugins.sandbox_functions': ['pyri-example-plugin-functions=pyri_example_plugin.sandbox_functions:get_sandbox_functions_factory'],
        'pyri.plugins.blockly': ['pyri-example-plugin-blockly=pyri_example_plugin.blockly:get_blockly_factory'],
        'pyri.plugins.webui_server': ['pyri-example-plugin-webui-server=pyri_example_plugin.webui_server:get_webui_factory']
    }
)