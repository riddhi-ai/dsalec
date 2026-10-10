#reverse pyramid with right alignment of 5 rows
n = 5  # number of rows

for i in range(n, 0, -1):              # outer loop starts from 5 down to 1
    print(" " * (n - i), end="")       # print spaces for right alignment
    for j in range(i, 0, -1):          # inner loop prints numbers from i down to 1
        print(j, end=" ")
    print()
