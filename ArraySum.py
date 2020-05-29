"""
Sample Input

6
1 2 3 4 10 11

Sample Output

31
"""
#!/bin/python3

import os
import sys
import functools


# Complete the simpleArraySum function below.
def simpleArraySum(ar):
    # return (functools.reduce(lambda x,y:x+y,ar))
    result=sum(ar) 
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
