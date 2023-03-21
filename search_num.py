class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self, head):
        self.head=None
    def search_num(self,B):
        current=self.head
        while current:
            if current.val==B:
                return 1
            current =current.next
        return 0

