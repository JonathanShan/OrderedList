class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        if self.dummy.next == self.dummy:
          return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        temp = Node(item)
        cur = self.dummy.next
        while cur != self.dummy and item > cur.item:
          cur = cur.next
        if item == cur.item:
          return None
        temp.next = cur
        temp.prev = cur.prev
        cur.prev.next = temp
        cur.prev = temp



    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        start = self.dummy.next
        while start != self.dummy:
          if item == start.item:
           start.prev.next = start.next
           start.next.prev = start.prev
           return True
          start = start.next
        return False


    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        start = self.dummy.next
        count = 0
        while start != self.dummy:
          if item == start.item:
            return count
          start = start.next
          count += 1
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if not index < self.size():
          raise IndexError
        count = 0
        start = self.dummy.next
        while count != index:
          start = start.next
          count += 1
        if self.remove(start.item):
          return start.item

    def _search(self, item, node):
        if node.item == item:
            return True
        elif node.next.item == None:
            return False
        else:
            return self._search(item, node.next)

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self._search(item, self.dummy.next)
    


    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        start = self.dummy.next
        returnlist = []
        while start != self.dummy:
          returnlist.append(start.item)
          start = start.next
        return returnlist

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        start = self.dummy.prev
        returnlist = []
        while start != self.dummy:
          returnlist.append(start.item)
          start = start.prev
        return returnlist

    def _size(self,node):
      if node == self.dummy:
        return 0
      return 1 + self._size(node.next)
      
    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self._size(self.dummy.next)