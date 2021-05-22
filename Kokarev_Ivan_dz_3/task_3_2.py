numbers = {
    'null': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

user_input = input("Введите число: ")


def num_translate_adv():
    for key, val in numbers.items():
        if user_input.islower():
            if user_input == key:
                return val
        if user_input.istitle():
            if user_input.lower() == key:
                return val.capitalize()


print(num_translate_adv())
