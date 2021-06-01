num = int(input("Введите число: "))


def nums_generator(num):
    for el in range(1, num + 1):
        yield el


print(*nums_generator(num))
print(type(nums_generator(num)))
