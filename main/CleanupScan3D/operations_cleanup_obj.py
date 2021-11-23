import bpy
from easybpy import *
import os
import glob
#import sys
import configparser

#argv = sys.argv
#argv = argv[argv.index("--") + 1:]  # get all args after "--"

#print(argv)  # --> ['example', 'args', '123']

config_path = bpy.path.abspath("//Config.ini")
objs_path = bpy.path.abspath("//input\\")
destination_path = bpy.path.abspath("//output\\")

config = configparser.ConfigParser()
config.read(config_path)
obj_scale = float(config['Settings']['scale'])
r = float(config['Settings']['decimate'])
#r = 0.02

#check if output directory exists
if not os.path.isdir(destination_path):
    print("Destination path does not exist, creating.")
    os.mkdir(destination_path)

filelist = os.listdir(objs_path)
for file in filelist:
    if file[-4::].lower()==".obj": #check extension, if OBJ then do the necessary stuff
        print(file+" is being imported")
        imported_object = bpy.ops.import_scene.obj(filepath=objs_path+file)
        select_object(get_all_objects()[0],True)
        object = get_selected_object()
        origin_to_geometry(object)
        location(object, [0, 0, 0])
        rotation(object,[radians(-90),0,0])
        scale(object,[obj_scale,obj_scale,obj_scale])
        apply_all_transforms(object)
        add_decimate(object, "Decimation")
        bpy.context.object.modifiers["Decimation"].ratio=r
        apply_all_modifiers(object)
        bpy.ops.export_scene.obj(filepath = destination_path + file, use_selection = False)
        select_all_objects()
        delete_selected_objects()
        
rempath = os.path.abspath(".") + "\\input\\*.obj"
files = glob.glob(objs_path + "*.obj", recursive=True)

for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))