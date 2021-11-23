from django.urls import path
from . import views
from .app_teleporteur import exscan_fonction as ef
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('<int:id>', views.index, name="index"),
    path('<int:id>/<int:gid>', views.see_group, name="see_group"),
    path('<int:id>/<int:gid>/voir', views.see_group_obj, name="see_group_obj"),
    path('<int:id>/<int:gid>/<int:aid>', views.see_ami, name="see_ami"),
    path('ecoles/', views.show_ecoles, name="home"),
    path("create/", views.create_ecole, name="=create"),
    path("createG/", views.create_groupe, name="=createG"),
    path("createA/", views.create_ami, name="=createA"),
    path("createScan/", views.create_scan, name="=createA"),
    path("confirm/", views.confirmationAmi, name="=confirm"),
    path("confirmGroupe/", views.confirmationGroupe, name="confirmationGroupe"),
    path("confirmEcole/", views.confirmationEcole, name="confirmationGroupe"),
    path("confirmChoice/", views.confirmationChoiceAmi, name="=confirmChoice"),
    path("confirmChoiceGroupe/", views.confirmationChoiceGroupe, name="=confirmChoiceGroupe"),
    path("confirmChoiceEcole/", views.confirmationChoiceEcole, name="=confirmChoiceGroupe"),
    path("start/", views.start, name="=start"),
    path("startTeleporteur/", views.openEx, name="startTeleporteur"),
    path("contact/", views.contact, name="contact"),
    path("scan/", views.scan, name="scan"),
    path("continuscan/", views.continu_scan, name="scan"),
    path("otherscan/", views.other_scan, name="other_scan"),
    # path("redoScan/", views.redo_scan, name="redo_scan"),
    path("save/", views.save, name="save"),
    path("saveRemovable/", views.save_to_removable, name="save_to_removable"),
    path("skipscan/", views.skip_scan, name="skipscan"),
    path("ToCollage3D/", views.open_in_collage3, name="ToCollage3D"),
    path("closeUE4/", views.closeUE4, name="closeUE4"),
    path("saveScreenshot/", views.saveScreenshot, name="saveScreenshot"),
    path("restart/", views.restart_ami, name="restart"),
    path("restart_ami_delete/", views.restart_scan, name="restart"),
    path("standalone/", views.standalone, name="standalone"),

]

# urlpatterns += staticfiles_urlpatterns()