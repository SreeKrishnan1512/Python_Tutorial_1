n=5
dic={}
for i in range(1,3):
   key=str(input("Enter the team name: "))

   total_match=int(input("Enter total number of match: "))
   win= int(input("Enter how many match won: "))
   lost= int(input("Enter how many match lost: "))
   winning_percentage= (win/total_match)*100
   print(winning_percentage)

   dic[key]=[f"The total match is {total_match}",f"Number of match won {win}",
                 f"Number of match lost {lost}",f" Winning Percentage {winning_percentage}"]
   
print(dic)

wins=[]
for i in dic:
   c=dic[i][1]
   wins.append(c)


print(f"Total number of wins are {wins}")



   

   














