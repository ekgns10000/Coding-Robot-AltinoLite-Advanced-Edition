from AltinoLite import*

Open()

speed = [0,100,200,300,400,500,400,300,200,100,0]

for i in range (0,11):
    go(speed[i],speed[i])
    delay(1000)

Close()
