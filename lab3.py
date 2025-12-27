#3.Write program to implement Dynamic Programming algorithm for 
#the 0/1 Knapsack problem. 

w=[10,20,30]
p=[60,100,120]
c=50
dp=[0]*(c+1)
for i in range(len(w)):
 for j in range(c,w[i]-1,-1):
  dp[j]=max(dp[j],p[i]+dp[j-w[i]])
print(dp[c])