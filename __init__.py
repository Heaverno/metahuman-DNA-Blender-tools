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

bl_info = {
    "name": "Metahuman DNA Tools", 
    "author": "Heaverno",
    "version": (0, 0, 1), 
    "blender": (3, 6, 2),
    "category": "Mesh", 
    "location": "Viewport > Right Panel",
    "description": "Toolset for editing metahuman dna file", 
    "tracker_url": "https://github.com/Heaverno/metahuman-DNA-Blender-interface"
}

import bpy
from . import DPanels

class PrintInConsole(bpy.types.Operator):
    """A init function test"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "interface.print_test"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Test print in console"         # Display name in the interface.
    #bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        print("This is a test print from __init__, qwq")
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


modules = [
    DPanels
]

def register():
    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()
    
