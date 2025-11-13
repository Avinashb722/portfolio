#include <stdio.h>
#include <stdbool.h>

// Pin definitions
#define LEFT_MOTOR_PIN1 2
#define LEFT_MOTOR_PIN2 3
#define RIGHT_MOTOR_PIN1 4
#define RIGHT_MOTOR_PIN2 5
#define LEFT_IR_SENSOR 6
#define RIGHT_IR_SENSOR 7
#define ULTRASONIC_TRIG 8
#define ULTRASONIC_ECHO 9

// Constants
#define OBSTACLE_DISTANCE 15  // cm
#define MOTOR_SPEED 150

// Motor control functions
void moveForward() {
    digitalWrite(LEFT_MOTOR_PIN1, HIGH);
    digitalWrite(LEFT_MOTOR_PIN2, LOW);
    digitalWrite(RIGHT_MOTOR_PIN1, HIGH);
    digitalWrite(RIGHT_MOTOR_PIN2, LOW);
}

void turnLeft() {
    digitalWrite(LEFT_MOTOR_PIN1, LOW);
    digitalWrite(LEFT_MOTOR_PIN2, LOW);
    digitalWrite(RIGHT_MOTOR_PIN1, HIGH);
    digitalWrite(RIGHT_MOTOR_PIN2, LOW);
}

void turnRight() {
    digitalWrite(LEFT_MOTOR_PIN1, HIGH);
    digitalWrite(LEFT_MOTOR_PIN2, LOW);
    digitalWrite(RIGHT_MOTOR_PIN1, LOW);
    digitalWrite(RIGHT_MOTOR_PIN2, LOW);
}

void stopMotors() {
    digitalWrite(LEFT_MOTOR_PIN1, LOW);
    digitalWrite(LEFT_MOTOR_PIN2, LOW);
    digitalWrite(RIGHT_MOTOR_PIN1, LOW);
    digitalWrite(RIGHT_MOTOR_PIN2, LOW);
}

void avoidObstacle() {
    stopMotors();
    delay(500);
    
    // Turn right to avoid obstacle
    digitalWrite(LEFT_MOTOR_PIN1, HIGH);
    digitalWrite(LEFT_MOTOR_PIN2, LOW);
    digitalWrite(RIGHT_MOTOR_PIN1, LOW);
    digitalWrite(RIGHT_MOTOR_PIN2, HIGH);
    delay(800);
    
    // Move forward
    moveForward();
    delay(1000);
    
    // Turn left to get back on track
    digitalWrite(LEFT_MOTOR_PIN1, LOW);
    digitalWrite(LEFT_MOTOR_PIN2, HIGH);
    digitalWrite(RIGHT_MOTOR_PIN1, HIGH);
    digitalWrite(RIGHT_MOTOR_PIN2, LOW);
    delay(800);
}

int getDistance() {
    digitalWrite(ULTRASONIC_TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(ULTRASONIC_TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(ULTRASONIC_TRIG, LOW);
    
    long duration = pulseIn(ULTRASONIC_ECHO, HIGH);
    int distance = duration * 0.034 / 2;
    return distance;
}

void setup() {
    // Initialize pins
    pinMode(LEFT_MOTOR_PIN1, OUTPUT);
    pinMode(LEFT_MOTOR_PIN2, OUTPUT);
    pinMode(RIGHT_MOTOR_PIN1, OUTPUT);
    pinMode(RIGHT_MOTOR_PIN2, OUTPUT);
    pinMode(LEFT_IR_SENSOR, INPUT);
    pinMode(RIGHT_IR_SENSOR, INPUT);
    pinMode(ULTRASONIC_TRIG, OUTPUT);
    pinMode(ULTRASONIC_ECHO, INPUT);
    
    Serial.begin(9600);
}

void loop() {
    int distance = getDistance();
    
    // Check for obstacles first
    if (distance < OBSTACLE_DISTANCE) {
        avoidObstacle();
        return;
    }
    
    // Read IR sensors for line following
    bool leftSensor = digitalRead(LEFT_IR_SENSOR);
    bool rightSensor = digitalRead(RIGHT_IR_SENSOR);
    
    // Line following logic
    if (!leftSensor && !rightSensor) {
        // Both sensors on line - move forward
        moveForward();
    }
    else if (!leftSensor && rightSensor) {
        // Left sensor on line - turn left
        turnLeft();
    }
    else if (leftSensor && !rightSensor) {
        // Right sensor on line - turn right
        turnRight();
    }
    else {
        // Both sensors off line - stop
        stopMotors();
    }
    
    delay(50);
}