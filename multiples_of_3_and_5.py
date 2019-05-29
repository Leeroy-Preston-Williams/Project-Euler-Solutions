# @Author:	Leeroy P. Williams
# @Date:	29/09/19
# @Problem:	If we list all the natural numbers below 10 that are
#           	multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#           	Find the sum of all the multiples of 3 or 5 below 1000 
# @Solution:	Correct

def multi(a, b, array):
    """
        Then print the sum of the multiples
    """
    MULTIPLES = []
    for i in array:
        if (i%a == 0) or (i%b == 0):
            MULTIPLES.append(i)
    print(sum(MULTIPLES))

if __name__ == "__main__":
    nums = [nums for nums in range(1, 1000)]
    a = 3
    b = 5
    multi(a, b, nums)
