
# 12.Write a program to implement the backtracking algorithm for the 
#sum of subsets problem.

def subset_sum(arr, target, i=0, curr=[]): 
    if sum(curr) == target: 
        print("Solution:", curr) 
        return 
    if i == len(arr) or sum(curr) > target: 
        return 
     
 
    subset_sum(arr, target, i+1, curr + [arr[i]]) 
    subset_sum(arr, target, i+1, curr) 
 
n = int(input("Enter number of elements: ")) 
arr = [int(input()) for _ in range(n)] 
target = int(input("Enter target sum: ")) 
 
subset_sum(arr, target) 