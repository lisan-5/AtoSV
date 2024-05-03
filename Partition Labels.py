class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        partitions = []
        start = 0
        end = 0
        
        for idx, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1
        
        return partitions
