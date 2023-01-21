import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_debouncer import Debouncer
import rotaryio

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

switch_pin = DigitalInOut(board.GP0)
switch_pin.direction = Direction.INPUT
switch_pin.pull = Pull.UP
switch = Debouncer(switch_pin)

encoder = rotaryio.IncrementalEncoder(board.GP2, board.GP3)
encoder_last = encoder.position

mouse = Mouse(usb_hid.devices)

while True:
    switch.update()
    led.value = not switch.value

    if switch.value:
        mouse.release(Mouse.LEFT_BUTTON)
    else:
        mouse.press(Mouse.LEFT_BUTTON)

    if encoder.position != encoder_last:
        delta = encoder_last - encoder.position
        encoder_last = encoder.position
        mouse.move(wheel=delta)
