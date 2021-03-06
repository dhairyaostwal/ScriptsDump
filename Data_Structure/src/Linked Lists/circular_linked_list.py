#Another python program to implement and Insert a node by taking an pointer pointing to locations one want to insert a node to. 
#The insertion operations are carried out: 
#a. in empty linked list
#b. at beginning of the linked  list
#c. at end of the linked list
#d. in between the nodes

class Node: 

    def init(self, data): 

        self.data = data 

        self.next = None 

class CircularLinkedList: 

    def init(self): 

        self.last = None 

    # for empty list 

    def addToEmpty(self, data): 

        if (self.last != None): 

            return self.last 

        # Creating the newnode temp 

        temp = Node(data) 

        self.last = temp 

        # Create Link 

        self.last.next = self.last 

        return self.last 

    def addBegin(self, data): 

        if (self.last == None): 

            return self.addToEmpty(data) 

        temp = Node(data) 

        temp.next = self.last.next 

        self.last.next = temp 

        return self.last 

    def addEnd(self, data): 

          if (self.last == None): 

            return self.addToEmpty(data) 

        temp = Node(data) 

        temp.next = self.last.next 

        self.last.next = temp 

        self.last = temp 

        return self.last 

    def addAfter(self, data, item): 

        if (self.last == None): 

            return None 

        temp = Node(data) 

        p = self.last.next 

        while p: 

            if (p.data == item): 

                temp.next = p.next 

                p.next = temp 

                if (p == self.last): 

                    self.last = temp 

                    return self.last 

                else: 

                    return self.last 

            p = p.next 

            if (p == self.last.next): 

                print(item, "not present in the list") 

                break 

    def traverse(self): 

        if (self.last == None): 

            print("List is empty") 

            return 

        temp = self.last.next 

        while temp: 

            print(temp.data, end = " ") 

            temp = temp.next 

            if temp == self.last.next: 

                break 

if name == 'main': 

    llist = CircularLinkedList() 

    last = llist.addToEmpty(6) 

    last = llist.addBegin(4) 

    last = llist.addBegin(2) 

    last = llist.addEnd(8) 

    last = llist.addEnd(12) 

    last = llist.addAfter(10,8) 

    llist.traverse()
