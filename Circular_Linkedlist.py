class Node:
    def __init__(self, data): # Constructor
        self.data = data # data declaration
        self.next = None # Node declaration


class CircularLinkedList:
    def __init__(self): # constructor
        self.head = None

    def is_empty(self): # Queue empty condition
        return self.head is None

    def append(self, data): # Enqueue condition
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head # Nodes linking
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self): # function to print
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print()


# Example usage:
if __name__ == "__main__": # main function
    ll = CircularLinkedList()

    # Appending the datas in the queue
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("Circular Linked List:") # printing the datas
    ll.display()
