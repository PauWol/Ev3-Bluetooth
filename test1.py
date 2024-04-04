import ev3_dc as ev3
import keyboard , sys , time

MACADDRESS = '00:16:53:48:08:C8'

my_ev3 = ev3.EV3(protocol=ev3.BLUETOOTH, host=MACADDRESS)
motor_d = ev3.Motor(ev3.PORT_D,protocol=ev3.BLUETOOTH,ev3_obj=my_ev3)
motor_b = ev3.Motor(ev3.PORT_B,protocol=ev3.BLUETOOTH,ev3_obj=my_ev3)

print(my_ev3.battery)
print(my_ev3.sensors_as_dict)
def run_motor(motor_d):
    if  not motor_d.busy:
        motor_d.start_move(speed=80)
def stop_motor(motor_d):
    if motor_d.busy:
         motor_d.stop()
try:
    while True:
        if keyboard.is_pressed('w'):
            run_motor(motor_d)
            print('started...')
    #time.sleep(5)
        else:
            stop_motor(motor_d)
            print('stopped...')

            
    while True:
        pass
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
except Exception as e:
    print(f'An error occurred: {e}')
    