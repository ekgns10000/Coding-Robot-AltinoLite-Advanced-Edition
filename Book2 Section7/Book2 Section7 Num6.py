from AltinoLite import*

Open()
while 1:
    
    for i in range(0,8):
    
        Heart=[120,252,254,127,127,254,252,120]
        displayline(Heart[i%8],Heart[(i+1)%8],Heart[(i+2)%8],Heart[(i+3)%8],Heart[(i+4)%8],Heart[(i+5)%8],Heart[(i+6)%8],Heart[(i+7)%8])
        delay(1000)

Close()
