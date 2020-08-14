import gpiozero
import time
import os

led = gpiozero.RGBLED(red=9, green=10, blue=11)
led.color = (1,0,0)

if input > x
    output high to noise machine (to demonstrate reception)
    execute Recording.py (which will return filename)

execute AudioProcessing.py, store output

        if output x
            for n in range(100):
            led.color = (1, n/100, n / 100);
            time.sleep(100)

        elif output y
            led.color = (1, 0, 0)
            time.sleep(100)

    else pass
"""
    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
"""

os.remove("input.wav")
