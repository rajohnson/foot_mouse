# foot_mouse

Foot operated buttons/scrollwheel for mouse clicks and a scrolling.

Using a Raspberry Pi Pico with Circuitpython (v7.3.3)


                    ┌─────────────────┐
    GP2         ┌───┤                 ├───┐
    ────────────┤ A │                 │ Sw│
                └───┤                 ├───┘
                    │                 │
    GND         ┌───┤     Rotary      │
    ────────────┤ C │     Encoder     │
                └───┤    (top view)   │
                    │    987-1188-ND  │
    GP3         ┌───┤                 ├───┐
    ────────────┤ B │                 │ Sw│
                └───┤                 ├───┘
                    └─────────────────┘


                    ┌──────────────────
                    │
                    │
               ┌────┴─────────────────────┐
           ┌───┤                          │
           │ NC│                          │
           └───┤     Momentary Switch     │
               │        V-156-1C25        │
    GP0    ┌───┤         Z5168-ND         │
    ───────┤ NO│                          │
           └───┤                          │
               └───────────────┬─────┬────┘
    GND                        │ COM │
    ───────────────────────────┴─────┘
