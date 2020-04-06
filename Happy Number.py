"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
"""

# Example 1
# Input: 19
# Output: true

# storing single digit != 1
num_history = []

def isHappy(n):
	# input: n->int
	# output: bool
	if len(str(n)) == 1:
		if n in num_history:
			return False

		elif n not in num_history:
			if n==1:
				return True

			else:
				num_history.append(n)
				return isHappy(make_reduce(n))
	
	else:
		return isHappy(make_reduce(n))



def make_reduce(n):
	num_lst = list(str(n))
	num_lst = [int(num)**2 for num in num_lst]
	return sum(num_lst)


if __name__ == "__main__":
	print 'Execute input n=19:: ', isHappy(19)
	print 'Execute input n=34:: ', isHappy(34)