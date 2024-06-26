a = set(input().split())
n = int(input())
result = True

for _ in range(n):
    other_set = set(input().split())
    if not (a > other_set):
        result = False
        break

print(result)
