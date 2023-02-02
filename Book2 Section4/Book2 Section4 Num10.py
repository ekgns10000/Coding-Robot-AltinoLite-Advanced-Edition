from AltinoLite import*

Open()

x=8
y=1

while 1:
    while x<1:
       break
    
    while y>8:
        x=x-1
        y=1
    displayon(x,y)
    delay(100)
    y=y+1

Close()
