from pyri.sandbox import blockly_compiler
import io

def _do_blockly_compile_test(blockly_json, expected_pysrc):
    json_io = io.StringIO(blockly_json)
    output_io = io.StringIO()

    blockly_compiler.compile_blockly_file(json_io, output_io)
    output_io.seek(0)
    pysrc_str = output_io.read()
    print(pysrc_str)
    assert pysrc_str == expected_pysrc

def test_blockly_compiler_print2():
    print2_blockly_json = \
"""
{
  "blocks": {
    "languageVersion": 0,
    "blocks": [
      {
        "type": "procedures_defnoreturn",
        "id": "ig-@O/ylKy_@*tL~m@X|",
        "x": 138,
        "y": 88,
        "icons": {
          "comment": {
            "text": "Describe this function...",
            "pinned": false,
            "height": 80,
            "width": 160
          }
        },
        "fields": {
          "NAME": "test_text_print2"
        },
        "inputs": {
          "STACK": {
            "block": {
              "type": "text_print2",
              "id": "leNnyydaklEu0$|E4fU~",
              "inputs": {
                "TEXT": {
                  "shadow": {
                    "type": "text",
                    "id": "wWggJq|t$BAzKbOf`dtu",
                    "fields": {
                      "TEXT": "test text_print2"
                    }
                  }
                }
              }
            }
          }
        }
      }
    ]
  }
}
"""
    expected_pysrc = "# Describe this function...\ndef test_text_print2():\n  text_print2('test text_print2')\n"

    _do_blockly_compile_test(print2_blockly_json, expected_pysrc)