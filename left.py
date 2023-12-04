import time

if __name__ == '__main__':
    from AlphaBot import AlphaBot
    Ab = AlphaBot()
    Ab.left()
    time.sleep(0.56)
    Ab.right()
    time.sleep(0.56)
    Ab.stop()