# Queue class - Save this as quel.py
class Queue:
    def __init__(self):
        self.qu = []
    
    def isempty(self):
        return self.qu == []

    def add(self, element):
        self.qu.append(element)

    def delete(self):
        if self.isempty(): 
            return -1
        else:
            return self.qu.pop(0)
        
    def search(self, element):
        if self.isempty():
            return -1 
        else:
            try:
                n = self.qu.index(element)
                return n+1
            except ValueError:
                return -2
    
    def display(self):
        return self.qu 
