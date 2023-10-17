# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN

n = 16
# number = int(input("Введите число: "))
number = 2
count = 0

while number ** count <= n:
        degree = number ** count
        count +=1
        print(degree)
