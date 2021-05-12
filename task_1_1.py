duration = int(input('Введите вычисляемое количество времени в секундах: '))
sec = duration % 60
minute = duration // 60
hour = minute // 60
day = hour // 24
week = day // 7
month = day // 30
year = month // 12

if duration < 60:
    print(f'{sec} секунд')
elif minute >= 1 and hour < 1:
    print(f'{minute} минут, {sec} секунд')
elif hour >= 1 and day < 1:
    min = minute % 60
    print(f'{hour} часов, {min} минут, {sec} секунд')
elif day >= 1 and week < 1:
    hour = hour % 24
    min = minute % 60
    print(f'{day} дней, {hour} часов, {min} минут, {sec} секунд')
elif week >= 1 and month < 1:
    day = day % 7
    hour = hour % 24
    min = minute % 60
    print(f'{week} недель, {day} дней, {hour} часов, {min} минут, {sec} секунд')

    # Дальше по аналогии, сократить код знаний пока не хватило =(
