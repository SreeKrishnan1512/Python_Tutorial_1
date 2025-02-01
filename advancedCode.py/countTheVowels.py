word=str(input("enter the word: "))
vowels=[]
word_without_space=word.replace(" ","")

lenghtCalc=len(word_without_space)

print("The length of the word is",lenghtCalc)

for i in word_without_space:
   if (i in 'aeiouAEIOU'):
        vowels.append(i)
   else:
        continue

print("The vowels from the word",word,"is",vowels)
VowelsLength= len(vowels)

percentageCalc= (VowelsLength/lenghtCalc)*100

print("The vowel percentage is: ", percentageCalc)

