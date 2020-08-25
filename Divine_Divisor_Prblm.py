# Problem Description
# Question -: Print a line containing all the divisors in increasing order separated by space.

# Input Format: The first line of input contains an integer ‘N’ denoting the number.

# Output Format: Print a line containing all the divisors in increasing order separated by space.

# Constraints:
# 1 <= N <= 10^8

# S.no	        Input	           Output	 
# 1	             10	               1 2 5 10

#how to find the divisir
#number is divisible by another number or not
# for i in range(1, number+1):
#     if number % i == 0:
#         print(i)


N = int(input("Enter the Number: \t"))
arr =[]
for i in range (1, N+1):
    if N % i == 0:
        arr.append(i)
print(arr)