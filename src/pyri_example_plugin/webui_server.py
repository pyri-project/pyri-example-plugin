from pyri.plugins.webui_server import PyriWebUIServerPluginFactory
from pyri.webui_server.webui_resource_router import PyriWebUIResourceRouteHandler

class PyriExampleWebUIServerPluginFactory(PyriWebUIServerPluginFactory):
    def get_plugin_name(self):
        return "pyri-example-plugin"

    def get_plugin_route_handler(self):
        return PyriWebUIResourceRouteHandler(__package__).handler

def get_webui_factory():
    return PyriExampleWebUIServerPluginFactory()
