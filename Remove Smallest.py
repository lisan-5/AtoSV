n = int(input())
for i in range(n):
    k = int(input())
    tests = list(map(int, input().split()))
    tests.sort()
    b = True
    for j in range(1, len(tests)):
        if abs(tests[j] - tests[j-1]) > 1:
            b = False
            break
    if b:
        print('YES')
    else:
        print('NO')
