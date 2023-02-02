from AltinoLite import*

Open()

while 1:
    go(300,300)

    if sensor.IR[2]>50:
        go(-300,-300)
        delay(500)
Close()
