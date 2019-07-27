bx=int(input())
xy=[]
for i in range(bx):
  ax=input()
  xy.append(ax)
mg=min(xy,key=len)
xy.remove(mg)
for i in range(len(mg)):
  for j in range(len(xy)):
     ck=xy[j]
     if mg[:i+1]==ck[:i+1]:
       result=mg[:i+1]
     else:
       break
print(result)
