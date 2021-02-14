from pyri.plugins.sandbox_functions import PyriSandboxFunctionsPluginFactory
from pyri.sandbox_context import PyriSandboxContext
import numpy as np

def text_print2(text):
    PyriSandboxContext.print_func("print2 function called!")
    PyriSandboxContext.print_func(text)


class ExampleSandboxFunctionsPluginFactory(PyriSandboxFunctionsPluginFactory):
    def get_plugin_name(self):
        return "pyri-example-plugin"

    def get_sandbox_function_names(self):
        return ["text_print2"]

    def get_sandbox_functions(self):
        return {"text_print2": text_print2}


def get_sandbox_functions_factory():
    return ExampleSandboxFunctionsPluginFactory()