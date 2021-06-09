import uasyncio as aysncio
from encoder_menu import *

# Define this function in the body of the program or (better) locally in an imported action module.
# This is the function that actually does the work.
set_data('Speed',0)
set_data('Stepp',0)
set_data('Frequency',0)
set_data('Cycle',0)
set_data('speed',0)

def vork():
    print('vork')

def do_something():



    Speed = get_integer(0,10,1,'Speed (0-100)','Speed')
    Stepp = get_integer(0,20,1,'Stepp (0-100)','Stepp')
    Frequency = get_integer(0,100,1,'Frequency (0-100)','Frequency')
    Cycle = get_integer(0,200,1,'Cycle (0-100)','Cycle')
    Start = dummy()

    root_menu = wrap_menu([('Speed',Speed),('Stepp',Stepp),('Frequency',Frequency),
                          ('Cycle',Cycle),('Start',Start)])
	    
    
    root_menu()  # Set up the initial root menu by calling its function
    print(menu_data['Speed'])

    run_menu() #Start the main loop running


    print('finished -  This should never get here because menu is an endless loop')


do_something()
