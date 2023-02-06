from AltinoLite import*

Open()

for i in range(1,9):
    displayon(i,1)
    delay(100)
        
for j in (2,3):
    for i in range(1,9):
        if i<4 or i>6:
            displayon(i,j)
            delay(100)

for j in range(4,9):
    for i in range(1,9):
            displayon(i,j)
            delay(100)

Close()
