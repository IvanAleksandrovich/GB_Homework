def thesaurus(*args):
    names = list(args)
    list_names = {}
    for i, val in enumerate(names):
        if list_names.get(val[0]):
            list_names[val[0]].append(val)
        else:
            list_names[val[0]] = list(names[i].split())
    return (list_names)


print(thesaurus('Иван', 'Илья', 'Даша', 'Дарина', 'Ксюша', 'Маша', 'Коля', 'Миша'))

thesaurus_sort = {}
for i, val in sorted(thesaurus('Иван', 'Илья', 'Даша', 'Дарина', 'Ксюша', 'Маша', 'Коля', 'Миша').items()):
    thesaurus_sort[i] = val
print(f'Сортировка: {thesaurus_sort}')
