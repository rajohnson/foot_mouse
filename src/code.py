import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_debouncer import Debouncer

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

switch_pin = DigitalInOut(board.GP0)
switch_pin.direction = Direction.INPUT
switch_pin.pull = Pull.UP
switch = Debouncer(switch_pin)

mouse = Mouse(usb_hid.devices)

while True:
    switch.update()
    led.value = switch.value

    if switch.value:
        mouse.press(Mouse.LEFT_BUTTON)
    else:
        mouse.release(Mouse.LEFT_BUTTON)
