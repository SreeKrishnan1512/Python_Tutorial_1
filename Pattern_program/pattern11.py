for i in range(5,0,-1):
    star= " * "*((2*i)-1)
    dash= (" - "*(5-i))
    result= dash+star+dash
    print(result,end=" ")
    print("\n")