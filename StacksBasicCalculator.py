class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Convert input to char array
        input =[]
        input = list(s)
        #Traverse the input if operand push to operand stack
        #If operator push to operator stack
        #If opening(0) Bracket then push to operator stack
        #If closing bracket, pop operator and and operand stack till operand ) is popped

        operandStack = []
        operatorStack = []
        i=len(input) -1
        while i >= 0:

            if str(input[i]) == " ":
                i-=1
                continue
            if str(input[i])>="0" and str(input[i])<="9":
                num =""
                while i >= 0 and str(input[i])>="0" and str(input[i])<="9" :
                    num +=str(input[i])
                    i -=1
                i+=1
                if len(num) > 1:
                    num = num[::-1]
                operandStack.append(int(num))
            elif input[i] == '(':
                while operatorStack[-1] != ')':
                    operation = operatorStack.pop()
                    if operation == '+':
                        operandStack.append(operandStack.pop() + operandStack.pop())
                    if operation == '-':
                        operandStack.append(operandStack.pop() - operandStack.pop())
                operatorStack.pop()
            else:
                operatorStack.append(input[i])
            i-=1
        while operatorStack:
            operation = operatorStack.pop()
            if operation == '+':
               operandStack.append(operandStack.pop() + operandStack.pop())
            if operation == '-':
               operandStack.append(operandStack.pop() - operandStack.pop())

        return int(operandStack.pop())