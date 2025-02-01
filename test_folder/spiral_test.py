'''
# Step 1: Create a 10x10 grid filled with zeros
l = []
for i in range(10):
    x = []
    for j in range(10):
        x.append(0)
    l.append(x)
'''

matrix= [[0]*10 for _ in range(1,10+1)]
print(matrix)

# Step 2: Fill the grid in a spiral order
n = 10  # Size of the matrix
current_Number = 0
count_first_i, count_last_i = 0, n - 1  # Row boundaries
count_first_j, count_last_j = 0, n - 1  # Column boundaries

while count_first_i <= count_last_i and count_first_j <= count_last_j:
    # Top row (left to right)
    for j in range(count_first_j, count_last_j + 1):
        current_Number += 1
        matrix[count_first_i][j] = current_Number
    count_first_i += 1

    # Right column (top to bottom)
    for i in range(count_first_i, count_last_i + 1):
        current_Number += 1
        matrix[i][count_last_j] = current_Number
    count_last_j -= 1

    # Bottom row (right to left)
    if count_first_i <= count_last_i:
        for j in range(count_last_j, count_first_j - 1, -1):
            current_Number += 1
            matrix[count_last_i][j] = current_Number
        count_last_i -= 1

    # Left column (bottom to top)
    if count_first_j <= count_last_j:
        for i in range(count_last_i, count_first_i - 1, -1):
            current_Number += 1
            matrix[i][count_first_j] = current_Number
        count_first_j += 1


# Step 3: Print the spiral matrix
for row in matrix:
    print(" ".join(f"{x:3}" for x in row))

