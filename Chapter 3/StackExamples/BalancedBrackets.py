from StackObj.Stack import Stack

def checkClosingBracket(s,expectedOpen):
    if not s.isEmpty():
        top = s.pop()

        if top != expectedOpen:
            return False
    else:
        return False

    return True

s = Stack()
expr = input("Enter an expression  ")
valid = True
i = 0

while valid and i < len(expr):
    c = expr[i]

    if c == "(" or c == "{" or c == "[":
        s.push(c)
    
    elif c == ")":
        valid = checkClosingBracket(s,"(")
    elif c == "}":
        valid = checkClosingBracket(s,"{")
    elif c == "]":
        valid = checkClosingBracket(s,"[")

    i += 1

if not s.isEmpty():
    valid = False

print(valid)