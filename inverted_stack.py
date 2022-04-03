class Stack():
    def __init__(self, stack_list = [], bark = []):
        self.stack_list = stack_list
        self.bark = bark
        
    def empty(self):
        if not self.stack_list:
            return True
        return False
        
    def push(self, element):
        self.bark = self.stack_list + [element]
        self.stack_list = self.bark
        return self.stack_list

        
    def pop(self):
        if self.empty() == True:
            print("Empty list")
        else:
            new_list = []
            index = 1
            first = self.stack_list[0]
            while index < len(self.stack_list):
                new_list.append(self.stack_list[index])
                index+=1
            self.stack_list = new_list.copy()
            return first
    
    def top(self):
        if self.empty() == True:
            print("Empty list")
        else:
            return self.stack_list[0]
        
    def inverted_stack(self):
        index = 1
        new_list = []
        while index <= len(self.stack_list):
            new_list.append(self.stack_list[len(self.stack_list)-index])
            index+=1
        self.stack_list = new_list
        return self.stack_list
    
list_of_stacks = []
number_of_tests = int(input())
for test in range(number_of_tests):
    s = Stack()
    list_of_stacks.append(s)
    number_of_elements = int(input())
    for index in range(number_of_elements):
        element = int(input())
        s.push(element)
        
for stack in list_of_stacks:
    stack.inverted_stack()
    for value in stack.stack_list:
        print(value)
    if list_of_stacks.index(stack) != len(list_of_stacks) - 1:
        print("")