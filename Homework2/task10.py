# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:

# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
# import random
# n = int(input("Введите количество монет: ")) #Значение для того чтобы задать количество монет 
# coins = [random.randint(0, 1)  for i in range(n)]
coins = [0, 1, 0, 1, 1, 0]
print(coins)
up_count = 0
down_count = 0
for count in coins:
    if count > 0:
        up_count +=1
    else:
        down_count +=1
# print(f"Лежат вверх гербом: ", up_count, "Лежат вниз гербом: ", down_count)
if up_count >= down_count:
    # print("Нужно перевернуть", down_count, "монет")
    print(down_count)
else:
    # print("Нужно перевернуть", up_count, "монет")
    print(up_count)