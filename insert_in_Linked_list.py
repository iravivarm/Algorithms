class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_num(self, head, val, pos):
        node=Node(self.val)
        if pos <= 0:
            node.next=head
            return head
        
            