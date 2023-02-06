from AltinoLite import*

Open()

a=1
for c in range(1,9):
    for i in range(1,9):
        a=a+1
        if a>3 and a<9:
            displayon(a,c)
            delay(100)
        a=a%8
    
Close()
