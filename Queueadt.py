class Queue:
  def __init__(self, cap=5):
      self._a = [None for _ in range(cap)]
      self._front = 0
      self._rare = -1
      self._c = 0

  def peek(self):
      if self._c == 0:
          return "No elements"
      return self._a[self._front]

  def enqueue(self, data):
    if self._c==len(self._a):
      print('overflow')
      return
      
    self._rare = (self._rare + 1) % len(self._a)
    self._a[self._rare] = data
    self._c += 1
  
  def dequeue(self):
    if self._c == 0:
      print('underflow')
      return
      
    data = self._a[self._front]
    self._a[self._front] = None
    self._front = (self._front + 1) % len(self._a)
    self._c -= 1
    return data
  
  def rare(self):
    if self._c == 0:
        return "No elements"
    return self._a[self._rare]   


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.peek())    
print(queue.dequeue()) 
print(queue.peek())    
print(queue.rare())    
