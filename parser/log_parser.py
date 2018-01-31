import re
import codecs


with codecs.open('charges.log', "r", "utf_8_sig") as f:
    row_data = [row for row in f]


def parse(rows):
    result = []
    for i in range(len(rows)):
        element = re.findall('<executionType>\w+.\w+</executionType>', rows[i])
        result.append(element)
    result = list(filter(None, result))
    return result

res = parse(row_data)

with open('result.txt', "w") as f:
    for i in range(len(res)):
        f.write('%s' % res[i] + '\n')
