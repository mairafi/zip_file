elements = [1, 5, 6, 5, 1, 2, 3]

duplicates = []

for i in elements:
    if elements.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)


