class Menu:
  def __init__(self, id, active=False, submenu = False, name = '', min=0, max=10):
    self.id = id
    self.active = active
    self.submenu = submenu
    self.name = name
    self.min = min
    self.max = max
 

  def activate(self):
    self.active = True
    self.name = '> '+ self.name

def get_active_menu():
    for i in menuelems:
        if i.active:
            return(i.name)

def set_active_menu(menuid):
    for i in menuelems:
        #print(i.id)
        if i.id == menuid:
            i.active = True
            i.name = '> '+ i.name
        else:
            i.active = False
        #print(i.name)
    
#print(i)
#menuelems = ['Step', 'Frequency', 'Cycle', 'Start' ]

Menu_Step = Menu(0, False, True, 'Step', 0 ,10)
Menu_Frequency = Menu(1, False,  True, 'Frequency', 0 ,10)
Menu_Cycle = Menu(2, False,  True, 'Cycle', 0 ,10)
Menu_Start = Menu(3, False, True, 'Start', 0 ,10)

#Menu_Cycle.activate()
#print(Menu_Cycle.active)

menuelems = [Menu_Step, Menu_Frequency, Menu_Cycle, Menu_Start]

set_active_menu(1)
print(get_active_menu())