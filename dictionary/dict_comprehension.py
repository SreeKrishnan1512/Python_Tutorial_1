users=[(0,"ALICE","ALICE123"),
       (1,"BOB","BOB456"),
       (2,"CAROLINE","CAROLINE789")
       ]

user_mapping= {user[1]:user for user in users}
print(user_mapping)

_,dict_user_name,dict_password=users

user_name=input("Enter the name: ")
password= input("Enter the password: ")

if user_name in user_mapping and user_mapping[user_name][2]==password:
    print("Logging Successful")
else:
    print("Logging Failed")


