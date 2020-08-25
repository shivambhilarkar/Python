# Problem Description
# Compute the nearest larger number by interchanging its digits updated.
# Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible print -1.

# Input Format
# 2 numbers a and b, separated by space.
# Output Format
# A single number greater than b.
# If not possible, print -1

# Constraints
# 1 <= a,b <= 10000000

# Example 1:

# Sample Input:

#     459 500

# Sample Output:
#     549

# Example 2:

# Sample Input:

#     645757 457765

# Sample Output:
#     465577




# #import itertools to get permutation function
# from itertools import permutations
# #take inputs
# num1 = int(input('Enter the 1st number :'))
# num2 = int(input('Enter the 2nd number :'))
# #initialize a flag variable
# flag = 0
# #convert num1 to string list
# num1 = list(str(num1))
# #sort the list
# num1 = sorted(num1)
# #find all permutations
# perm = permutations(num1) 
# #iterate through all permutations 
# for i in list(perm): 
#     #initialize an string
#     string = " "
#     #iterate through an string
#     for j in i:
#         string+=j
#     #typecast string to integer
#     #check for next greater value
#     if int(string) > num2:
#         #if True Change the flag variable 
#         #break the loop
#         flag = 1
#         break
# #check if the number is found or not
# if flag == 1:
#     print(string)
# else:
#     print(-1)




from itertools import permutations                          #import permutation module
n=int(input())                                              #first number
m=int(input())                                              #second number
grt_ele=[]
n=list(str(n))                                              #conver first number into list in string format
perm=list(permutations(n))                                  #calculate the permutations
res = list(map("".join, perm))                              #join the permutations
for i in res:
    if int(m)<int(i):
        grt_ele.append(i)                                   #store the element which are greater than  second number
print(min(grt_ele))                                         #print min num from the list of greter numbeers