from AltinoLite import*

Open()

def Go_repeat():
    Go(300,300)
    delay(1000)
    Go(-300,-300)
    delay(1000)
    Go(0,0)

Go_repeat()

Close()
