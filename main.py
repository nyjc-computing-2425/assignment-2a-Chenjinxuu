num = input('Enter a number (decimal or integer): ')


# type your code here
num1 = num.replace(".", "")
num2 = num1.lstrip("0").lstrip(" ")


if num1.isdigit() == False or num.count(".") > 1 or num[0] == ".":
  print("Make sure that the number you typed is a valid decimal number")  
  num = "is invalid,so it" 
  sf = "an uncalculable number of"
else:
  num = num.lstrip("0")
  if num[0] == ".":
    num = "0" + num
    sf = len(num2)
  else:
    sf = len(num2)
 
# do not change any code beyond this point

print('The number', num, 'has', sf, 'significant figures.')
