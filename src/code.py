import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.GP0)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    led.value = switch.value
