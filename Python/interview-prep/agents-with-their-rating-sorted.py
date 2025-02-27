
"""
Imagine we have a customer support ticketing system. The system allows customers to rate the replies the support agent gives them out of 5. To start with, write a function which accepts a rating, and another which will tell me the average rating for each agent, ordered highest to lowest.
"""
import unittest

class RatingSystem:
    
    def __init__(self):
        self.map = dict()
   
    def record_review_for(self, name, rating):
        if rating not in range(1,6):
            raise ValueError("Range should be in 1 to 5")
        if name not in self.map:
            self.map[name] = (1, rating)
        else:
            self.map[name] = (self.map[name][0] +1, self.map[name][1] + rating)
    
  
    def average_reviews_of(self, name):
        if name in self.map:
            num_of_ratings, sum_of_ratings = self.map[name]
            return sum_of_ratings/num_of_ratings
        else:
            return None
        
    def agents_ordered_by_rating(self):
        all_agents_data = list()
        for name, rating in self.map.items():
            all_agents_data.append((name, rating))
        
        return sorted(all_agents_data, key= lambda item: item[1], reverse=True)
        

class unitTester(unittest.TestCase):
    
    def test_average_value(self):
        ratingSys = RatingSystem()
        ratings = [5,1,2,2,]
        for rating in ratings:
            ratingSys.record_review_for("sai", rating)
        actualRating = ratingSys.average_reviews_of("sai")
        expected_rating = sum(ratings)/len(ratings)
        self.assertEqual(actualRating, expected_rating)
    
    
    def test_agents_ordering(self):
        ratingSys = RatingSystem()
        ratingSys.record_review_for("sai", 4)
        ratingSys.record_review_for("kiran", 2)
        ratingSys.record_review_for("albert", 5)
        actual_result = ratingSys.agents_ordered_by_rating()
        self.assertEqual(actual_result[0][0], "albert")
        self.assertEqual(actual_result[1][0], "sai")
        self.assertEqual(actual_result[2][0], "kiran")
        
    def test_input_validation(self):
        ratingSys = RatingSystem()
        with self.assertRaises(ValueError):
            ratingSys.record_review_for("sai", 0)
        with self.assertRaises(ValueError):
            ratingSys.record_review_for("sai", 7)
        

unittest.main()
