#write a program to reverse a string and check whether its palindrome or not

text = str(input())
rev_text = " "

for j in text:
  rev_text = j + rev_text
  print(rev_text)
if text == rev_text:
  print("palindrome")
else:
  print("not palindrome")
