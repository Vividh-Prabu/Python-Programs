from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def f(self):
        pass

    # @abstractmethod
    def b(self):
        pass

    @abstractmethod
    def fm(self):
        pass

class Swift(Car):
    @staticmethod
    def f():
        print("Swift is moving forward")

    # def b(self):
    #     print("Swift is moving backward")

    def fm(self):
        print("Swift is playing FM")

class WRV(Car):
    def f(self):
        print("WRV is moving forward")

    def b(self):
        print("WRV is moving backward")

    def fm(self):
        print("WRV is playing FM")

# swift = Swift()
# swift.b()
Swift.f()
