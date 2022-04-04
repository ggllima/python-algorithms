class Element():
    def __init__(self, priority, element):
        self.priority = priority
        self.element = element

    def get_element(self):
        return self.element
    
    def get_priority(self):
        return self.priority
    
class PriorityQueue():
    def __init__(self):
        self.queue = []
        self.size = 0
        
    def push(self, element):
        if self.empty():
            self.queue.append(element)
        else:
            flag_push = False
            for index in range(self.size):
                if self.queue[index].get_priority() < element.get_priority():
                    self.queue.insert(index, element)
                    flag_push = True
                    break
            if not flag_push:
                self.queue.insert(self.size, element)
        self.size+=1
        
    def pop(self, priority):
        for elem in self.queue:
            if elem.get_priority() == priority:
                indice = self.queue.index(elem)
                self.queue.pop(indice)
                    
    def empty(self):
        if not self.size:
            return True
        return False
    
    def show(self):
        for element in self.queue:
            print("%d %s"%(element.get_priority(), element.get_element()))
        