import open3d as o3d
import numpy as np
from time import sleep
from PIL import  Image
from rembg import remove



def creationMesh(fileNameMesh:str):
    # Load the mesh
    mesh=o3d.io.read_triangle_mesh('./3DModelsObjects/cocacolaVieja/cocaCola.glb',True)

    # Get the axis aligned bounding box
    bbox = mesh.get_axis_aligned_bounding_box()
    bbox.color = (1, 0, 0)
    center = bbox.get_center()

    # Rotate the mesh
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
       
    
    return mesh 


def creationWindow(mesh,name,output):
    # Create a window
    vis = o3d.visualization.O3DVisualizer(name, 1280, 720)
    vis.set_background((0., 0.78, 0., 1.0), None)
    vis.add_geometry("objeto",mesh)
    vis.reset_camera_to_default()
    vis.animation_time_step = 1.0
    vis.show_skybox(False)

    # Define arguments for some objects that are not output with reset_camera_to_defaul
    arg0 = 0.1
    arg1 = np.array([0.0, 0.0, 0.0], dtype=np.float32).reshape(3, 1)
    arg2 = np.array([0.0, 0.0, 0.2], dtype=np.float32).reshape(3, 1)
    arg3 = np.array([0.0, 1.0,0.0], dtype=np.float32).reshape(3, 1)

    # Call the function with the defined arguments
    vis.setup_camera(arg0, arg1, arg2, arg3)

    o3d.visualization.gui.Application.instance.add_window(vis)
    vis.export_current_image(output)

    

    sleep(0.2)
    o3d.visualization.gui.Application.instance.run_one_tick()

    #Remove bg
    myImage = Image.open(output)
    myCroppedImage=remove(myImage)
    myCroppedImage.save(output)

    #Cut the Image
    try:
        myImage = Image.open(output)
        black = Image.new('RGBA', myImage.size)
        myImage = Image.composite(myImage, black, myImage)
        myCroppedImage = myImage.crop(myImage.getbbox())
        myCroppedImage.save(output)
    except:
        print('Error cropping the image')




    vis.close()




#Paths to the meshes

meshes=[
    {
        'name':'cocaCola',
        'mesh':'cocacolaVieja/cocaCola.glb',
        'output':'./outputImagesModel3D/cocaCola/'
    }
]



if __name__ == '__main__':
    meshArray=[]

    times=3
    # Create the meshes
    for mesh in meshes:
        for i in range(times):
            meshArray.append(creationMesh(mesh['mesh']))
            print(f'Creating mesh {i} for {mesh["name"]}')

    #Importante para que no se cuelgue 
    o3d.visualization.gui.Application.instance.initialize()

    # Create the windows
    for i in range(len(meshArray)):
        print(f'Creating window {i}')
        creationWindow(meshArray[i],f'{meshes[i//times]["name"]}_{i+1}',f'{meshes[i//times]["output"]}{meshes[i//times]["name"]}_{i+1}.png')