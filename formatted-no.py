a = input()
lenA = len(a)

if lenA%3 != 0 : 
  comma = int(lenA/3)
else: 
  comma = int((lenA/3)-1)
  
i,j = 1,1
count = 1

result = ['']*(lenA+comma)
resLen = len(result)

while i <= (resLen): 
  if(count%3 != 0):
    result[resLen-i] = a[lenA-j]
    i+=1
    j+=1
    count+=1
  else: 
    if comma != 0 : 
      result[resLen-i] = a[lenA-j]
      result[resLen-(i+1)] = ','
      i+=2
      j+=1
      count = 1
      comma-=1
      result[resLen-i] = a[lenA-j]
      
    result[resLen-i] = a[lenA-j]
    i+=1
    j+=1
    count+=1
  
str = ''.join(result)
print(str)