import open3d as o3d
import numpy as np




# model=o3d.io.read_triangle_model("./3DModelsObjects/cocaColaLumaAI/cocaColaLuma.glb",True)

mesh=o3d.io.read_triangle_mesh("./CocaCompleja/Node0.glb",True)
material = o3d.visualization.rendering.MaterialRecord() 
material.albedo_img = o3d.io.read_image("./CocaCompleja/texture.png")


mesh2=o3d.io.read_triangle_mesh("./CocaCompleja/Node0_2.glb",True)

material2 = o3d.visualization.rendering.MaterialRecord() 
material2.albedo_img = o3d.io.read_image("./CocaCompleja/texture_2.png")

mesh3=o3d.io.read_triangle_mesh("./CocaCompleja/Node0_3.glb",True)
material3 = o3d.visualization.rendering.MaterialRecord()
material3.albedo_img = o3d.io.read_image("./CocaCompleja/texture_3.png")

mesh4=o3d.io.read_triangle_mesh("./CocaCompleja/Node0_4.glb",True)
material4 = o3d.visualization.rendering.MaterialRecord()
material4.albedo_img = o3d.io.read_image("./CocaCompleja/texture_4.png")
bbox = mesh.get_axis_aligned_bounding_box()
center=bbox.get_center()
bbox.color = (1, 0, 0)

# # load texture 
# mesh = o3d.t.geometry.TriangleMesh.from_legacy(mesh) 
# mesh.material.material_name = 'defaultLit'
# mesh.material.scalar_properties['metallic']=1.0
# mesh.material.texture_maps['albedo'] = o3d.t.io.read_image("./CocaCompleja/texture.png")

# mesh2 = o3d.t.geometry.TriangleMesh.from_legacy(mesh2)
# mesh2.material.material_name = 'defaultLit'
# mesh2.material.texture_maps['albedo'] = o3d.t.io.read_image("./CocaCompleja/texture_2.png")

# mesh3 = o3d.t.geometry.TriangleMesh.from_legacy(mesh3)
# mesh3.material.material_name = 'defaultLit'
# mesh3.material.texture_maps['albedo'] = o3d.t.io.read_image("./CocaCompleja/texture_3.png")

# mesh4 = o3d.t.geometry.TriangleMesh.from_legacy(mesh4)
# mesh4.material.material_name = 'defaultLit'
# mesh4.material.texture_maps['albedo'] = o3d.t.io.read_image("./CocaCompleja/texture_4.png")

for i in range(3):
    matrix = [[0],[0],[0]]
    if(i==0):
        random_number = np.random.uniform(0, 2*np.pi)
        matrix = [[0],[random_number],[0]]
    if(i==1):
        random_number = np.random.uniform(-np.pi/3, np.pi/3)
        matrix = [[0],[0],[random_number]]
    if(i==2):
        random_number = np.random.uniform(0, np.pi/3)
        matrix = [[random_number],[0],[0]]   
    R = mesh.get_rotation_matrix_from_axis_angle(matrix)
    mesh.rotate(R,center)
    mesh2.rotate(R,center)
    mesh3.rotate(R,center)
    mesh4.rotate(R,center)

#Importante para que no se cuelgue 
o3d.visualization.gui.Application.instance.initialize()


# Create a window
vis = o3d.visualization.O3DVisualizer("nameVentana", 1280, 720)
vis.set_background((0., 0.78, 0., 1.0), None)
vis.add_geometry("mesh1",mesh,material)
vis.add_geometry("mesh2",mesh2,material2)
vis.add_geometry("mesh3",mesh3,material3)
vis.add_geometry("mesh4",mesh4,material4)

# vis.add_geometry("model",model)
vis.add_geometry("bbox",bbox)
vis.show_skybox(False)

# ma=np.array([0.0, 0.0, 0.0], dtype=np.float32).reshape(3, 1)
# scene=vis.scene
# scene.set_lighting(scene.LightingProfile.SOFT_SHADOWS, (4, 5, 5))
# render=o3d.visualization.RenderOption()
# render.light_on=True





vis.reset_camera_to_default()
vis.animation_time_step = 1.0
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

