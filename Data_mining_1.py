"""
My solution to : https://www.codewars.com/kata/58f89357d13bab79dc000208/python
"""

import math

class Datamining:
    
    def __init__(self, train_set):
        self.x = [p[0] for p in train_set]
        self.y = [p[1] for p in train_set]
        self.mean_x = sum(self.x) / len(self.x)
        self.mean_y = sum(self.y) / len(self.y)
        self.m = sum([(self.x[i] - self.mean_x) * (self.y[i] - self.mean_y) for i in range(len(self.x))]) / sum([(x - self.mean_x) ** 2 for x in self.x])
    def predict(self, x):
        return self.mean_y + self.m * (x - self.mean_x)



"""
Sample test cases:


Test.describe("Sample tests")
example_train_set = [(0, 1),
    (2, 2),
    (4, 3),
    (9, 8),
    (3, 5)
]

dm = Datamining(example_train_set)
predicted = [dm.predict(point[0]) for point in example_test_set]
Test.assert_equals(test_prediction(predicted), True)
"""
