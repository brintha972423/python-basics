a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

print("Addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)

choice=input("choose an operation")

if choice=="1":
   print("Answer:",a+b)
elif choice=="2":
   print("Answer:",a-b)
elif choice=="3":
   print("Answer:",a*b)
elif choice=="4":
   print("Answer:",a/b)
else:
   print("invalid choice")