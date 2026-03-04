import heapq

class TaskQueue:

    def __init__(self):
        self.priority_list = []
        self.cancelled_set = set()
        self.index = 0

    def add(self, name, priority):
        self.index += 1
        heapq.heappush(self.priority_list, (-priority, self.index, name)) # [name, -priority, status, status (False = run, True = cancel)]

    def clean(self):
        name =  self.priority_list[0][2]
        while self.priority_list and name in self.cancelled_set:
            self.cancelled_set.remove(name)
            heapq.heappop(self.priority_list)

    def next(self):
        self.clean()

        if self.is_empty():
            raise IndexError("Task queue is empty")
        
        next_val = heapq.heappop(self.priority_list)
        return next_val[2]
    
    def peek(self):
        self.clean()

        if self.is_empty():
            raise IndexError("Task queue is empty")
        
        return self.priority_list[0][2] # returns first item, third index (name)

    def cancel(self, name):
        for t in self.priority_list:
            if t[2] == name:
                self.cancelled_set.add(name)
                return True
        
        return False

    def is_empty(self):
        self.clean()
        return (len(self.priority_list) == 0) # true if 0, false otherwise


tq = TaskQueue()
tq.add("Fix login bug", 3)
tq.add("Update docs", 1)
tq.add("Deploy hotfix", 3)

print(tq.peek())   # → "Fix login bug"  (priority 3, added first)
print(tq.next())   # → "Fix login bug"  (removes it)
print(tq.next())   # → "Deploy hotfix"
print(tq.cancel("Update docs"))  # → True
print(tq.is_empty())  # → True
