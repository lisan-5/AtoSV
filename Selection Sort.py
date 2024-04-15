class Solution: 
    def select(self, arr, start):
        min_index = start
        for j in range(start + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index
    
    def selectionSort(self, arr, n):
        for i in range(n - 1):
            min_idx = self.select(arr, i)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
