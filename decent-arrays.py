a = int(input())

b = list(map(int,input().strip().split()))[:a]

c = sorted(b)
if c == b: 
  print("Yes")
else: 
  print("No")