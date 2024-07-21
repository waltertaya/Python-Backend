class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            # self.head.next = newNode
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            
            lastNode.next = newNode
    
    def printList(self):
        if self.head == None:
            print('Singly linked list is empty')
            return
        currentNode = self.head
        while True:
            if currentNode == None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


if __name__ == '__main__':
    node1 = Node(10)
    node2 = Node('Brett')
    node3 = Node('Taya')
    print(node1)
    print(node2)
    print(node3)
    linkedList = LinkedList()
    linkedList.insert(node1)
    linkedList.insert(node2)
    linkedList.insert(node3)

    linkedList.printList()
