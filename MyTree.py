from TreeNode import TreeNode;

class MyTree:
    __root = None;

    #Completed - Responsibe for creating a new node / self.__root declared and assigned OR adds newnode to an existing self.__root. 
    def append(self, data):#add
        newNode = TreeNode(data, None, None);#create new node

        if self.__root is None:# If there is no root assigned yet,
            self.__root = newNode;# set root to newNode
        else: #root already exists, self.__root,
            self.__appendHelper(self.__root, newNode);#root exist - Call Next Helper Function - Takes 2 Parameters (self.__root, newNode)

    #Completed - Assigning the Newnode if self.__root already exists based on the self.__root size. Recursive. 
    def __appendHelper(self, currentNode, newNode): #HelperFunction - rootNode and newNode
        if newNode.getData() < currentNode.getData():# if the newNode data is smaller than the self.__root data then:
            if ( currentNode.getLeftChild() is None ): #if the left child of self.__root is empty then
                currentNode.setLeftChild(newNode); #self.__root's left child has been assigned with the data in newNode
            else:
                self.__appendHelper( currentNode.getLeftChild(), newNode); #if the left child is taken for that element recall appendHelper and repeat the process till you find the empty left child.
        else: # if the newNode is greater than the self.root data then: -> we are going to assign the element to the right child
            if ( currentNode.getRightChild() is None): #if the right child of self.__root is empty then
                currentNode.setRightChild( newNode ); #set the newNode data to the right child of self.__root
            else:
                self.__appendHelper( currentNode.getRightChild(), newNode);# if the right child of the self.__root is takken, we will set this right child of the self.__root to be the new self._root.

    #Calls printLinearHelper(self.__root)
    def printLinear(self):
        self.__printLinearHelper(self.__root);

    #PrintHelp Function - looking for an empty left/Sright child node in a self.__root. Once found it gets the data of the self.__root
    def __printLinearHelper(self, currentNode):#calls currentNode which is self.__root
        if ( currentNode.getLeftChild() is not None ): # if the self.__root's left child element exist (so there is data in the child of the element of self.__root)
            self.__printLinearHelper(currentNode.getLeftChild()); #recursive- reiterates back starting with the self.__root's left child

        print( currentNode.getData()); # get the data of the self.__root which has the empty left child 

        if ( currentNode.getRightChild() is not None ):# if the self.__root's right child element exist
            self.__printLinearHelper(currentNode.getRightChild()); #recursive - reiterates back startingw ith the self.root's right child
     
    
    def find(self, data): #passes in the data 
        return self.__findHelper(self.__root, data); #passes the root and the data into the function findHelper

    #Responsible for: Checking to see if a data being passed through exist in the TreeNode. 
    def __findHelper(self, currentNode, data):#self.__root node and the data
        if currentNode is None: # if the self._root is empty. This is important because it keeps drilling down from the top to bottom. If data does not exist it will return false after recusively going through all childs/elements.
            return False;

        if currentNode.getData() == data: # if the self.__root data is equal to the data being passed through
            return True;
        else:
            if ( data < currentNode.getData() ): #if the data being pass through is < then the self.__root data then...see below
                return self.__findHelper(currentNode.getLeftChild(), data ); # recursive- reiterates back starting with the self.__root data working it's way down.
            else:
                return self.__findHelper(currentNode.getRightChild(), data); # recursive- reiterates back starting with the self.__root data otw down.


    #grabs the child elements of each node in the given level that is being passed through
    def __getNextLevelFromCurrentLevel(self, currentLevel):
        nextLevel = [];#create an empty list called nextLevel for storage

        for node in currentLevel:#for each node in the current level that is being passed through: 
            if node is None: #if node is empty
                nextLevel.append(None); # add None as the child element
                nextLevel.append(None); # add None as the child element
            else: # if node is not empty and has data
                nextLevel.append ( node.getLeftChild()); # add the left child of the node in the current level
                nextLevel.append ( node.getRightChild());# add the right child of the node in the current level

        return nextLevel; 

    #This is responsible for returning True when there is a Node that has an empty field in the given level that is has been assigned.
    def __allNodesNone(self, level): 

        for node in level:# for node in level
            if node is not None: # if node is not empty , return false 
                return False;

        return True;

    #returns all the levels 
    #REVISIT THIS FUNCTION
    # we are adding each TreeNode object into allLevels - This includes data and None 
    def __getAllLevels(self):
        allLevels = []; #create an empty list called allLevels

        currentLevel = [ self.__root]; # set the self.__root, currentnode, to currentLevel

        while ( not self.__allNodesNone( currentLevel ) ): #?
            allLevels.append(currentLevel);
            currentLevel = self.__getNextLevelFromCurrentLevel(currentLevel);

        return allLevels;


    #This function is responsible for creating strings when a node is empty
    #if data of the node is < 10, print 2 spaces, if its less than 10, print 1 space. 
    def __getStringNode(self, node):
        if node is None:#if node is empty -> create 4 empty spaces
            return "     ";
        else:
            if ( node.getData() < 10 ): # hardcode 10
                return "  " + str ( node.getData() ) + "  "; # the string value of data w/ 2 spaces
            else:
                return "  " + str ( node.getData() ) + " "; # the string value of data w/ 1 space

     
    #actual data in the node
    # this is responsible for consolidating all the data values into string type from (getstringnode) for the level that is being passed throughl
    def __getStringLevel(self, level):
    #This is responsible for getting the number of values per level conslidated.
        levelString = ""; #string
        for node in level: # for each node in the given level that is being passed through
            levelString = levelString + self.__getStringNode(node); # we are passing through the function that gets the data of the node into a string, but for the all nodes in the given level

        return levelString; # the ful value for the given level
    def __getALlLevelsString(self, allLevels):
        totalOutput = ""; #string
        for level in allLevels: # for each level in all the levels available
            totalOutput = totalOutput + self.__getStringLevel(level) + "\n";#get the number of values in string value

        return totalOutput;

    def prettyPrint(self):
        allLevels = self.__getAllLevels(); # see functino above
        updatedLevels = []; # populate this list for each node in level
        ncount = 1;
        for currentLevel in reversed( allLevels ): # for each level in all the levels in the treenode
            updatedLevel = []; #

            for node in currentLevel: # for eaach node in the level
                counterA = ncount - 1; # 0, ->
                counterB = ncount;     #  1,  ->

                while ( counterA > 0 ): # if counterBerfore > 0 
                    updatedLevel.append(None); # updatedLevel adds none when CB is greater than 0
                    counterA = counterA -1; # -1

                updatedLevel.append( node ); #assign the node data value into updatedLevel

                while ( counterB > 0 ):
                    updatedLevel.append(None); # see above
                    counterB = counterB - 1;# see above


            updatedLevels.append(updatedLevel);
            ncount = ncount * 2;

        updatedLevelStrings = self.__getALlLevelsString(reversed(updatedLevels));

        print( updatedLevelStrings);




tree = MyTree();



tree.append(18)
tree.append(16);
tree.append(14);
tree.append(13);
tree.append(11);
tree.append(9);
tree.append(7);
tree.append(5);
tree.append(3);
tree.append(2);
tree.append(1);


#tree.printLinear();
tree.prettyPrint();
#tree.printLinear();