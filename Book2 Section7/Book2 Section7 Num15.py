from AltinoLite import*

Open()

for i in range(1,9):
    for j in range(1,9):
        if j>2 and j<8:
            displayon(i,j)
            delay(100)
    
Close()
