# A Naive recursive solution 
# for Rod cutting problem 
import sys 

# function to get the maximum of two integers 
def max(a, b): 
	return a if (a > b) else b 
	
# Returns the best obtainable price for a rod of length n 
# and price[] as prices of different pieces 
def cutRod(price, n): 
	if(n <= 0): 
		return 0
	max_val = -sys.maxsize-1
	
	# Recursively cut the rod in different pieces 
	# and compare different configurations 
	for i in range(0, n): 
		#print(max_val)
		max_val = max(max_val, price[i] +
					cutRod(price, n - i - 1)) 
	return max_val 

# Driver code 
#arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = int(input("enter the length of rod "))
arr = input("Insert price of pieces of rod in incresing order")
#size = int(input("enter the length of rod "))
#arr = list(map(int, input("Insert price of pieces of rod in incresing order ").split(' ')))
#size = len(arr) - 1

print("Maximum Obtainable Value is ", cutRod(arr, size)) 

