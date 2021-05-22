from random import choice


def get_jokes(count, repeat=True):
    text = []
    for i in range(count):
        text_r = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        text.append(text_r)
        if not repeat:
            nouns.remove(text_r.split(' ')[0])
            adverbs.remove(text_r.split(' ')[1])
            adjectives.remove(text_r.split(' ')[2])
    return text


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

count = int(input('Введите количество шуток: '))

print(get_jokes(count))
print(get_jokes(count, repeat=False))
