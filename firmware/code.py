import board
import busio
import time
import usb_cdc

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.encoder import EncoderHandler
from kmk.extensions.display import Display
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()
encoder = EncoderHandler()
keyboard.extensions.append(encoder)

i2c = busio.I2C(board.D5, board.D4)
display_driver = SSD1306(i2c, width=128, height=32)
display = Display(display=display_driver)
keyboard.extensions.append(display)

text = "Hi Malik!"
x = (128 - len(text) * 6) // 2

display_driver.fill(0)
display_driver.text(text, x, 12, 1)
display_driver.show()

startup_until = time.monotonic() + 2
intro_done = False

current_time = "00:00"
current_song = "No song"
cpu_usage = 0
ram_usage = 0
display_mode = 0
last_update = time.monotonic()
update_interval = 1.0

def update_display():
    display_driver.fill(0)

    if not intro_done:
        content = text
    elif display_mode == 0:
        content = current_time
    elif display_mode == 1:
        content = current_song
    elif display_mode == 2:
        content = f"CPU: {cpu_usage}% RAM: {ram_usage}%"

    x = (128 - len(content) * 6) // 2
    display_driver.text(content, x, 12, 1)
    display_driver.show()

def update_system_info():
    global current_time, current_song, cpu_usage, ram_usage
    if usb_cdc.data and usb_cdc.data.in_waiting > 0:
        try:
            line = usb_cdc.data.readline().decode('utf-8').strip()
        except (UnicodeDecodeError, AttributeError):
            return

        prefix, separator, value = line.partition(":")
        if not separator:
            return

        value = value.strip()
        try:
            if prefix == "TIME":
                current_time = value or "00:00"
            elif prefix == "SONG":
                current_song = value or "No song"
            elif prefix == "CPU":
                cpu_usage = max(0, min(100, int(value)))
            elif prefix == "RAM":
                ram_usage = max(0, min(100, int(value)))
        except ValueError:
            return

def reset_display_data():
    global current_time, current_song, cpu_usage, ram_usage
    current_time = "00:00"
    current_song = "No song"
    cpu_usage = 0
    ram_usage = 0
    update_display()

def cycle_display_mode():
    global display_mode
    display_mode = (display_mode + 1) % 3
    update_display()

TOGGLE_DISPLAY = KC.Macro(cycle_display_mode)
PLAY_PAUSE = KC.Macro(reset_display_data, KC.MPLY)
SLEEP = KC.Macro(reset_display_data, KC.SLEP)
update_display()

keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D3, board.D6, board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        TOGGLE_DISPLAY, KC.NO, KC.NO, KC.MO(1),
        KC.MPRV, PLAY_PAUSE, KC.MNXT, KC.MUTE,
        KC.CALC, KC.LCTRL(KC.LSHIFT(KC.ESC)), KC.PSCR, SLEEP
    ],
    [
        KC.TRNS, KC.NO, KC.NO, KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ]
]

encoder.pins = (
    (board.D9, board.D10),
)

encoder.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.BRID, KC.BRIU),)
]

@keyboard.before_matrix_scan
def background_tasks(keyboard):
    global last_update, intro_done
    if not intro_done and time.monotonic() >= startup_until:
        intro_done = True
        update_display()
    update_system_info()
    now = time.monotonic()
    if intro_done and (now - last_update >= update_interval):
        last_update = now
        update_display()

if __name__ == "__main__":
    keyboard.go()
