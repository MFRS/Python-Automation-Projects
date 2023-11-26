import vgamepad as vg
from time import sleep
import keyboard
import threading
from time import sleep
from threading import Event, Thread
import pyautogui
gamepad = vg.VX360Gamepad()
lock = threading.Lock()
code_active = False


condition = Event()


def do_sth():
    print("truckin' ...")


def check_sth():
    while not condition.is_set():
        sleep(0.25)
        do_sth()  # Do something everytime the condition is not set.

    print("Condition met, ending.")


def disableControllers():
    gamepad.left_joystick(0, 0)  # values between -32768 and 32767
    gamepad.right_joystick(0, 0)  # values between -32768 and 32767
    gamepad.update()
    gamepad.reset()
    condition.set()


def on_key_press(event):
    global code_active

    if event.name == "t":
        code_active = not code_active
        if code_active:
            condition.clear()
            Thread(target=lambda: moveforward([0, 10000]), args=()).start()
        else:
            disableControllers()

    if event.name == "r":
        code_active = not code_active
        if code_active:
            condition.clear()
            Thread(target=lambda: rotate360([9000, 0], [-10000, 0]), args=()).start()
            # !Original values
            # Thread(target=lambda: rotate360([10000, 0], [-9000, 0]), args=()).start()
        else:
            disableControllers()
    if event.name == "g":
        code_active = not code_active
        if code_active:
            condition.clear()
            Thread(target=lambda: moveforward([0, -10000]), args=()).start()
        else:
            disableControllers()
    if event.name == "y":
        code_active = not code_active
        if code_active:
            condition.clear()
            # Thread(target=lambda: rotate360([0, 0], [9000, 0]), args=()).start()
            Thread(target=lambda: rotate360(
                [-10000, 0], [9000, 0]), args=()).start()
        else:
            disableControllers()
    if event.name == "f":
        code_active = not code_active
        if code_active:
            condition.clear()
            Thread(target=lambda: moveforward([-10000, 0]), args=()).start()
        else:
            disableControllers()
    if event.name == "h":
        code_active = not code_active
        if code_active:
            condition.clear()
            Thread(target=lambda: moveforward([10000, 0]), args=()).start()
        else:
            disableControllers()
    if event.name == "u":
        code_active = not code_active
        if code_active:
            condition.clear()
            Thread(target=lambda: rotate360(
                [0, 8600], [0, -9000]), args=()).start()
        else:
            disableControllers()
    if event.name == "o":
        code_active = not code_active
        if code_active:
            condition.clear()
            Thread(target=lambda: scrollMiddleMouseButton(), args=()).start()
        else:
            # pass
            disableControllers()


def scrollMiddleMouseButton():
    # incremental function which slowly increases the scroll speed
    for x in range(10000):
        while not condition.is_set():
            currentValue = int(-20)
            pyautogui.scroll(currentValue)
            sleep(0.01)


def rotate360(left, right):
    while not condition.is_set():
        print("r start")
        # values between -32768 and 32767
        gamepad.left_joystick(x_value=left[0], y_value=left[1])
        sleep(0.2)
        # values between -32768 and 32767
        gamepad.right_joystick(x_value=right[0], y_value=right[1])
        gamepad.update()  # send the updated state to the computer
    disableControllers()
    print("r over")
    # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button
    # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button


def moveforward(vals):
    while not condition.is_set():
        # values between -32768 and 32767
        gamepad.left_joystick(x_value=vals[0], y_value=vals[1])
        gamepad.update()  # send the updated state to the computer
        print("t start")

    disableControllers()
    print("t over")
    # for xva in range(10000):
    # for xv in range(10000):
    # gamepad.right_joystick(x_value=xv, y_value=xv)  # values between -32768 and 32767
    # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button
    # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button


def movesideways(vals):
    global code_active
    try:
        while code_active == True:
            # gamepad.left_joystick(x_value=vals[0], y_value=vals[1])
            # gamepad.update()  # send the updated state to the computer
            print("Running...")
        else:
            # gamepad.reset()
            print("Stopping...")

    except KeyboardInterrupt:
        print("test")
        sleep(3)
        keyboard.on_press(on_key_press)
        keyboard.wait()


# scrollMiddleMouseButton()
# sleep(10)
# moveforward2([0,10000])
keyboard.on_press(on_key_press)
# !Rotate around same axis
# rotate360([8600,0],[9000,0])

# !Rotate more widely
# rotate360([8550,0],[9000,0])
# moveforward()
keyboard.wait()
