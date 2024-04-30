t = int(input())
while t > 0:
    sum = 0
    t -= 1
    n = int(input())
    l = list(map(int, input().split()))
    temp = [0] * n
    for i in range(n):
        if i == 0 or l[i] * l[i - 1] < 0:
            temp[i] = l[i]
            if i != 0 and l[i] * l[i - 1]:
                sum += temp[i - 1]
        else:
            temp[i] = l[i] = max(l[i], l[i - 1])
    sum += temp[-1]
    print(sum)
