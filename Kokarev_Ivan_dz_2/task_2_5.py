def result(price):
    for value in price:
        print((f'{int(value):02d} руб, {int(value * 100 % 100):02d} коп.'), end = " ")

price = [57.8, 46.51, 97, 116.37, 86.15, 99.99, 85.25, 0.5, 53.4, 65.05, 32.64, 3, 10.20, 18.65, 96.52, 44, 69.10,
         81.90, 39, 58.32]

print(f'Список цен:')
result(price)
print(f'\nID списка: {id(price)}')

price.sort()
print(f'\nСписок после сортировки по возрастанию:')
result(price)
print(f'\nID списка после сортировки: {id(price)}')

invert_result = sorted(price, reverse=True)
print(f'\nСписок после сортировки по убыванию:')
result(invert_result)
print(f'\nID списка после сортировки: {id(invert_result)}')

print(f'\n5 самых дорогих товаров:')
result(invert_result[:5])