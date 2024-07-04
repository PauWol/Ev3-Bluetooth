from ev3_bluetooth import EV3_Bluetooth
MACADDRESS = 'xx:xx:xx:xx:xx:xx'

ev = EV3_Bluetooth(MACADDRESS)
m = ev.Motor('a')
led = ev.Led('red','flash')
m.stop()
