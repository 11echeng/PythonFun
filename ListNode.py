class ListNode:
    __data = None;
    __next = None;
    __previous = None;

    def __init__(self, data, previous, next):
        self.__data = data;
        self.__next = next;
        self.__previous = previous;

    def getPrevious(self):
        return self.__previous;

    def setPrevious(self, previous):
        self.__previous = previous;
        
    def getNext(self):
        return self.__next;

    def setNext(self, next):
        self.__next = next;

#Implement MyList and MyTree using ListNode and TreeNode. Implement all of the functions that print "Implement".