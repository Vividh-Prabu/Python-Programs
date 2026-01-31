def fibanocci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibanocci(n-1) + fibanocci(n-2)
n = 10
print(fibanocci(n))