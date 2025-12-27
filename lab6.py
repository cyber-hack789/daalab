def quicksort(x):
  if (len(x) <=1):
	   return x

  p = x[1]
  left=[i for i in x if i < p]
  right=[i for i in x if i > p]
  return(quicksort(left) +[p]+ quicksort(right))

print(quicksort([10,8,9,3,2,1]))