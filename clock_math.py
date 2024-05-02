hr,min = map(int, input().split())

result = float((30*hr)-(5.5*min))
if result > 180 : 
  result = float(360-result) 
  
print(result)

