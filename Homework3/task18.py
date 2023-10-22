# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11
closest = list_1[0]
for i in list_1:
    if abs(k - closest) >= abs(k - i):
        closest = i
    else:
        closest = closest + 0
print(closest)