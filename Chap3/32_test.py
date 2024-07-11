def check_parentheses(expression):
    stack = []
    matching_parentheses = {')': '(', ']': '[', '}': '{'}
    open_parentheses = set(matching_parentheses.values())

    for index, char in enumerate(expression):
        if char in open_parentheses:
            stack.append(char)
        elif char in matching_parentheses:
            if not stack:
                return f"{expression} close paren excess"
            top = stack.pop()
            if top != matching_parentheses[char]:
                return f"{expression} Unmatch open-close"

    if stack:
        open_count = len(stack)
        open_chars = ''.join(stack)
        return f"{expression} open paren excess   {open_count} : {open_chars}"

    return f"{expression} MATCH"

# รับค่านิพจน์จากผู้ใช้
expression = input("Enter expression: ")
result = check_parentheses(expression)
print(result)