n = int(input("Введите число: "))

nums_generator = (num for num in range(1, n + 1))
print(*nums_generator)
print(type(nums_generator))