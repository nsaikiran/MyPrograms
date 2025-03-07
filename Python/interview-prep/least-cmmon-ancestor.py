
"""
Input Target employees - Lisa, Marley 

Output: FE 

Input Target employees - Alice, Marley 

Output: Engg 

Input Target employees - Mona, Lisa, Bob

Output


Imagine you are the team that maintains the Atlassian employee directory. 
At Atlassian - there are multiple groups, and each can have one or more groups. Every employee is part of a group.
You are tasked with designing a system that could find the closest common parent group  given a target set of employees in the organization.
"""

#from collections import namedtuple

#Node = namedtuple("Node", 'name', 'children')

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = list() # list of Nodes.


class DepartmentBook:
    def __init__(self, root):
        self.root = root
        self.lookup_leaves = dict()
        self.pre_process()
    
    # class method
    def dfs_look_up(self, node):
        if not node.children:
            self.lookup_leaves[node.name] = node #assuming names are distict.
            return
        else:
            for child in root.children:
                self.dfs_look_up(child)
                
    def path_to_root(self, node):
        path = []
        while node:
            path.append(node.name)
            node = node.parent
        return path

    def pre_process(self):
        for child in root.children:
            self.dfs_look_up(child)
            
            
    def common_department(self, list_of_employees):
        emp_objs = []
        for emp in list_of_employees:
            if emp in self.lookup_leaves:
                emp_objs.append(emp)
            else:
                raise ValueError("Invalid input")
        paths = dict()
        for obj in emp_objs:
            paths[obj.name] = reversed(self.path_to_root(obj)) # c, HR, Mona
        
        for path
        """
        Find the common prefix of the paths and last of the common prefix is the common root. Wrote code only till here. Explained interviewr
        """
        

root = Node("Company")
emp1= "Bob"
emp2= "Mona"

lookup_helper = DepartmentBook(root)


lookup_helper.common_department(emp1, emp2)
