def insertionSort1(n, arr):
    # Write your code here
    key = arr[-1]
    i = n - 2
    while (i >= 0 and arr[i] > key):
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = key
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
