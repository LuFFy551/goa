import random

# Control Flow-ის 3 კომპონენტი:
# 1) Conditionals (პირობები): პროგრამის ნაკადის მართვა if-else კონსტრუქციით.
# 2) Loops (ციკლები): კოდის განმეორებითი შესრულება while ან for ციკლით.
# 3) Branching (განშტოება): პროგრამის სხვადასხვა ბლოკებში გადასვლა პირობის მიხედვით.

# 1) Name and vowel extraction
name = "გიგა"
vowels = "აეიოუ"
for letter in name:
    if letter in vowels:
        print(letter, end=" ")
print()

# 2) True or False? Strings are mutable, Lists are immutable.
# False - Strings are immutable, Lists are mutable.

# 3) Explanation:
# Strings cannot be changed after creation, while lists can be modified by adding, removing, or changing elements.

# 4) Collect user information
user_info = []
for field in ["სახელი", "გვარი", "ასაკი", "დაბადების თარიღი", "სიმაღლე", "ქალაქი", "პროფესია", "საყვარელი ფერი"]:
    user_info.append(input(f"შეიყვანეთ თქვენი {field}: "))
print("შეყვანილი მონაცემები:", user_info)

# 5) Store and analyze 10 numbers
numbers = []
for _ in range(10):
    numbers.append(int(input("შეიყვანეთ რიცხვი: ")))
for num in numbers:
    print(f"{num} არის {'ლუწი' if num % 2 == 0 else 'კენტი'}")

# 6) Analyze name lengths
names = []
for _ in range(5):
    names.append(input("შეიყვანეთ სახელი: "))
for name in names:
    if len(name) > 5:
        print(f"{name} consists of more than five letters.")

# 7) Modify food list
healthy_foods = ["ვაშლი", "ბროკოლი", "თხილი", "ავოკადო", "სტაფილო"]
del healthy_foods[0]
del healthy_foods[-1]
print("განახლებული სია:", healthy_foods)

# 8) Find unique number in a list
numbers = [1, 1, 2, 1, 1]
numbers.sort()
for i in range(len(numbers)):
    if (i == 0 or numbers[i] != numbers[i-1]) and (i == len(numbers)-1 or numbers[i] != numbers[i+1]):
        print(f"განსხვავებული ელემენტი: {numbers[i]}")
        break

# 9) Sum of even-indexed numbers using range
total = sum(range(0, 101, 2))
print(f"ლუწ ინდექსებზე მდგომი რიცხვების ჯამი: {total}")

# 10) Sum numbers from 1 to 10 using for loop
total = 0
for i in range(1, 11):
    total += i
print(f"1-დან 10-მდე რიცხვების ჯამი: {total}")

# 11) Sum numbers from 1 to 10 using while loop
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"1-დან 10-მდე რიცხვების ჯამი (while): {total}")

# 12) Print even numbers from 2 to 20 using for loop
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# 13) Print odd numbers from 30 to 70 using while loop
num = 31
while num <= 70:
    print(num, end=" ")
    num += 2
print()

# 14) Check if a number is prime
num = int(input("შეიყვანეთ რიცხვი: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print("რიცხვი მარტივია" if is_prime else "რიცხვი არ არის მარტივი")

# 15) Sum numbers from 1 to user input
n = int(input("შეიყვანეთ რიცხვი: "))
total = sum(range(1, n + 1))
print(f"1-დან {n}-მდე რიცხვების ჯამი: {total}")