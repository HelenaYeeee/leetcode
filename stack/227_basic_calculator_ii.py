# sol 1 (best). use stack to store number to evaluate later
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        stack = []
        current_number = 0 
        operation = '+'

        for i in range(n):
            current_char = s[i]
            if current_char.isdigit():
                current_number = int(current_number) * 10 + int(current_char)
            if not current_char.isdigit() and not current_char.isspace() or i == n-1:
                # Q: why? 
                if operation == '-':
                    stack.append(-current_number)
                elif operation == '+':
                    stack.append(current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    stack.append(int(stack.pop() / current_number)) # int() b/c question description about int division
                operation = current_char
                current_number = 0 
        result = 0 
        while stack: 
            result += int(stack.pop())
        return result



# sol 2. string manipulation without using stack
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        result = 0
        current_number = 0 
        last_number = 0 
        operation = '+'

        for i in range(n):
            current_char = s[i]
            if current_char.isdigit():
                current_number = int(current_number) * 10 + int(current_char)
            if not current_char.isdigit() and not current_char.isspace() or i == n-1:
                if operation == '+' or operation == '-':
                    result += last_number
                    if operation == '-':
                        last_number = -current_number 
                    else: 
                        last_number = current_number
                elif operation == '*':
                    last_number = last_number * current_number
                elif operation == '/':
                    last_number = int(last_number / current_number)
                operation = current_char
                current_number = 0 
        result += last_number
        return result