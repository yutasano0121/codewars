import re

def phone(strng, num):
    pattern_num = ('[^|\n].*?' num '.*?[\n|$]')
    pattern_name = '<(.*?)>'
    pattern_address =
    match = re.findall(pattern_num, string)

    if len(match) == 0:
        return ("Error => Not found: " num)
    elif len(match) > 1:
        return ("Error => Too many people: " num)
    else:
        name = re.search(pattern_name, match[0]).group(1)
        line = re.sub(('\+' pattern_num), '', match[0])
        line = re.sub(pattern_name, '', line)
        line = re.sub([^A-Za-z\.-], ' ', line)
        address = ' '.join(line).split()

# [^] and (?!pattern) for negative selection

    # your code
