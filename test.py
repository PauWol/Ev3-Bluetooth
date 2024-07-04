from ev3_bluetooth import EV3_Bluetooth
import struct
MACADDRESS = '00:16:53:48:08:C8'

ev = EV3_Bluetooth(MACADDRESS)
evstate = ev.Status()
m = ev.Motor('a')
#led = ev.Led('red','flash')

m.stop()