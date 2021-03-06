
class Node:
    #node is the data inside the linked list
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

    #method insert beg
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked is empty")
            return 
        
        #else
        itr = self.head #temp var for head
        llstr=''

        #this loop the data and print it as str
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


    def insert_at_end(self,data):
        #if the linked list is blank, put the data inside the head
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        #keep iteration till the end
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)


    #insert list of values(data_list) and turn into new linkedList
    def insert_values(self,data_list):
        self.head = None
        
        #using insert_at_end method 
        for data in data_list:
            self.insert_at_end(data)


    #get lenght of the linkedList
    def get_length(self):

        count = 0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,index):
        #check if the index is negative or exceed len LinkedList
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        #if zero the , appoint the next data
        if index==0:
            #point at the next element of 0
            self.head = self.head.next
            return 

        count=0
        itr = self.head
        while itr:
            #the data before the index (beforedata == index-1)
            if count == index-1:
                #skipped the remove index data 
                itr.next = itr.next.next
                break  
            itr = itr.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        #index at 0 use insert beg method
        if index ==0:
            self.insert_at_beginning(data)
            return
        
        count=0
        itr = self.head
        while itr:
            #check the before data the index
            if count == index-1:
                #put the new data , in between those two 
                node = Node(data,itr.next)
                itr.next = node

            itr= itr.next
            count+=1

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(100)
    ll.insert_values(['banana','mangoes','grapes','orange'])
    ll.print()
    print("Lenght of the LinkedList:",ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(0,"figs")
    ll.print()








