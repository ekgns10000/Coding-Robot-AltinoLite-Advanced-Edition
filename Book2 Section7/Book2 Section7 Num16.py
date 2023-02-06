from AltinoLite import*

Open()

for j in range(1,9):
    for i in range(1,9):
        if i>3 and j>4:
            displayon(i,j)
            delay(100)
            
Close()
