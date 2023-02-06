from AltinoLite import*

Open()

while 1:
    if sensor.IR[2]>=200:
        go(-300,-300)
        delay(1000)
        
    elif sensor.IR[6]>=200:
        go(300,300)
        delay(1000)
        
Close()
