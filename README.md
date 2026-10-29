# My Hackpad

## Overview
My hackpad features 8 keys, two rotary encoder and an OLED Display. It also uses ////.  
**Work in Progress:** I'll submited the project and build my Hackpad as soon as possible.  
Check my progress on [Stardance](https://stardance.hackclub.com/projects/44913)!

## Features
- 8x MX Switches
- 1x 128x32 OLED Display
- 2x EC11 Rotary Encoders
  
Because I don't have enough pins, just one of the two rotary encoders can send a rotary signal. But you can at least press both of them!

## PCB
I designed my PCB inside KiCad. The libraries I used were from the Hackpad website.

### Schematic

<img width="1446" height="781" alt="Screenshot 2026-10-24 001218" src="https://github.com/user-attachments/assets/0d30c047-267d-489a-b2f2-df4c2261d03f" />

<br>
<br>

### PCB

<img width="919" height="632" alt="Screenshot 2026-10-24 001314" src="https://github.com/user-attachments/assets/19f4add1-b053-4086-8374-246af9139047" />

<br>
<br>

### PCB in 3d

<img width="1117" height="773" alt="Screenshot 2026-10-24 001358" src="https://github.com/user-attachments/assets/93ba9f8b-b2c8-43d7-b150-4a086057aa2d" />

<br>
<br>

## Case

The case consists of the top and bottom plate. The two plates are held together using four M3 screws and four heat-set inserts. The  encoder knobs are based on the [Hack Club knob design](https://github.com/hackclub/hackpad?tab=readme-ov-file). The color scheme is inspired by Teenage Engineering designs.

<img width="1195" height="691" alt="Screenshot 2026-10-24 001435" src="https://github.com/user-attachments/assets/5acb33e7-de89-4f57-9614-b82aa590e3e5" />

## Firmware
The firmware runs on CircuitPython using the KMK fromework. To set it up you need to do this few things:
- Install CircuitPython on your XIAO
- Download the KMK framework and put into the lib folder
- Download the Adafruit CircuitPython Bundle and add `adafruit_displayio_ssd1306` and `adafruit_display_text` to lib
- Upload the code.py file and the lib folder to the root
<br>

It should look like this:
```
CIRCUITPY
├─── code.py
└─── lib/
   ├─── kmk/
   ├─── adafruit_display_text/
   └─── adafruit_displayio_ssd1306/
```

## BOM

| Comment | Designator | Footprint | Quantity |
| :--- | :--- | :--- | :--- |
| Seeed XIAO RP2040 | U1 | XIAO_RP2040 | 1 |
| MX Switch | SW1-SW8 | Button_Switch_Keyboard:SW_KEY_MX | 8 |
| EC11 Rotary Encoder | RE1-RE2 | RotaryEncoder_Switch | 2 |
| 0.91 inch OLED Display | U2 | OLED_128x32 | 1 |
| 1N4148 Diode | D2-D11 | Diode_SMD:D_SOD-123 | 10 |
| M3 Heat-Set Insert | H1-H4 | Hardware | 4 |
| M3x12mm Screw | S1-S4 | Hardware | 4 |

## Next Steps
- Build my Hackpad
<br>
  
It was really fun to make this project and I learned a lot of things. Thanks to Hackclub!
<br>

### Stay tuned for updates!
