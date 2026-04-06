class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ['+','-','*','/']:
                if tokens[i] == '-':
                    val = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                if tokens[i] == "*":
                    val = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                if tokens[i] == "/":
                    val = stack[-2]/stack[-1]
                    if val >= 0 or val.is_integer() == True:
                        val = stack[-2]//stack[-1]
                    if  val < 0 and type(val)!= int:
                        val = stack[-2]//stack[-1]
                        val += 1
                    stack.pop()
                    stack.pop()
                    stack.append(val)
                if tokens[i] == '+':
                    val = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(val)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
                



        