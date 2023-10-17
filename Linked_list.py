class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self , data):
        node = Node(data , self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data)
                itr = itr.next
            print(llstr)
            
if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.print()