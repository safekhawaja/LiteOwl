import gpiozero
import time
import os
import AudioProcessing

led = gpiozero.RGBLED(red=9, green=10, blue=11)
mike = gpiozero.Button(2)
buzzer = gpiozero.LED(18)
led.color = (1,0,0)

if button.is_pressed:
    buzzer.on()
    time.sleep(1)
    buzzer.off()
    os.system('Recording.py')

if AudioProcessing.sample_recognize(/Users/Saif/Documents/GitHub/LiteOwl/input.wav) = "owl":
            for n in range(100):
            led.color = (1, n/100, n / 100);
            time.sleep(100)
    elif AudioProcessing.sample_recognize(/Users/Saif/Documents/GitHub/LiteOwl/input.wav) = "red":
            led.color = (1, 0, 0)
            time.sleep(100)

os.remove("input.wav")
