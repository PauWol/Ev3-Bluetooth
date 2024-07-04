import bluetooth

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


    def get_device_info_by(self, search):
        """
        Get the info of a device.

        If the device is already discovered and its MAC address or name matches the `search` parameter,
        it will return the information directly. Otherwise, it will scan for nearby devices first.

        Args:
            search (str): The search string for MAC address or name of the Bluetooth device.

        Returns:
            A list of tuples containing the MAC address and name of the Bluetooth devices matching the search,
            along with a flag indicating whether the match is exact or possible.

        Raises:
            ValueError: If the `search` parameter is not provided.
        """
        if not search:
            raise ValueError('Missing parameter: search')

        if not self.nearby_devices:
            print('Scanning for nearby devices...')
            self.nearby_devices = self.discover_devices()

        matching_devices = []
        for device in self.nearby_devices:
            if search.lower() in device[0].lower() or search.lower() in device[1].lower():
                match_type = 'Exact match' if search.lower() == device[0].lower() or search.lower() == device[1].lower() else 'Possible match'
                print(f'Found {match_type}: {device}')
                matching_devices.append((device, match_type))

        if not matching_devices:
            print(f'No matching value found for "{search}"')

        return matching_devices
