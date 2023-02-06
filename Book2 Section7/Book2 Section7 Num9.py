from AltinoLite import*

Open()

while 1:
    if (sensor.IR[1]>=200) and (sensor.IR[2]>=200) and (sensor.IR[3]>=200):
        steering(-127)
        go(-300,-300)
        delay(1000)
    else:
        steering(0)
        go(300,300)
        
Close()
