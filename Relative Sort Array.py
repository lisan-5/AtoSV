class Solution:
    def relativeSortArray(self, arr1, arr2):
        rank = {val: i for i, val in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (rank.get(x, len(arr2)), x))
