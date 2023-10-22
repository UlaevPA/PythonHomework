# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

dictionary1 = dict({1 : "AEIOULNSTR", 2: "DG", 3 : "BCMP", 4: "FHVWY", 5: "K", 8 : "JX", 10: "QZ"})
dictionary2 = dict({1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3 : "БГЁЬЯ", 4 : "ЙЫ" ,5: "ЖЗХЦЧ", 8: "ШЭЮ", 10 : "ФЩЪ"})
k = "ноутбук"
k = k.upper()
result = [key for letter in k for key, value in dictionary2.items() if letter in value] or [key for letter in k for key, value in dictionary1.items() if letter in value]
print(sum(result))