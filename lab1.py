#1.Write a program to sort a list of N elements using Selection Sort      
#Technique.

n = int(input("enter how ny ele:"))
a =[]
print("enter a number")
for i in range(n):
	a.append(int(input()))

for i in range(n):
	min=i
	for j in range(i+1, n):
		if a[j] < a[i]:
			min=j
		a[i],a[j]= a[j],a[i]

print("sorted list:",a)
