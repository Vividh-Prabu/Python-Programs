class Summation:
    def summ(self,*args):
        ans = 0
        for i in args:
            ans += i
        return ans

sum1 = Summation()
print(sum1.summ(1,2,3))

# Method Overriding
class Father:
    def __init__(self):
        print("Father Constructor")
    def say_hello(self):
        print("Hello from Father!")
class Child(Father):
    def __init__(self):
        print("Child Constructor")

    def say_hello(self,name):
        print("Hello from Child!",name)
child = Child()
child.say_hello("VIVI")

father = Father()
father.say_hello()