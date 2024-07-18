"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    number_mapping = {"a": "2", "b": "3", "c": "4", "d": "5", "e": "6"}
    counter = 1
    for item in s:
            new_item = {}
            for key in item.keys():
                if key in number_mapping:
                    new_item[str(counter)] = item[key]
                    counter += 1 
                else:
                    new_item[key] = item[key]
                result.append(new_item)
    return result
