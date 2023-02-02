from AltinoLite import*

Open()
x=1
y=1 
while 1:
    while y<=8:
        x=1
        for i in range(1,10):
             if x>8:              
                 y=y+1
                 break
             else:
                 displayon(x,y)
                 delay(200)
                 x=x+1

Close()
