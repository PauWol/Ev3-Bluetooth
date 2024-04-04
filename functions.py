import ev3_dc as ev3
import bluetooth , time

MACADDRESS = '00:16:53:48:08:C8'

class Bluetooth():
    def __init__(self) -> None:
        self.nearby_devices = None
        pass

    def discover_devices(self):
        """
        Scan for nearby Bluetooth devices.

        Returns:
            A list of tuples containing the MAC address and name of nearby devices.
        """
        self.nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=10)
        return self.nearby_devices

    def print_near_devices(self):
        """
        Scan for nearby Bluetooth devices and print them.

        Prints:
            The mac addresses and if available their names.
        """
        print("Found devices:")
        for addr, name in self.discover_devices():
            print(f"  MAC: {addr}, Name: {name if name else 'Unknown'}")

    def get_device_info_by(self,search):
        """
        Get the info of a device.

        If the device is already discovered and its MAC address or name matches the `search` parameter,
        it will return the information directly. Otherwise, it will scan for nearby devices first.

        Args:
            search (str): The MAC address or name of the Bluetooth device to search for.

        Returns:
            A tuple containing the MAC address and name of the Bluetooth device.

        Raises:
            ValueError: If the `search` parameter is not provided.
        """
        print('Missing param search!' if not search else '')
        if self.nearby_devices:
            print('Devicelist already there using old')
            pass
        else:
            print('Scanning for near devices...')
            self.nearby_devices = self.discover_devices()
            #print(self.nearby_devices)

        for i in self.nearby_devices:
            if  search in i:
                print(f'Found match: {i}')
                return i
        print(f'No matching value found! --> "{search}"')


class Info():
    def __init__(self,device_mac):
        self.mac = device_mac
        self.my_ev3 = ev3.EV3(protocol=ev3.BLUETOOTH, host=device_mac)

    def sensor_info(self):
        return {'dict':self.my_ev3.sensors_as_dict,'list':self.my_ev3.sensors}
    
    def general(self):
        return {'name':self.my_ev3.name,'host':self.my_ev3.host,'battery':self.my_ev3.battery,'volume':self.my_ev3.volume}
    
    def extra(self):
        return {'memory':self.my_ev3.memory,'sleep(min)':self.my_ev3.sleep,'system':self.my_ev3.system}

class Motor():
    def __init__(self,ev3_object,port):
        """
        Initiate Motor class 
        Args:
            ev3_object (ev3.Ev3): Instance of an ev3.EV3 object.
            port (ev3.PORT_A): The EV3 brick port to which the motor is connected.
        """
        self.motor_ = ev3.Motor(port,protocol=ev3.BLUETOOTH,ev3_obj=ev3_object)

    def run_motor(self,speed:float,direction=1):
        if  not self.motor_.busy:
            self.motor_.start_move(speed=speed,direction=direction)

    def stop_motor(self):
        if self.motor_.busy:
            self.motor_.stop()


"""

inf = Info(MACADDRESS)
print(inf.general())

mot = Motor(inf.my_ev3,ev3.PORT_D)

mot.run_motor(50)

time.sleep(5)

mot.stop_motor()
        
#Bluetooth().print_near_devices()

"""