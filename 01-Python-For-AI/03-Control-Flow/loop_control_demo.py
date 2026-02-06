# Demonstration of break, continue, pass

print("Break Example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\nContinue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\nPass Example:")
for i in range(1, 4):
    if i == 2:
        pass
    print(i)