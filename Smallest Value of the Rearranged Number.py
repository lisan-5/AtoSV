class Solution:
    def smallestNumber(self, num):
        if num == 0:
            return 0
        negative = num < 0
        num_str = str(abs(num))
        sorted_digits = sorted(num_str)
        if negative:
            result = '-' + ''.join(sorted_digits[::-1])
        else:
            # Find the first non-zero digit and swap it to the front
            for i, digit in enumerate(sorted_digits):
                if digit != '0':
                    sorted_digits[0], sorted_digits[i] = sorted_digits[i], sorted_digits[0]
                    break
            result = ''.join(sorted_digits)
        return int(result)
