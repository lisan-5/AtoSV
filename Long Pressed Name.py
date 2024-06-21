class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        a = []
        b = []
        last = name[0]   
        flag = 0
        
        count = 0
        for i in range(len(name)):
            if name[i] == last:
                count+=1
                flag = 0
            else:
                a.append([count, last])
                count = 1
                last = name[i]
                flag = 1
  
        a.append([count, last])

        last = typed[0]   
        flag = 0
        
        count = 0
        for i in range(len(typed)):
            if typed[i] == last:
                count+=1
                flag = 0
            else:
                b.append([count, last])
                count = 1
                last = typed[i]
                flag = 1

        b.append([count, last])
    
        if len(b) !=len(a):
            return False
        
        for i in range(len(a)):
            if a[i][1] == b[i][1]:
                if b[i][0] >= a[i][0]:
                    continue
                else:
                    return False
            else:
                return False
        return True
