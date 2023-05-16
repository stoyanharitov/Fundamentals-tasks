divisor = int(input())
boundry = int(input())
result = 0

for i in range( boundry, divisor-1, -1):
    if i % divisor == 0 and i <= boundry and i > 0:
        result = i
        break

print(result)