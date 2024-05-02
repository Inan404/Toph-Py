ls = int(input())
string = input()
a = ['']*len(string)
p = 0
for i in string: 
  if i == " ": 
    a[p] = " "
    p+=1
  else: 
    j = ord(i) - ls 
    if j < 97: 
      k = 97 - j 
      l = 123 - k 
      a[p] = chr(l)
      p+=1
    else: 
      a[p] = chr(j)
      p+=1
      
res = ''.join(a)
print(res)
