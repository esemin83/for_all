import re


f = open('data.txt', 'r')
d = [row for row in f]
f.close()
#print(d)


def parse(data):
    result = []
    for row in range(len(data)):
        element = re.findall('<price>\w+.\w+</price>', data[row])
        result.append(element)
    result = list(filter(None, result))
    return result


print('res', parse(d))


