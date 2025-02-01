a="Good Morning"
count_words = len(a.split())  # Splits by space and counts words

print(f"The count of words is {count_words}")

count_letters = len(a)  # Direct length of the string

print(f" The Number of characters are {count_letters}")

count_aplhanum = sum(c.isalnum() for c in a)  # Count alphanumeric characters


percentOfAlpnum = (count_aplhanum / count_letters) * 100

print(f" The Percentage of Alpha numeric is {percentOfAlpnum}")