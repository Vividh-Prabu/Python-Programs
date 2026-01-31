def decorator(func):
    def wrapper(*args,**kwargs):
        print("Welcome")
        func(*args,**kwargs)
        print('Thank you for Visiting')
        print("You will be redirected")
    return wrapper
@decorator
def a(n,i):
    print(f"Name:{n}")
    print(f"ID:{i}")
a('Vividh',100)
