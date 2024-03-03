num = input('Enter a number (decimal or integer): ')


# type your code here

num1 = num.replace(".", "")
print(num1)


if num1.isdigit() == False or num.count(".") > 1 or num[0] == ".":
  print("Make sure that the number you typed is a valid decimal number")  
  num = "ERROR!!!!!!!!!!!"
  sf = "ERROR!!!!!!!!!!!!!!"
else:
  num1 = num1.lstrip("0")
  sf = len(num1)
 
# do not change any code beyond this point

print('The number', num, 'has', sf, 'significant figures.')
