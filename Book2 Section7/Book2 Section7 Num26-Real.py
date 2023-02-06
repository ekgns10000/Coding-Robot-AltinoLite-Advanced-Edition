from AltinoLite import*

Open()

for j in (1,2):
    for i in range(1,9):
        if i<4 or i>5:
            displayon(i,j)
            delay(100)
            
for j in (3,4):
    for i in range(1,9):
        displayon(i,j)
        delay(100)            

for j in (5,6):
    for i in range(1,9):
        if i<4 or i>5:
            displayon(i,j)
            delay(100)
            
for j in (7,8):
    for i in range(1,9):
        displayon(i,j)
        delay(100)
            
Close()
