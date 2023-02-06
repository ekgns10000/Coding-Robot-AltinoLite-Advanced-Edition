from AltinoLite import*

Open()

i=1
j=1

while 1:
    for j in range(1,9):
        if j>4:
            break
        
        elif i>9:
                i=1
                j=j+1

        for i in range(1,9):
            displayon(i,j)
            delay(100)
            i=i+1
Close()
