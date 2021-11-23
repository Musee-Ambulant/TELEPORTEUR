from . import info
import pyautogui as pyauto, time


def click_on(png_name):
    my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
    while my_location is None:
        my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
        print(png_name + " could not be found")
    my_location = pyauto.center(my_location)
    pyauto.click(my_location)


def left_click_on(png_name):
    my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
    while my_location is None:
        my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
        print(png_name + " could not be found")
    my_location = pyauto.center(my_location)
    pyauto.click(my_location, button="right")


def double_click_on(png_name):
    my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
    while my_location is None:
        my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
        print(png_name + " could not be found")
    my_location = pyauto.center(my_location)
    pyauto.doubleClick(my_location)


def triple_click_on(png_name):
    my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
    while my_location is None:
        my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
        print(png_name + " could not be found")
    my_location = pyauto.center(my_location)
    pyauto.tripleClick(my_location)


def while_its_there(png_name):
    my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
    while my_location:
        my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
        print(png_name + " is found")
        time.sleep(0.5)


def while_its_not_there(png_name):
    my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
    while my_location is None:
        my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
        print(png_name + " not found")
        time.sleep(0.5)


def is_on_screen(png_name):
    is_there = None
    my_location = pyauto.locateOnScreen(png_name, confidence=0.9)
    if my_location != None:
        is_there = True
    else:
        is_there = False
    return is_there


def write(to_write):
    pyauto.write(to_write)


def ask_current_friend_name():
    current_friend_name = pyauto.prompt(text="Entrez le nom de l'ami", title="Nom", default="Mon ami")
    info.current_friend_name = current_friend_name.replace(" ", "")


def alert_place_object():
    pyauto.alert(text="Placez l'objet de {} dans le téléporteur".format(info.current_friend_name), button="Continuer")


def confirm():
    return pyauto.confirm(text='Voulez-vous effectuer un autre scan', title='confirmation', buttons=['Oui', 'Non'])


def press(key):
    pyauto.press(key)
    return


def hotkey(key1, key2):
    pyauto.hotkey(key1, key2)
    return
