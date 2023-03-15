import pyttsx3
import time

engine = pyttsx3.init()
engine.startLoop(False)

engine.say("knock knock, who's there")

start = time.time()

while time.time() - start < 1:
    engine.iterate()
    time.sleep(.01)

engine.stop()
engine.say('interrupting cow!')

while time.time() - start < 10:
    engine.iterate()
    time.sleep(.01)

engine.endLoop()