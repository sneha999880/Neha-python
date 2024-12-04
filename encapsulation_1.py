class Sum_odd:
  def calc(self):
    __n = int(input())
    x = 0
    for i in range(1,__n+1,2):
      x+=i
    print(x)
m=Sum_odd()
m.calc()
