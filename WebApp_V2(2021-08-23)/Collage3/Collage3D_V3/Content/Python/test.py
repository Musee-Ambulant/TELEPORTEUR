import glob, os, shutil, unreal


# unreal.log("google")

#
def delete_content_groupe_01_assets():
    # parent_dir = "/Game/groupe_01"
    # # parent_dir = "C:/Users/varse/_documents/MuseeAmbulant/unreal_project/Collage3D_V3/Content/groupe_01"
    # target_dir = "C:/Users/varse/Desktop/TKInterCollage/UAssetArchive"
    #
    # files_names = os.listdir(parent_dir)
    #
    # for file_name in files_names:
    #     unreal.log_warning(file_name)
    #     # print(os.path.abspath(file_name))
    #     # unreal.EditorAssetLibrary(file_name)

    parent_dir = "/Game/groupe_01"

    unreal.EditorAssetLibrary.delete_directory(parent_dir)


delete_content_groupe_01_assets()
