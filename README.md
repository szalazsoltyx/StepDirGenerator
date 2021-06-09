python tools/pyboard.py --device /dev/ttyUSB0 -f cp ssd1306.py :
python tools/pyboard.py --device /dev/ttyUSB0 test.py

screen /dev/ttyUSB0 115200


cp libs/* /pyboard/



rshell --buffer-size=30 -p /dev/ttyUSB0 -a


 d4 () Core 2
 d0 16
 d8 15
