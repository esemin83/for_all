from threading import Thread
from generate import generate_data, call_insert_into_table
import datetime

print('start generate data', str(datetime.datetime.now())[0:19])
x = generate_data(500000)
print('start inset data   ', str(datetime.datetime.now())[0:19])
#call_insert_into_table(x)
#print('end inset data     ', str(datetime.datetime.now())[0:19])


t1 = Thread(target=call_insert_into_table(x))
t2 = Thread(target=call_insert_into_table(x))

t1.start()
t2.start()
t1.join()
t2.join()

print('end inset data     ', str(datetime.datetime.now())[0:19])