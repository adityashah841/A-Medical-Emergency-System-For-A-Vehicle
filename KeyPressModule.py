import time
import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def GetKey(keyname):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    my_key = getattr(pygame, "K_{}".format(keyname))
    if keyInput [my_key]:
        ans = True
    return ans
def main():
    if GetKey():
        return True

if __name__ == '__main()':
     init()
     while True:
         main()