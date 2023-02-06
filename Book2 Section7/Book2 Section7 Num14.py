from AltinoLite import*

Open()

i=1
j=1

for j in range(1,9):
    if i>8:
        i=1
        
    for i in range(1,9):
        if i<3 or i>5:
            displayon(i,j)
            delay(100)
        i=i+1
        
Close()
