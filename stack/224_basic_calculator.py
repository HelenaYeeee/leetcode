# sol 1 (best). stack and string reversal
class Solution:
    def evaluate_expr(self, stack):
        # if stack is empty (Q: when will this happen? A: never, you can remove this condition)
        # or the expression starts with a symbol, append 0 to the stack 
        # e.g. [1,'-',2,'-'] becomes [1,'-',2,'-',0]
        #if not stack or type(stack[-1]) == str: 
        if type(stack[-1]) == str: 
            stack.append(0)
        
        res = stack.pop() # pop first operand 

        # evaluate the expression till we get ')'
        while stack and stack[-1] != ')':
            sign = stack.pop() # the next element after the first operand must be a + or -
            if sign == '+':
                res += stack.pop()
            else: 
                res -= stack.pop()
        
        return res

    def calculate(self, s: str) -> int:
        stack = []
        n = 0 
        operand = 0 # store the whole number when processing digits one by one 

        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                # forming the operand - in reverse order 
                operand += 10**n * int(ch)
                n += 1
            
            elif ch != ' ':
                if n:
                    
                    # we encounter + or -, push the operand to the stack 
                    stack.append(operand)
                    n = 0
                    operand = 0 
                
                if ch == '(':
                    # we encounter the end of a sub-expression
                    # evaluate the result, then push it to the stack
                    res = self.evaluate_expr(stack)
                    stack.pop() # pop ')'
                    stack.append(res)
                else:
                    # for other char that is not '(', push to the stack
                    # note: this "else" is only associated with "if ch =='('"
                    # meaning that the case when ch=+ or - and n != 0
                    # will also run the line below 
                    stack.append(ch)
            
        # push the last operand to stack, if any 
        if n: 
            stack.append(operand)
        # evaluate the main expr in the stack
        return self.evaluate_expr(stack)
