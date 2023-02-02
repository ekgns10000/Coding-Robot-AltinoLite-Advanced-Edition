from AltinoLite import*

Open()

def AutomaticDriving():
    go(300,300)

while 1:
    if sensor.IR[6]>200:
        break

while 1:
    AutomaticDriving()

Close()
