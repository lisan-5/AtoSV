class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        actual_dict = {}
        for i in range(len(words[0])):
            if words[0][i] in actual_dict:
                actual_dict[words[0][i]]+=1
            else:
                actual_dict[words[0][i]]=1
        
        for i in range(1, len(words), 1):
            
            another = {}
            for j in range(len(words[i])):
                if words[i][j] in another:
                    another[words[i][j]] +=1
                else:
                    another[words[i][j]] = 1
            
            for j in actual_dict:
                if j in another:
                    if another[j] <= actual_dict[j]:
                        actual_dict[j] = another[j]
                else:
                    actual_dict[j] = -1
        ans = []
        for i in actual_dict:
            if actual_dict[i] == -1:
                continue
            else:
                ans+= [i] * actual_dict[i]
        return ans
