from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Ecole, Ami, Groupe
from .forms import CreateNewEcole, CreateNewGroupe, CreateNewAmi, DeleteEcole
from main.app_teleporteur import exscan_fonction, pyautogui_fonction as pyauto_fonct
import psutil, os, time, subprocess, cv2
import main.collage_fonct


def index(response, id):
    ecole = Ecole.objects.get(id=id)
    form = CreateNewGroupe()
    return render(response, "main/ecole.html", {"ecole": ecole, "form": form})


def home(response):
    return render(response, "main/home.html", {})


def show_ecoles(response):
    ecoles = Ecole.objects.all()
    return render(response, "main/ecoles.html", {"ecoles": ecoles})


def create_ecole(response):
    if response.method == "POST":
        form = CreateNewEcole(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Ecole(name=n)
            t.save()

        return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewEcole()
    return render(response, "main/createEcole.html", {"form": form})


def create_groupe(response):
    context = {}
    system = response.POST.get("ecole", None)
    context["ecole"] = system
    ecole = Ecole.objects.get(name="%s" % system)

    if response.method == "POST":
        form = CreateNewGroupe(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            g = ecole.groupe_set.create(name=n)
            g.save()

        return HttpResponseRedirect("/%i" % ecole.id)
    return HttpResponseRedirect("/%i" % ecole.id)


def create_ami(response):
    print(response.POST)

    groupe_id = response.POST.get("groupe_id")
    groupe = Groupe.objects.get(id=groupe_id)

    if response.method == "POST":
        form = CreateNewAmi(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            a = groupe.ami_set.create(name=n)
            a.save()

    # return HttpResponseRedirect("/%i/%i" % (ecole.id, groupe.id))
    return render(response, "main/groupe.html", {"groupe": groupe})


def create_scan(response):
    print(response.POST)

    groupe_id = response.POST.get("groupe_id")
    groupe = Groupe.objects.get(id=groupe_id)

    if response.method == "POST":
        form = CreateNewAmi(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            ami = groupe.ami_set.create(name=n)
            ami.save()

    return render(response, "main/placeAmi.html", {"ami": ami})


def see_group(request, id, gid):
    ecole = Ecole.objects.get(id=id)
    groupe = ecole.groupe_set.get(id=gid)
    form = CreateNewAmi()
    formB = DeleteEcole

    return render(request, "main/groupe.html", {"ecole": ecole,
                                                "groupe": groupe,
                                                "form": form,
                                                "formB": formB})


def see_group_obj(request, id, gid):
    ecole = Ecole.objects.get(id=id)
    groupe = Groupe.objects.get(id=gid)

    return render(request, "main/groupe(archive).html", {"ecole": ecole,
                                                         "groupe": groupe})


def see_ami(request, id, gid, aid):
    ecole = Ecole.objects.get(id=id)
    groupe = ecole.groupe_set.get(id=gid)
    ami = groupe.ami_set.get(id=aid)
    gif_path = 'main/GIF/' + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".gif"
    return render(request, "main/ami.html", {"ecole": ecole, "groupe": groupe, "ami": ami, "gif_path": gif_path})


def confirmationAmi(response):
    context = {}
    print(response.POST.get("ami_id"))
    system = response.POST.get("ami_id", None)
    context["ami_id"] = system

    ami = Ami.objects.get(id=system)
    return render(response, "main/confirmation.html", {"ami": ami})


def confirmationGroupe(response):
    context = {}
    print(response.POST.get("groupe"))
    system = response.POST.get("groupe", None)
    context["groupe"] = system

    groupe = Groupe.objects.get(id=system)
    return render(response, "main/confirmationGroupe.html", {"groupe": groupe})


def confirmationEcole(response):
    context = {}
    print(response.POST.get("ecole"))
    system = response.POST.get("ecole", None)
    context["ecole"] = system

    ecole = Ecole.objects.get(id=system)

    return render(response, "main/confirmationEcole.html", {"ecole": ecole})


def confirmationChoiceAmi(response):
    context = {}
    system = response.POST.get("confirm", None)
    context["confirm"] = system
    form = CreateNewAmi()

    if system == "no":
        return HttpResponseRedirect("/ecoles")
    else:
        ami = Ami.objects.get(id=system)
        groupe = ami.groupe

        # remove static obj and stl
        if os.path.exists(
                "C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                    ami.groupe) + "/" + ami.name + "-" + (
                        str(ami.id)) + ".stl"):
            os.remove("C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                ami.groupe) + "/" + ami.name + "-" + (
                          str(ami.id)) + ".stl")
        if os.path.exists(
                "C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                    ami.groupe) + "/" + ami.name + "-" + (
                        str(ami.id)) + ".obj"):
            os.remove("C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                ami.groupe) + "/" + ami.name + "-" + (
                          str(ami.id)) + ".obj")

        # remove static gif
        if os.path.exists(
                "C:/Users/musee/Documents/teleporteur/main/static/main/GIF/" + str(ami.groupe.ecole) + "/" + str(
                    ami.groupe) + "/" + ami.name + "-" + (
                        str(ami.id)) + ".gif"):
            os.remove("C:/Users/musee/Documents/teleporteur/main/static/main/GIF/" + str(ami.groupe.ecole) + "/" + str(
                ami.groupe) + "/" + ami.name + "-" + (
                          str(ami.id)) + ".gif")

        ami.delete()  # Do you need to delete the ami.object ?

    return render(response, "main/newScan.html", {"groupe": groupe,
                                                  "form": form})  # if ami.object is not delete. Can render palceAmi instead...


def restart_scan(response):
    context = {}
    system = response.POST.get("confirm", None)
    context["confirm"] = system
    form = CreateNewAmi()

    if system == "no":
        return HttpResponseRedirect("/ecoles")
    else:
        ami = Ami.objects.get(id=system)
        groupe = ami.groupe

        # remove static obj and stl
        if os.path.exists(
                "C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                    ami.groupe) + "/" + ami.name + "-" + (
                        str(ami.id)) + ".stl"):
            os.remove("C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                ami.groupe) + "/" + ami.name + "-" + (
                          str(ami.id)) + ".stl")
        if os.path.exists(
                "C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                    ami.groupe) + "/" + ami.name + "-" + (
                        str(ami.id)) + ".obj"):
            os.remove("C:/Users/musee/Documents/teleporteur/main/static/main/3D/" + str(ami.groupe.ecole) + "/" + str(
                ami.groupe) + "/" + ami.name + "-" + (
                          str(ami.id)) + ".obj")

        # remove static gif
        if os.path.exists(
                "C:/Users/musee/Documents/teleporteur/main/static/main/GIF/" + str(ami.groupe.ecole) + "/" + str(
                    ami.groupe) + "/" + ami.name + "-" + (
                        str(ami.id)) + ".gif"):
            os.remove("C:/Users/musee/Documents/teleporteur/main/static/main/GIF/" + str(ami.groupe.ecole) + "/" + str(
                ami.groupe) + "/" + ami.name + "-" + (
                          str(ami.id)) + ".gif")

        ami.delete()  # Do you need to delete the ami.object ?
        if "EXScan S.exe" not in (p.name() for p in
                                  psutil.process_iter()):  # Check if ExscanS if already open. if it's open, don't open again
            exscan_fonction.open_exscan()
        time.sleep(2)
        pyauto_fonct.while_its_there("main/app_teleporteur/EXScanS.PNG")
        time.sleep(2)
        if pyauto_fonct.is_on_screen("main/app_teleporteur/DeviceOffline.PNG"):
            return render(response, "main/deviceOffline.html")
        else:
            if pyauto_fonct.is_on_screen("main/app_teleporteur/Setup.PNG"):
                pyauto_fonct.click_on("main/app_teleporteur/Setup.PNG")
                pyauto_fonct.press("enter")
                exscan_fonction.setup_exscan(groupe)
            else:
                exscan_fonction.setup_exscan(groupe)

    return render(response, "main/newScan.html", {"groupe": groupe,
                                                  "form": form})


def restart_ami(response):
    context = {}
    print(response.POST.get("ami_id"))
    system = response.POST.get("ami_id", None)
    context["ami_id"] = system

    ami = Ami.objects.get(id=system)
    return render(response, "main/restartAmi.html", {"ami": ami})


def confirmationChoiceGroupe(response):
    context = {}
    system = response.POST.get("confirm", None)
    context["confirm"] = system
    if system == "no":
        return HttpResponseRedirect("/ecoles")
    else:
        groupe = Groupe.objects.get(id=system)
        groupe.delete()
    return HttpResponseRedirect("/ecoles")


def confirmationChoiceEcole(response):
    context = {}
    system = response.POST.get("confirm", None)
    context["confirm"] = system
    if system == "no":
        return HttpResponseRedirect("/ecoles")
    else:
        ecole = Ecole.objects.get(id=system)
        ecole.delete()
    return HttpResponseRedirect("/ecoles")


def start(response):
    context = {}
    system = response.POST.get("groupe", None)
    context["groupe"] = system
    groupe = Groupe.objects.get(id=system)
    return render(response, "main/start.html", {"groupe": groupe})


def openEx(response):
    form = CreateNewAmi()
    context = {}
    system = response.POST.get("groupe", None)
    context["groupe"] = system
    print(system)
    groupe = Groupe.objects.get(id=system)

    if "EXScan S.exe" not in (p.name() for p in
                              psutil.process_iter()):  # Check if ExscanS if already open. if it's open, don't open again
        exscan_fonction.open_exscan()
    time.sleep(2)
    pyauto_fonct.while_its_there("main/app_teleporteur/EXScanS.PNG")
    time.sleep(2)
    if pyauto_fonct.is_on_screen("main/app_teleporteur/DeviceOffline.PNG"):
        return render(response, "main/deviceOffline.html")
    else:
        if pyauto_fonct.is_on_screen("main/app_teleporteur/Setup.PNG"):
            pyauto_fonct.click_on("main/app_teleporteur/Setup.PNG")
            pyauto_fonct.press("enter")
            exscan_fonction.setup_exscan(groupe)
        else:
            exscan_fonction.setup_exscan(groupe)

    return render(response, "main/newScan.html", {"groupe": groupe,
                                                  "form": form})


def scan(response):
    context = {}
    system = response.POST.get("ami", None)
    context["ami"] = system
    ami = Ami.objects.get(id=system)
    if pyauto_fonct.is_on_screen("main/app_teleporteur/PlayButton.PNG"):
        exscan_fonction.scan(ami)
        return render(response, "main/replaceAmi.html", {"ami": ami})
    else:
        return render(response, "main/ErrorTeleporteurNotStart.html", {"groupe": ami.groupe})


def continu_scan(response):
    context = {}
    system = response.POST.get("ami", None)
    context["ami"] = system
    ami = Ami.objects.get(id=system)
    exscan_fonction.continu_scan(ami)
    gif_path = 'main/GIF/' + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".gif"
    ami.gif_path = gif_path
    ami.save()
    exscan_fonction.mk_save_dir_static(ami)
    exscan_fonction.mk_save_dir_drive(ami)
    exscan_fonction.save(ami)
    pyauto_fonct.while_its_there("main/app_teleporteur/saveLoading.PNG")
    exscan_fonction.move_saved_file(ami)
    ami.stl_path = "main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".stl"
    ami.obj_path = "main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".obj"
    ami.is_save = True
    ami.save()
    return render(response, "main/postScan.html", {"ami": ami, "gif_path": ami.gif_path})
    # return render(response, "main/postScan.html", {"ami": ami, "gif_path": gif_path})


def rescan(response, ami):
    exscan_fonction.scan(ami)
    gif_path = 'main/GIF/' + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".gif"
    ami.gif_path = gif_path
    ami.save()
    return render(response, "main/postScan.html", {"ami": ami, "gif_path": gif_path})


def other_scan(response):
    context = {}
    system = response.POST.get("ami", None)
    context["ami"] = system
    print("***********************************")
    print(system)
    ami = Ami.objects.get(id=system)
    groupe = ami.groupe
    form = CreateNewAmi()
    exscan_fonction.other_scan()
    return render(response, "main/newScan.html", {"groupe": groupe, "form": form})


def skip_scan(response):
    context = {}
    system = response.POST.get("ami", None)
    context["ami"] = system
    ami = Ami.objects.get(id=system)
    exscan_fonction.skip_scan(ami)
    gif_path = 'main/GIF/' + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".gif"
    ami.gif_path = gif_path
    ami.save()
    exscan_fonction.mk_save_dir_static(ami)
    exscan_fonction.mk_save_dir_drive(ami)
    exscan_fonction.save(ami)
    pyauto_fonct.while_its_there("main/app_teleporteur/saveLoading.PNG")
    exscan_fonction.move_saved_file(ami)
    ami.stl_path = "main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".stl"
    ami.obj_path = "main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".obj"
    ami.is_save = True
    ami.save()
    return render(response, "main/postScan.html", {"ami": ami, "gif_path": ami.gif_path})
    # return render(response, "main/postScan.html", {"ami": ami, "gif_path": gif_path})


def save(response):
    context = {}
    system = response.POST.get("ami_id", None)
    context["ami_id"] = system

    ami = Ami.objects.get(id=system)
    exscan_fonction.mk_save_dir_static(ami)
    exscan_fonction.mk_save_dir_drive(ami)
    exscan_fonction.save(ami)
    pyauto_fonct.while_its_there("main/app_teleporteur/saveLoading.PNG")
    exscan_fonction.move_saved_file(ami)
    ami.stl_path = "main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".stl"
    ami.obj_path = "main/3D/" + str(ami.groupe.ecole) + "/" + str(ami.groupe) + "/" + ami.name + "-" + (
        str(ami.id)) + ".obj"
    ami.is_save = True
    ami.save()
    return render(response, "main/postScan.html", {"ami": ami, "gif_path": ami.gif_path})


def save_to_removable(response):
    form = CreateNewAmi()
    context = {}
    system = response.POST.get("groupe", None)
    context["groupe"] = system
    groupe = Groupe.objects.get(id=system)

    exscan_fonction.mk_save_dir_removable_drive(groupe)
    groupe.is_save = True

    return render(response, "main/saveConfirmation.html", {"groupe": groupe})


def open_in_collage3(response):
    print("ToCollage3D")
    main.collage_fonct.empty_input()
    main.collage_fonct.empty_importUE4()
    context = {}
    system = response.POST.get("groupe", None)
    context["groupe"] = system
    groupe = Groupe.objects.get(id=system)

    # start cleanupScan3D
    main.collage_fonct.open_cleanup3D()
    time.sleep(0.3)
    main.collage_fonct.copy_3D_to_cleanupScan(groupe)
    sec = 1
    while pyauto_fonct.is_on_screen("main/app_teleporteur/BlenderQuit.PNG") is False:
        print("Decimating since: " + str(sec) + " Seconde(s)")
        sec += 1
        time.sleep(1)
    print('Done with decimate')

    main.collage_fonct.copy_cleanupScanOutput_to_importUE4(groupe)
    pyauto_fonct.hotkey("alt", "f4")
    main.collage_fonct.open_UE4()


    if "EXScan S.exe" in (p.name() for p in
                              psutil.process_iter()):  # Check if ExscanS if already open. if it's open, kill it
        os.system('TASKKILL /F /IM "EXScan S.exe"')

    return render(response, "main/unreal.html", {"ecole": groupe.ecole,
                                                 "groupe": groupe})


def standalone(response):
    context = {}
    system = response.POST.get("groupe", None)
    context["groupe"] = system
    groupe = Groupe.objects.get(id=system)

    main.collage_fonct.start_in_standalone()
    return render(response, "main/unreal.html", {"ecole": groupe.ecole,
                                                 "groupe": groupe})

def closeUE4(response):
    main.collage_fonct.empty_importUE4()
    context = {}
    system = response.POST.get("groupe", None)
    context["groupe"] = system
    groupe = Groupe.objects.get(id=system)

    # fermer UE4
    os.system('TASKKILL /F /IM "UE4Editor.exe"')

    return render(response, "main/groupe.html", {"ecole": groupe.ecole,
                                                 "groupe": groupe})


def saveScreenshot(response):
    context = {}
    system = response.POST.get("groupe", None)
    context["groupe"] = system
    groupe = Groupe.objects.get(id=system)

    main.collage_fonct.mk_UE4_photo_dir(groupe)
    main.collage_fonct.move_UE4_screenshots(groupe)
    groupe.photos_path = "main/static/main/photos/" + str(groupe.ecole) + "/" + str(groupe)
    groupe.save()

    return render(response, "main/unreal.html", {"ecole": groupe.ecole,
                                                 "groupe": groupe})


def contact(response):
    return render(response, "main/contact.html")
