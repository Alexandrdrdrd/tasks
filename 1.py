a = int(input())
if ((a//1000)+(a%10))==((a%10**3//10**2)-(a%10**2//10**1)):
    print("ДА")
else:
    print("НЕТ")