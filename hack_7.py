"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if not s:
        return [0]
    result = []
    index = 0
    while index < len(s):
        char = s[index]
    if index % 2 == 0:
      result.append(str(ord(char) - ord('a') + 1))
    else:
      result.append(ord(char) - ord('a') + 1)
    index += 1
    return result
