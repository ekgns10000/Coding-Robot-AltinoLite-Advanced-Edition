from AltinoLite import*

Open()

i=1
j=1

for j in range(1,9):
    if i>9:
        i=1
       
    for i in range(1,9):
        if i>3:
            displayon(i,j)
            delay(100)
Close()
