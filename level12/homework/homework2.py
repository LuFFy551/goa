import random

# Control Flow-ის 3 კომპონენტი:
# 1) Conditionals (პირობები): პროგრამის ნაკადის მართვა if-else კონსტრუქციით.
# 2) Loops (ციკლები): კოდის განმეორებითი შესრულება while ან for ციკლით.
# 3) Branching (განშტოება): პროგრამის სხვადასხვა ბლოკებში გადასვლა პირობის მიხედვით.

# 1) Number guess game using if-else
number = random.randint(1, 100)
guess = int(input("გამოიცანით რიცხვი 1-დან 100-მდე: "))
if guess == number:
    print("გილოცავთ! სწორია.")
elif guess > number:
    print("რიცხვი მეტია, სცადეთ თავიდან.")
else:
    print("რიცხვი ნაკლებია, სცადეთ თავიდან.")

# 2) Number guess game using while loop
number = random.randint(1, 100)
guess = None
while guess != number:
    guess = int(input("გამოიცანით რიცხვი 1-დან 100-მდე: "))
    if guess == number:
        print("გილოცავთ! სწორია.")
    elif guess > number:
        print("რიცხვი მეტია, სცადეთ თავიდან.")
    else:
        print("რიცხვი ნაკლებია, სცადეთ თავიდან.")

# 3) User login attempt using while loop
correct_username = "admin"
correct_password = "password123"
while True:
    username = input("შეიყვანეთ მომხმარებლის სახელი: ")
    password = input("შეიყვანეთ პაროლი: ")
    if username == correct_username and password == correct_password:
        print("სისტემაში წარმატებით შეხვედი!")
        break
    else:
        print("არასწორი მონაცემები, სცადეთ თავიდან.")

# 4) Iterate through a string and print even-indexed characters
text = "Programming"
for i in range(0, len(text), 2):
    print(text[i], end="")
print()

# 5) Sum of even-indexed numbers using range
total = sum(range(0, 101, 2))
print(f"ლუწ ინდექსებზე მდგომი რიცხვების ჯამი: {total}")

# 6) Sum of numbers from 1 to 10 using for loop
total = 0
for i in range(1, 11):
    total += i
print(f"1-დან 10-მდე რიცხვების ჯამი: {total}")

# 7) Sum of numbers from 1 to 10 using while loop
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"1-დან 10-მდე რიცხვების ჯამი (while): {total}")

# 8) Print even numbers from 2 to 20 using for loop
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# 9) Print odd numbers from 30 to 70 using while loop
num = 31
while num <= 70:
    print(num, end=" ")
    num += 2
print()

# 10) Indexing in Python
# Index არის ელემენტის პოზიცია მონაცემთა სტრუქტურაში (მაგალითად, სიაში ან სტრინგში).
# Python-ში ინდექსაცია იწყება 0-დან, რაც ნიშნავს, რომ პირველი ელემენტი აქვს ინდექსი 0, მეორე - 1 და ა.შ.

# 11) Check if a number is prime
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

# 12) Sum numbers from 1 to user input
n = int(input("შეიყვანეთ რიცხვი: "))
total = sum(range(1, n + 1))
print(f"1-დან {n}-მდე რიცხვების ჯამი: {total}")
