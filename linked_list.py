#creat a node of linked list

#class whick represent the node of singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class represent the all the oprations of linked list

class Linkedlist:
    def __init__(self,):
        self.head = None

#this function add the node at the begining of the liked list
#this needs to hsndle two scenario/cases
# 1. when list is empty
# 2. list has some elements
    def  insert_at_beginning(self, data):
        #creat a new Node
        new_node = Node(data)

        #case 1; if the list is empty,make the new node as head
        if (self.head == None):
            self.head= new_node
            return

        # case 2: if the list is not empty , make the new node as head and point to the ald node
        new_node.next = self.head
        self.head = new_node
        return


#Drive code to test the above class

if __name__ == "__main__":
    #creat a new singly list
    list = Linkedlist()

    list.insert_at_beginning(10)
    list.insert_at_beginning(20)
    list.insert_at_beginning(30)

    print("List is Created succesfully ")
    print("head node  data is: ", list.head.data)
    print("next node data is: ", list.head.next.data)
    print("next node data is :", list.head.next.next.data)

        
            


# new_node = Node(10)
# print(new_node.data)