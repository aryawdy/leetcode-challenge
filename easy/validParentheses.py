def isValid(s):
    stack = []
    closeToOpen = {")":"(", "]":"[", "}":"{"}
    for n in s:
        if n in closeToOpen:
            if stack and stack[-1] == closeToOpen[n]:
                stack.pop()
            else:
                return False
        else:
            stack.append(n)
    print(stack)
    return True if not stack else False



isValid("()")
isValid("()[]{}")
isValid("(]")