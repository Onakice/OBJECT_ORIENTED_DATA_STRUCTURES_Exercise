def check_parenthesis(expresion):
    stack = []
    matching_parentheses = {')': '(', ']': '[', '}': '{'}
    open_parentheses = set(matching_parentheses.values())

    for index, char in enumerate(expresion):
        if char in open_parentheses:
            stack.append(char)
        elif char in matching_parentheses:
            if not stack:
                return f"{expresion} close paren excess"
            top = stack.pop()
            if top != matching_parentheses[char]:
                return f"{expresion} Unmatch open-close"
    
    if stack:
        open_count = len(stack)
        open_chars = ''.join(stack)
        return f"{expresion} open paren excess   {open_count} : {open_chars}"

    return f"{expresion} MATCH"

expresion = input("Enter expresion : ")
result = check_parenthesis(expresion)
print(result)