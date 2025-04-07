# მომხმარებლისგან წინადადების მიღება
sentence = input("შეიყვანე წინადადება: ")

# ყველა პატარა ასოებით
print("პატარა ასოებით:", sentence.lower())

# ყველა დიდი ასოებით
print("დიდი ასოებით:", sentence.upper())

# პირველი ასო დიდი, დანარჩენი პატარა
print("პირველი ასო დიდი:", sentence.capitalize())

def process_sentence(sentence):
    print("პატარა ასოებით:", sentence.lower())
    print("დიდი ასოებით:", sentence.upper())
    print("პირველი ასო დიდი:", sentence.capitalize())

# მომხმარებლისგან წინადადების მიღება
user_input = input("შეიყვანე წინადადება: ")
process_sentence(user_input)


#codewars