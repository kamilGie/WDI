class node:
    def __init__(self, val):
        self.val = val
        self.next = None


    def contains(self, val):

        def rek(c_node, target):

            if c_node.val == val:
                return True

            if c_node.next is None:
                return False
            
            return rek(c_node.next, target)
        

        return rek(self, val)
    


    def add(self, val):

        def rek(c_node, val):

            if c_node.next is None:
                c_node.next = node(val)
                return "Added"
            
            rek(c_node.next, val)
        
        
        if not self.contains(val):
            rek(self, val)


    def remove(self, val):

        def rek(c_node, target):
            if c_node.next.val == target:
                c_node.next = c_node.next.next
        

        if self.contains(val):
            rek(self, val)
    
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

