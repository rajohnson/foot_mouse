import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

switch_pin = DigitalInOut(board.GP0)
switch_pin.direction = Direction.INPUT
switch_pin.pull = Pull.UP
switch = Debouncer(switch_pin)

while True:
    switch.update()
    led.value = switch.value
    switch.update()
