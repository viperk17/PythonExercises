# """
# Chef decided to write an infinite sequence. Initially, he wrote 0

# , and then he started repeating the following process:

#     Look at the last element written so far (the l

# -th element if the sequence has length l so far); let's denote it by x
# .
# If x
# does not occur anywhere earlier in the sequence, the next element in the sequence is 0
# .
# Otherwise, look at the previous occurrence of x
# in the sequence, i.e. the k-th element, where k<l, this element is equal to x and all elements between the k+1-th and l−1-th are different from x. The next element is l−k, i.e. the distance between the last two occurrences of x

#     .

# The resulting sequence is (0,0,1,0,2,0,2,2,1,…)
# : the second element is 0 since 0 occurs only once in the sequence (0), the third element is 1 since the distance between the two occurrences of 0 in the sequence (0,0) is 1, the fourth element is 0 since 1 occurs only once in the sequence (0,0,1)

# , and so on.

# Chef has given you a task to perform. Consider the N
# -th element of the sequence (denoted by x) and the first N elements of the sequence. Find the number of occurrences of x among these N

# elements.
# Input

#     The first line of the input contains a single integer T

# denoting the number of test cases. The description of T
# test cases follows.
# The first and only line of each test case contains a single integer N

#     .

# Output

# For each test case, print a single line containing one integer ― the number of occurrences of the N

# -th element.
# Constraints

#     1≤T≤128

# 1≤N≤128

# Subtasks

# Subtask #1 (30 points): 1≤N≤16

# Subtask #2 (70 points): 1≤N≤128

# Example Input

# 1
# 2

# Example Output

# 2

# Explanation

# Example case 1: The 2
# -nd element is 0. It occurs twice among the first two elements, since the first two elements are both 0.
# """

# # for i in range(int(input())):
# #     n = int(input())
# #     index=[-1]*10000
# #     count=[0]*10000
# #     a=[0]*n
# #     j=0
# #     while(j<n-1):

# #         if(index[a[j]]==-1):

# #             # print(j+1)
# #             a[j+1]=0
# #         else:
# #             ans = j-index[a[j]]
# #             # print(j,index[a[j]])
# #             a[j + 1] = ans
# #         index[a[j]] = j
# #         j += 1

# #     print(a.count(a[n-1]) )



# # n = int(input())
# # for num in range(n):
# #     if num%5==0 and num %3==0:
# #         print("Fizz Buzz")
# #         continue
# #     elif num % 5 == 0:
# #         print("Buzz")
# #         continue
# #     elif num % 3 == 0:
# #         print("Fizz")
# #         continue
# #     else:
# #         print(num)
# from pip._vendor.urllib3.connectionpool import xrange

# count = input("Please enter the number to FizzBuzz up to: ")
# count = int(count)

# for i in xrange(1, count):
# 	if i % 15 == 0:
# 		print ("FizzBuzz")
# 	elif i % 3 == 0:
# 		print ("Fizz")
# 	elif  i % 5 == 0:
# 		print ("Buzz")
# 	else:
# 		print(i)



# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# # write your code here
# def avg(*args):
#     argCount = len(args)
#     if argCount>0:
#         sumofnum=0
#         for el in args:
#             sumofnum +=el
#         return sumofnum / argCount
#     else:
#         return 0

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
#     nums = list(map(int, input().split()))
#     res = avg(*nums)
    
#     fptr.write('%.2f' % res + '\n')

#     fptr.close()

