import open3d as o3d
import numpy as np


# model3d=o3d.io.read_triangle_model("./3DModelsObjects/cocaColaLumaAI/CocaColaLowpoly.glb")
mesh = o3d.io.read_triangle_mesh("./3DModelsObjects/cocaColaLumaAI/CocaColaLowpoly.glb")

#Load texture
material = o3d.visualization.rendering.MaterialRecord()
material.albedo_img = o3d.io.read_image("./CocaCompleja/texture.png")

bbox = mesh.get_axis_aligned_bounding_box()
center = bbox.get_center()
bbox.color = (1, 0, 0)

# #another form to texture
# mesh = o3d.t.geometry.TriangleMesh.from_legacy(mesh)
# mesh.material.material_name = 'defaultLit'
# mesh.material.texture_maps['albedo'] = o3d.t.io.read_image("./CocaCompleja/texture.png")

# # Rotate the mesh
# for i in range(3):
#     matrix = [[0],[0],[0]]
#     if(i==0):
#         random_number = np.random.uniform(0, 2*np.pi)
#         matrix = [[0],[random_number],[0]]
#     if(i==1):
#         random_number = np.random.uniform(-np.pi/3, np.pi/3)
#         matrix = [[0],[0],[random_number]]
#     if(i==2):
#         random_number = np.random.uniform(0, np.pi/3)
#         matrix = [[random_number],[0],[0]]

#     R = geometry.get_rotation_matrix_from_axis_angle(matrix)
#     geometry.rotate(R,center)


#Importante para que no se cuelgue
o3d.visualization.gui.Application.instance.initialize()


# Create a window
vis = o3d.visualization.O3DVisualizer("nameVentana", 1280, 720)
# vis.set_background((0., 0.78, 0., 1.0), None)
# vis.add_geometry("objeto",model3d)
vis.add_geometry("mesh",mesh,material)
vis.add_geometry("bbox",bbox)
vis.show_skybox(False)
vis.reset_camera_to_default()
vis.animation_time_step = 1.0


# ma=np.array([0.0, 0.0, 0.0], dtype=np.float32).reshape(3, 1)
# scene=vis.scene
# print(scene)
# scene.set_lighting(scene.LightingProfile.SOFT_SHADOWS, (4, 5, 5))
# render=o3d.visualization.RenderOption()
# render.light_on=True


# # Define arguments for some objects that are not output with reset_camera_to_defaul
# arg0 = 0.1
# arg1 = np.array([0.0, 0.0, 0.0], dtype=np.float32).reshape(3, 1)
# arg2 = np.array([0.0, 0.0, 0.2], dtype=np.float32).reshape(3, 1)
# arg3 = np.array([0.0, 1.0,0.0], dtype=np.float32).reshape(3, 1)

# # Call the function with the defined arguments
# vis.setup_camera(arg0, arg1, arg2, arg3)


o3d.visualization.gui.Application.instance.add_window(vis)
o3d.visualization.gui.Application.instance.run()

vis.close()
