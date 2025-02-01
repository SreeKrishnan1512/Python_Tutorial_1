for i in range(1,9+1):
    if (i==1 or i==9):
        star="*  " * 9
        print(star, end=" ")
    else:
      for j in range(1,9+1):
        if (j==1 or j==9):
            print("* ",end=" ")

        else:
           if(j==(9-i+1)):
              print("* ",end=" ")
           else:
             print("  ",end=" ")

    print("\n")
        