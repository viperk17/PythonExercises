a = input("Enter a string: ")

def reverseWord(w):
  return ' '.join(w.split()[::-1])

print(reverseWord(a))
