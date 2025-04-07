#len() – სიგრძის დასადგენად

#sum() – ჯამის გამოსათვლელად

#max() – მაქსიმალური მნიშვნელობის დასადგენად

#min() – მინიმალური მნიშვნელობის დასადგენად

#input() – მომხმარებლისგან ინფორმაციის მისაღებად

#print() – ეკრანზე დასაბეჭდად

#type() – ტიპის დასადგენად

#range() – რიცხვების დიაპაზონის შესაქმნელად#


# len()
print(len("hello"))  # -> 5
print(len([1, 2, 3]))  # -> 3
# len აბრუნებს ობიექტის ელემენტების რაოდენობას

# sum()
print(sum([1, 2, 3]))  # -> 6
print(sum([10, 20]))  # -> 30
# sum აბრუნებს რიცხვების სიის ჯამს

# max()
print(max([1, 5, 3]))  # -> 5
print(max("zebra"))   # -> 'z'
# max აბრუნებს ყველაზე დიდ მნიშვნელობას

# min()
print(min([4, 2, 7]))  # -> 2
print(min("chat"))    # -> 'a'
# min აბრუნებს ყველაზე პატარა მნიშვნელობას

# input()
name = input("შეიყვანე სახელი: ")
print("გამარჯობა", name)
# input იღებს ტექსტს მომხმარებლისგან

# print()
print("Hello, world!")
print(3 + 5)
# print ბეჭდავს ინფორმაციას ეკრანზე

# type()
print(type(5))      # -> <class 'int'>
print(type("hi"))   # -> <class 'str'>
# type აბრუნებს ცვლადის ტიპს

# range()
print(list(range(5)))       # -> [0, 1, 2, 3, 4]
print(list(range(1, 6)))    # -> [1, 2, 3, 4, 5]
# range ქმნის რიცხვების მიმდევრობას



# len-ის კოპი
def my_len(data):
    count = 0
    for _ in data:
        count += 1
    return count

# sum-ის კოპი
def my_sum(data):
    total = 0
    for num in data:
        total += num
    return total



numbers = [1, 3, 5, 3, 2]
choice = int(input("აირჩიე რიცხვი სიიდან: "))
count = numbers.count(choice)
print(f"რიცხვი {choice} სიაში მეორდება {count}-ჯერ")





my_list = ["apple", "banana", "kiwi", "cherry", "orange"]
response = input("გსურს სიის გასუფთავება? (კი/არა): ")

if response.lower() == "კი":
    my_list.clear()
    print("სია გასუფთავდა:", my_list)
else:
    print("სია დარჩა უცვლელი:", my_list)



fruits = ["apple", "banana", "kiwi", "orange", "grape"]
index = int(input("შეიყვანე ინდექსი, რომლის წაშლაც გსურს: "))

if 0 <= index < len(fruits):
    fruits.pop(index)
    print("განახლებული სია:", fruits)
else:
    print("არასწორი ინდექსია")


#codewars
