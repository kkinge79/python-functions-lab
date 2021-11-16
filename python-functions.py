
#*  problem 1

def sum_to(n):
  sum = 0
  for num in range(0, n + 1):
    sum = (sum + num)
  print(sum)

sum_to(10)


#* problem 2

def largest(list):
  print(max(list))

largest([1, 2, 3, 4, 0, 55])

#*  problem 3

def occurances(str1, str2):
  count = str1.count(str2)
  print(count)

occurances('fleep floop', 'f')


#* problem 4

def product(*args):
  product = 1
  for a in args:
      product *= a
  return product

print(product(-1, 4))
