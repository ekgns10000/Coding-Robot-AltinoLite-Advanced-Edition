from AltinoLite import*

Open()

for i in range(1,9):
    displayon(i,1)
    delay(100)

for i in range(1,9):
    if i<8:
        displayon(i,2)
        delay(100)

for i in range(1,9):
    if i<7:
        displayon(i,3)
        delay(100)

for i in range(1,9):
    if i<6:
        displayon(i,4)
        delay(100)

for i in range(1,9):
    if i<5:
        displayon(i,5)
        delay(100)

for i in range(1,9):
    if i<4:
        displayon(i,6)
        delay(100)

for i in range(1,9):
    if i<3:
        displayon(i,7)
        delay(100)

for i in range(1,9):
    if i<2:
        displayon(i,8)
        delay(100)
        
Close()
