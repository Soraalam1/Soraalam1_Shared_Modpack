import ssbh_data_py

modl_a = ssbh_data_py.modl_data.read_modl("C:/Users/Sami/AppData/Roaming/Ryujinx/sdcard/ultimate/mods/homerunKalos/stage/poke_kalos/normal/model/stc_b00_battlering_bighall_set/model.numdlb")
modl_b = ssbh_data_py.modl_data.read_modl("C:/Users/Sami/Desktop/ground_forimpact - Copy/model.numdlb")

mesh_a = ssbh_data_py.mesh_data.read_mesh("C:/Users/Sami/AppData/Roaming/Ryujinx/sdcard/ultimate/mods/homerunKalos/stage/poke_kalos/normal/model/stc_b00_battlering_bighall_set/model.numshb")
mesh_b = ssbh_data_py.mesh_data.read_mesh("C:/Users/Sami/Desktop/ground_forimpact - Copy/model.numshb")

matl_a = ssbh_data_py.matl_data.read_matl("C:/Users/Sami/AppData/Roaming/Ryujinx/sdcard/ultimate/mods/homerunKalos/stage/poke_kalos/normal/model/stc_b00_battlering_bighall_set/model.numatb")
matl_b = ssbh_data_py.matl_data.read_matl("C:/Users/Sami/Desktop/ground_forimpact - Copy/model.numatb")

skel_a = ssbh_data_py.skel_data.read_skel("C:/Users/Sami/AppData/Roaming/Ryujinx/sdcard/ultimate/mods/homerunKalos/stage/poke_kalos/normal/model/stc_b00_battlering_bighall_set/model.nusktb")
skel_b = ssbh_data_py.skel_data.read_skel("C:/Users/Sami/Desktop/ground_forimpact - Copy/model.nusktb")


# Append all of the mesh entries from B to A.
for b_modl_entry in modl_b.entries:
    modl_a.entries.append(b_modl_entry)

# Append all of the mesh objects from B to A.
for b_mesh_object in mesh_b.objects:
    mesh_a.objects.append(b_mesh_object)

# Append all of the matl objects from B to A.
for b_matl_entry in matl_b.entries:
    matl_a.entries.append(b_matl_entry)

for b_skel_bone in skel_b.bones:
    skel_a.bones.append(b_skel_bone)

modl_a.save("model.numdlb")
mesh_a.save("model.numshb")
matl_a.save("model.numatb")
skel_a.save("model.nusktb")