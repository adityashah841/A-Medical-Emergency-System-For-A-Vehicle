import KeyPressModule as kp
import time
kp.init()
from AlphaBot import AlphaBot
Ab = AlphaBot()
Ab.stop()

while True:
    if kp.GetKey('LEFT'):
        Ab.left()
        time.sleep(0.3)
        Ab.stop()
    if kp.GetKey('RIGHT'):
        Ab.right()
        time.sleep(0.3)
        Ab.stop()
    if kp.GetKey("UP"):
        Ab.forward()
        time.sleep(0.3)
        Ab.stop()
    if kp.GetKey("DOWN"):
        Ab.backward()
        time.sleep(0.3)
        Ab.stop()