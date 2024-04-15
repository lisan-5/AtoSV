class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mydict = {}
        for m in matches:
            mydict[m[0]] = mydict.get(m[0], 0)
            mydict[m[1]] = mydict.get(m[1], 0) + 1
        
        lost0 = [key for key, value in mydict.items() if value == 0]
        lost1 = [key for key, value in mydict.items() if value == 1]

        return [sorted(lost0), sorted(lost1)]
