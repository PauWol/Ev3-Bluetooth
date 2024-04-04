import bluetooth , re


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

    def connect_to_device(mac_address, port=1):
        """Connects to a Bluetooth device by its MAC address and specified port.

        Args:
            mac_address: The MAC address of the Bluetooth device (e.g., "00:11:22:33:44:55").
            port: The port to use for communication (default is 1, commonly used for RFCOMM).

        Returns:
            A Bluetooth socket object representing the connection, or None if connection fails.
        """

    def connect_to_device(self,device_address, port):
        try:
            # Ensure that port is an integer
            port = int(port)
            
            # Create a Bluetooth socket
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            
            # Connect to the device
            sock.connect((device_address, port))
            
            print("Connected to device at address:", device_address)
            
            # Return the connected socket
            return sock
            
        except ValueError:
            print("Error: Port number must be an integer.")
            return None
        except bluetooth.btcommon.BluetoothError as e:
            print("Error:", e)
            return None
        
        
#Bluetooth().connect_to_device('88:9F:6F:63:18:E9', 1)
Bluetooth().print_near_devices()