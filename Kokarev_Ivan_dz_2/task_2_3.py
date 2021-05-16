words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for word in words:
    if word.isdigit():
        print(("".join(f'"{int(word):02d}"')), end =" ")
    elif not word.isalpha():
        print(("".join(f'"+{int(word):02d}"')), end =" ")
    else:
        print(("".join(f'{word}')), end =" ")