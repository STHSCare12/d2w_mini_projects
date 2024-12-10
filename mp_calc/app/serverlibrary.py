import re

def merge(array: list, p: int, q: int, r: int, byfunc = None) -> list:
  n_left = q - p + 1
  n_right = r - q
  left = array[p:q+1]
  right = array[q+1:r+1]
  i = 0 #left
  j = 0 #right
  k = p
  if byfunc == None:
    while i < n_left and j < n_right:
      if left[i] <= right[j]:
        array[k] = left[i]
        i += 1
        k += 1
      else:
        array[k] = right[j]
        j += 1
        k += 1
    while i < n_left:
      array[k] = left[i]
      i += 1
      k += 1
    while j < n_right:
      array[k] = right[j]
      j += 1
      k += 1

  else:
      while i < n_left and j < n_right:
          if byfunc(left[i]) <= byfunc(right[j]):
              array[k] = left[i]
              i += 1
              k += 1
          else:
              array[k] = right[j]
              j += 1
              k += 1
      while i < n_left:
          array[k] = left[i]
          i += 1
          k += 1
      while j < n_right:
          array[k] = right[j]
          j += 1
          k += 1
  return array

def mergesort_recursive(array: list, p: int, r: int, byfunc) -> list:
  if r - p > 0:
    q = int((p+r) / 2)
    mergesort_recursive(array, p, q, byfunc)
    mergesort_recursive(array, q+1, r, byfunc)
    merge(array, p, q, r, byfunc)
  return array
 

def mergesort(array, byfunc=None):
  if byfunc==None:
      return mergesort_recursive(array, 0, len(array) - 1, byfunc)
  else:
      return mergesort_recursive(array, 0, len(array) - 1, byfunc)

class Stack:
  def __init__(self) -> None:
        self._Stack__items = []
        
  def push(self, item):
      self._Stack__items.append(item)

  def pop(self):
      pop_number = 0
      if len(self._Stack__items) == 0:
          pop_number = None
      else:
          pop_number = self._Stack__items.pop()
      return pop_number

  def peek(self):
      if len(self._Stack__items) == 0:
          return None
      else:
          return self._Stack__items[-1]

  @property
  def is_empty(self) -> bool:
      return len(self._Stack__items) == 0

  @property
  def size(self):
      return len(self._Stack__items)

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    if string == " " or not all(char in self.valid_char for char in string):
      self._expr = ""
    else:
      self._expr = string

  @property
  def expression(self):
    return self._expr

  @expression.setter
  def expression(self, new_expr):
    if new_expr == " " or not all(char in self.valid_char for char in new_expr):
      self._expr = ""
    else:
      self._expr = new_expr

  def insert_space(self):
    result = ' '.join(re.split(r'([+\-*/()])', self._expr))
    return result

  def process_operator(self, operand_stack, operator_stack) -> str:
    self.operand_stack = operand_stack #num
    self.operator_stack = operator_stack #symbol
    a = self.operand_stack.pop()
    b = self.operand_stack.pop()
    op = self.operator_stack.pop()
    if op == '+':
      self.operand_stack.push(b + a) 
    if op == '-':
      self.operand_stack.push(b - a) 
    if op == '*':
      self.operand_stack.push(b * a) 
    if op == '/':
      self.operand_stack.push(b // a) 

  def evaluate(self):
    self.operand_stack = Stack()
    self.operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()    

    #Phase 1
    for i in tokens:
      if i.isnumeric():
        self.operand_stack.push(int(i))
      elif i in '*/+-':
        while(not self.operator_stack.is_empty and self.operator_stack.peek() != '(' and self.operator_stack.peek() in '*/'): 
          self.process_operator(self.operand_stack, self.operator_stack)
        self.operator_stack.push(i)
        
      elif i == '(':
        self.operator_stack.push(i)
      elif i == ')':
        while(self.operator_stack.peek() != '('):
          self.process_operator(self.operand_stack, self.operator_stack)
        self.operator_stack.pop()
    
    #Phase 2
    while(not self.operator_stack.is_empty):
      self.process_operator(self.operand_stack, self.operator_stack)
    return self.operand_stack.peek() 


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





