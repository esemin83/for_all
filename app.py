import pymysql.cursors

connection = pymysql.connect(host='localhost', database='db', user='root', password='')
connection.autocommit(True)

'''
def select_test():
    list = []
    cursor = connection.cursor()
    try:
        cursor.execute("select * from test")
        for row in cursor:
            list.append(row)
    finally:
        cursor.close()
    return list


def select_data():
    list = []
    cursor = connection.cursor()
    try:
        cursor.execute("select * from data")
        for row in cursor:
            list.append(row)
    finally:
        cursor.close()
    return list
'''


def insert(value):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO data_for_generate(id, data_1, data_2, data_3) VALUES(null, '%s', '%s', '%s')" % (value, value, value))
    finally:
        cursor.close()

