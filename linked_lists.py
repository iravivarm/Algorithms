###Initializing the nodes#######

from xxlimited import new


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_List:
    #######this will add the head to the nodes#########
    def __init__(self):
        self.head = None

    ######Insertion of a Linked List#######
    def insertionatEnd(self, insertingNum):
        newNode=Node(insertingNum)
        ##check head is there or not.If not make current node as the head.

        if self.head is None:
            self.head=newNode
            return
        last = self.head
        while(last.next):
            last= last.next

        last.next=newNode

    #########Insertion at begining of the Node
    def atBegining(self, newnum):
        new_node=Node(newnum)

        new_node.next=self.head
        self.head=new_node

        #############Traversing the linked list
    def traverse_linkedList(self):
        currentHead=self.head
        while (currentHead):
            print(currentHead.data)
            currentHead=currentHead.next



        
      
    
nodes = Linked_List()
nodes.head=Node(4)
node1=Node(5)
node2=Node(6)

nodes.head.next=node1;
node1.next=node2;
nodes.atBegining(28)
nodes.atBegining(30)
nodes.insertionatEnd(25)
nodes.insertionatEnd(26)
nodes.insertionatEnd(27)

nodes.traverse_linkedList()

