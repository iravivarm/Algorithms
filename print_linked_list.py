class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next



ll=LinkedList()
ll.head=Node(1)
second=Node(2)
third=Node(3)
fourth=Node(5)



ll.head.next=second
second.next=third
third.next=fourth

ll.printList()