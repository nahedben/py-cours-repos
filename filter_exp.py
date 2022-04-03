from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
print(data)

filtred = list(filter(lambda x : x >0 and x % 2 ==0, data))
if len(filtred) ==0:
  print(' Our filter is empty')

print(filtred)

l = ['yani' , 'phill', ' nahed', 'sebastien', 'fernando']
fil = list(filter(lambda e: e.startswith('p'), l))

print(fil)

par = input('enter the alphabet youo want to filter with: ')

def fil_function(l,t):
  fil = filter(lambda e: e.startswith(t), l)
  return list(fil)

print(fil_function(l,par))