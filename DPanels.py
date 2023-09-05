# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

class TestFuncInDPanels(bpy.types.Operator):
    """Create a text in the scene, to test code in DPanels"""      
    bl_idname = "interface.test_dpanels"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Put in a text"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        font_curve = bpy.data.curves.new(type="FONT", name="numberPlate")
        font_curve.body = "DPanels"
        obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
        obj.location = (0, 0, 0)
        bpy.context.scene.collection.objects.link(obj)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

class DNA_Import_Panel(bpy.types.Panel):
    bl_label = "Import DNA"
    bl_category = "metahuman DNA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.separator()
        col.operator("interface.test_dpanels")
        col.separator()
        col.operator("interface.test_dpanels")
        col.separator()
        row = col.row(align=True)
        row.operator("ed.undo", icon='LOOP_BACK')
        row.operator("ed.redo", icon='LOOP_FORWARDS')
        col.separator()
        col.label(text="qwq")

        
classes = [DNA_Import_Panel]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

