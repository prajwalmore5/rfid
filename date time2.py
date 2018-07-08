import datetime
now = datetime.datetime.now()
t1 = now.replace(hour = 8, minute = 10, second = 0, microsecond = 0)
t2 = now.replace(hour = 8, minute = 20, second = 0, microsecond = 0)
t3 = now.replace(hour = 9, minute = 10, second = 0, microsecond = 0)
t4 = now.replace(hour = 9, minute = 20, second = 0, microsecond = 0)
t5 = now.replace(hour = 10, minute = 10, second = 0, microsecond = 0)
t6 = now.replace(hour = 10, minute = 35, second = 0, microsecond = 0)
t7 = now.replace(hour = 11, minute = 25, second = 0, microsecond = 0)
t8 = now.replace(hour = 11, minute = 35, second = 0, microsecond = 0)
t9 = now.replace(hour = 12, minute = 25, second = 0, microsecond = 0)
t10 = now.replace(hour = 12, minute = 55, second = 0, microsecond = 0)
t11 = now.replace(hour = 1, minute = 45, second = 0, microsecond = 0)
t12 = now.replace(hour = 1, minute = 55, second = 0, microsecond = 0)

if now <= t2:
    print ('entry')
elif (now >= t1) & (now <= t2):
    print ('lec1')
elif (now >= t3) & (now <= t4):
    print ('lec2')
elif (now >= t5) & (now <= t6):
    print ('lec3')
elif (now >= t7) & (now <= t8):
    print ('lec3')
elif (now >= t9) & (now <= t10):
    print ('lec4')
elif (now >= t11) & (now <= t12):
    print ('lec5')
else :
    print ('you are late')
