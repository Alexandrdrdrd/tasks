a = int(input())
if a > 36 or a < 0:
    print("ошибка ввода")
elif a == 0:
    print("зеленый")
elif a > 36 or a < 0:
    print("ошибка ввода")
elif a % 2 == 0 and (1 <= a <= 10) or (19 <= a <= 28) and a % 2 == 0:
    print("черный")
elif (1 <= a <= 10) or (19 <= a <= 28) and a % 2 != 0:
    print("красный")
elif a % 2 != 0 and (11 <= a <= 18) or (29 <= a <= 36) and a % 2 != 0:
    print("черный")

elif a % 2 == 0 and (11 <= a <= 18) or (29 <= a <= 36):
    print("красный")