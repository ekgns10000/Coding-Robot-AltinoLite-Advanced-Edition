from AltinoLite import*

Open()

for j in range(1,9):
    for i in range(1,9):
        if (i>1) and (i<4) and (j>2) and (j<8):
            displayon(i,j)
            delay(100)
Close()
