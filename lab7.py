def m(a):
 if len(a)<=1:return a
 mid=len(a)//2
 l,r=m(a[:mid]),m(a[mid:])
 i=j=0;res=[]
 while i<len(l) and j<len(r):
  if l[i]<r[j]:res+=[l[i]];i+=1
  else:res+=[r[j]];j+=1
 return res+l[i:]+r[j:]
print(m([10,15,8,7,6]))