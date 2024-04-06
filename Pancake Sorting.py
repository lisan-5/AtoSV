class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        a = []
        end = len(A)
        while end > 0:
            maxi = max(A[:end])
            max_index = A[:end].index(maxi)
            if max_index+1 == end:
                end -= 1
            else:
                a.append(max_index+1)
                A[:max_index+1] = A[:max_index+1][::-1]
                a.append(end)
                A[:end] = A[:end][::-1]
                end -= 1
        return a
