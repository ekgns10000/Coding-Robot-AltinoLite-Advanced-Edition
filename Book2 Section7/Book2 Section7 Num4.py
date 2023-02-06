from AltinoLite import*

Open()
a=53
display(a)
delay(1000)

while 1:
    if sensor.IR[1]>=50:
        a=a-1
        display(a)
        delay(1000)
    elif sensor.IR[3]>=50:
        a=a+1
        display(a)
        delay(1000)       
Close()
