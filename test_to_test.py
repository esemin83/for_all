'''
import datetime
import time

x = datetime.datetime.now()
unixtime_1 = time.mktime(x.timetuple())
print(unixtime_1)
time.sleep(3)
y = datetime.datetime.now()
unixtime_2 = time.mktime(x.timetuple())
print(unixtime_2)

print(unixtime_2 - unixtime_1)

#print(time.mktime((datetime.datetime.now()).timetuple())
'''

x = '79265694331'
y = x[1:]
print(y)