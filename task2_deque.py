from collections import deque

def is_palindrome(string_to_test):
    if not string_to_test:
        return print("Рядок пустий")
        
    string_to_test = string_to_test.lower().replace(" ", "")
    queue = deque()

    for i in string_to_test:
        queue.append(i)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

string_to_test = input("Введіть рядок >>> ")

if is_palindrome(string_to_test):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")
