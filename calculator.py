print('''THIS IS A CALCULATOR WRITTEN IN PYTHON THAT PERFORM SOME ARITHMETIC CALCULATION LIKE
1.ADDITION(+)
2.SUBTRACTION(-)
3.MULTIPLICATION(*)
4.DIVISION(/)
5.,modulous(%)
''')
num1 = float(input("enter first number : "))
opt = input("enter a  operator(+,-,*,/,%):")
num2 = float(input("enter second number : "))

if opt == '+':
  result = num1 + num2
  print(f" the addition of {num1} and {num2} is : {result}")
elif opt == '+':
  result = num1 - num2
  print(f" the subtraction of {num1} and {num2} is : {result}")
elif opt == '*':
  result = num1 * num2
  print(f" the multiplication of {num1} and {num2} is : {result}")
elif opt == '/':
  result = num1 / num2
  print(f" the division of {num1} and {num2} is : {result}")
elif opt == '%':
  result = num1 % num2
  print(f" the modulous of {num1} and {num2} is : {result}")
else:
  print('''you enter invalid opt please enter(+,-,*,/) these opt TRY AGAIN''')