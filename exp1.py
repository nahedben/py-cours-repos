//Second modification
list1 = [x for x in range(5)]
list2 = list(map(lambda x :x**2 , list1))
print(list2)

// the second map test powering all items inside list2
for x in map(lambda x : x *x , list2):
  print(x, end=' ')
print()
