for i in range(1,6+1):
    if (i==6):
        print("* "*11,end=" ")
    
    else:
        star= "* " * (i)
        empty= "  " * (10-((2*i)-1))
        result=star+empty+star
        print(result,end=" ")
    print("\n")