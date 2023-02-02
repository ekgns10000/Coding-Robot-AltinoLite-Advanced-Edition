from AltinoLite import*

Open()

a=8
displayon(a,4)
delay(1000)

for i in range(0,7):
    a=a-1
    displayon(a,4)
    delay(500)

Close()
