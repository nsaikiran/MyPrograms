"""
Given a stream of numbers, we are interested in most recent K numbers.
Queries on most recent K numbers: sum
"""

class CircularQueue:
    def __init__(self, K):
        self.queue = [None] * K #initialize array of required size.
        self.queue_size = K
        self.queue_item_count = 0
        self.running_sum = 0
    
    def enqueue(self, number):

    def dequeue(self): #next()

    def __str__(self):
        print(str(self.queue))
