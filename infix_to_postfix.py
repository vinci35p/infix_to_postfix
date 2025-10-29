class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
    def print_stack(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            current = self.top
            print("Stack Elements (top --> bottom): ")
            while current:
                print(current.data)
                current = current.next

gamestack = Stack()
gamestack.push("Minecraft")
gamestack.push("Honkai Star Rail")
gamestack.push("Genshin Impact")
gamestack.push("Mobile Legends")
gamestack.pop()
print("Top Item: " + gamestack.peek())
gamestack.print_stack()