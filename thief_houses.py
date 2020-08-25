# this code is not correct

# Problem Description
# Question:- There are n houses build in a line, each of which contains some value in it.

#  A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two neighbours left and right side.

# What is the maximum stolen value?

# Sample Input: val[] = {6, 7, 1, 3, 8, 2, 5}

# Sample Output: 20


num = list(map(int, input().split()))
sum = num[0]
for i in range(0, len(num)//2):
    sum = sum + int(num[i])
print(sum)