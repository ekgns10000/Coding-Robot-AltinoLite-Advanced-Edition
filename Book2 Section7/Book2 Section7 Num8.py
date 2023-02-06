from AltinoLite import*

Open()

while 1:
    if (sensor.IR[1]>=200) and (sensor.IR[2]>=200) and (sensor.IR[3]>=200):
        go(-300,-300)
        delay(1000)
    else:
        go(300,300)
        
Close()
