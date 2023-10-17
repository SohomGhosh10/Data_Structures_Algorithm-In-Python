class Node: #creating a class of node
    def __init__(self , data , next = None): #constructor containing data and pointer to next node
        self.data = data # data
        self.next = next # next pointer
        
class linkedlist: # class for linkedlist
    def __init__(self): # constructor 
        self.head = None # Head is pointing to NULL
        
    def insert_at_beginning(self , data):
        node = Node(data , self.head) # creating a new node that will present before the head node
        self.head = node # linking the new node and head node
        
    def print(self): # function for printing linkedlist
        if self.head is None: # if head node is empty
            print("Linkedlist is empty")
            return
        else:
            itr = self.head
            llstr = ''
            while itr: # iterating the full list
                llstr += str(itr.data) # storing data
                itr = itr.next # iterate the next node
            print(llstr)
            
if __name__ == '__main__': # main function
    ll = linkedlist()
    # inserting the nodes
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.print() # printing the full list
