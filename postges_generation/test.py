from postges_generation.db import select, insert_into_clients
from postges_generation.generate_data import *
import datetime

print('start generate data', str(datetime.datetime.now())[0:19])
client_id_data = generate_random_string(1000)
address_data = generate_random_numbers(1000)
through_id_data = generate_random_numbers(1000)


def call_insert_into_table(client_id, address, through_id):
    for k in range(len(client_id)):
        insert_into_clients(client_id[k], address[k], through_id[k])

print('start inset data   ', str(datetime.datetime.now())[0:19])
call_insert_into_table(client_id_data, address_data, through_id_data)
print('end inset data     ', str(datetime.datetime.now())[0:19])

#s = select()
#print(s)