from app import *
import random
import string


def random_numbers(maxlen):
    numbers = string.digits
    return "".join([random.choice(numbers) for x in range(maxlen)])


def generate_data(_len):
    data_list = []
    for i in range(_len):
        j = random_numbers(6)
        data_list.append(j)
    return data_list


def call_insert_into_table(data):
    for k in range(len(data)):
        insert(data[k])
