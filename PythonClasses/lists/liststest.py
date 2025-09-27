
# multi_list=[[1,2,3,3,7,7],"Erol", [["a","b","c"],3,4,5]]
# print(multi_list[2][0][1])

# numbers=[1,2,3,3,7,7,"Erol"]
# numbers2=["a","b","c"]

# print(numbers)
# numbers.append(9)
# print(numbers)
# numbers.insert(2,"Desak")
# print(numbers)
# numbers.insert(0,"Zelal")
# print(numbers)
# numbers.extend(numbers2)
# print(numbers)

n =int(input("How many item would you like to add? "))
numbers=[]
for i in range(n):
  x= str(input(f"item number {i+1} "))
  numbers.append(x)

print(numbers)