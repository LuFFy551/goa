def find_unique(lst):
    # სიის დალაგება
    lst.sort()
    
    # განსხვავებული ელემენტის პოვნა
    for i in range(1, len(lst) - 1):
        if lst[i] != lst[i - 1] and lst[i] != lst[i + 1]:
            return lst[i]
    
    # კიდეების შემოწმება, თუკი განსხვავებული ელემენტი თავში ან ბოლოშია
    return lst[0] if lst[0] != lst[1] else lst[-1]

# ტესტირება
numbers = [3, 3, 7, 3, 3]
unique_number = find_unique(numbers)
print("განსხვავებული ელემენტია")