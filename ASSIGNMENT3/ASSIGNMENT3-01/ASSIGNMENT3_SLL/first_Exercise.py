class ListNode():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class SinglyLinkedList():
    def __init__(self,head = None,tail= None,size = None):
        self._head = head
        self._tail = tail
        self._size - size
    def __iter__(self):
        self._iter_index = self._head
        return self
    def __len__(self):
        return self._size
    def __next__(self):
        if self._iter_index:
            val = self._iter_index.data
            self._iter_index = self._iter_index.next
            return val
        else:
            raise StopIteration
    def __getitem__(self,index):
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def __setitem__(self,index,val):
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = val
    
    def __repr__(self):
        current_node = self._head
        values = ""
        while current_node:
            values += f",{current_node.data}"
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'
        
    def insert_left(self,val):
        """
        This method is used to append the given value at the begening of the list node        
        """
        new_node = ListNode(val)
        if self._size == 0:
            new_node.next = null
            self._head = self._tail = new_node
        else:
            old_head = self._head
            self._head = new_node
            new_node.next = old_head
            self._tail = self._tail
        size +=1
    