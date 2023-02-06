from AltinoLite import*

Open()

i=1
j=1

for j in range(1,9):
    if i>8:
        i=1

    for i in range(1,9):
        if i>4 and i<6:
            displayon(i,j)
            delay(100)
        i=i+1
        
Close()
