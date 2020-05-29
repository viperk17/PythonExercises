a = input("Enter a string: ")

word = str(a)
rev = word[::-1]

c = [print("Palindrome") if word == rev else print("Not a Palindrome")]
