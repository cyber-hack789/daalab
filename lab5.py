#5.Write a program to find minimum and maximum value in an array 
#using divide and conquer. 

n = int(input("Enter number of elements: "))
a =[int(input("Enter elements: ")) for _ in range(n)]
m = n//2
print(min(a[:m]+a[m:]), max(a[:m]+a[m:]))
    
