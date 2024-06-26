from collections import defaultdict

n, m = map(int, input().split())
group_a = defaultdict(list)
group_b = []

for i in range(n):
    word = input().strip()
    group_a[word].append(str(i + 1))

for i in range(m):
    word = input().strip()
    group_b.append(word)

for word in group_b:
    if word in group_a:
        print(' '.join(group_a[word]))
    else:
        print(-1)
