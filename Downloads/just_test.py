class just_testing:
    def __init__(self):
        self.counter = 0
    def foo(self):
        self.counter+=1
    def bar(self):
        self.foo()

a = just_testing()
print(a.counter) # 0
a.bar()
print(a.counter) # 1
