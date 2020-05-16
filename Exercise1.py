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
rank = int(input("Enter your rank: " ))

a=100
b=50

if rank in range(1,51):
    print(a)
elif rank in range(51,101):
    print(b)
else:
    print(0)