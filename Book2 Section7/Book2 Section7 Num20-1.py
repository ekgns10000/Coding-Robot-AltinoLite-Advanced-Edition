from AltinoLite import*

Open()

for j in range(1,9):
    for i in range(8,0,-1):
        if i>=j:
            displayon(i,j)
            delay(100)
        
Close()
