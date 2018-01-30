from app import *
from generate import generate_data, call_insert_into_table
import datetime

print('start generate data', str(datetime.datetime.now())[0:19])
x = generate_data(1000000)
print('start inset data   ', str(datetime.datetime.now())[0:19])
call_insert_into_table(x)
print('end inset data     ', str(datetime.datetime.now())[0:19])

#print('x', x)

