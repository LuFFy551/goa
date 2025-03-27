names = []
for i in range(5):
    name = input("Enter name {i+1}: ")
    names.append(name)

for name in names:
    if len(name) > 5:
        print(f"The name {name} consists of more than five letters.")