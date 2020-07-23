n =  int(input("Enter the max term value:"))
a = 1
b = 2
list = [1,2]
sum = 0
while list[-1] < n :
    c = a+b
    a= b
    b=c
    if c < n:
     list.append(c)
    else:
      break
for N in list:
  if N%2 == 0:
    sum = sum + N
print('this  is list :',list)
print('this is the sum :', sum)
