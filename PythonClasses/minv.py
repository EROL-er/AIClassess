lis=[2,8,6,-3,-4,-6,-10,-15,25]
count=0
minv=lis[0]
while(count <len(lis)):
  v = lis[count]
  if(v>minv):
    minv=v
   
  else:
    pass

  count= count+1

      
list2 = [1, 4, 0, 3, 5, 7]


for i in range(len(list2)-1):

  for j in range(len(list2)-1):
     if list2[j] > list2[j + 1]:
            temp = list2[j]
            print(temp)
            list2[j] = list2[j + 1]
            
            list2[j + 1] = temp

print(list2)





