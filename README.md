# Line Following Robot with Obstacle Avoidance

A C-based autonomous robot that follows lines and avoids obstacles using IR sensors and ultrasonic detection.

## Demo Video

*Upload your demo video to YouTube and replace VIDEO_ID with your actual video ID*

## Gallery

<div align="center">
  <img src="images/robot_front.jpg" alt="Line Following Robot" width="400"/>
</div>

## Features

- **Line Following**: Dual IR sensor system for accurate line tracking
- **Obstacle Avoidance**: Ultrasonic sensor with automatic bypass maneuvers
- **Motor Control**: Precise movement control for smooth navigation

## Hardware Requirements

- Arduino/Microcontroller
- 2x DC Motors with H-Bridge Driver
- 2x IR Sensors
- 1x Ultrasonic Sensor (HC-SR04)
- Chassis and wheels

## Pin Configuration

| Component | Pin |
|-----------|-----|
| Left Motor | 2, 3 |
| Right Motor | 4, 5 |
| IR Sensors | 6, 7 |
| Ultrasonic | 8, 9 |

## Circuit Diagram

*Add circuit diagram image to show wiring connections*

## Quick Start

1. Upload `line_following_robot.c` to your microcontroller
2. Connect hardware according to pin configuration
3. Place robot on a black line track
4. Power on and watch it navigate

## How It Works

The robot uses a priority-based decision system:
1. **Obstacle Detection**: Ultrasonic sensor checks for obstacles first
2. **Line Following**: IR sensors detect line position and adjust motors
3. **Navigation Logic**: Forward, left turn, right turn, or stop based on sensor input

## License

MIT License