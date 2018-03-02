from mqtt import MQTTClient
from network import WLAN
import machine
import time
from SI7006A20 import SI7006A20

t_sensor = SI7006A20()
global x

class Pycom1:

    def __init__(self):
        self.x = '0'

    def sub_cb(self, topic, msg):
        self.x = str(msg)

    def wifi_enable(self):
        wlan = WLAN(mode=WLAN.STA)
        wlan.connect("thingQbator", auth=(WLAN.WPA2, "C1sco12345"), timeout=5000)

        while not wlan.isconnected():
            machine.idle()
        print("\nConnected to Wifi\n")

    def mqtt_enable(self):
        self.client = MQTTClient("pycom1", "173.39.91.118", port=1883)
        self.client.set_callback(self.sub_cb)
        self.client.connect()
        self.client.subscribe(topic="qbator/call_temp")

    def run(self):
        while True:
            self.client.check_msg()
            if self.x.strip("b'") == '1':
                print(self.x)
                self.client.publish(topic="qbator/temp", msg=str(int(t_sensor.temperature())))
                self.client.publish(topic="qbator/hum", msg=str(int(t_sensor.humidity())))
            else:
                continue
