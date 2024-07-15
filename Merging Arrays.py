def merge_sorted_arrays(a, b):
    i, j = 0, 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1
    return merged

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = merge_sorted_arrays(a, b)
print(' '.join(map(str, result)))
