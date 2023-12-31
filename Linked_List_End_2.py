class Node:
    def __init__(self , data = None , next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_At_Beginning(self , data):
        node = Node(data , self.head)
        self.head = node
      
    def print(self):  
        if self.head is None:
            print("NULL")
            return
        else:
            itr = self.head
            llstr = ''
            
            while itr:
                llstr += str(itr.data)
                itr = itr.next
            
            print(llstr)

    def insert_At_End(self , data):
        if self.head is None:
            self.head = Node(data , None)
            return
        else:
            itr = self.head
            
            while itr.next:
                itr = itr.next
                
            itr.next = Node(data , None)
                        
    def insert_data(self , data_list): # function for inserting whole data list
        if self.head is None:
            for data in data_list: # Traversing the whole list
                self.insert_At_End(data) # Inserting the list at the end
                
if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_data(["Banana" , "Apple" , "Grape"])
    ll.print()
