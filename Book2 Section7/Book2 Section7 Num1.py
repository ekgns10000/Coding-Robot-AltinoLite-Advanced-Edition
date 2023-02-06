from AltinoLite import*

Open()

while 1:
    if sensor.IR[1]>200:
        display('1')
        delay(1000)

    elif sensor.IR[2]>200:
        display('2')
        delay(1000)

    elif sensor.IR[3]>200:
        display('3')
        delay(1000)

    elif sensor.IR[4]>200:
        display('4')
        delay(1000)

    elif sensor.IR[5]>200:
        display('5')
        delay(1000)

    elif sensor.IR[6]>200:
        display('6')
        delay(1000)

    else:
        display(0)
        delay(1000)
Close()
