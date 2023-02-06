from AltinoLite import*

Open()
Heart=[120,252,254,127,127,254,252,120]
while 1:
    for i in range(0,8):
        displayline(Heart[0],Heart[1],Heart[2],Heart[3],Heart[4],Heart[5],Heart[6],Heart[7])
        delay(1000)
        Heart[i]=Heart[i]<<1
        Heart[i]=Heart[i]%256
        
        Heart[i+1]=Heart[i+1]<<1
        Heart[i+1]=Heart[i+1]%256
        
        Heart[i+2]=Heart[i+2]<<1
        Heart[i+2]=Heart[i+2]%256
        
        Heart[i+3]=Heart[i+3]<<1
        Heart[i+3]=Heart[i+3]%256
        
        Heart[i+4]=Heart[i+4]<<1
        Heart[i+4]=Heart[i+4]%256
        
        Heart[i+5]=Heart[i+5]<<1
        Heart[i+5]=Heart[i+5]%256
        
        Heart[i+6]=Heart[i+6]<<1
        Heart[i+6]=Heart[i+6]%256
        
        Heart[i+7]=Heart[i+7]<<1
        Heart[i+7]=Heart[i+7]%256
        

Close()
