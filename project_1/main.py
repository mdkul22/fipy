from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from MPL3115A2 import MPL3115A2
from pysense import Pysense
import time
py = Pysense()
acc = LIS2HH12()
temp = SI7006A20()
prs = MPL3115A2(mode=0)

while True:
   pitch = acc.pitch()
   roll = acc.roll()

   t = temp.temperature()
   h = temp.humidity()

   alt = prs.altitude()
   t2 = prs.temperature()

   print('pitch = {}, roll = {},'.format(pitch,roll))
   print('temperature = {}, humidity = {}'.format(t, h))
   print('altitude = {}, temperature = {} \n' .format(alt,t2))
   time.sleep_ms(100)
