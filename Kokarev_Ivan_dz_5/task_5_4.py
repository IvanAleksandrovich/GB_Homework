src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
src = [src[el] for el in range(1, len(src)) if src[el] > src[el - 1]]
print(src)



