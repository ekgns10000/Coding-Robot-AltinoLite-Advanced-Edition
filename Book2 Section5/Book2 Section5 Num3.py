from AltinoLite import*

Open()

while 1:
    steering(0)
    go(300,300)

    if (sensor.IR[1]>50) and (sensor.IR[2]>50) and (sensor.IR[3]>50):
        steering(127)
        go(-300,-300)
        delay(1000)

Close()
