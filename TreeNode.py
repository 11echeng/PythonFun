class TreeNode:
    __data = None;
    __left = None;
    __right = None;

    def __init__(self, data, left, right):
        self.__data = data;
        self.__left = left;
        self.__right = right;

    def getRightChild(self):
        return self.__right;

    def setRightChild(self, right):
        self.right = right;

    def getLeftChild(self):
        return self.__left;

    def setLeftChild(self, left):
        self.__left = left;
        
    def getData(self):
        return self.__data;
        

#Implement MyList and MyTree using ListNode and TreeNode. Implement all of the functions that print "Implement".