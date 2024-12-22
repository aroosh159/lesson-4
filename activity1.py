n = int(input("Enter the number of stars"))

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")

#While loops
num1 = 1
sum = 0

while(num1<=10):
  sum=sum+num1
  num1=num1+1

print("The sum of first ten natural numbers are",sum)

#nested while conditions

num = int(input("Enter the number "))

flag = False  

if num>1:
   for i in range(2,num):
     if num%2==0:
      flag = True
      break
   
if flag:
   print("Number is not prime")
else :
   print("Number is prime")