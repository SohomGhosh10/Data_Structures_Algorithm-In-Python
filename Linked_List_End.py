class Node: #Class of Node
    def __init__(self , data = None , next = None): # Constructor containing data and next pointer
        self.data = data #data
        self.next = next #pointer to next node
    
class Linkedlist: #Class of linkedlist
    def __init__(self): #Constructor
        self.head = None #head pointer pointing to NULL.
    
    def insert_At_begining(self , data): #Function for insert at beginning
        node = Node(data , self.head) # new node is before head node
        self.head = node # linking the nodes
    
    def print(self):  # function for printing the linkedlist
        if self.head is None: # if head pointer is pointing NULL
            print("NULL")
            return 
        else:
            # Iteration
            itr = self.head # itr pointing to head
            llstr = '' 
            while itr:
                llstr += str(itr.data)
                itr = itr.next
            print(llstr)
            
    def insert_At_End(self , data): #function for insert at end
        if self.head is None:
            self.head = Node(data , None) # head is linking to new node and new node is linked to NULL
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data , None)
            
            
if __name__ == '__main__': #main function
    ll = Linkedlist()
    # Node insertion
    ll.insert_At_begining(18)
    ll.insert_At_begining(45)
    ll.insert_At_End(60)
    ll.print()
                
                
                
                
            
        
        
        
    
