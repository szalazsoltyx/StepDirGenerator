from encoder_menu import *

set_data('Speed',0)
set_data('Stepp',30)
set_data('Frequency',27)
set_data('Cycle',2)
set_data('speed',5)


Speed = get_integer(0,20,5,'Speed (0-100)','Speed')
Stepp = get_integer(0,20,5,'Stepp (0-100)','Stepp')
Frequency = get_integer(0,20,5,'Frequency (0-100)','Frequency')
Cycle = get_integer(0,20,5,'Cycle (0-100)','Cycle')
Start = info('I dont have a clock')
 


#print (data)
#print('get_int',menu_data,self.value,encoder.value())

#Root menu should be last menu because it depends on all the previous things
root_menu = wrap_menu([('Speed',Speed),('Stepp',Stepp),('Frequency',Frequency),
                       ('Cycle',Cycle),('Start',Start)])

#Finally we set up the root menu and set it running

root_menu()  # Set up the initial root menu by calling its function
print(menu_data['Speed'])
run_menu() #Start the main loop running


print('finished -  This should never get here because menu is an endless loop')