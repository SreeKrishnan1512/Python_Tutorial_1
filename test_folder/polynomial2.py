from itertools import zip_longest

list1=[2,6,4,7]
list2=[3,8,0,5,2]
Polynomial_List=""


if len(list1)>len(list2):
    max= len(list1)
    
    print(f"The maximum length of list is {max} and its from list 1")

else:
    max=len(list2)
    
    print(f"The maximum length of list is {max} and its from list 2")

power= max-1


#for index,(coeff_list1,coeff_list2) in enumerate(zip_longest(list1,list2,fillvalue=0)):
for (coeff_list1,coeff_list2) in (zip_longest(list1,list2,fillvalue=0)):
    if power>0:
        summingList = coeff_list1+ coeff_list2
        summingList_into_String = f"{summingList} X^{power} + "
        Polynomial_List=Polynomial_List+summingList_into_String
        power=power-1
    else:
        summingList = str(coeff_list1+ coeff_list2) 
        Polynomial_List=Polynomial_List+summingList

print(Polynomial_List)

        





