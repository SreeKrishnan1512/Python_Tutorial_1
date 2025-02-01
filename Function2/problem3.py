def SecondsinYear():
    
    Minute=1440
    Seconds=Minute*60*365
    return Seconds

SecondsinYear()

def Return(Seconds):
    print(f"From SecondsinYear function returning to Return Function and the data is {Seconds}")

Return(SecondsinYear())



