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

# Infix to postfix conversion

def ranking(oper):
    if oper == '+' or oper == '-':
        return 1
    if oper == '*' or oper == '/':
        return 2
    if oper == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    output = ""
    stack = Stack()

    for char in expression:
        if char.isalnum():
            output += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() is not None and stack.peek() != '(':
                output += stack.pop()
            stack.pop()
        else:
            while (not stack.is_empty() and ranking(stack.peek()) >= ranking(char)):
                output += stack.pop()
            stack.push(char)

    while not stack.is_empty():
        output += stack.pop()

    return output

