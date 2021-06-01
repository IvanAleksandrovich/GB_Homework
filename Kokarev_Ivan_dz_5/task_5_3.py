tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Василий', 'Руслан', 'Антон', 'Мария',
          'Георгий']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

while len(tutors) > len(klasses):
    klasses.append(None)

generate = ((tutors[i], klasses[i]) for i in range(len(tutors)))

print(*generate)
print(type(generate))
