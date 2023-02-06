from AltinoLite import*

Open()

for j in range (1,9):
    for i in range(1,9):
        if i+j<=9:
            displayon(i,j)
            delay(100)

Close()
