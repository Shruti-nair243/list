n=int(input("Enter number of elements in the list:"))
a=[]
b=[]
for i in range(0,n):
	a.append(int(input()))
print("The input list is:",a)
for i in a:
	if(i>0):
		b.append(i)
print("The output list is:",b)
