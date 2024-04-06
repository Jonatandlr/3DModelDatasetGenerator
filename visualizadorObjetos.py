import open3d as o3d
import numpy as np



# 
mesh=o3d.io.read_triangle_mesh("./3DModelsObjects/cocacolaVieja/cocaCola.glb",True,True)
bbox = mesh.get_axis_aligned_bounding_box()
bbox.color = (1, 0, 0)



#Importante para que no se cuelgue 
o3d.visualization.gui.Application.instance.initialize()


# Create a window
vis = o3d.visualization.O3DVisualizer("nameVentana", 1280, 720)
vis.set_background((0., 0.78, 0., 1.0), None)
vis.add_geometry("objeto",mesh)
vis.add_geometry("bbox",bbox)

vis.reset_camera_to_default()
vis.animation_time_step = 1.0
# Define arguments for some objects that are not output with reset_camera_to_defaul
arg0 = 0.1
arg1 = np.array([0.0, 0.0, 0.0], dtype=np.float32).reshape(3, 1)
arg2 = np.array([0.0, 0.0, 0.2], dtype=np.float32).reshape(3, 1)
arg3 = np.array([0.0, 1.0,0.0], dtype=np.float32).reshape(3, 1)

# Call the function with the defined arguments
vis.setup_camera(arg0, arg1, arg2, arg3)



o3d.visualization.gui.Application.instance.add_window(vis)
o3d.visualization.gui.Application.instance.run()

vis.close()

