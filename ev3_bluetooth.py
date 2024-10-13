import ev3_dc as ev3

class EV3_Bluetooth():
    def __init__(self,macaddres:str):
        """
        Initilises a connection with the Provided Ev3(macaddres)

        Args:
            `macaddres` (str): MAC address of the EV3
        """
        self.MACADDRES = macaddres
        #Init connection:
        self.EV3 = ev3.EV3(protocol=ev3.BLUETOOTH, host=macaddres)
    
    def Motor(self,port:str):
            """
            Initializes the requested Motor

            Args:
                `port` (str): Port of the motor -> a,b,c,d

            Returns:
                The Motor object with the provided port.
            """
            match port.lower():
                case 'a':
                    evport = ev3.PORT_A
                case 'b':
                    evport = ev3.PORT_B
                case 'c':
                    evport = ev3.PORT_C
                case 'd':
                    evport = ev3.PORT_D
                case _:
                    raise ValueError(f"Invalid motor port: {port}")
            try:          
                motor = ev3.Motor(evport,protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
            except Exception as e:
                raise Exception(f"Error: {e}")

            #create subclass for each motor
            class MotorWrapper:
                def __init__(self,motor):
                    self.motor = motor
                    
                def run(self,direction = 1,speed = 80):
                    """
                    Starts motor with given propertys till its stoped

                    Args:
                        `direction` (int): direction of the wheels to spin -> 1,-1
                        `speed` (int): speed of the motor to go -> 0-100
                    """
                    if  not self.motor.busy:
                        self.motor.start_move(direction = direction,speed= speed)

                def run_to(self,degrees,speed = 80):
                    """
                    Starts motor with given propertys till set angle is reached

                    Args:
                        `degrees` (int): number of degrees the wheel should turn
                        `speed` (int): speed of the motor to go -> 0-100
                    """
                    if  not self.motor.busy:
                        self.motor.start_move_by(degrees,speed= speed)

                def stop(self):
                    """
                    Stops the motor -> (opposite of `run()`)
                    """
                    if self.motor.busy:
                        self.motor.stop()
            
            return MotorWrapper(motor)

    def Sensor(self,port:int,type:str):
        """
        Initializes the requested sensor

        Args:
            `port` (int): Port of the sensor -> 1,2,3,4
            `type` (string): Type of the sensor -> color,touch,ultrasonic,infrared,gyro

        Returns:
            The sensor object with the provided port and type.
        """
        #check the port
        match port:
            case 1:
                evport = ev3.PORT_1
            case 2:
                evport = ev3.PORT_2
            case 3:
                evport = ev3.PORT_3
            case 3:
                evport = ev3.PORT_4
            case _:
                raise ValueError(f"Invalid sensor port: {port}")

        #init the type
        try:
            match type.lower():
                case 'color':
                    color: ev3.Color = ev3.Color(port=evport,protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
                    return color
                case 'touch':
                    touch: ev3.Touch = ev3.Touch(port=evport,protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
                    return touch
                case 'ultrasonic':
                    ultrasonic: ev3.Ultrasonic = ev3.Ultrasonic(port=evport,protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
                    return ultrasonic
                case 'infrared':
                    infrared: ev3.Infrared = ev3.Infrared(port=evport,protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
                    return infrared
                case 'gyro':
                    gyro: ev3.Gyro = ev3.Gyro(port=evport,protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
                    return gyro
                case _:
                    raise ValueError(f"Invalid sensor type: {type}")
        except Exception as e:
            raise Exception(f"Error: {e}")
        
    def Led(self,color,type = 'static'):
        """
        Changes the color of the integrated LED

        Args:
            `color` (str): name of the desired color -> red,orange,green
            `type` (str): type of the LED -> flash,pulse,static(means just on),off
        """
        if type == 'off':
            led = ev3.LED_OFF
        elif color == 'red':
            if type == 'flash':
                led = ev3.LED_RED_FLASH
            if type == 'pulse':
                led = ev3.LED_RED_PULSE
            if type == 'static':
                led = ev3.LED_RED
        elif color == 'orange':
            if type == 'flash':
                led = ev3.LED_ORANGE_FLASH
            if type == 'pulse':
                led = ev3.LED_ORANGE_PULSE
            if type == 'static':
                led = ev3.LED_ORANGE
        elif color == 'green':
            if type == 'flash':
                led = ev3.LED_GREEN_FLASH
            if type == 'pulse':
                led = ev3.LED_GREEN_PULSE
            if type == 'static':
                led = ev3.LED_GREEN     
        else:
            raise ValueError(f"Invalid color: {color} or type: {type}")

        jk = ev3.Jukebox(protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
        jk.change_color(led)

    def Sound(self,volume=80):
        """
        Initializes the Sound method

        Args:
            `volume` (int): volume of the sound -> 0-100

        Returns:
            The Sound object with the provided volume.
        """
        jk = ev3.Jukebox(protocol=ev3.BLUETOOTH,ev3_obj=self.EV3,volume=volume)
        return jk

    def Voice(self):
        """
        Initializes the Voice methods

        Returns:
            The initialized Voice object with the right dependencies.

        Dependencies:
            Exsisting `Wifi` connection on the host Pc.
        """
        fs = ev3.FileSystem(protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
        voice = ev3.Voice(protocol=ev3.BLUETOOTH,ev3_obj=self.EV3)
        return voice
    
    def Status(self):
        """
        Initializes the Status methods

        Returns:
            The initialized Status object with the right dependencies.
        """
        class StatusWrapper:
            def __init__(self,EV3,sensor,motor):
                self.EV3 = EV3
                self.sensor = sensor
                self.motor = motor
                self.types = {7: 'large_motor', 8: 'medium_motor', 16: 'touch', 29: 'color', 30: 'ultrasonic', 32: 'gyro', 33: 'infrared',124:'none',125:'none'}

            @property
            def sensors(self):
                '''
                all connected sensors and motors at all ports (as named tuple Sensors)

                You can address a single one by e.g.:
                ev3_dc.EV3.sensors.Port_3 or
                ev3_dc.EV3.sensors.Port_C
                '''
                self.EV3._physical_ev3.introspection(self.EV3._verbosity)
                return (
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_1]["type"],
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_2]["type"],
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_3]["type"],
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_4]["type"],
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_A_SENSOR]["type"],
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_B_SENSOR]["type"],
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_C_SENSOR]["type"],
                    self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_D_SENSOR]["type"]
                )
            
            @property
            def sensors_as_dict(self):
                '''
                all connected sensors and motors at all ports (as dict)

                You can address a single one by e.g.:
                ev3_dc.EV3.sensors_as_dict[ev3_dc.PORT_1] or
                ev3_dc.EV3.sensors_as_dict[ev3_dc.PORT_A_SENSOR]
                '''
                self.EV3._physical_ev3.introspection(self.EV3._verbosity)
                return {
                    key: sensor["type"]
                    for key, sensor in self.EV3._physical_ev3._introspection["sensors"].items()
                }
            
            @property
            def get_only_sensors(self):
                self.EV3._physical_ev3.introspection(self.EV3._verbosity)
                return {
                    'port_1':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_1]["type"],
                    'port_2':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_2]["type"],
                    'port_3':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_3]["type"],
                    'port_4':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_4]["type"],
                }
            
            @property
            def get_only_motors(self):
                self.EV3._physical_ev3.introspection(self.EV3._verbosity)
                return {
                    'port_a':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_A_SENSOR]["type"],
                    'port_b':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_B_SENSOR]["type"],
                    'port_c':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_C_SENSOR]["type"],
                    'port_d':self.EV3._physical_ev3._introspection["sensors"][ev3.PORT_D_SENSOR]["type"]        
                }
            
            def translate(self,dict):
                try:
                    r = {}
                    for k, v in dict.items():
                        if v != None:
                            if v in self.types:
                                r[k] = self.types[v]
                            else:
                                r[k] = v
                        else:
                            r[k] = v
                    return r
                except Exception as e:
                    print(e)
            
            def get_number_from_name_or_char(self,name):
                char = False
                val = name.split('_')[1]
                if val.isalpha() and len(val) == 1:
                    char = True
                return val , char
            
            def get_value_from_instance(self,name,port_name):
                try:
                    match name.lower():
                        case 'color':
                            sen = getattr(self, port_name)
                            return self.translate_color(int(sen.color))
                        case 'touch':
                            sen = getattr(self, port_name)
                            return sen.touched 
                        case 'ultrasonic':
                            sen = getattr(self, port_name)
                            return sen.distance
                        case 'infrared':
                            sen = getattr(self, port_name)
                            return sen.distance
                        case 'gyro':
                            sen = getattr(self, port_name)
                            return sen.angle
                        case 'large_motor':
                            sen = getattr(self, port_name)
                            return sen.motor.position
                        case 'medium_motor':
                            sen = getattr(self, port_name)
                            return sen.motor.position
                        case _:
                            raise ValueError(f"Invalid sensor type: {type}")
                except Exception as e:
                    raise Exception(f"Error: {e}")
            
            def make_instance_get_value(self,dict):
                try:
                    r = {}
                    for k, v in dict.items():
                        digit , ischar = self.get_number_from_name_or_char(k)
                        if v != None:
                            if ischar:
                                setattr(self,k,self.motor(str(digit)))
                            else:
                                setattr(self, k, self.sensor(int(digit),str(v)))
                            r['data_'+str(digit)] = self.get_value_from_instance(str(v),k)
                        else:
                            r['data_'+str(digit)] = v
                    return r
                except Exception as e:
                    print(e)

            def translate_color(self,num):
                match num:
                    case 0:
                        return 'nothing'
                    case 1:
                        return 'black'
                    case 2:
                        return 'blue'
                    case 3:
                        return 'green'
                    case 4:
                        return 'yellow'
                    case 5:
                        return 'red'
                    case 6:
                        return 'white'
                    case 7:
                        return 'brown'
                    case _:
                        return 'none'

            @property
            def get_sensor_data(self):
                a = self.translate(self.get_only_sensors)
                r = self.make_instance_get_value(a)
                try:
                    r = {**a,**r}
                except Exception as e:
                    print(e)
                return r
            @property
            def get_motor_data(self):
                a = self.translate(self.get_only_motors)
                r = self.make_instance_get_value(a)
                try:
                    r = {**a,**r}
                except Exception as e:
                    print(e)
                return r
                
        return StatusWrapper(self.EV3,self.Sensor,self.Motor)
