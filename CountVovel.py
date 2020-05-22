# string of vowels
vowels = 'aeiou'

ip_str = input()

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()
print(ip_str)

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
# print(count)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
