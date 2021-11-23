import glob
import shutil
import zipfile
import win32api
import win32file
import pyautogui
from . import paths, pyautogui_fonction as pyauto_fonct, gif_maker
import os, time
from shutil import move, copy
from main import views


def open_exscan():
    os.startfile(paths.exscan)


def setup_exscan(groupe):
    pyautogui.moveTo(1712, 491)
    pyauto_fonct.click_on("main/app_teleporteur/EinScan-SP.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/NewWork.PNG")
    # pyauto_fonct.click_on("main/app_teleporteur/MyComputer.PNG")
    pyauto_fonct.double_click_on("main/app_teleporteur/Desktop.PNG")
    pyauto_fonct.double_click_on("main/app_teleporteur/Teleporteur.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/ProjectName.PNG")
    pyauto_fonct.write(groupe.name + "-" + (str(groupe.created_at))[:11])
    pyauto_fonct.click_on("main/app_teleporteur/New.PNG")
    time.sleep(0.5)
    if pyauto_fonct.is_on_screen("main/app_teleporteur/FileExist.PNG"):
        time.sleep(0.5)
        pyauto_fonct.press("enter")
        pyauto_fonct.click_on("main/app_teleporteur/Apply.PNG")

    else:
        pyauto_fonct.click_on("main/app_teleporteur/Apply.PNG")

    print("Le teleporteur est prêt à teleporter")


def remove_project():
    if pyauto_fonct.is_on_screen("main/app_teleporteur/Work.PNG"):
        pyauto_fonct.click_on("main/app_teleporteur/Work.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/Project1.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/RemoveProject.PNG")
    pyauto_fonct.press("enter")
    time.sleep(2)


def scan(ami):
    # if pyauto_fonct.is_on_screen("main/app_teleporteur/Work.PNG"):
    #     pyauto_fonct.click_on("main/app_teleporteur/Work.PNG")
    # pyauto_fonct.click_on("main/app_teleporteur/Project1.PNG")
    # pyauto_fonct.click_on("main/app_teleporteur/RemoveProject.PNG")
    # pyauto_fonct.press("enter")
    # time.sleep(2)
    # pyauto_fonct.click_on("main/app_teleporteur/NewProject.PNG")
    # pyauto_fonct.click_on("main/app_teleporteur/Apply.PNG")
    # time.sleep(1)

    pyauto_fonct.click_on("main/app_teleporteur/PlayButton.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/ApplyEdit.PNG")


def continu_scan(ami):
    pyauto_fonct.click_on("main/app_teleporteur/PlayButton.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/ApplyEdit.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/GlobalOptimization.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/ConfirmOptimization.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/MeshModel.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/WatertightModel.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/LowDetail.PNG")
    time.sleep(0.5)
    print("Working dir:", os.getcwd())
    print("Files in here:", os.listdir("."))
    if not pyauto_fonct.is_on_screen("main/app_teleporteur/MeshingData.PNG"):
        print("did not see meshing data")

    pyauto_fonct.while_its_there("main/app_teleporteur/MeshingData.PNG")
    gif_maker.main(ami)
    mk_save_dir_static(ami)


def other_scan():
    pyauto_fonct.click_on("main/app_teleporteur/Scan.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/Confirm.PNG")
    if pyauto_fonct.is_on_screen("main/app_teleporteur/Work.PNG"):
        pyauto_fonct.click_on("main/app_teleporteur/Work.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/Project1.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/RemoveProject.PNG")
    pyauto_fonct.press("enter")
    time.sleep(2)
    pyauto_fonct.click_on("main/app_teleporteur/NewProject.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/Apply.PNG")
    time.sleep(1)


def skip_scan(ami):
    pyauto_fonct.click_on("main/app_teleporteur/GlobalOptimization.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/ConfirmOptimization.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/MeshModel.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/WatertightModel.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/LowDetail.PNG")
    pyauto_fonct.while_its_there("main/app_teleporteur/MeshingData.PNG")
    gif_maker.main(ami)
    mk_save_dir_static(ami)


def redo_scan(ami):
    if os.path.exists("main/static/" + ami.gif_path):
        os.remove("main/static/" + ami.gif_path)
    pyauto_fonct.click_on("main/app_teleporteur/Scan.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/Confirm.PNG")
    ami.num_scan += 1
    views.rescan(None, ami)


def mk_save_dir_drive(ami):
    ecole_path = "C:/Users/musee/Desktop/Fichier_3d/" + str(ami.groupe.ecole)
    groupe_path = "C:/Users/musee/Desktop/Fichier_3d/" + str(ami.groupe.ecole) + "/" + str(ami.groupe)
    if not os.path.exists(ecole_path):
        os.mkdir(ecole_path)
    if not os.path.exists(groupe_path):
        os.mkdir(groupe_path)
    dir = os.listdir(groupe_path)
    print(dir)

    if os.path.exists(groupe_path):
        return

    os.mkdir(groupe_path)


def mk_save_dir_removable_drive(groupe):
    drive_list = win32api.GetLogicalDriveStrings()  # Returns a list containing letters from removable drives
    drive_list = drive_list.split("\x00")[0:-1]
    drives = []
    for drive in drive_list:
        if win32file.GetDriveType(drive) == win32file.DRIVE_REMOVABLE:  # check if the drive is of type removable
            drives.append(drive)
    drive = drives[0]

    if not os.path.exists(drive[:2] + "/teleporteur"):
        os.mkdir((drive[:2] + "/teleporteur"))

    ecole_path_stl = drive[:2] + "teleporteur/3D/" + str(groupe.ecole)
    ecole_path_gif = drive[:2] + "teleporteur/GIF/" + str(groupe.ecole)
    ecole_path_photos = drive[:2] + "teleporteur/photos/" + str(groupe.ecole)
    groupe_path_stl = drive[:2] + "teleporteur/3D/" + str(groupe.ecole) + "/" + str(groupe)
    groupe_path_gif = drive[:2] + "teleporteur/GIF/" + str(groupe.ecole) + "/" + str(groupe)
    groupe_path_photos = drive[:2] + "teleporteur/photos/" + str(groupe.ecole) + "/" + str(groupe)

    if not os.path.exists(drive[:2] + "teleporteur/3D/"):
        os.mkdir(drive[:2] + "teleporteur/3D/")
    if not os.path.exists(drive[:2] + "teleporteur/GIF/"):
        os.mkdir(drive[:2] + "teleporteur/GIF/")
    if not os.path.exists(drive[:2] + "teleporteur/photos/"):
        os.mkdir(drive[:2] + "teleporteur/photos/")

    if not os.path.exists(ecole_path_stl):
        os.mkdir(ecole_path_stl)
    if not os.path.exists(ecole_path_gif):
        os.mkdir(ecole_path_gif)
    if not os.path.exists(ecole_path_photos):
        os.mkdir(ecole_path_photos)

    if not os.path.exists(groupe_path_stl):
        os.mkdir(groupe_path_stl)
    if not os.path.exists(groupe_path_gif):
        os.mkdir(groupe_path_gif)
    if not os.path.exists(groupe_path_photos):
        os.mkdir(groupe_path_photos)

    save_to_removable(groupe, groupe_path_stl, groupe_path_gif, groupe_path_photos, drive[:2])
    return


def save_to_removable(groupe, stl_path, gif_path, photos_path, drive):
    static_stl_path = glob.glob("main/static/main/3D/" + str(groupe.ecole) + "/" + str(groupe) + "/*.stl")
    static_photos_path = glob.glob("main/static/main/photos/" + str(groupe.ecole) + "/" + str(groupe) + "/*.png")
    static_gif_path = glob.glob("main/static/main/GIF/" + str(groupe.ecole) + "/" + str(groupe) + "/*.gif")

    # Save STL
    if os.path.exists("main/static/main/3D/" + str(groupe.ecole) + "/" + str(groupe)):
        stl_zip_path = zipfile.ZipFile(stl_path + "/fichiers_stl.zip", "w")
        os.chdir("main/static/main/3D/" + str(groupe.ecole) + "/" + str(groupe))
        for stl in static_stl_path:
            print("compress et copying:" + os.path.basename(stl))
            stl_zip_path.write(os.path.basename(stl))
        stl_zip_path.close()
        os.chdir("C:/Users/musee/Documents/teleporteur")

    # Save GIF
    if os.path.exists("main/static/main/GIF/" + str(groupe.ecole) + "/" + str(groupe)):
        gif_zip_path = zipfile.ZipFile(gif_path + "/GIF.zip", "w")
        os.chdir("main/static/main/GIF/" + str(groupe.ecole) + "/" + str(groupe))
        for gif in static_gif_path:
            print("compress et copying:" + os.path.basename(gif))
            gif_zip_path.write(os.path.basename(gif))
        gif_zip_path.close()
        os.chdir("C:/Users/musee/Documents/teleporteur")

    # Save ScreenShots
    if os.path.exists("main/static/main/photos/" + str(groupe.ecole) + "/" + str(groupe)):
        photos_zip_path = zipfile.ZipFile(photos_path + "/photos.zip", "w")
        os.chdir("main/static/main/photos/" + str(groupe.ecole) + "/" + str(groupe))
        for photo in static_photos_path:
            print("compress et copying:" + os.path.basename(photo))
            photos_zip_path.write(os.path.basename(photo))
        photos_zip_path.close()
        os.chdir("C:/Users/musee/Documents/teleporteur")
    return


def mk_save_dir_static(ami):
    ecole_path_3D = "main/static/main/3D/" + str(ami.groupe.ecole)
    groupe_path_3D = "main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe)

    if not os.path.exists(ecole_path_3D):
        os.mkdir(ecole_path_3D)

    if not os.path.exists(groupe_path_3D):
        os.mkdir(groupe_path_3D)

    if os.path.exists(groupe_path_3D):
        return

    os.mkdir(groupe_path_3D)


def save(ami):
    pyauto_fonct.click_on("main/app_teleporteur/SaveScan.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/Desktop.PNG")
    pyauto_fonct.double_click_on("main/app_teleporteur/ScanFolder.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/OBJ.PNG")
    pyauto_fonct.triple_click_on("main/app_teleporteur/FileName.PNG")
    pyauto_fonct.write(ami.name + "-" + (str(ami.id)))
    pyauto_fonct.click_on("main/app_teleporteur/Save.PNG")
    pyauto_fonct.click_on("main/app_teleporteur/ApplySave.PNG")


def move_saved_file(ami):
    stl_files = glob.glob("C:/Users/musee/Desktop/Scan/*.stl")
    obj_files = glob.glob("C:/Users/musee/Desktop/Scan/*.obj")
    # dst_dir = "C:/Users/musee/Desktop/Fichier_3d/" + str(ami.groupe.ecole) + "/" + str(ami.groupe)
    static_dir = "main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe)

    for stl_file in stl_files:
        print(stl_file)
        move(stl_file, static_dir)
    for obj_file in obj_files:
        print(obj_file)
        move(obj_file, static_dir)

    # for stl_file in glob.glob(dst_dir + "/*.stl"):
    #     print(stl_file)
    #     copy(stl_file, static_dir)
    # for obj_file in glob.glob(dst_dir + "/*.obj"):
    #     print(obj_file)
    #     copy(obj_file, static_dir)

    return
