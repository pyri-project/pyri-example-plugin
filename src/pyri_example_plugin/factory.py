from pyri.plugins.factory import PyriPluginFactory
from pyri.plugins.types import PyriPluginInfo


class ExamplePluginFactory(PyriPluginFactory):
    
    def get_info(self):
        return PyriPluginInfo("pyri_example_plugin")

def get_factory():
    return ExamplePluginFactory()