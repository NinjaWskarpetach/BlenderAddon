# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Titan-Forge",
    "author" : "Sebastian", 
    "description" : "",
    "blender" : (4, 2, 0),
    "version" : (1, 0, 8),
    "location" : "",
    "warning" : "",
    "doc_url": "https://ninjawskarpetach.github.io/Titan-Forge_Doc.github.io/docs/category/tutorial---basics/", 
    "tracker_url": "", 
    "category" : "Company" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None


def sna_update_sna_latticeresolution_5E75F(self, context):
    sna_updated_prop = self.sna_latticeresolution
    PROP1 = int(sna_updated_prop[0])
    PROP2 = int(sna_updated_prop[1])
    PROP3 = int(sna_updated_prop[2])
    from mathutils import Vector

    def add_or_update_lattice_for_object(obj, margin=1.4):
        bbox_corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        min_corner = Vector((min(c[0] for c in bbox_corners),
                             min(c[1] for c in bbox_corners),
                             min(c[2] for c in bbox_corners)))
        max_corner = Vector((max(c[0] for c in bbox_corners),
                             max(c[1] for c in bbox_corners),
                             max(c[2] for c in bbox_corners)))
        size = max_corner - min_corner
        center = min_corner + size / 2
        lattice_mod = None
        for mod in obj.modifiers:
            if mod.type == 'LATTICE':
                lattice_mod = mod
                break
        # Function to create a new lattice object and link to modifier

        def create_and_assign_lattice():
            lattice_data = bpy.data.lattices.new(name=f"Lattice_for_{obj.name}")
            lattice_obj = bpy.data.objects.new(name=f"Lattice_for_{obj.name}", object_data=lattice_data)
            bpy.context.collection.objects.link(lattice_obj)
            lattice_obj.location = center
            lattice_obj.scale = (size * margin) / 2
            lattice_obj.parent = obj
            lattice_obj.matrix_parent_inverse = obj.matrix_world.inverted()
            lattice_data.points_u = PROP1
            lattice_data.points_v = PROP2
            lattice_data.points_w = PROP3
            if lattice_mod is None:
                lattice_mod_local = obj.modifiers.new(name="Lattice", type='LATTICE')
            else:
                lattice_mod_local = lattice_mod
            lattice_mod_local.object = lattice_obj
            print(f"Created and assigned new lattice to {obj.name}")
            return lattice_obj
        if lattice_mod:
            if not lattice_mod.object or lattice_mod.object.type != 'LATTICE':
                # Lattice modifier exists but has no object – create one
                lattice_obj = create_and_assign_lattice()
            else:
                lattice_obj = lattice_mod.object
                # Always update resolution
                lattice_obj.data.points_u = PROP1
                lattice_obj.data.points_v = PROP2
                lattice_obj.data.points_w = PROP3
                # Only update transform if not already a child
                if lattice_obj.parent == obj:
                    print(f"Lattice for {obj.name} is child; skipping transform update.")
                else:
                    lattice_obj.location = center
                    lattice_obj.scale = (size * margin) / 2
                    lattice_obj.parent = obj
                    lattice_obj.matrix_parent_inverse = obj.matrix_world.inverted()
                    print(f"Updated lattice transform for {obj.name}")
                lattice_mod.object = lattice_obj
        else:
            # No modifier — create modifier and lattice
            create_and_assign_lattice()

    def add_or_update_lattices_for_selected_objects():
        selected_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        if not selected_objs:
            print("No mesh objects selected.")
            return
        for obj in selected_objs:
            add_or_update_lattice_for_object(obj)
    add_or_update_lattices_for_selected_objects()


class SNA_PT_TITANFORGE_V108_F6B06(bpy.types.Panel):
    bl_label = 'Titan-Forge_v1.0.8'
    bl_idname = 'SNA_PT_TITANFORGE_V108_F6B06'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Titan-Forge'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_765CC = layout.box()
        box_765CC.alert = False
        box_765CC.enabled = True
        box_765CC.active = True
        box_765CC.use_property_split = False
        box_765CC.use_property_decorate = False
        box_765CC.alignment = 'Expand'.upper()
        box_765CC.scale_x = 1.0
        box_765CC.scale_y = 1.0
        if not True: box_765CC.operator_context = "EXEC_DEFAULT"
        op = box_765CC.operator('wm.url_open', text='DocumentationWebSite', icon_value=125, emboss=True, depress=False)
        op.url = 'https://ninjawskarpetach.github.io/Titan-Forge_Doc.github.io/docs/category/tutorial---basics/'
        col_31667 = layout.column(heading='', align=False)
        col_31667.alert = False
        col_31667.enabled = True
        col_31667.active = True
        col_31667.use_property_split = False
        col_31667.use_property_decorate = False
        col_31667.scale_x = 1.0
        col_31667.scale_y = 1.0
        col_31667.alignment = 'Expand'.upper()
        col_31667.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_58896 = col_31667.box()
        box_58896.alert = False
        box_58896.enabled = True
        box_58896.active = True
        box_58896.use_property_split = False
        box_58896.use_property_decorate = False
        box_58896.alignment = 'Expand'.upper()
        box_58896.scale_x = 1.0
        box_58896.scale_y = 1.0
        if not True: box_58896.operator_context = "EXEC_DEFAULT"
        row_A14D0 = box_58896.row(heading='', align=False)
        row_A14D0.alert = False
        row_A14D0.enabled = True
        row_A14D0.active = True
        row_A14D0.use_property_split = False
        row_A14D0.use_property_decorate = False
        row_A14D0.scale_x = 1.0
        row_A14D0.scale_y = 1.0
        row_A14D0.alignment = 'Expand'.upper()
        row_A14D0.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_A14D0.operator('sna.exporttruescale_c617c', text='ExportTrueScale', icon_value=638, emboss=True, depress=False)
        op = row_A14D0.operator('sna.importtruescale_a8b5b', text='ImportTrueScale', icon_value=661, emboss=True, depress=False)
        box_7185A = layout.box()
        box_7185A.alert = False
        box_7185A.enabled = True
        box_7185A.active = True
        box_7185A.use_property_split = False
        box_7185A.use_property_decorate = False
        box_7185A.alignment = 'Expand'.upper()
        box_7185A.scale_x = 1.0
        box_7185A.scale_y = 1.0
        if not True: box_7185A.operator_context = "EXEC_DEFAULT"
        row_6EDBA = box_7185A.row(heading='', align=False)
        row_6EDBA.alert = False
        row_6EDBA.enabled = True
        row_6EDBA.active = True
        row_6EDBA.use_property_split = False
        row_6EDBA.use_property_decorate = False
        row_6EDBA.scale_x = 1.0
        row_6EDBA.scale_y = 1.0
        row_6EDBA.alignment = 'Expand'.upper()
        row_6EDBA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_6EDBA.operator('mesh.separate', text='SeperatByMaterial', icon_value=140, emboss=True, depress=False)
        op.type = 'MATERIAL'
        op = row_6EDBA.operator('view3d.tool_shelf_titanforge_splitbyfacesets', text='SplitByFaceSets', icon_value=202, emboss=True, depress=False)
        op = layout.operator('sna.transfervertexgrupe_a9866', text='TransferVertexGrupe', icon_value=439, emboss=True, depress=False)
        col_24202 = layout.column(heading='', align=True)
        col_24202.alert = False
        col_24202.enabled = True
        col_24202.active = True
        col_24202.use_property_split = False
        col_24202.use_property_decorate = False
        col_24202.scale_x = 1.0
        col_24202.scale_y = 1.0
        col_24202.alignment = 'Expand'.upper()
        col_24202.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        box_C9A60 = col_24202.box()
        box_C9A60.alert = False
        box_C9A60.enabled = True
        box_C9A60.active = True
        box_C9A60.use_property_split = False
        box_C9A60.use_property_decorate = False
        box_C9A60.alignment = 'Expand'.upper()
        box_C9A60.scale_x = 1.0
        box_C9A60.scale_y = 1.0
        if not True: box_C9A60.operator_context = "EXEC_DEFAULT"
        box_C9A60.label(text='Add Lattice', icon_value=450)
        box_C9A60.prop(bpy.context.scene, 'sna_latticeresolution', text='', icon_value=450, emboss=True, slider=False, toggle=True)
        box_F3718 = layout.box()
        box_F3718.alert = False
        box_F3718.enabled = True
        box_F3718.active = True
        box_F3718.use_property_split = False
        box_F3718.use_property_decorate = False
        box_F3718.alignment = 'Expand'.upper()
        box_F3718.scale_x = 1.0
        box_F3718.scale_y = 1.0
        if not True: box_F3718.operator_context = "EXEC_DEFAULT"
        row_CAA13 = box_F3718.row(heading='', align=False)
        row_CAA13.alert = False
        row_CAA13.enabled = True
        row_CAA13.active = True
        row_CAA13.use_property_split = False
        row_CAA13.use_property_decorate = False
        row_CAA13.scale_x = 1.0
        row_CAA13.scale_y = 1.0
        row_CAA13.alignment = 'Expand'.upper()
        row_CAA13.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_CAA13.operator('sna.applyposetomesh_1292b', text='ApplyPoseToMesh', icon_value=322, emboss=True, depress=False)
        op = row_CAA13.operator('sna.applypose_c6a54', text='ApplyPose', icon_value=175, emboss=True, depress=False)
        row_EF479 = box_F3718.row(heading='', align=False)
        row_EF479.alert = False
        row_EF479.enabled = True
        row_EF479.active = True
        row_EF479.use_property_split = False
        row_EF479.use_property_decorate = False
        row_EF479.scale_x = 1.0
        row_EF479.scale_y = 1.0
        row_EF479.alignment = 'Expand'.upper()
        row_EF479.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_EF479.operator('sna.extractbasemesh_78986', text='ExtrackBaseMesh', icon_value=553, emboss=True, depress=False)
        op = row_EF479.operator('sna.newbasefrommesh_933c5', text='NewBaseFromMesh', icon_value=261, emboss=True, depress=False)
        op = box_F3718.operator('sna.attachedtoarmature_d85de', text='AttachedToArmature', icon_value=241, emboss=True, depress=False)


class SNA_OT_Seperatbymaterial_0D494(bpy.types.Operator):
    bl_idname = "sna.seperatbymaterial_0d494"
    bl_label = "SeperatByMaterial"
    bl_description = "SeperatByMaterial"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        obj = bpy.context.active_object
        if obj and obj.type == 'MESH':
            bpy.ops.object.mode_set(mode='EDIT')         # Go to Edit Mode
            bpy.ops.mesh.select_all(action='SELECT')     # Select all geometry
            bpy.ops.mesh.separate(type='MATERIAL')       # Separate by material
            bpy.ops.object.mode_set(mode='OBJECT')       # Return to Object Mode
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        else:
            print("No active mesh object selected.")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Attachedtoarmature_D85De(bpy.types.Operator):
    bl_idname = "sna.attachedtoarmature_d85de"
    bl_label = "attachedtoarmature"
    bl_description = "attachedtoarmature"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        import mathutils
        # Get selected objects and identify the armature
        selected = bpy.context.selected_objects
        armature = next((obj for obj in selected if obj.type == 'ARMATURE'), None)
        objects = [obj for obj in selected if obj.type == 'MESH']
        if not armature:
            print("No armature selected!")
        else:
            bpy.ops.object.select_all(action='DESELECT')
            constraints_to_update = []
            for obj in objects:
                bpy.context.view_layer.objects.active = obj
                obj.select_set(True)
                try:
                    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')
                except Exception as e:
                    print(f"Failed to set origin for {obj.name}: {e}")
                obj_loc = obj.matrix_world.translation
                closest_bone = None
                min_dist = float('inf')
                for pbone in armature.pose.bones:
                    if pbone.bone.use_deform:
                        bone_world_pos = armature.matrix_world @ pbone.head
                        dist = (obj_loc - bone_world_pos).length
                        if dist < min_dist:
                            min_dist = dist
                            closest_bone = pbone
                if closest_bone:
                    # Remove existing Child Of constraints
                    for con in obj.constraints:
                        if con.type == 'CHILD_OF':
                            obj.constraints.remove(con)
                    # Add new Child Of constraint
                    con = obj.constraints.new(type='CHILD_OF')
                    con.name = f"Child Of {closest_bone.name}"
                    con.target = armature
                    con.subtarget = closest_bone.name
                    constraints_to_update.append((obj, con))
                    print(f"{obj.name} → {closest_bone.name} (Child Of constraint added)")
                else:
                    print(f"No deform bone found for {obj.name}")
            bpy.context.view_layer.update()
            # Now set inverse using Blender operator
            for obj, con in constraints_to_update:
                bpy.context.view_layer.objects.active = obj
                # Ensure only obj selected to avoid issues
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                try:
                    bpy.ops.constraint.childof_set_inverse(constraint=con.name, owner='OBJECT')
                    print(f"Inverse set for {obj.name}")
                except Exception as e:
                    print(f"Failed to set inverse for {obj.name}: {e}")
            # Reselect all processed objects at the end
            for obj in objects:
                obj.select_set(True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Exporttruescale_C617C(bpy.types.Operator):
    bl_idname = "sna.exporttruescale_c617c"
    bl_label = "ExportTrueScale"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.object.transform_apply('INVOKE_DEFAULT', scale=True)
        bpy.context.active_object.scale = (25.399999618530273, 25.399999618530273, 25.399999618530273)
        bpy.ops.scene.gob_export_button('INVOKE_DEFAULT', )
        bpy.context.active_object.scale = (1.0, 1.0, 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Importtruescale_A8B5B(bpy.types.Operator):
    bl_idname = "sna.importtruescale_a8b5b"
    bl_label = "ImportTrueScale"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.scene.gob_import('INVOKE_DEFAULT', )
        bpy.context.active_object.scale = (0.03937000036239624, 0.03937000036239624, 0.03937000036239624)
        bpy.ops.object.transform_apply('INVOKE_DEFAULT', scale=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Transfervertexgrupe_A9866(bpy.types.Operator):
    bl_idname = "sna.transfervertexgrupe_a9866"
    bl_label = "TransferVertexGrupe"
    bl_description = "TransferVertexGrupe"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):

        def transfer_weights_and_add_armature():
            context = bpy.context
            active_obj = context.active_object
            selected_objs = [obj for obj in context.selected_objects if obj != active_obj]
            if not active_obj or active_obj.type != 'MESH':
                print("Active object must be a mesh.")
                return
            # Find armature from active object's modifiers
            armature = None
            for mod in active_obj.modifiers:
                if mod.type == 'ARMATURE' and mod.object:
                    armature = mod.object
                    break
            if not armature:
                print("Active object has no armature modifier with an assigned armature.")
                return
            source_groups = [vg.name for vg in active_obj.vertex_groups]
            for target in selected_objs:
                if target.type != 'MESH':
                    print(f"Skipping non-mesh object: {target.name}")
                    continue
                # Ensure target has all vertex groups with same names
                for group_name in source_groups:
                    if group_name not in target.vertex_groups:
                        target.vertex_groups.new(name=group_name)
                # Add Data Transfer modifier
                dt_mod = target.modifiers.new(name="TransferWeights", type='DATA_TRANSFER')
                dt_mod.object = active_obj
                dt_mod.use_vert_data = True
                dt_mod.data_types_verts = {'VGROUP_WEIGHTS'}
                dt_mod.vert_mapping = 'NEAREST'
                # Apply the modifier
                bpy.context.view_layer.objects.active = target
                bpy.ops.object.modifier_apply(modifier=dt_mod.name)
                # Assign the armature to the object
                has_armature = False
                for mod in target.modifiers:
                    if mod.type == 'ARMATURE':
                        mod.object = armature
                        has_armature = True
                        break
                if not has_armature:
                    arm_mod = target.modifiers.new(name="Armature", type='ARMATURE')
                    arm_mod.object = armature
                print(f"Transferred weights and assigned armature to: {target.name}")
            # Set active object back
            bpy.context.view_layer.objects.active = active_obj
        # Run it
        transfer_weights_and_add_armature()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Newbasefrommesh_933C5(bpy.types.Operator):
    bl_idname = "sna.newbasefrommesh_933c5"
    bl_label = "NewBaseFromMesh"
    bl_description = "NewBaseFromMesh"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        isMultirezOn = bpy.context.object.modifiers["Multires"].show_viewport
        multirezLevel = bpy.context.active_object.modifiers["Multires"].levels
        bpy.context.active_object.modifiers["Armature"].show_viewport = False
        # Get the active object
        obj = bpy.context.active_object
        mod = obj.modifiers.get("Multires")
        # Ensure it has shape keys
        if obj and obj.data.shape_keys:
            for sk in obj.data.shape_keys.key_blocks:
                if sk.name != "Basis":  # Don't mute Basis
                    sk.mute = True  # Blender 4.x adds a mute property for shape keys
        bpy.context.active_object.modifiers["CorrectiveSmooth"].show_viewport = False
        bpy.context.object.modifiers["Multires"].show_viewport = True
        bpy.context.active_object.modifiers["Multires"].levels = mod.total_levels
        bpy.ops.object.multires_reshape(modifier="Multires")
        bpy.context.active_object.modifiers["Armature"].show_viewport = True
        # Ensure it has shape keys
        if obj and obj.data.shape_keys:
            for sk in obj.data.shape_keys.key_blocks:
                if sk.name != "Basis":  # Don't mute Basis
                    sk.mute = False  # Blender 4.x adds a mute property for shape keys
        bpy.context.active_object.modifiers["CorrectiveSmooth"].show_viewport = True
        bpy.context.active_object.modifiers["Multires"].levels = multirezLevel
        bpy.context.object.modifiers["Multires"].show_viewport = isMultirezOn
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Extractbasemesh_78986(bpy.types.Operator):
    bl_idname = "sna.extractbasemesh_78986"
    bl_label = "ExtractBaseMesh"
    bl_description = "ExtractBaseMesh"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        # Ensure there is an active object
        obj = bpy.context.active_object
        if not obj:
            raise Exception("No active object selected!")
        # Duplicate the active object
        bpy.ops.object.duplicate()
        dup_obj = bpy.context.active_object
        # Iterate through modifiers
        for mod in dup_obj.modifiers:
            # Hide Armature and CorrectiveSmooth modifiers
            if mod.type in {'ARMATURE', 'CORRECTIVE_SMOOTH'}:
                mod.show_viewport = False
            # If there's a Multires modifier, set it to highest level for viewport
            if mod.type == 'MULTIRES':
                try:
                    # set to the highest subdivision level
                    highest = mod.total_levels
                    mod.levels = highest
                    mod.sculpt_levels = highest
                except AttributeError:
                    print(f"Warning: Multires modifier on {dup_obj.name} missing total_levels property")
        bpy.ops.object.parent_clear(type='CLEAR')
        # Reset location to (0, 0, 0)
        dup_obj.location = (0.0, 0.0, 0.0)
        # Apply visual geometry to mesh
        bpy.ops.object.convert(target='MESH', keep_original=False)
        print(f"Duplicated and processed object: {dup_obj.name}")
        print('ExtractBase')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Applyposetomesh_1292B(bpy.types.Operator):
    bl_idname = "sna.applyposetomesh_1292b"
    bl_label = "ApplyPoseToMesh"
    bl_description = "ApplyPoseToMesh"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.object.modifier_copy('INVOKE_DEFAULT', modifier='Armature', use_selected_objects=True)
        bpy.ops.object.modifier_apply('INVOKE_DEFAULT', modifier='Armature.001', use_selected_objects=True)
        bpy.ops.pose.armature_apply('INVOKE_DEFAULT', selected=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Applypose_C6A54(bpy.types.Operator):
    bl_idname = "sna.applypose_c6a54"
    bl_label = "ApplyPose"
    bl_description = "ApplyPose"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.object.mode_set('INVOKE_DEFAULT', mode='POSE', toggle=True)
        bpy.ops.pose.armature_apply('INVOKE_DEFAULT', selected=False)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_latticeresolution = bpy.props.IntVectorProperty(name='LatticeResolution', description='', size=3, default=(3, 3, 3), subtype='NONE', update=sna_update_sna_latticeresolution_5E75F)
    bpy.utils.register_class(SNA_PT_TITANFORGE_V108_F6B06)
    bpy.utils.register_class(SNA_OT_Seperatbymaterial_0D494)
    bpy.utils.register_class(SNA_OT_Attachedtoarmature_D85De)
    bpy.utils.register_class(SNA_OT_Exporttruescale_C617C)
    bpy.utils.register_class(SNA_OT_Importtruescale_A8B5B)
    bpy.utils.register_class(SNA_OT_Transfervertexgrupe_A9866)
    bpy.utils.register_class(SNA_OT_Newbasefrommesh_933C5)
    bpy.utils.register_class(SNA_OT_Extractbasemesh_78986)
    bpy.utils.register_class(SNA_OT_Applyposetomesh_1292B)
    bpy.utils.register_class(SNA_OT_Applypose_C6A54)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_latticeresolution
    bpy.utils.unregister_class(SNA_PT_TITANFORGE_V108_F6B06)
    bpy.utils.unregister_class(SNA_OT_Seperatbymaterial_0D494)
    bpy.utils.unregister_class(SNA_OT_Attachedtoarmature_D85De)
    bpy.utils.unregister_class(SNA_OT_Exporttruescale_C617C)
    bpy.utils.unregister_class(SNA_OT_Importtruescale_A8B5B)
    bpy.utils.unregister_class(SNA_OT_Transfervertexgrupe_A9866)
    bpy.utils.unregister_class(SNA_OT_Newbasefrommesh_933C5)
    bpy.utils.unregister_class(SNA_OT_Extractbasemesh_78986)
    bpy.utils.unregister_class(SNA_OT_Applyposetomesh_1292B)
    bpy.utils.unregister_class(SNA_OT_Applypose_C6A54)
