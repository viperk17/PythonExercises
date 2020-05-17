"""
Define as the sum of the factorials of the digits of . For example,

.

Define
as the sum of the digits of . So

.

Define
to be the smallest positive integer such that . Though is , is also , and it can be verified that is

.

Define
as the sum of the digits of . So

.

Further, it can be verified that
is and is

.

What is
? As the number can be large, print it modulo

.

Input Format

The first line of each test file contains a single integer
, which is the number of queries per test file. lines follow, each containing two integers separated by a single space: and

of the corresponding query.

Constraints

Output Format

Print exactly

lines, each containing a single integer, which is the answer to the corresponding query.

Sample Input 0

2
3 1000000
20 1000000

Sample Output 0

8
156

Explanation 0

, and . .
"""


def f(n):
    num_li=[int(i) for i in str(n)]
    sum_li=[]
    for num in num_li:
        value=1
        for a in range(1,num+1):
            value=value*a
        sum_li.append(value)
    return sum(sum_li)

# define sf(n)
def sf(n):
    num_li=[int(i) for i in str(f(n))]
    return sum(num_li)

# define g(i)
def g(i):
    signal=1
    while sf(signal)!=i:
        signal=signal+1
    return signal

# define sg(i)
def sg(i):
    num_li=[int(i) for i in str(g(i))]
    return sum(num_li)

# define m value, input is a list
def m(li):
    for i in li:
        value=0
        for j in range(1,i+1):
            value=sg(j)+value
        print(value)

# get the input format in a list
input_list=[]
while True:
    try:
        input_list.append(input())
    except:
        break

# break down the list, put each value in the list of its line
temp_list=[]
for each_line in input_list:
  values_list=each_line.split()
  temp_list.append(values_list)

# no need for the first list which is the q value, pop it
q=temp_list.pop(0)

# get the final list that can be used in m()
final_list=[]
for value in temp_list:
  final_list.append(int(value[0]))

# run(m)
m(final_list)