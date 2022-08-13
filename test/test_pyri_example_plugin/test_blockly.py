from pyri.sandbox.util import run_blockly_compile_test


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

    run_blockly_compile_test(print2_blockly_json, expected_pysrc)