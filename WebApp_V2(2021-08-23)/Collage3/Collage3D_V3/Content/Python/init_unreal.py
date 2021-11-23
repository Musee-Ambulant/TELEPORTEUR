import os, AssetFunctions, unreal_asset_automation, unreal, glob

import archive


# def main():
#     import_asset_in_dir()
#     spawn_actors_in_scene()
#     save_dir()


def import_asset_in_dir():
    student_num = 0
    group_num = 1
    path_list_with_name = []

    # for file_name in glob.iglob(r'C:/Users/varse/_documents/Perso/Unreal Projects/3Dobject_collection/*.obj'):
    for file_name in glob.iglob(r'C:/Users/musee/Desktop/ImportToUnreal/*.obj'):
        unreal.log_warning(file_name[38:-4])
        file_path = os.path.abspath(file_name)
        path_list_with_name.append([file_name.strip(".obj").split()[-1], file_path.strip()])
        # At this point the asset path is found
        unreal_asset_automation.import_skeletal_mesh(file_name, "/Game/groupe_01", "mon_ami_" + file_name[38:-4])
        student_num += 1


def save_dir():
    AssetFunctions.saveDirectory(path='/Game/groupe_01/', force_save=True, recursive=True)


def spawn_actors_in_scene():
    asset_array = unreal.EditorAssetLibrary.list_assets('/Game/groupe_01')
    print(asset_array)
    actor_position = 0

    for asset in asset_array:
        if actor_position == 0:
            actor_location = unreal.Vector(-690.0, -2280.0, 160.0)
        if actor_position == 1:
            actor_location = unreal.Vector(840.0, -2390.0, 160.0)
        if actor_position == 2:
            actor_location = unreal.Vector(190.0, -1850.0, 160.0)
        if actor_position == 3:
            actor_location = unreal.Vector(-350.0, -1350.0, 160.0)
        if actor_position == 4:
            actor_location = unreal.Vector(-900.0, -820.0, 160.0)
        if actor_position == 5:
            actor_location = unreal.Vector(840.0, -1430.0, 160.0)
        if actor_position == 6:
            actor_location = unreal.Vector(290.0, -1040.0, 160.0)
        if actor_position == 7:
            actor_location = unreal.Vector(-330.0, -620.0, 160.0)
        if actor_position == 8:
            actor_location = unreal.Vector(-1150.0, -50.0, 160.0)
        if actor_position == 9:
            actor_location = unreal.Vector(690.0, -460.0, 160.0)
        if actor_position == 10:
            actor_location = unreal.Vector(210.0, -70.0, 160.0)
        if actor_position == 11:
            actor_location = unreal.Vector(-410.0, -20.0, 160.0)
        if actor_position == 12:
            actor_location = unreal.Vector(270.0, 480.0, 160.0)
        if actor_position == 13:
            actor_location = unreal.Vector(-360.0, 650.0, 160.0)
        if actor_position == 14:
            actor_location = unreal.Vector(-780.0, 770.0, 160.0)
        if actor_position == 15:
            actor_location = unreal.Vector(850.0, 1170.0, 160.0)

        # Load the staticMesh asset
        loaded_asset = unreal.EditorAssetLibrary.load_asset(asset)
        # Specify the uv channel to save into
        channel_index = 0
        # Set the angle threshold
        angle_threshold = 55
        # Unwrap the mesh into the UV channel
        unreal.UVGenerationFlattenMapping.generate_flatten_mapping_u_vs(loaded_asset, channel_index, angle_threshold)
        # Save the modified Asset
        unreal.EditorAssetLibrary.save_asset(asset)

        # Set actor rotation to spawn to
        actor_rotation = unreal.Rotator(90.0, 0.0, 0.0)
        # SpawnActorToScene
        unreal.EditorLevelLibrary.spawn_actor_from_object(loaded_asset, actor_location, actor_rotation)
        actor_position += 1


def delete_previous_actors():
    actors_list = unreal.EditorLevelLibrary.get_all_level_actors()

    for actor in actors_list:
        if str(actor)[47:54] == "mon_ami":
            unreal.EditorLevelLibrary.destroy_actor(actor)
        else:
            pass


def delete_content_groupe_01_assets():
    parent_dir = "/Game/groupe_01"

    unreal.EditorAssetLibrary.delete_directory(parent_dir)


# main()
if __name__ == '__main__':
    delete_previous_actors()
    delete_content_groupe_01_assets()
    import_asset_in_dir()
    spawn_actors_in_scene()
    save_dir()
