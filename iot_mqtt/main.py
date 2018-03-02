from mqtt_enable import Pycom1

device = Pycom1()
device.wifi_enable()
device.mqtt_enable()
device.run()
