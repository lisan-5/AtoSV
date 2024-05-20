class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/",]



        path = path.split("/")

        for i in range(len(path)):
            if(path[i] == "." or path[i] == ""):
                continue
            else:
                if(path[i] == ".."):
                    if(len(stack) == 1):
                        continue
                    else:
                        stack.pop()
                        stack.pop()
                else:
                    stack.append(path[i])
                    stack.append("/")



        stack = "".join(stack)

        if(len(stack) == 1):
            return "/"
        else:

            return stack[:len(stack) -1]

