from AltinoLite import*

Open()

x=1
y=1

while 1:
    while y>8:
        break

    while x>8:
        y=y+1
        x=1
    displayon(x,y)
    delay(100)
    x=x+1
    
Close()
