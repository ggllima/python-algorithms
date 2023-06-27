class Element():
    def __init__(self, priority, element = ''):
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
    
    def return_objs(self):
        return self.queue
            

            
    def count_time(self, chosen_priority):
        objects = self.queue.copy()
        objects.reverse()
        for obj in objects:
            if obj.get_priority() ==  chosen_priority:
                indice = objects.index(obj)
        return len(objects) - indice
        
        
        
tests = int(input())
for test in range(tests):
    p = PriorityQueue()
    jobs, position = map(int, input().split())
    priority = [int(priority) for priority in input().split(" ")]
    for job in range(jobs):
        e = Element(priority[job])
        p.push(e)
objs = p.return_objs()
print(p.count_time(objs.index(objs[position])))
