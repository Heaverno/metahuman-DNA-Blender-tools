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
import os
from bpy_extras.io_utils import ImportHelper
from dna_demo import load_dna
import dnacalib_demo

class TestFunc(bpy.types.Operator):
    bl_idname = "object.test_dpanels" 
    bl_label = "Create test text curve" 
    bl_description = ("Create a test text curve")
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context): 
        font_curve = bpy.data.curves.new(type="FONT", name="numberPlate")
        font_curve.body = "Blender functionality test"
        obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
        obj.location = (0, 0, 0)
        bpy.context.scene.collection.objects.link(obj)

        return {'FINISHED'} 
    
class ImportDNA(bpy.types.Operator, ImportHelper):
    bl_idname = "io.import_dna"
    bl_label = "Import metahuman DNA"
    bl_description = "Import metahuman DNA"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        filedir = self.properties.filepath

        with open(filedir, 'rb') as fid:
            print(fid)
            reader = load_dna(fid)

        root_path = os.path.dirname(os.path.realpath(__file__))
        print(root_path)
        #load_bvh(res_db, root_path, gender)

        return{'FINISHED'}

classes = [TestFunc, ImportDNA]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

