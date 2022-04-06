def on_button_pressed_a():
    basic.show_string("l")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("l")
    basic.show_string("l")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(69)
basic.show_string("living")

def on_forever():
    if 500 < pins.analog_read_pin(AnalogPin.P0):
        radio.send_string("l")
    basic.pause(1000)
basic.forever(on_forever)
