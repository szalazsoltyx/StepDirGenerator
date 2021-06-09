python tools/pyboard.py --device /dev/ttyUSB0 -f cp ssd1306.py :
python tools/pyboard.py --device /dev/ttyUSB0 test.py

screen /dev/ttyUSB0 115200


cp libs/* /pyboard/



rshell --buffer-size=30 -p /dev/ttyUSB0 -a


 d4 () Core 2
 d0 16
 d8 15


Freqency Mondjuk milisec be. = 1000 ms,  100 ms, 10 ms, 1 ms, 0,1 ms, 0,01 ms.              val_new = 10 ** r.value() /100
Step Egy kibekapcsolási ciklust hányszor csináljon meg. = 1, 10, 100, 1000, 10 000, 100 000. 
Cycle = 1, 10, 100, 1000.                               val_new = 10 ** r.value() #hatvanyozas