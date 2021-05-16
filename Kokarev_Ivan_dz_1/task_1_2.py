arr = [i**3 for i in range(1, 1001, 2)]
result = 0

for number in arr:
    value = number
    idx = 0
    while value > 0:
        last_value = value % 10
        idx += last_value
        value = value // 10
        if idx % 7 == 0:
             result += value

print(f'Решение {result}')

for i in range(len(arr)):
    arr[i] += 17

result_17 = 0

for number in arr:
    value = number
    idx = 0
    while value > 0:
        last_value = value % 10
        idx += last_value
        value = value // 10
        if idx % 7 == 0:
             result_17 += number

print(f'Решение {result_17}')
