class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        container = []
        #signs = ("+","-","*","/")
        for num_s in tokens:
            if num_s == "+":
                x,y = container.pop(),container.pop()
                container.append(x + y)
            elif num_s == "-":
                x,y = container.pop(),container.pop()
                container.append(y - x)
            elif num_s == "*":
                x,y = container.pop(),container.pop()
                container.append( x*y)
            elif num_s == "/":
                x,y = container.pop(),container.pop()
                val = int(y/x)
                container.append(val)
            else:
                container.append(int(num_s))
        return container[-1]
            
                
                

        