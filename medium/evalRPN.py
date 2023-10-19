def evalRPN(tokens):
    stack = []
    for char in tokens:
        if char == "+":
            stack.append(stack.pop() + stack.pop())
        elif char == "-":
            x,y = stack.pop(),stack.pop()
            stack.append(y - x)
        elif char == "*":
            stack.append(stack.pop() * stack.pop())
        elif char == "/":
            x,y = stack.pop(),stack.pop()
            stack.append(int(y/x))
        else:
            stack.append(int(char))

    return stack[0]


evalRPN(["2","1","+","3","*"])
evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])