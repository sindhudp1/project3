num=int(input("enter a number"))
rev=0
r=num
while num != 0:
    rem=num%10
    rev=rev*10+rem
    num=int(num/10)
if r==rev:
    print(r, "is palindrome")
else:
    print(r, "is not a palindrome")
~                                                                               
~                                                                               
~                                   
