def countingSort(arr, n):
    maximum = max(arr)
    frequency = [0] * 100
    for num in arr:
        frequency[num] += 1
        
    return frequency
    

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr, n)
    print(' '.join(map(str, result)))
