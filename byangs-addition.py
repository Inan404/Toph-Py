a,b = input().split()
strlen  = min(len(a),len(b))
i = 1
flag = 0
while i <= strlen:
  if (int(a[-i])+int(b[-i])) > 9:
    flag = 1
    print("Yes")
    break
  i+=1
if flag == 0 :
  print("No")
  