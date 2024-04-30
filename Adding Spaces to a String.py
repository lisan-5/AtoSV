class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = ""
        j = 0
        for i in range(len(s)):
            
            if j< len(spaces) and spaces[j] == i:
                string+= " "
                string+= s[i]
                j+=1
            else:
                string+= s[i]
        return string
