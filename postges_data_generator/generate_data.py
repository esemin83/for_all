import string
import random


def random_numbers(maxlen):
    numbers = string.digits
    return "".join([random.choice(numbers) for x in range(maxlen)])


def random_string(maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for x in range(maxlen)])


def generate_random_numbers(_len):
    data_list = []
    for i in range(_len):
        j = random_numbers(6)
        data_list.append(j)
    return data_list


def generate_random_string(_len):
    data_list = []
    for i in range(_len):
        j = random_string(6).upper()
        data_list.append(j)
    return data_list
