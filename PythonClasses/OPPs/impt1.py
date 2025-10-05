def allValues(**kwargs):
  for key, value in kwargs.items():
    print(key, "=", value)



def findSmall(list2):
  for i in range(len(list2)-1):

    for j in range(len(list2)-1):
     if list2[j] > list2[j + 1]:
            temp = list2[j]
            list2[j] = list2[j + 1]
            list2[j + 1] = temp
  print(list2)


  

def findDublicate(l):
    dupes = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] == l[i]:
                dupes.add(l[j])
    return dupes