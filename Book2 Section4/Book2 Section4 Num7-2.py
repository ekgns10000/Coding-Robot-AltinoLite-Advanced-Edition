from AltinoLite import*

Open()

x=1
y=1

while 1:
    while y<=8:
        x=1
        while x<=8:
            displayon(x,y)
            delay(200)
            x=x+1
        y=y+1
Close()
