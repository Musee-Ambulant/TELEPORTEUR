import unreal


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
            actor_location = unreal.Vector(-780.0, -770.0, 160.0)
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

    # POSITION 1 - 16

    # 1: (-690.0, -2280.0, 160.0)
    # 2: (840.0, -2390.0, 160.0)
    # 3: (190.0, -1850.0, 160.0)
    # 4: (-350.0, -1350.0, 160.0)
    # 5: (-900.0, -820.0, 160.0)
    # 6: (840.0, -1430.0, 160.0)
    # 7: (290.0, -1040.0, 160.0)
    # 8: (-330.0, -620.0, 160.0)
    # 9: (-1150.0, -50.0, 160.0)
    # 10: (690.0, -460.0, 160.0)
    # 11: (210.0, -70.0, 160.0)
    # 12: (-410.0, -20.0, 160.0)
    # 13: (-880.0, 510.0, 160.0)
    # 14: (340.0, 630.0, 160.0)
    # 15: ()
    # 16:

    """
        ORIGINAL POSITIONS
    
        for asset in asset_array:
        if actor_position == 0:
            actor_location = unreal.Vector(-690.0, -2280.0, 160.0)
        if actor_position == 1:
            actor_location = unreal.Vector(840.0, -2110.0, 160.0)
        if actor_position == 2:
            actor_location = unreal.Vector(190.0, -1400.0, 160.0)
        if actor_position == 3:
            actor_location = unreal.Vector(-460.0, -740.0, 160.0)
        if actor_position == 4:
            actor_location = unreal.Vector(760.0, -590.0, 160.0)
        if actor_position == 5:
            actor_location = unreal.Vector(-1330.0, -60.0, 160.0)
        if actor_position == 6:
            actor_location = unreal.Vector(60.0, 540.0, 160.0)
        if actor_position == 7:
            actor_location = unreal.Vector(1150.0, 1170.0, 160.0)
    """
