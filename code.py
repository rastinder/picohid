print("Hello World!")
import os
import ipaddress
import wifi
import socketpool
import board
import digitalio
import time
import adafruit_requests as requests
import ssl
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard

# led om of stuff
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
#led.value = True
# key board mouse stuff
mouse = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

print()
print("Connecting to WiFi")
ipv4 =  ipaddress.IPv4Address(os.getenv('IP'))
netmask =  ipaddress.IPv4Address("255.255.255.0")
gateway =  ipaddress.IPv4Address("192.168.1.1")
wifi.radio.set_ipv4_address(ipv4=ipv4,netmask=netmask,gateway=gateway)
#wifi.radio.set_ipv4_address(ipv4="192.168.1.101",netmask="255.255.255.0",gateway="192.168.1.1")

#wifi.stop_dhcp()
#  connect to your SSID WIFI_PASSWORD
while not wifi.radio.ipv4_address:
    try:
        wifi.radio.connect('fearless','qweqweqwe')
    except:
        pass
    try:
        wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))
    except:
        print("waiting for WiFi")
        led.value = True
        time.sleep(1)
        led.value = False
    
print("Connected to WiFi")
pool  = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
#print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
# tell me m online
sendURL = 'https://api.telegram.org/bot' + '1331062094:AAEsirbmiJk1RsPLsbHxa2Kh5KjF6jtmMjc' + '/sendMessage'
chatId = '706316494'
requests = requests.Session(pool, ssl.create_default_context())
response = requests.post(sendURL + "?chat_id=" + str(chatId) + "&text=" + str(wifi.radio.ipv4_address) + ' is up')
response.close()
#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
#ipv4 = ipaddress.ip_address("8.8.4.4")
#print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
#time.sleep(0.9)


HOST = str(wifi.radio.ipv4_address)
PORT = 4455
TIMEOUT = None

BACKLOG = 2
MAXBUF = 1
buf = bytearray(MAXBUF)

#server_ipv4 = ipaddress.ip_address(pool.getaddrinfo(HOST, PORT)[0][4][0])
#print("Server ping", server_ipv4, wifi.radio.ping(server_ipv4), "ms")

# code to send
#print("Received", buf[:name], name, "bytes from", addr)
#name = s.sendto(buf[:name], addr)
#print("Sent", buf[:name], name, "bytes to", addr)
keyboardkeys = {
"a": 0x04,
"b": 0x05,
"c": 0x06,
"d": 0x07,
"e": 0x08,
"f": 0x09,
"g": 0x0a,
"h": 0x0b,
"i": 0x0c,
"j": 0x0d,
"k": 0x0e,
"l": 0x0f,
"m": 0x10,
"n": 0x11,
"o": 0x12,
"p": 0x13,
"q": 0x14,
"r": 0x15,
"s": 0x16,
"t": 0x17,
"u": 0x18,
"v": 0x19,
"w": 0x1a,
"x": 0x1b,
"y": 0x1c,
"z": 0x1d,
"1": 0x1e,
"2": 0x1f,
"3": 0x20,
"4": 0x21,
"5": 0x22,
"6": 0x23,
"7": 0x24,
"8": 0x25,
"9": 0x26,
"0": 0x27,
"A" : 0x04,
"B" : 0x05,
"C" : 0x06,
"D" : 0x07,
"E" : 0x08,
"F" : 0x09,
"G" : 0x0A,
"H" : 0x0B,
"I" : 0x0C,
"J" : 0x0D,
"K" : 0x0E,
"L" : 0x0F,
"M" : 0x10,
"N" : 0x11,
"O" : 0x12,
"P" : 0x13,
"Q" : 0x14,
"R" : 0x15,
"S" : 0x16,
"T" : 0x17,
"U" : 0x18,
"V" : 0x19,
"W" : 0x1A,
"X" : 0x1B,
"Y" : 0x1C,
"Z" : 0x1D,
"ctrl" : 0xE0,
"alt" : 0xE2,
"shift":  0xE1,
"enter" : 0x28,
"win" : 0xE3,
"Return" : 0x28,
"Escape" : 0x29,
"Backspace" : 0x2A,
"Tab" : 0x2B,
"Spacebar" : 0x2C,
"Minus" : 0x2D,
"Equals" : 0x2E,
"LeftSquareBracket" : 0x2F,
"RightSquareBracket" : 0x30,
"Backslash" : 0x31,
"NonUsHash" : 0x32,
"Semicolon" : 0x33,
"Quote" : 0x34,
"GraveAccent" : 0x35,
"Comma" : 0x36,
"Period" : 0x37,
"Slash" : 0x38,
"CapsLock" : 0x39,
"F1" : 0x3A,
"F2" : 0x3B,
"F3" : 0x3C,
"F4" : 0x3D,
"F5" : 0x3E,
"F6" : 0x3F,
"F7" : 0x40,
"F8" : 0x41,
"F9" : 0x42,
"F10" : 0x43,
"F11" : 0x44,
"F12" : 0x45,
"PrintScreen" : 0x46,
"ScrollLock" : 0x47,
"Pause" : 0x48,
"Insert" : 0x49,
"Home" : 0x4A,
"PageUp" : 0x4B,
"Delete" : 0x4C,
"End" : 0x4D,
"PageDown" : 0x4E,
"RightArrow" : 0x4F,
"LeftArrow" : 0x50,
"DownArrow" : 0x51,
"UpArrow" : 0x52,
"KeypadNumLock" : 0x53,
"KeypadDivide" : 0x54,
"KeypadMultiply" : 0x55,
"KeypadAdd" : 0x56,
"KeypadSubtrace" : 0x57,
"KeypadReturn" : 0x58,
"Keypad1" : 0x59,
"Keypad2" : 0x5A,
"Keypad3" : 0x5B,
"Keypad4" : 0x5C,
"Keypad5" : 0x5D,
"Keypad6" : 0x5E,
"Keypad7" : 0x5F,
"Keypad8" : 0x60,
"Keypad9" : 0x61,
"Keypad0" : 0x62,
"enter": 0x28,
"escape": 0x29,
"backspace": 0x2a,
"tab": 0x2b,
"spacebar": 0x2c,
"minus": 0x2d,
"equals": 0x2e,
"left_bracket": 0x2f,
"right_bracket": 0x30,
"backslash": 0x31,
"pound": 0x32,
"semicolon": 0x33,
"quote": 0x34,
"grave_accent": 0x35,
"comma": 0x36,
"period": 0x37,
"forward_slash": 0x38,
"caps_lock": 0x39,
"f1": 0x3a,
"f2": 0x3b,
"f3": 0x3c,
"f4": 0x3d,
"f5": 0x3e,
"f6": 0x3f,
"f7": 0x40,
"f8": 0x41,
"f9": 0x42,
"f10": 0x43,
"f11": 0x44,
"f12": 0x45,
"print_screen": 0x46,
"scroll_lock": 0x47,
"pause": 0x48,
"insert": 0x49,
"home": 0x4a,
"page_up": 0x4b,
"delete": 0x4c,
"end": 0x4d,
"page_down": 0x4e,
"right_arrow": 0x4f,
"left_arrow": 0x50,
"down_arrow": 0x51,
"up_arrow": 0x52,
"keypad_numlock": 0x53,
"keypad_forward_slash": 0x54
}
'''''
print("Create UDP Server socket")
s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
s.settimeout(TIMEOUT)
s.bind((HOST, PORT))
buf = bytearray(MAXBUF)
'''''
print("Create TCP Client Socket")
s = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
s.settimeout(TIMEOUT)

s.bind((HOST, PORT))
s.listen(BACKLOG)

print("Accepting connections")
conn, addr = s.accept()
conn.settimeout(TIMEOUT)
print("Accepted from", addr)

# adjust angle
angle_table = [1.146666667,1.104,1.08,1.066964286,1.047272727,1.027692308,0.9947089947,0.9835294118,0.9620253165,0.9190207156,0.9050966608,0.8817891374,0.8624260355,0.844137931]
def cal_angle(newX):
    stroke = newX // 50
    if stroke < len(angle_table):
        return newX * angle_table[stroke]
    else:
        return newX * 0.8036144578

print("ready to recieve :)")
for i in range(1,6):
    led.value = True
    time.sleep(0.02)
    led.value = False
    time.sleep(0.02)
name = ''
text= ''
name1 = ''

while True:
        try:
            #name = conn.recv_into(buf, MAXBUF)
            while True:
                name1 = conn.recv_into(buf)
                if name1:
                    data = buf[:name1].decode("utf-8")
                    if data == "@":
                        name1 = ''
                        break
                    else:
                        name += data
           # name = conn.recv_into(buf)
        except OSError:
            print("Accepting connection")
            conn, addr = s.accept()
            conn.settimeout(TIMEOUT)
        if name:
            led.value = True
            #start = time.monotonic()
            #name = buf[:name].decode("utf-8")
            print(name)
            nn = name.split(",")
            #pc = pc_mouse[nn[0]]
            device = int(nn[1]) # keyboard or mouse
            if device == 9:    
                    print('9')                                                                 # aim bot 
                    mouse.move(int(cal_angle(int(nn[2]))), int(cal_angle(int(nn[3]))))
                    mouse.click(Mouse.LEFT_BUTTON)
                    conn.send(b's')
            elif device == 8:    
                print('8')                                                           # mousemoveonly
                mouse.move(int(cal_angle(int(nn[2]))), int(cal_angle(int(nn[3]))))
            elif device == 4:                                                               # main menu mouse move
                if abs(int(nn[2])) < 15 and abs(int(nn[3])) < 15:
                    mouse.move(int(nn[2]), int(nn[3]))
                else:
                    mouse.move(int(int(nn[2])* 0.392541708), int(int(nn[3])* 0.392927308))
            elif device == 3 or device == 7 or device == 6:                                 # keyboard moments
                #print(f'device = , {device}')
                #print(nn[2])
                if int(nn[3]) == 7 or device == 7:
                    kbd.release(keyboardkeys[nn[2]])
                    #print(f'krlease =   {nn[2]}')
                elif int(nn[3]) == 6 or device == 6:
                    print(f'kpress =  + {nn[2]}')
                    kbd.press(keyboardkeys[nn[2]])
                else:
                    #print(f'ksend =  + {nn[2]}')
                    kbd.send(keyboardkeys[nn[2]])
            elif device == 1:
                mouse.release(Mouse.LEFT_BUTTON)
            elif device == 5:
                mouse.press(Mouse.LEFT_BUTTON)
            else: # device == 2
                mouse.move(int(int(nn[2])* 0.392541708), int(int(nn[3])* 0.392927308))
                mouse.click(Mouse.LEFT_BUTTON)
                #print(ff'wrong device = {device}')
            #conn.send(str("done").encode('utf-8'))
            # print(f'name={name} device = {device}')
            #print(f'sent > {name} in {time.monotonic() - start}')
            led.value = False
            name = ''
