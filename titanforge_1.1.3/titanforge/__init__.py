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
    "version" : (1, 1, 3),
    "location" : "",
    "warning" : "",
    "doc_url": "https://ninjawskarpetach.github.io/Titan-Forge_Doc.github.io/docs/category/tutorial---basics/", 
    "tracker_url": "", 
    "category" : "Company" 
}


import bpy
import bpy.utils.previews
import csv
from mathutils import Vector


addon_keymaps = {}
_icons = None
class SNA_PT_RENDER_ADDON_32741(bpy.types.Panel):
    bl_label = 'Render_Addon'
    bl_idname = 'SNA_PT_RENDER_ADDON_32741'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'output'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        split_2F51A = layout.split(factor=0.2499999701976776, align=False)
        split_2F51A.alert = False
        split_2F51A.enabled = True
        split_2F51A.active = True
        split_2F51A.use_property_split = False
        split_2F51A.use_property_decorate = False
        split_2F51A.scale_x = 1.0
        split_2F51A.scale_y = 1.0
        split_2F51A.alignment = 'Expand'.upper()
        if not True: split_2F51A.operator_context = "EXEC_DEFAULT"
        split_2F51A.label(text='Find_STL', icon_value=0)
        split_2F51A.prop(bpy.context.scene, 'sna_renderbatchpath', text='', icon_value=0, emboss=True)
        op = split_2F51A.operator('sna.makecsv_31931', text='MakeCSV', icon_value=206, emboss=True, depress=False)
        split_853B0 = layout.split(factor=0.2499999701976776, align=False)
        split_853B0.alert = False
        split_853B0.enabled = True
        split_853B0.active = True
        split_853B0.use_property_split = False
        split_853B0.use_property_decorate = False
        split_853B0.scale_x = 1.0
        split_853B0.scale_y = 1.0
        split_853B0.alignment = 'Expand'.upper()
        if not True: split_853B0.operator_context = "EXEC_DEFAULT"
        split_853B0.label(text='CSV_File', icon_value=0)
        split_853B0.prop(bpy.context.scene, 'sna_csv_path', text='', icon_value=0, emboss=True)
        split_9602E = layout.split(factor=0.2499999701976776, align=False)
        split_9602E.alert = False
        split_9602E.enabled = True
        split_9602E.active = True
        split_9602E.use_property_split = False
        split_9602E.use_property_decorate = False
        split_9602E.scale_x = 1.0
        split_9602E.scale_y = 1.0
        split_9602E.alignment = 'Expand'.upper()
        if not True: split_9602E.operator_context = "EXEC_DEFAULT"
        split_9602E.label(text='PNG_Folder', icon_value=0)
        split_9602E.prop(bpy.context.scene, 'sna_png_folder_path', text='', icon_value=0, emboss=True)
        op = layout.operator('sna.movepng_f1d9f', text='Move And  Rename Renders', icon_value=612, emboss=True, depress=False)
        op = layout.operator('import_scene.import_csv_polars', text='My Button', icon_value=0, emboss=True, depress=False)


class SNA_OT_Makecsv_31931(bpy.types.Operator):
    bl_idname = "sna.makecsv_31931"
    bl_label = "MakeCSV"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        RenderBatchPath = bpy.context.scene.sna_renderbatchpath
        import os
        # =========================
        # USER SETTINGS
        # =========================
        SEARCH_DIRECTORY = RenderBatchPath
        # =========================
        # MAIN SCRIPT
        # =========================
        if not os.path.isdir(SEARCH_DIRECTORY):
            print(f"ERROR: Invalid search directory: {SEARCH_DIRECTORY}")
        else:
            # Collect all STL files recursively
            stl_files = [
                os.path.join(root, f)
                for root, _, files in os.walk(SEARCH_DIRECTORY)
                for f in files
                if f.lower().endswith(".stl")
            ]
            if not stl_files:
                print("WARNING: No STL files found in directory")
            else:
                stl_files.sort(key=lambda p: p.lower())
                # Save CSV next to .blend, fallback to search dir if unsaved
                blend_dir = os.path.dirname(bpy.data.filepath) or SEARCH_DIRECTORY
                output_path = os.path.join(blend_dir, "stl_files_Render.csv")
                try:
                    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(["index", "filename", "full_path", "folder_path", "name_render"])
                        for i, path in enumerate(stl_files, 1):
                            writer.writerow([
                                i,
                                os.path.basename(path),
                                path,
                                os.path.dirname(path),
                                os.path.splitext(os.path.basename(path))[0]
                            ])
                    print(f"✅ CSV saved at: {output_path}")
                except Exception as e:
                    print(f"ERROR: Failed to write CSV: {e}")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Movepng_F1D9F(bpy.types.Operator):
    bl_idname = "sna.movepng_f1d9f"
    bl_label = "MovePNG"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        CSV_path = bpy.context.scene.sna_csv_path
        png_folder_path = bpy.context.scene.sna_png_folder_path
        import os
        import shutil
        # ---------------------------
        # User settings - define here
        # ---------------------------
        csv_file = CSV_path    # Full path to your CSV
        png_folder = png_folder_path      # Full path to your PNG folder
        # ---------------------------
        # Script logic
        # ---------------------------
        # Check if CSV exists
        if not os.path.isfile(csv_file):
            print(f"ERROR: CSV file not found: {csv_file}")
        else:
            print(f"Reading CSV: {csv_file}")
        # Check if PNG folder exists
        if not os.path.isdir(png_folder):
            print(f"ERROR: PNG folder not found: {png_folder}")
        else:
            print(f"PNG folder: {png_folder}")
        # Read CSV
        try:
            with open(csv_file, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        except Exception as e:
            print(f"ERROR: Failed to read CSV: {e}")
            rows = []
        # Process each row
        for i, row in enumerate(rows):
            png_index = i + 1
            png_name = f"{png_index:04d}.png"
            png_src = os.path.join(png_folder, png_name)
            if not os.path.isfile(png_src):
                print(f"WARNING: PNG not found: {png_src}")
                continue
            folder_path = row.get("folder_path")
            name_render = row.get("name_render")
            if not folder_path or not name_render:
                print(f"WARNING: Invalid CSV row {i+1}: {row}")
                continue
            # Ensure target folder exists
            os.makedirs(folder_path, exist_ok=True)
            png_dst = os.path.join(folder_path, f"{name_render}.png")
            try:
                shutil.copy2(png_src, png_dst)
                print(f"Copied {png_src} -> {png_dst}")
            except Exception as e:
                print(f"WARNING: Failed to copy {png_src} -> {png_dst}: {e}")
        print("All PNGs processed.")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_TITANFORGE_V113_740F8(bpy.types.Panel):
    bl_label = 'Titan-Forge_v1.1.3'
    bl_idname = 'SNA_PT_TITANFORGE_V113_740F8'
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
        op = box_765CC.operator('wm.url_open', text='DocumentationWebSite', icon_value=769, emboss=True, depress=False)
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
        op = row_A14D0.operator('sna.exporttruescale_c617c', text='ExportTrueScale', icon_value=655, emboss=True, depress=False)
        op = row_A14D0.operator('sna.importtruescale_a8b5b', text='ImportTrueScale', icon_value=678, emboss=True, depress=False)
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
        op = row_6EDBA.operator('mesh.separate', text='SeperatByMaterial', icon_value=263, emboss=True, depress=False)
        op.type = 'MATERIAL'
        op = row_6EDBA.operator('view3d.tool_shelf_titanforge_splitbyfacesets', text='SplitByFaceSets', icon_value=204, emboss=True, depress=False)
        op = layout.operator('sna.transfervertexgrupe_a9866', text='TransferVertexGrupe', icon_value=450, emboss=True, depress=False)
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
        op = box_C9A60.operator('object.lattice_add_to_selected', text='Add Lattice', icon_value=0, emboss=True, depress=False)
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
        op = row_CAA13.operator('sna.applyposetomesh_1292b', text='ApplyPoseToMesh', icon_value=177, emboss=True, depress=False)
        op = row_CAA13.operator('sna.applypose_c6a54', text='ApplyPose', icon_value=177, emboss=True, depress=False)
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
        op = row_EF479.operator('sna.extractbasemesh_78986', text='ExtrackBaseMesh', icon_value=569, emboss=True, depress=False)
        op = row_EF479.operator('sna.newbasefrommesh_933c5', text='NewBaseFromMesh', icon_value=270, emboss=True, depress=False)
        op = box_F3718.operator('sna.attachedtoarmature_d85de', text='AttachedToArmature', icon_value=250, emboss=True, depress=False)
        split_2B2FD = layout.split(factor=0.44999998807907104, align=False)
        split_2B2FD.alert = False
        split_2B2FD.enabled = True
        split_2B2FD.active = True
        split_2B2FD.use_property_split = False
        split_2B2FD.use_property_decorate = False
        split_2B2FD.scale_x = 1.0
        split_2B2FD.scale_y = 1.0
        split_2B2FD.alignment = 'Expand'.upper()
        if not True: split_2B2FD.operator_context = "EXEC_DEFAULT"
        op = split_2B2FD.operator('sna.placeongrid_035f6', text='PlaceOnGrid', icon_value=624, emboss=True, depress=False)
        split_2B2FD.prop(bpy.context.scene, 'sna_padding', text='Padding', icon_value=0, emboss=True)
        op = layout.operator('sna.placemini_9140f', text='PlaceMini', icon_value=0, emboss=True, depress=False)


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


class SNA_OT_Placeongrid_035F6(bpy.types.Operator):
    bl_idname = "sna.placeongrid_035f6"
    bl_label = "PlaceOnGrid"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        padding = bpy.context.scene.sna_padding
        import math
        # ==========================
        # Settings
        # ==========================
        sort_mode = 'AREA'  # 'AREA', 'VOLUME', 'WIDTH'
        # ==========================
        # Helper: Get World BBox Data
        # ==========================

        def get_world_bbox_data(obj):
            corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
            min_corner = Vector((
                min(c.x for c in corners),
                min(c.y for c in corners),
                min(c.z for c in corners)
            ))
            max_corner = Vector((
                max(c.x for c in corners),
                max(c.y for c in corners),
                max(c.z for c in corners)
            ))
            size = max_corner - min_corner
            center = (min_corner + max_corner) / 2
            return min_corner, max_corner, size, center
        # ==========================
        # Main
        # ==========================
        selected_objects = bpy.context.selected_objects
        if not selected_objects:
            print("No objects selected.")
        else:
            object_data = []
            # Collect bbox info
            for obj in selected_objects:
                min_corner, max_corner, size, center = get_world_bbox_data(obj)
                if sort_mode == 'AREA':
                    metric = size.x * size.z
                elif sort_mode == 'VOLUME':
                    metric = size.x * size.y * size.z
                elif sort_mode == 'WIDTH':
                    metric = size.x
                else:
                    metric = size.x * size.z
                object_data.append((obj, size, center, metric))
            # Sort largest first
            object_data.sort(key=lambda x: x[3], reverse=True)
            count = len(object_data)
            # Auto balanced grid
            columns = math.ceil(math.sqrt(count))
            rows = math.ceil(count / columns)
            # Determine max column widths and row heights
            col_widths = [0] * columns
            row_heights = [0] * rows
            for i, (_, size, _, _) in enumerate(object_data):
                row = i // columns
                col = i % columns
                col_widths[col] = max(col_widths[col], size.x)
                row_heights[row] = max(row_heights[row], size.z)
            # Compute center positions for grid
            col_centers = []
            current_x = 0
            for width in col_widths:
                col_centers.append(current_x + width / 2)
                current_x += width + padding
            row_centers = []
            current_z = 0
            for height in row_heights:
                row_centers.append(current_z + height / 2)
                current_z += height + padding
            # Place objects so BBOX CENTER matches grid center
            for i, (obj, size, bbox_center, _) in enumerate(object_data):
                row = i // columns
                col = i % columns
                target_center = Vector((
                    col_centers[col],
                    0,  # Y reset
                    row_centers[row]
                ))
                offset = target_center - bbox_center
                obj.location += offset
            print(f"Arranged {count} objects by bounding-box center.")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Placemini_9140F(bpy.types.Operator):
    bl_idname = "sna.placemini_9140f"
    bl_label = "PlaceMini"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        import mathutils
        # Ensure we're in Object Mode
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type != 'MESH':
                continue
            # Make object active
            bpy.context.view_layer.objects.active = obj
            # Get world matrix
            world_matrix = obj.matrix_world
            # Get bounding box corners in world space
            bbox_world = [world_matrix @ mathutils.Vector(corner) for corner in obj.bound_box]
            # Compute bottom center in world space
            min_z = min(v.z for v in bbox_world)
            center_x = sum(v.x for v in bbox_world) / 8
            center_y = sum(v.y for v in bbox_world) / 8
            bottom_center_world = mathutils.Vector((center_x, center_y, min_z))
            # Move origin to bottom center
            # Step 1: Move 3D cursor to bottom center
            bpy.context.scene.cursor.location = bottom_center_world
            # Step 2: Set origin to 3D cursor
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
            # Step 3: Move object so origin is at world center
            obj.location = (0, 0, 0)
        print("Done! Origins set to bottom center and objects moved to world center.")
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_png_folder_path = bpy.props.StringProperty(name='png_folder_path', description='', default='', subtype='DIR_PATH', maxlen=0)
    bpy.types.Scene.sna_csv_path = bpy.props.StringProperty(name='CSV_path', description='', default='', subtype='FILE_PATH', maxlen=0)
    bpy.types.Scene.sna_renderbatchpath = bpy.props.StringProperty(name='RenderBatchPath', description='', default='', subtype='DIR_PATH', maxlen=0)
    bpy.types.Scene.sna_padding = bpy.props.FloatProperty(name='padding', description='', default=0.20000000298023224, subtype='DISTANCE', unit='NONE', max=1.0, step=3, precision=6)
    bpy.utils.register_class(SNA_PT_RENDER_ADDON_32741)
    bpy.utils.register_class(SNA_OT_Makecsv_31931)
    bpy.utils.register_class(SNA_OT_Movepng_F1D9F)
    bpy.utils.register_class(SNA_PT_TITANFORGE_V113_740F8)
    bpy.utils.register_class(SNA_OT_Seperatbymaterial_0D494)
    bpy.utils.register_class(SNA_OT_Attachedtoarmature_D85De)
    bpy.utils.register_class(SNA_OT_Exporttruescale_C617C)
    bpy.utils.register_class(SNA_OT_Importtruescale_A8B5B)
    bpy.utils.register_class(SNA_OT_Transfervertexgrupe_A9866)
    bpy.utils.register_class(SNA_OT_Newbasefrommesh_933C5)
    bpy.utils.register_class(SNA_OT_Extractbasemesh_78986)
    bpy.utils.register_class(SNA_OT_Applyposetomesh_1292B)
    bpy.utils.register_class(SNA_OT_Applypose_C6A54)
    bpy.utils.register_class(SNA_OT_Placeongrid_035F6)
    bpy.utils.register_class(SNA_OT_Placemini_9140F)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_padding
    del bpy.types.Scene.sna_renderbatchpath
    del bpy.types.Scene.sna_csv_path
    del bpy.types.Scene.sna_png_folder_path
    bpy.utils.unregister_class(SNA_PT_RENDER_ADDON_32741)
    bpy.utils.unregister_class(SNA_OT_Makecsv_31931)
    bpy.utils.unregister_class(SNA_OT_Movepng_F1D9F)
    bpy.utils.unregister_class(SNA_PT_TITANFORGE_V113_740F8)
    bpy.utils.unregister_class(SNA_OT_Seperatbymaterial_0D494)
    bpy.utils.unregister_class(SNA_OT_Attachedtoarmature_D85De)
    bpy.utils.unregister_class(SNA_OT_Exporttruescale_C617C)
    bpy.utils.unregister_class(SNA_OT_Importtruescale_A8B5B)
    bpy.utils.unregister_class(SNA_OT_Transfervertexgrupe_A9866)
    bpy.utils.unregister_class(SNA_OT_Newbasefrommesh_933C5)
    bpy.utils.unregister_class(SNA_OT_Extractbasemesh_78986)
    bpy.utils.unregister_class(SNA_OT_Applyposetomesh_1292B)
    bpy.utils.unregister_class(SNA_OT_Applypose_C6A54)
    bpy.utils.unregister_class(SNA_OT_Placeongrid_035F6)
    bpy.utils.unregister_class(SNA_OT_Placemini_9140F)
