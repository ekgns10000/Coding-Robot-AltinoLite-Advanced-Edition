from AltinoLite import*

Open()

a=[1,2,5,6]
for j in a:
    for i in range(1,9):
        if i<4 or i>5:
            displayon(i,j)
            delay(100)
a=[3,4,7,8]
for j in a:
    for i in range(1,9):
        if i<9:
            displayon(i,j)
            delay(100)            

Close()
