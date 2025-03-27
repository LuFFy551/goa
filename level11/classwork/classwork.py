numbers = []

for i in range(10):
    while True:
        try:
            num = int(input(f"{i+1}/10 - შეიყვანეთ მთელი რიცხვი: "))
            numbers.append(num)
            break
        except ValueError:
            print("გთხოვთ, შეიყვანოთ მხოლოდ მთელი რიცხვი.")

sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)

print(f"რიცხვების ჯამი: {sum_numbers}")
print(f"საშუალო არითმეტიკული: {average}")
