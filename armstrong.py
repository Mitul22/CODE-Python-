# CODE-Python-
#This includes Python Codes
#armstrong number in python
num=int(input('enter a number'))
order=len(str(num))
count=0
rem=0
sum=0
n=num
while n>0:
    rem=n%10
    sum=sum+rem**order
    n//=10
if num==sum:
    print('ARMSTRONG NUMBER')
else:
    print('NOT A ARMSTRONG NUMBER')
