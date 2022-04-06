def on_button_pressed_a():
    serial.write_string("z")
    basic.show_string("R")
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    serial.write_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    serial.write_string("e")
    basic.show_string("e")
    control.reset()
input.on_button_pressed(Button.B, on_button_pressed_b)

serial.redirect_to_usb()
basic.show_string("R")
radio.set_group(69)

def on_forever():
    pass
basic.forever(on_forever)
