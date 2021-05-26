tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Василий', 'Руслан']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) > len(klasses):
    klasses.append(None)

generate = ((tutors[i], klasses[i]) for i in range(len(tutors)))

print(*generate)
print(type(generate))
