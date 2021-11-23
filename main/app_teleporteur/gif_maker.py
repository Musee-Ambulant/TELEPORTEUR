import pyautogui, os, glob
from . import info
from PIL import Image
from main.models import Groupe, Ecole, Ami


def mk_photo_folder_photo(ami):
    ecole_path = "C:/Users/musee/Desktop/Photo_gif/" + str(ami.groupe.ecole)
    groupe_path = "C:/Users/musee/Desktop/Photo_gif/" + str(ami.groupe.ecole) + "/" + str(ami.groupe)
    if not os.path.exists(ecole_path):
        os.mkdir(ecole_path)
    if not os.path.exists(groupe_path):
        os.mkdir(groupe_path)
    dir = os.listdir(groupe_path)
    print(dir)

    if os.path.exists(groupe_path + "/" + ami.name + "-" + (str(ami.id))):
        return

    os.mkdir(groupe_path + "/" + ami.name + "-" + (str(ami.id)))


def mk_photo_folder_gifA(ami):
    ecole_path = "C:/Users/musee/Desktop/GIF/" + str(ami.groupe.ecole)
    groupe_path = "C:/Users/musee/Desktop/GIF/" + str(ami.groupe.ecole) + "/" + str(ami.groupe)
    if not os.path.exists(ecole_path):
        os.mkdir(ecole_path)
    if not os.path.exists(groupe_path):
        os.mkdir(groupe_path)
    dir = os.listdir(groupe_path)
    print(dir)

    if os.path.exists(groupe_path + "/" + ami.name + "-" + (str(ami.id))):
        return

    os.mkdir(groupe_path + "/" + ami.name + "-" + (str(ami.id)))


def mk_photo_folder_gifB(ami):
    ecole_path = 'C:/Users/musee/Documents/teleporteur/main/static/main/GIF/' + str(ami.groupe.ecole)
    groupe_path = 'C:/Users/musee/Documents/teleporteur/main/static/main/GIF/' + str(ami.groupe.ecole) + "/" + str(
        ami.groupe)
    if not os.path.exists(ecole_path):
        os.mkdir(ecole_path)
    if not os.path.exists(groupe_path):
        os.mkdir(groupe_path)
    dir = os.listdir(groupe_path)
    print(dir)

    if os.path.exists(groupe_path):
        return

    os.mkdir(groupe_path)


def take_photos(ami):
    groupe_path = "C:/Users/musee/Desktop/Photo_gif/" + str(ami.groupe.ecole) + "/" + str(ami.groupe)
    ami_path = groupe_path + "/" + ami.name + "-" + (str(ami.id))
    photo_count = 1
    num_photo = 20
    while photo_count < num_photo:
        photo = pyautogui.screenshot(region=(675, 300, 600, 600))
        photo.save(ami_path + "/photo" + str(photo_count) + ".png")
        photo_count += 1
        pyautogui.moveTo(960, 540)
        pyautogui.dragTo(440, 540, button="left")


def mk_gif(ami):
    frames = []
    # photos = glob.glob("D:/Photo/" + info.current_friend_name)
    photos = glob.glob(
        "C:/Users/musee/Desktop/Photo_gif/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
            str(ami.id)) + "/*.png")
    print(photos)
    print("******************************************")
    for photo in photos:
        print(photo)
        new_frame = Image.open(photo)
        frames.append(new_frame)

    # save to gif

    # frames[0].save(
    #     "C:/Users/musee/Desktop/GIF/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + str(
    #         ami.id) + ".gif",
    #     format="GIF",
    #     append_images=frames[1:],
    #     save_all=True,
    #     duration=150,
    #     loop=0)

    frames[0].save(
        "main/static/main/GIF/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + str(
            ami.id) + ".gif",
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=150,
        loop=0)

    # Uncomment the following "for loop" if you want the "photos" to be removed after making the gif:

    # for photo in photos:
    #     os.remove(photo)


def main(ami):
    mk_photo_folder_photo(ami)
    mk_photo_folder_gifA(ami)
    mk_photo_folder_gifB(ami)
    take_photos(ami)
    mk_gif(ami)
