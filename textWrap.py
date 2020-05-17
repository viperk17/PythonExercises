"""
Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

**********************************Explanation************************
l= list() Defines an empty list for i in range(0,len(string),max_width): Now the loop is running from 0 till the length of the string (Ex. if the String is cat , Length of string will be 3 and the loop will iterate 3 times i.e. for i=0,1,2). Now since we need to print the strings in block of 4 , for the next iteration it should print the string from 5-8 , so the incerement in next iteration is defined by the 3rd argument in the for loop statemnt l.append(string[i:i+max_width]) this statemnt will start adding the 4 letter blocks in the list "l" so the content of the list at the end of the for loop will be something like this ['ABCD', 'EFGH', 'IJKL', 'IMNO', 'QRST', 'UVWX', 'YZ'] return "\n".join(l) The last statement is just joining the each items of the list with \n which is a new line
"""

import textwrap

def wrap(string, max_width):
    # return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    l= list()
    for i in range(0,len(string),max_width): l.append(string[i:i+max_width])
    return "\n".join(l) 


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)