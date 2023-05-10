try:
  import usocket as socket
except:
  import socket

from machine import Pin, ADC, PWM
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

#ssid = 'Familie'
#password = 'Actar11s pilote G0ld0rak !'
#ssid = 'Livebox-D800'
#password = 'Roxane01'
ssid = 'erable'
password = 'Neirda82!Rukka!'

station = network.WLAN(network.STA_IF)

station.active(True)
if station.active():
    print('True')
else:
    print('False')
  
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led_rouge = Pin(23, Pin.OUT)
# led_rouge_pwm = PWM(Pin(23),5000)
led_blanche = Pin(22, Pin.OUT)
# led_blanche_pwm = PWM(Pin(22),5000)
led_bleu = Pin(21, Pin.OUT)
# led_bleu_pwm = PWM(Pin(21),5000)
led_jaune = Pin(19, Pin.OUT)
# led_jaune_pwm = PWM(Pin(19),5000)


pot_rouge=ADC(Pin(35))           
pot_rouge.width(ADC.WIDTH_12BIT)  
pot_rouge.atten(ADC.ATTN_11DB)

pot_blanc=ADC(Pin(34))           
pot_blanc.width(ADC.WIDTH_12BIT)  
pot_blanc.atten(ADC.ATTN_11DB)

pot_bleu=ADC(Pin(39))           
pot_bleu.width(ADC.WIDTH_12BIT)  
pot_bleu.atten(ADC.ATTN_11DB)

watersensor=ADC(Pin(36))           
watersensor.width(ADC.WIDTH_10BIT)   
watersensor.atten(ADC.ATTN_11DB)         

