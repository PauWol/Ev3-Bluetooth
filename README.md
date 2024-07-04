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
- [License](#license)

## Installation

To use this library, you need to have the `ev3_dc` library installed. You can install it via pip:

```bash
pip install ev3_dc
```

## Usage

### Initialization

To initialize the connection with the EV3 robot, you need to provide the MAC address of the EV3 brick.

```python
import ev3_dc as ev3

 Initialize the EV3 Bluetooth connection
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
