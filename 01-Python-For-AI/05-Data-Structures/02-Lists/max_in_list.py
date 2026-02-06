# Find maximum value in a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value:", maximum)
