from AltinoLite import*

Open()

while 1:
    if sensor.IR[2]>=800:
        displayline(128,128,128,128,128,128,128,128)
        delay(1000)

    elif sensor.IR[2]>=700:
        displayline(64,64,64,64,64,64,64,64)
        delay(1000)

    elif sensor.IR[2]>=500:
        displayline(32,32,32,32,32,32,32,32)
        delay(1000)

    elif sensor.IR[2]>=400:
        displayline(16,16,16,16,16,16,16,16)
        delay(1000)

    elif sensor.IR[2]>=200:
        displayline(8,8,8,8,8,8,8,8)
        delay(1000)

    elif sensor.IR[2]>=100:
        displayline(4,4,4,4,4,4,4,4)
        delay(1000)
        
    elif sensor.IR[2]>=50:
        displayline(2,2,2,2,2,2,2,2)
        delay(1000)

    elif sensor.IR[2]>=1:
        displayline(1,1,1,1,1,1,1,1)
        delay(1000)
        
    else:
        display(0)
        delay(1000)       
Close()
