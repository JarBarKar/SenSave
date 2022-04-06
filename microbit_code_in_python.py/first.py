def on_button_pressed_a():
    basic.show_string("f")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("f")
    basic.show_string("f")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(69)
basic.show_string("f")

def on_forever():
    if 500 < pins.analog_read_pin(AnalogPin.P0):
        radio.send_string("f")
    basic.pause(1000)
    control.reset()
basic.forever(on_forever)
