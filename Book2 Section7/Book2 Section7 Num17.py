from AltinoLite import*
     
Open()

for i in range(1,9):
    for j in range(1,9):
        if (i>3) and (i<6) and (j>3) and (j<6):
            displayon(j,i)
            delay(100)
Close()
