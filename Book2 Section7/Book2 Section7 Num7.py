from AltinoLite import*
Open()
while 1:
    if sensor.IR[4]>=100 and sensor.IR[5]>=100:
        light(15)
    else:
        light(0)
Close()
