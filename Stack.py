class stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.max_size
    
    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
        else:
            print("Stack Overflow")
            
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack Underflow")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None
        
    def size_stack(self):
        return len(self.stack)
    
    def display(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty")

# Example usage:
my_stack = stack(3)

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Top element:", my_stack.peek())  # 3
print("Size of stack:", my_stack.size_stack())  # 3

my_stack.display()  # Display all stack elements

print(my_stack.pop())  # 3 
print(my_stack.pop())  # 2

print("Top element:", my_stack.peek())  # 1
print("Size of stack:", my_stack.size_stack())  # 1

my_stack.display()  # Display remaining stack element
