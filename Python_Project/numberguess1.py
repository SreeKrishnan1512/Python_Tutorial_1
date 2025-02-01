import random

def number_Guess():
    print("Welcome to the number guessing game")
    print("Guess the number between 1 and 100")

    target_number= random.randint(1,100)
    #print(f"the target number is {target_number}")
    count=0

    while True:

        user_find= int(input("Enter the number: "))
        if (user_find<=100):
        
            if (target_number== user_find):
                count=count+1
                print(f"Congrats you found the number {target_number} in {count} attempt")
                break

            else:
                if (target_number>user_find):

                  print(f" The given number {user_find} is lesser than target number... Please try again")
                  count=count+1
                
                else:

                  print(f" The given number {user_find} is greater than target number... Please try again")
                  count=count+1

        else:
           print(f"The number {user_find} which you have given is invalid... Please enter the number between 1 to 100")

   

    #print(target_number)


number_Guess()