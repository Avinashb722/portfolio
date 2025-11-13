#ifndef ROBOT_CONFIG_H
#define ROBOT_CONFIG_H

// Hardware abstraction layer for different platforms
#ifdef ARDUINO
    #include <Arduino.h>
    #define digitalWrite(pin, val) digitalWrite(pin, val)
    #define digitalRead(pin) digitalRead(pin)
    #define pinMode(pin, mode) pinMode(pin, mode)
    #define delay(ms) delay(ms)
    #define delayMicroseconds(us) delayMicroseconds(us)
    #define pulseIn(pin, state) pulseIn(pin, state)
    #define Serial Serial
#else
    // Simulation functions for testing
    void digitalWrite(int pin, int value);
    int digitalRead(int pin);
    void pinMode(int pin, int mode);
    void delay(int ms);
    void delayMicroseconds(int us);
    long pulseIn(int pin, int state);
    
    #define HIGH 1
    #define LOW 0
    #define INPUT 0
    #define OUTPUT 1
    
    typedef struct {
        void (*begin)(int);
        void (*println)(const char*);
    } SerialType;
    extern SerialType Serial;
#endif

#endif