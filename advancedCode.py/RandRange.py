import random



for i in range (1,11):

    num1= random.randrange(1,9)
    num2=random.randrange(1,9)

    Answer=num1*num2

    print (f" What is {num1} x {num2} ? ")

    c=int(input("Enter the answer: "))

    if(c==Answer):
        print("Well Done!")
    else:
        print(f"Sorry, The answer is {Answer}")



