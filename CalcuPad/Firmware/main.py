import board
import digitalio
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC

# Initialize keyboard
keyboard = KMKKeyboard()

# Define rows and columns using GP names
keyboard.row_pins = [board.GP29, board.GP6, board.GP7, board.GP0]
keyboard.col_pins = [board.GP4, board.GP2, board.GP1]

# Use matrix scanner
keyboard.matrix = MatrixScanner(
    row_pins=keyboard.row_pins,
    col_pins=keyboard.col_pins
)

# Set up LED on GP29
led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT

# Function to turn the LED on
def turn_led_on():
    led.value = True

# Function to turn the LED off
def turn_led_off():
    led.value = False

# Hook to turn LED on when any key is pressed
def on_press(key, keyboard, *args, **kwargs):
    turn_led_on()

# Hook to turn LED off when any key is released
def on_release(key, keyboard, *args, **kwargs):
    turn_led_off()

# Register the hooks
keyboard.on_press_handler.append(on_press)
keyboard.on_release_handler.append(on_release)

# Keymap: 10 number keys in calculator layout
keyboard.keymap = [
    [
        KC.N7,   KC.N8,   KC.N9,     # Row 0
        KC.N4,   KC.N5,   KC.N6,     # Row 1
        KC.N1,   KC.N2,   KC.N3,     # Row 2
        KC.NO,   KC.N0,   KC.NO,     # Row 3
    ]
]

# Start the keyboard
if __name__ == '__main__':
    keyboard.go()