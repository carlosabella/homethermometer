import time
import adafruit_dht
import board
from beebotte import *

#Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)

### Data from Bebotte account
bbt = BBT('uH3mHFgKF4E3KHjaMFLza6R3', 'wUz6vUMvGyZsblX1MDhxnWaFLTwzq9p8')

period = 1800 ## Reading every * seconds

temp_resource   = Resource(bbt, 'MainRoom', 'temperature')
humid_resource  = Resource(bbt, 'MainRoom', 'humidity')

def run():
  while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        #print ("Temp: {0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        try:
          #Send temperature to Beebotte
          temp_resource.write(temperature)
          #Send humidity to Beebotte
          humid_resource.write(humidity)
        except RuntimeError as error:
          print ("Error while writing to Beebotte")

    except RuntimeError as error:
        print (error.args[0]) # Errors happen fairly often, DHT's are hard to read, just keep going

    time.sleep( period )

run()
