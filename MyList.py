from ListNode import ListNode

class MyList:
    __start = None;
    __end = None;
    __length = None;

    def __init__(self):
       self.__length = 0;

    def push_back(self, data): #runs in constant time. # this is append
        if (self.__start is None): # checks to see if there is no node out there aka none
            self.__start = ListNode(data, None, None); # we just created a new node and assigned start to that node.
            self.__end = self.__start;# set the start and end to the existing Node as shown line above(is this correct?)
        else:
            newNode = ListNode(data, None, self.__end); # if there is already a node out there, we assign a new node called newnode. the end points to that
            self.__end.setNext(newNode);# using pattern below but unclear
            self.__end = newNode #see line 26
        print("Implement Push_back")

    def push_front(self, data): #runs in constant time
        if (self.__start is None): # checks to see if there is no node out there aka none
            self.__start = ListNode(data, None, None);# we just created a node and assigned the start to it.
            self.__end = self.__start; # see line 12.
        else: 
            newNode = ListNode(data, None, self.__start);# if there is already a node out there we create a new node and we assign it start to it because we push to the front.
            self.__start.setPrevious(newNode); # because this node will be in front, and start is the exisiting node, we set the new start to the previous node we just created above.
            self.__start = newNode; #assign self.__start to newnode. !!!Confused- why do i need line 25 then...
            
        print("Implement push_Front")


    #if you had insert(3, data) i want to start with the data to become the third node of the list. so what is the third node of the list and then assign data into third node.
    def insert(self, index, data): #runs in O(n) time. #we are inserting the data at the index you assign to. 
        newNode = ListNode(data, None, None);
        itrNode = self.__start;
        counter = 1;
        while ( counter < index): # we are going to loop based on where we want to insert the new node
            itrNode = self.__start.getNext(); # this iteraters through each node
            counter = counter + 1 # we are keeping track of whwere the index is in the linked list.
        
        if (index == 0):
            self.push_front(data)
        elif (index > self.__length):
            self.push_back(data)
        else:
        #A in the code will be itrNode
        #B in the code will be itrNode.getPrevious();
            A = itrNode;
            B = itrNode.getPrevious();
            newNode.setPrevious(B)
            newNode.setNext(A)
            B.setNext(newNode)
            A.setPrevious(newNode)
    

    def get(self, index): #runs in O(n) time. # we are getting the specific node? EG : we are trying to get index node, or lets say 3
        if (self.__start is None ): # checks to see if there is even a start to begin with
            return None;
        else:
            i = 0; # set to 0
            tempNode = self.__start; 
            while ( i < index ):
                tempNode = tempNode.getNext();
                i = i + 1;
            return tempNode
        print("Implement")

    def length(self): #runs in constant time.
        counter = 0;
        tempNode = self.__start
        while (tempNode.getNext() != None):
            tempNode = tempNode.getNext();
            counter = counter + 1       
        self.__length = counter
        return counter            

    def print(self): #runs in O(n) time. Prints all the data in the list with a space in 
        if (self.__start is None):
            return None;
        else:
            tempNode = self.__start
            templist = []
            while(tempNode.getNext() != None):
                templist = tempNode
                tempNode = tempNode.getNext
        print(*templist)

list = MyList();
list.push_back(10);
list.push_back(20);
list.push_back(30);
list.push_back(40);
list.push_front(5);
list.get(3);
list.print();
list.length();