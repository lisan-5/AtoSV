class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(char):
            max_count = 0
            left = 0
            count = 0

            for right in range(len(answerKey)):
                if answerKey[right] != char:
                    count += 1
                while count > k:
                    if answerKey[left] != char:
                        count -= 1
                    left += 1
                max_count = max(max_count, right - left + 1)
            return max_count
        
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))
