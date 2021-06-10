class Menu:
  def __init__(self, id, submenu = False, name = '', min=0, max=10):
    self.id = id
    self.submenu = submenu
    self.name = name
    self.min = min
    self.max = max

  def myfunc(self):
    print("Hello my name is " + self.name)

menuelems = ['Step', 'Frequency', 'Cycle', 'Start' ]
for i in menuelems:
    print(menuelems.index(i))

#p1 = Menu(0, name = "John")
#p1.myfunc() 
#print(p1.id, p1.max, p1.submenu)