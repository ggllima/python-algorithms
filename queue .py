class Queue():
    def __init__(self, queue = []):
        self.queue = queue
        
    def push(self, element):
        self.queue = self.queue + [element]
        
    def pop(self):
        if len(self.queue):    
            new_queue = []
            for index in range(1,len(self.queue)):
                new_queue.append(self.queue[index])
            self.queue = new_queue.copy()
        return print("queue empty")