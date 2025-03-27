numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
         print(f"{num} is even.")
else:
    print(f"{num} is odd.")