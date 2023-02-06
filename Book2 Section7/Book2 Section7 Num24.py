from AltinoLite import*

Open()

for j in range(1,9):
    for i in range(1,9):
        if i>5 and j>2 and j<7:
            displayon(i,j)
            delay(100)

Close()
