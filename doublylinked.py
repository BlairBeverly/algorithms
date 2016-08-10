

class Node(object):
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode


class DoublyLinkedList(object):
    def __init__(self, head, tail):
        head.nextNode = tail
        tail.prevNode = head
        self.head = head
        self.tail = tail


    def addNode(self, node):
        self.tail.nextNode = node
        node.prevNode = self.tail
        node.nextNode = None

        
    def deleteNode(self, value):
        prevNode, node, nextNode = self.getNearbyNodes(value)
        prevNode.nextNode = nextNode
        if nextNode:
            nextNode.prevNode = prevNode
        else:
            self.tail = prevNode


    def insertNodeBetween(self, newNode, nodeValueBefore, nodeValueAfter):
        prevNode, node, nextNode = self.getNearbyNodes(nodeValueBefore)
        newNode.prevNode = node
        newNode.nextNode = nextNode
        node.nextNode = newNode
        nextNode.prevNode = newNode


    def getNearbyNodes(self, desiredNodeValue):
        node = self.head
        while True:
            if node.value == desiredNodeValue:
                return (node.prevNode, node, node.nextNode)
            if node.nextNode:
                node = node.nextNode
            else:
                break


    def printValues(self):
        node = self.head
        print node.value
        while node.nextNode:
            print node.nextNode.value
            node = node.nextNode
            

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
l = DoublyLinkedList(n1,n5)
l.insertNodeBetween(n2,1,5)
l.insertNodeBetween(n3,2,5)
l.insertNodeBetween(n4,3,5)
l.printValues()

print "\n"

l.deleteNode(3)
l.printValues()
