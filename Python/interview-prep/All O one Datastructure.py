"""
Problem: https://leetcode.doocs.org/en/lc/432/
Name: All O`one Data Structure
"""


class ListNode:
    def __init__(self, rank):
        self.rank = rank
        self.set_of_items = set()
        self.nextNode = None
        self.prevNode = None
    def add_item(self, item):
        self.set_of_items.add(item)
    def remove_item(self, item):
        #assumption is that the value exists, however adding this check
        if item in self.set_of_items:
            self.set_of_items.remove(item)
    def len_of_items(self):
        return len(self.set_of_items)
    
class AllOne:
    def __init__(self):
        self.head = ListNode(1)
        self.tail = self.head
        self.obj_map = dict()
    def inc(self, item):
        if item not in self.obj_map:
            if self.head.rank == 1:
                self.head.add_item(item)
                self.obj_map[item] = self.head
            else:
                head = ListNode(1)
                head.add_item(item)
                self.obj_map[item] = head
                #make this as head
                self.head.prevNode = head
                head.nextNode = self.head
                self.head = head
        else:
            representatvie_node = self.obj_map[item]
            if representatvie_node.nextNode:
                if representatvie_node.nextNode.rank == representatvie_node.rank + 1:
                    representatvie_node.remove_item(item)
                    representatvie_node.nextNode.add_item(item)
                    self.obj_map[item] = representatvie_node.nextNode
                    #clean the current node if no items
                    if representatvie_node.len_of_items() == 0:
                        #remove this from list
                        if representatvie_node.prevNode:
                            representatvie_node.prevNode.nextNode = representatvie_node.nextNode
                            representatvie_node.nextNode.prevNode = representatvie_node.prevNode
                        else:
                            self.head = representatvie_node.nextNode
                else:# key is greater than + 1
                    new_node = ListNode(representatvie_node.rank + 1)
                    temp = representatvie_node.nextNode
                    representatvie_node.nextNode = new_node
                    new_node.prevNode = representatvie_node
                    new_node.nextNode = temp
                    new_node.add_item(item)
                    self.obj_map[item] = new_node
                    self.tail = new_node
            else:
                new_node = ListNode(representatvie_node.rank + 1)
                representatvie_node.nextNode = new_node
                new_node.prevNode = representatvie_node
                new_node.add_item(item)
                self.obj_map[item] = new_node
                self.tail = new_node
    
    def dec(self, item):
        # key exists
        representatvie_node = self.obj_map[item]
        if representatvie_node.prevNode:
            if representatvie_node.prevNode.rank == representatvie_node.prevNode.rank - 1:
                representatvie_node.prevNode.add_item(item)
                representatvie_node.remove_item(item)
                self.obj_map[item] = representatvie_node.prevNode
            else:
                new_node = ListNode(representatvie_node.prevNode.rank - 1)
                new_node.add_item(item)
                self.obj_map[item] = new_node
                temp = representatvie_node.prevNode
                representatvie_node.prevNode = new_node
                new_node.nextNode = representatvie_node
                new_node.prevNode = temp
        else:
            new_node = ListNode(representatvie_node.rank - 1)
            new_node.add_item(item)
            self.obj_map[item] = new_node
            temp = representatvie_node.prevNode
            representatvie_node.prevNode = new_node
            new_node.nextNode = representatvie_node
            new_node.prevNode = temp
            self.head = new_node
        
    def getMaxKey(self):
        if self.tail.len_of_items() != 0:
            return list(self.tail.set_of_items)[0] # any element fromt hat set
        return ""
        
    def getMinKey(self):
        if self.head.len_of_items() != 0:
            return list(self.head.set_of_items)[0]
        return ""
        
"""
store = AllOne()
print(store.getMaxKey())
print(store.getMinKey())

store.inc("Sai")
#store.dec("Sai")
#store.inc("Sai")
#print(store.getMaxKey())
#print(store.getMinKey())
store.inc("Rajat")
#print(store.getMaxKey())
#print(store.getMinKey())
store.inc("Sai")
#store.inc("Rajat")
#store.inc("test")
#store.inc("test")
#store.inc("test")
print(store.getMaxKey())
print(store.getMinKey())

"""
store = AllOne()

store.inc("A")      # A -> 1
store.inc("B")      # B -> 1
store.dec("A")      # A -> 2
store.inc("C") 
store.dec("C")       # C -> 1
store.inc("C")      # C -> 2
store.dec("C")      # C -> 3

print("Max:", store.getMaxKey())  
print("Min:", store.getMinKey())   

store.dec("C")     
store.dec("A")     

print("After decrement:")
print("Max:", store.getMaxKey())   
print("Min:", store.getMinKey())   # Expected: A or B    


Rajat Saxena


