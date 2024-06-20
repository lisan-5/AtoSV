class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        required_numbers = set(range(left, right + 1))
        
        for start, end in ranges:
            for num in range(start, end + 1):
                if num in required_numbers:
                    required_numbers.remove(num)
                    
        return len(required_numbers) == 0
