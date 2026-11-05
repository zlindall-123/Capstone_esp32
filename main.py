from machine import Pin, I2C
import time
import network
from sensors import sensors

# Lets you know the code was sent
class command_sent():
    led = Pin(2, Pin.OUT)
    for i in range(10):
        led.on()
        time.sleep(.025)
        led.off()
        time.sleep(.025)

#States if and Sensors are connected and where
class I2C_connections():
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # default ESP32 I2C pins
    devices = i2c.scan()

    if devices:
        for d in devices:
            print("Found device at address:", hex(d))
    else:
        print("No I2C devices found")

#Tell you details about networks detectable
class network_connections_options():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    for ssid, bssid, channel, rssi, auth, hidden in wlan.scan():
        print("name:   ", ssid.decode(), "\nsignal: ", rssi, "dBm \nchannel:", channel, "\n")


#command_sent()
#I2C_connections()
#network_connections_options()

test = sensors()

test.H20()