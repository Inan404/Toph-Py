def ascii_plotter(percentage):
  arr = ['.']*10
  val = percentage//10
  arr[:val] = '+'*val
  print("[", end="")
  for i in arr: 
    print(i, end="")
  print("] ", end="")
  print(str(percentage)+"%",)

a = int(float(input()))
ascii_plotter(a)
