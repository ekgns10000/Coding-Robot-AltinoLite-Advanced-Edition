from AltinoLite import*

Open()
data=0x01

for i in range (0,8):
    displayline(data,data,data,data,data,data,data,data)
    delay(1000)

    data=data<<1

Close()
