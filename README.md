# EV3 Bluetooth Python Interface

This library provides a simple interface for connecting to and controlling a LEGO Mindstorms EV3 robot via Bluetooth using the `ev3_dc` library.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Initialization](#initialization)
  - [Motor Control](#motor-control)
  - [Sensor Control](#sensor-control)
  - [LED Control](#led-control)
  - [Sound Control](#sound-control)
  - [Voice Control](#voice-control)
  - [Status Monitoring](#status-monitoring)

## Installation

To use this library, you need to have the `ev3_dc` library installed. You can install it via pip:

```bash
pip install ev3_dc
```

## Usage

### Initialization

To initialize the connection with the EV3 robot, you need to provide the MAC address of the EV3 brick.

```python
from ev3_bluetooth import EV3_Bluetooth

#Initialize the EV3 Bluetooth connection
ev3_brick = EV3_Bluetooth(macaddress='00:16:53:AB:C3:D4')
```

### Motor Control

Control motors connected to the EV3:

```python
# Initialize motor on port 'A'
motor_A = ev3_brick.Motor(port='A')

# Start the motor
motor_A.run(direction=1, speed=50)

# Stop the motor
motor_A.stop()
```

### Sensor Control
Read data from sensors connected to the EV3:

```python
# Initialize color sensor on port 1
color_sensor = ev3_brick.Sensor(port=1, type='color')

# Get color sensor value
color_value = color_sensor.get_color()

# Initialize touch sensor on port 2
touch_sensor = ev3_brick.Sensor(port=2, type='touch')

# Check if touch sensor is pressed
is_pressed = touch_sensor.is_pressed()
```

### LED Control
Control the integrated LED on the EV3 brick:

```python
# Set LED to red and flash
ev3_brick.Led(color='red', type='flash')

# Turn off the LED
ev3_brick.Led(color='red', type='off')
```
>**Note**: The following feature is currently not functioning properly due to its incomplete development, and there are no plans to finish it.

### Sound Control
Play sounds through the EV3:

```python
s = ev3_brick.Sound(volume=80)
s.play_tone("c")
s.play_sound('path to sound file')
```
>**Note**: The following feature is currently not functioning properly due to its incomplete development, and there are no plans to finish it.

### Voice Control
Interact with the EV3 using voice commands:

```python
#Not realy finished to be used!!!
```

### Status Monitoring
Monitor the status of connected sensors and motors:

```python
# Initialize status monitoring
status = ev3_brick.Status()

# Get sensor and motor data
sensor_data = status.get_sensor_data()
motor_data = status.get_motor_data()

# Print sensor and motor status
print("Sensor Data:", sensor_data)
print("Motor Data:", motor_data)
```
