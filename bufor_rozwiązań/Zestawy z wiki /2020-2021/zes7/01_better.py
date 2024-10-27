class node:
    def __init__(self, val):
        self.val = val
        self.next = None


    def contains(self, val):

        c_node = self

        while c_node.next is not None:
            if c_node.val == val:
                return True
        
        return False
            


    def add(self, val):

        if self.contains(val):
            return "Already there"

        
        c_node = self
        
        while c_node.next is not None:
            c_node = c_node.next
        
        
        c_node.next = node(val)

        return "Added"


    def remove(self, val):
        if self.val == val:
            self = self.next
            return "Removed"

        c_node = self

        while c_node.next is not None and c_node.next.val != val:
            c_node = c_node.next
        

        if c_node.next.val == val:
            after = c_node.next.next
            del c_node.next
            c_node.next = after
            return "Removed"
        else:
            return "Not there"


    
    def __str__(self):
        a = self
        ans = ""
        while a.next is not None:
            # yield str(a.val) + " "
            ans += str(a.val) + " "
            # print(a.val, end=" ")
            a = a.next
        
        return ans


my_set = node(5)
my_set.add(7)
my_set.add(9)
my_set.add(234)
my_set.add(7)
my_set.add(-3)

print(my_set)

