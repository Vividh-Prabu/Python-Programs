# Checks the stack is full or not
def IsFull(S,n,TOP):
    if TOP == n-1:
        return 1
    else:
        return 0
# Checks the stack is empty or not
def IsEmpty(S,n,TOP):
    if TOP == -1:
        return 1
    else:
        return 0

def push(S,n,TOP,value):
    if IsFull(S,n,TOP):
        print("Stack Overflow")
        return TOP
    else:
        TOP+=1
        S[TOP]=value
        print("Element Inserted:",value)
        return TOP
n = 5
S = [None]*n
TOP = -1
TOP = push(S,n,TOP,"A")
TOP = push(S,n,TOP,"B")
TOP = push(S,n,TOP,"C")
TOP = push(S,n,TOP,"E")
TOP = push(S,n,TOP,"F")
TOP = push(S,n,TOP,"G")
print(S)
print("The current TOP of S:",TOP)
print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")

def pop(S,n,TOP):
    if IsEmpty(S,n,TOP):
        print("Stack Underflow")
    else:
        value = S[TOP]
        TOP -= 1
        print("Element Removed:",value)
        return TOP
TOP = pop(S,n,TOP)
TOP = pop(S,n,TOP)
TOP = pop(S,n,TOP)
TOP = pop(S,n,TOP)
TOP = pop(S,n,TOP)
TOP = pop(S,n,TOP)
print(S)
print("The current TOP of S:",TOP)
print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")