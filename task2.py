print('''
      WELCOME TO MY SIMPLE CALCULATOR 
      + ADD
      - SUBSTRACT
      * MULTIPLY
      / DIVIDE
      ''')

num1=int(input("enter first value \n"))
num2=int(input("enter second value \n"))

while True:
    operator=input("enter the operator \n")
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
    else:
        print("invalid operator \n")                