n = int(input())
j = n
count = 0
countt = 0

while n != 0:
    n = n // 10
    count += 1

n = j
while n % 10 <= n % 100 // 10:
    n = n // 10
    countt += 1

if count == countt + 1:
    print("YES")
else:
    print("NO")