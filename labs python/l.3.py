print("Пінда Марія Володимирівна \nГрупа КМ-92 \nЛабораторна робота №3 \n")
print("Рядки \nЗаміна першої малої літери на заголовну в словах, що мають обрану довжину \n")
print("Варіант 12\n")

import re
import string

def is_integer(text):
    return bool(re.match(r"^[-+]{0,1}\d+$", text))

def integer_validator(prompt):
    var = input(prompt)
    while not is_integer(var):
        var = input(prompt)
    return int(var)

def get_integer_greater_than(prompt, number):
    digit = integer_validator(prompt)
    while digit <= number:
        digit = integer_validator(prompt)
    return digit

text = input("Введіть текст: ")
select_length = get_integer_greater_than("Оберіть довжину слова: ", 0)

def create_words(text):
    words = text.split(' ')
    return words
words = create_words(text)

def new_text(words):
    addit_text = []
    for word in create_words(text):
        if len(word) == select_length:
            word = word[0].upper() + word[1:]
        addit_text.append(word)
    return str((' '.join(addit_text)))

print("Новий текст: ", new_text(words))