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


def num_translate():
    for key, val in numbers.items():
        if user_input == key:
            return val


print(num_translate())
