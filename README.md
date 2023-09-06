# metahuman-DNA-Blender-tools
Intention is to make reading, editing and writing dna files of metahuman possible in Blender.

Please read me thoroughly. This is a WIP. 

# License
Since this is a Blender addon, it has to go with with [GPL licence](LICENSE). 
Mean while the usage of assets and resources related to Epic's metahuman must follow [Epic's license](https://github.com/EpicGames/MetaHuman-DNA-Calibration/blob/main/LICENSE).

TBH, I have no idea about correctly licensing. 

# Workflow
- Acquire metahuman source files (Uassets and dna) through Metahuman Creator and Quxiel Bridge in Unreal Engine 5
- Export head mesh and body mesh with morph targets and armature (Not concerning LODs)
- Import into Blender as fbx. fbx with morph targets won't import correctly without the help of Fbx Converter
- You can do almost whatever you want with the body mesh since there is no specific data on it, casual artistic workflow will be fine
- The head do have something with it, AFAIK, within fbx file, they are: 
	- morph targets (shape keys/ blend shapes) that drive micro muscle motion as facial bones moving
	- custom vertex normals mainly for more obvious nasolabial fold
	- weights, as facial expression is still driven by skeletal mesh after all
- Mean while, more important datas are stored inside dna file, such as how CTRL_expression manage bones and curves
- You can copy the head mesh in Blender for data transfer after editing the head mesh
- Now you have an editable head mesh! You can use Zbrush or Wrap4D or any method you'd like to, just make sure it's topology won't change
- Here is where things split up.

	After Unreal Engine 5.2, the [metahuman identity](https://dev.epicgames.com/documentation/en-US/metahuman/mesh-to-metahuman-quick-start-in-unreal-engine) can accept mesh of same topology bypassing identity solve.
	This means you can throw in your just edited head mesh and let Metahuman Creator generate everything for you. Then you can take care of groom and textures and so on. 
	And BAM! everything is done. Then why does this repo exists? 
	I initally wrote this workflow to help me teasing out what the addon should be capable of, but here now it's raising a philosophical problem to me. 

	Or you can import the head mesh right back to Blender, transfer those data mentioned above, use this addon (not exist yet) to edit corresponding dna, and finally reimport them into UE5.
	Just like what was in my mind before this workflow is writen.

- Anyway, it still can be good if you'd like to refine expression with Blender.

# Usage
- Download [DNACalib](https://github.com/EpicGames/MetaHuman-DNA-Calibration) release
- Grab all files but mlls under lib/maya2023/windows/ and drag them to the folder of this addon

```
                                                        qwq
```
