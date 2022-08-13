from pyri.plugins.blockly import PyriBlocklyPluginFactory, PyriBlocklyBlock, PyriBlocklyCategory, add_blockly_block, \
    add_blockly_category

from . import sandbox_functions

from typing import List, Dict, NamedTuple, TYPE_CHECKING

def _get_blocks() -> Dict[str,PyriBlocklyBlock]:
    blocks = {}

    add_blockly_block(blocks,
        category = "Example",
        blockly_json = { 
            "type": "text_print2", 
            "message0": "print2 %1", 
            "args0": 
            [ 
                { 
                    "type": "input_value", 
                    "name": "TEXT"
                } 
            ],
            "previousStatement": None, 
            "nextStatement": None,
            "colour": 230,
            "tooltip": "This is a test print() function",
            "helpUrl": ""
        
        },
        sandbox_function = (sandbox_functions.text_print2, "TEXT")
    )

    return blocks

def _get_categories() -> Dict[str,PyriBlocklyCategory]:
    categories = {}
    add_blockly_category(categories, "Example", 230)
    return categories


class ExampleBlocklyPluginFactory(PyriBlocklyPluginFactory):
    def get_plugin_name(self):
        return "pyri-example-plugin"

    def get_category_names(self) -> List[str]:
        return list(_get_categories().keys())

    def get_categories(self) -> List[PyriBlocklyCategory]:
        return _get_categories()

    def get_block_names(self) -> List[str]:
        return list(_get_blocks().keys())

    def get_block(self,name) -> PyriBlocklyBlock:
        return _get_blocks()[name]

    def get_all_blocks(self) -> Dict[str,PyriBlocklyBlock]:
        return _get_blocks()

def get_blockly_factory():
    return ExampleBlocklyPluginFactory()