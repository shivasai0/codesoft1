a=int(input ("enter first number"))
b=int(input("enter second number"))
print("+ - * / %")
x=input("enter what operation shold have to perform:")
if(x=="+"):
    print("addition of two numbers is:")
    print(a+b)
elif(x=="-"):
    print("subraction of two numbers is:")
    print(a-b)
elif(x=="*"):
    print("multiplication of two numbers is:")
    print(a*b)
elif(x=="/"):
    print("division of two numbers is:")
    print(a/b)
elif(x=="%"):
    print("module of two numbers is:")
    print(a%b)
else:
    print("enter the valid opearion")
    
    
