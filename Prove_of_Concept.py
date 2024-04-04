import ev3_dc as ev3
import keyboard , sys

MACADDRESS = '00:16:53:48:08:C8'

my_ev3 = ev3.EV3(protocol=ev3.BLUETOOTH, host=MACADDRESS)
motor_d = ev3.Motor(
    ev3.PORT_D,
    protocol=ev3.BLUETOOTH,
    ev3_obj=my_ev3
)
motor_c = ev3.Motor(
    ev3.PORT_C,
    protocol=ev3.BLUETOOTH,
    ev3_obj=my_ev3
)
print(my_ev3.battery)
print(my_ev3.sensors_as_dict)
def run(motor_d,direction = 1):
    print('The key is pressed!')
    if  not motor_d.busy:
        #print(motor_d.busy)
        motor_d.start_move(direction = direction,speed=80)
def stop(motor_d):
    if motor_d.busy:
         motor_d.stop()
try:
    while True:
        if keyboard.is_pressed('w'):
            run(motor_d)
            run(motor_c)
            print('started...')
        elif keyboard.is_pressed('a'):
            run(motor_d)
            run(motor_c,direction=-1)
            print('started...')
        elif keyboard.is_pressed('d'):
            run(motor_d,direction=-1)
            run(motor_c)
            print('started...')
        elif keyboard.is_pressed('s'):
            run(motor_d,direction=-1)
            run(motor_c,direction=-1)
            print('started...')
        else:
            stop(motor_d)
            stop(motor_c)
            print('stopped...')


except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
except Exception as e:
    print(f'An error occurred: {e}')
    