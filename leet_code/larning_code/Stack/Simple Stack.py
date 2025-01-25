class Stack:
    def __init__(self):
        self.values = []
    def Push(self,x):
        self.values = [x] + self.values
    def Pop(self, x):
        return self.values.pop(0)

my_stack = Stack()

print(my_stack.values)
my_stack.Push(5)
my_stack.Push(5)
print(my_stack.values)