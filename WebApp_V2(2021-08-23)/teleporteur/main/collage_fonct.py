import time
from shutil import copy, move
import glob, os
from time import sleep

import pyautogui

from main.app_teleporteur import exscan_fonction, pyautogui_fonction


def copy_3D_to_cleanupScan(groupe):
    print(groupe)
    dst_dir = "C:/Users/musee/Documents/teleporteur/main/CleanupScan3D/input"
    print("****")
    for obj in glob.glob("C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(groupe.ecole) + "/" + str(
            groupe) + "/*.obj"):
        print("copying : " + obj)
        copy(obj, dst_dir)

    return


def copy_cleanupScanOutput_to_importUE4(groupe):
    print(groupe)
    empty_importUE4()
    dst_dir = "C:/Users/musee/Desktop/ImportToUnreal"
    print("****")
    for obj in glob.glob(
            "C:/Users/musee/Documents/teleporteur/main/CleanupScan3D/output/*.obj"):
        print("copying : " + obj)
        move(obj, dst_dir)
    for mtl in glob.glob(
            "C:/Users/musee/Documents/teleporteur/main/CleanupScan3D/output/*.mtl"):
        print("removing: " + mtl)
        os.remove(mtl)
    return


def mk_UE4_photo_dir(groupe):
    ecole_path = "main/static/main/photos/" + str(groupe.ecole)
    groupe_path = "main/static/main/photos/" + str(groupe.ecole) + "/" + str(groupe)
    if not os.path.exists(ecole_path):
        os.mkdir(ecole_path)
    if not os.path.exists(groupe_path):
        os.mkdir(groupe_path)
    dir = os.listdir(groupe_path)
    print(dir)
    if os.path.exists(groupe_path):
        return
    os.mkdir(groupe_path)


def empty_importUE4():
    for file in glob.glob("C:/Users/musee/Desktop/ImportToUnreal/*"):
        print("Deleting: " + file)
        os.remove(file)

    return


def empty_input():
    for file in glob.glob("C:/Users/musee/Documents/teleporteur/main/CleanupScan3D/input/*"):
        print("removing: " + file + " from input folder (This is normal behavior...)")
        os.remove(file)

    return


def move_UE4_screenshots(groupe):
    photos = glob.glob("C:/Users/musee/Documents/Collage3/Collage3D_V3/Saved/Screenshots/Windows/*.png")
    dst_dir = "main/static/main/photos/" + str(groupe.ecole) + "/" + str(groupe)
    for photo in photos:
        print(photo + "123")
        if photo not in dst_dir:
            move(photo, dst_dir)
    return


def start_in_standalone():
    try:
        pyautogui_fonction.click_on("main/app_teleporteur/PLayStandalone.PNG")
        time.sleep(0.5)
        if pyautogui_fonction.is_on_screen("main/app_teleporteur/SaveSelected1.PNG"):
            pyautogui_fonction.click_on("main/app_teleporteur/SaveSelected1.PNG")
    except:

        try:
            pyautogui_fonction.click_on("main/app_teleporteur/UE4play.PNG")
            time.sleep(0.1)
            pyautogui_fonction.click_on("main/app_teleporteur/Standalone.png")
            if pyautogui_fonction.is_on_screen("main/app_teleporteur/SaveSelected1.PNG"):
                pyautogui_fonction.click_on("main/app_teleporteur/SaveSelected1.PNG")
        except:
            print("Could not found play button")


def open_UE4():
    close_UE4()
    os.startfile("C:/Users/musee/Documents/Collage3/Collage3D_V3/Collage3D_V3.uproject")
    pyautogui_fonction.while_its_there("main/app_teleporteur/Collage3DEditor.PNG")
    time.sleep(3)
    if pyautogui_fonction.is_on_screen("main/app_teleporteur/SkipRestore.PNG"):
        pyautogui_fonction.click_on("main/app_teleporteur/SkipRestore.PNG")
    else:
        print("allo")
    return


def close_UE4():
    os.system('TASKKILL /F /IM "UE4Editor.exe"')
    return


def open_cleanup3D():
    os.chdir("C:/Users/musee/Documents/teleporteur/main/CleanupScan3D")
    os.startfile("Start.bat")
    os.chdir("C:/Users/musee/Documents/teleporteur")
    return
