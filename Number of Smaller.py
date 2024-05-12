n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
i = 0
j = 0

while i < n and j < m:
    if a[i] < b[j]:
        count += 1
        i += 1
    else:
        print(count, end=" ")
        j += 1

while j < m:
    print(count, end=" ")
    j += 1
