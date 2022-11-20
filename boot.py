import digitalio
import time
import usb_hid
import usb_midi
import usb_cdc
import storage
import board
import supervisor

# led om of stuff
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True


# GP2 switch 2nd 
switch = digitalio.DigitalInOut(board.GP2)
switch.direction = switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# wait for the keypress for enabling usb mass storage and com ports 
start = time.monotonic()
while(time.monotonic() - start < 1):
        if  not switch.value:  # if button pressed
            print("key press detected")
            led.value = False
            break
else:
    storage.disable_usb_drive()
    usb_midi.disable()
    usb_cdc.disable()
    supervisor.set_usb_identification("Logitech Inc.","USB Receiver",0x046D,0xC534)     
    print("key not pressed in ")
    led.value = False