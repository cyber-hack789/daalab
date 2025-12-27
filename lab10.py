#4.Write a program to implement Dynamic Programming algorithm for 
#the Optimal Binary Search Tree problem.

def obst(prob, n): 
    dp = [[0]*n for _ in range(n)] 
     
    for i in range(n): 
        dp[i][i] = prob[i] 
 
    for length in range(2, n+1): 
        for i in range(n-length+1): 
            j = i + length - 1 
            dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + sum(prob[i:j+1]) 
 
    return dp[0][n-1] 
 
n = int(input("Enter number of keys: ")) 
prob = [float(input()) for _ in range(n)] 
 
print("Minimum cost:", obst(prob, n))