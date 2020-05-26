"""
Input Format

A single line containing a string

Output Format
In the first line, print True if
has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False.

Sample Input
qA2

Sample Output
True
True
True
True
True
"""

if __name__ == '__main__':
    s = input()
    # for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    #     print(any(eval("c." + test + "()") for c in s))
    for f in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any(getattr(c, f)() for c in s))
