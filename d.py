# """
# Problem description.

# Chef recently had been studying about Fibonacci numbers and wrote a code to print out the kth term of the Fibonacci series(1, 1, 2, 3, 5, 8, 13….). He was wondering whether he could write a program to generate the kth term for similar series. More specifically : T(n, k) is 1 if n <= k and T(n, k) = T(n-1, k) + T(n-2, k) + T(n-3, k) … + T(n-k, k) if n > k . Given n and k output T(n, k)%(1000000007) as the answer could be very large
# Input
# Two integers, N and K
# Output
# Output description.

# One integer, the nth term of the series mod 1000000007
 

# Constraints
# 1 ≤ N, K ≤ 2*105
# Example
# Input:
# 7 5

# Output:
# 9
# """

# n,k=map(int,input().split())
# a=[1]*(k)
# b=k
# c=0
# for i in range(k,n):
#     b=b%(10**9+7)
#     a.append(b)
#     b+=b
#     b-=a[c]
#     c+=1
# print(a[n-1])

"""
The ZCO Scholarship Contest has just finished, and you finish with a rank of R. You know that Rank 1 to Rank 50 will get 100% scholarship on the ZCO exam fee and Rank 51 to Rank 100 will get 50% percentage scholarship on the ZCO exam fee. The rest do not get any scholarship.
What percentage of scholarship will you get ?

Input
Input consist of single line of input containing one integer R.
Output
Output a single line containing one integer — the percentage of scholarship you will get.
Constraints
1≤R≤109
Example Input 1
49
Example Output 1
100
Explanation 1
Since 1≤49≤50, answer is 100 percentage scholarship.

Example Input 2
317
Example Output 2
0
Explanation 2
Since 317>100, you do not get any scholarship.
"""
# rank = int(input("Enter your rank: " ))

# a=100
# b=50

# if rank in range(1,51):
#     print(a)
# elif rank in range(51,101):
#     print(b)
# else:
#     print(0)

def fib(number):
    a=0
    b=1
    for i in range(number):
        print("This is ", a)
        yield a
        
        tmp = a
        a = b
        b = tmp + b

for x in fib(7):
    print(x)