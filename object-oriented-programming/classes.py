class ClassName:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2

    def method1(self):
        pass

    def method2(self, extra_paramater):
        pass

obj = ClassName(value1, value2) #type:ignore

obj.method1()
obj.method2("hello")


