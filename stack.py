list1 = ["{[]}", "{{}}[](){[((]}"]


for string in list1:
    stack = []
    result = False
    for c in string:
        if c in ['{', '[', '(']:
            stack.append(c)
        elif c in [']', '}', ')']:
            try:
                value = stack.pop()
            except IndexError:
                result = False
            else:
                if c == ']' and value == '[':
                    result = True
                elif c == '}' and value == '{':
                    result = True
                elif c == ')' and value == '(':
                    result = True
                else:
                    result = False
    print(result)
