from AltinoLite import*

Open()

def AutomaticDriving():
    go(300,300)
    
while 1:
    if sensor.IR[4]>200:
        break

while 1:
    AutomaticDriving()
    if sensor.CDS<200:
        break
    
go(0,0)
steering(0)
led(0x01)

Close()
