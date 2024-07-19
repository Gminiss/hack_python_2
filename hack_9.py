"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    for key, value in s.items():
        if key.startswith("foo"): 
         value_none = value.replace('k', '')
         result[key.capitalize()] = value_none.capitalize()
    return result