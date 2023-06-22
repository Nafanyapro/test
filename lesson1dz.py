def palindrome():
    word = input("Введите слово  ")
    if word == word[::-1]:
        return True
    else:
        return False

while True:
    palindrome()