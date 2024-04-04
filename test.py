import ev3_dc as ev3
import keyboard
import time

MACADDRESS = '00:16:53:48:08:C8'

class MyEV3:
    def __init__(self, mac_address):
        self.ev3 = ev3.EV3(protocol=ev3.BLUETOOTH, host=mac_address)
        self.motor_d = ev3.Motor(
            ev3.PORT_D,
            protocol=ev3.BLUETOOTH,
            ev3_obj=self.ev3
        )
        self.motor_d.sync_mode = ev3.STD
    def set_speed(self, speed, direction):
        self.motor_d.start_move(speed=int(speed * direction))

    def stop_movement(self):
        self.motor_d.stop()

my_ev3 = MyEV3(MACADDRESS)

print(my_ev3.ev3.battery)
print(my_ev3.ev3.sensors_as_dict)

try:
    while True:
        if keyboard.is_pressed('w'):
            print('The W key is pressed!')
            my_ev3.set_speed(speed=100, direction=1)  # Example arguments
            time.sleep(0.2)
        else:
            my_ev3.stop_movement()

except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(f'An error occurred: {e}')
