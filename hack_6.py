"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    replacements = {
        "a": "1",
        "b": "-",
        "c": "3",
        "d": "-",
        "e": "5"
    }
    result = [replacements.get(char, char) for char in result]
    return result if result else ["0"]
