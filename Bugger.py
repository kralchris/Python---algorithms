"""
My solution to : https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python

"""


def persistence(n):

    if n < 10:
        return 0
    
    num_str = str(n)    
    persistence_count = 0
    product = 1
    
    while len(num_str) > 1:
        for digit in num_str:
            product *= int(digit)
        
        persistence_count += 1
        num_str = str(product)        
        product = 1
    
    return persistence_count
