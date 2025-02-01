a = [1, 2, 3, 4, 5]
b = []

first_element=a[0]
for i in range(0, len(a)):
    if i == len(a) - 1:
        a[i] = first_element  # Set the last element to the first element
        print(a[i], "if statement")
    else:
        a[i] = a[i + 1]  # Shift elements to the left
        print(a[i], "else statement")

    b.append(a[i])

print(b)
