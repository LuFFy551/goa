import random

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
