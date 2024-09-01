from collections import defaultdict

"""
Refer https://docs.python.org/3/reference/datamodel.html#emulating-container-types for more details.
Or look for dunder methods in python
"""
class MyCounter(defaultdict):
    def __init__(self):
        super().__init__(int)
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if not value: # or < 0
            self.pop(key, None)

if __name__=="__main__":
    a = MyCounter()
    a['a'] += 1
    a['b'] += 1
    print(a)
    a['a']  -= 1
    print(a) #shouldn't contain key 'a'