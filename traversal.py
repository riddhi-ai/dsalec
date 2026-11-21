numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for index in range(len(numbers)):
    print(f"Index {index} → {numbers[index]}")