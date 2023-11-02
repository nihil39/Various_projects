def draw_voronoi_cell_given_id(cell_id, box, flag_draw_neighbors, flag_draw_normals, flag_draw_box):
    
    #lines to keep commented if one wants to change the plot prameters
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.set_xlim(box.get_walls()[0][0], box.get_walls()[1][0])
    ax.set_ylim(box.get_walls()[0][1], box.get_walls()[1][1])
    ax.set_zlim(box.get_walls()[0][2], box.get_walls()[1][2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    if (flag_draw_box):

        x = [box.get_walls()[0][0], box.get_walls()[1][0], box.get_walls()[1][0], box.get_walls()[0][0], box.get_walls()[0][0], box.get_walls()[1][0], box.get_walls()[1][0], box.get_walls()[0][0]]
        y = [box.get_walls()[0][1], box.get_walls()[0][1], box.get_walls()[1][1], box.get_walls()[1][1], box.get_walls()[0][1], box.get_walls()[0][1], box.get_walls()[1][1], box.get_walls()[1][1]]
        z = [box.get_walls()[0][2], box.get_walls()[0][2], box.get_walls()[0][2], box.get_walls()[0][2], box.get_walls()[1][2], box.get_walls()[1][2], box.get_walls()[1][2], box.get_walls()[1][2]]

    # Face IDs
        vertices = [[0,1,2,3], [1,5,6,2], [3,2,6,7], [4,0,3,7], [5,4,7,6], [4,5,1,0]] # rightly connect the box vertices
        tupleList = list(zip(x, y, z))
        poly3d = [[tupleList[vertices[ix][iy]] for iy in range(len(vertices[0]))] for ix in range(len(vertices))]
       
        ax.add_collection3d(Poly3DCollection(poly3d, facecolors = 'r', linewidths = 1, edgecolors = 'r', alpha = 0))

    color = []
    number_of_cell_faces = len(box[cell_id].face_vertices())
    #print(box[cell_id].neighbors())

    neighbours_id = box[cell_id].neighbors()
    neighbors_cell_not_edge = list(filter(lambda id: id >= 0, box[cell_id].neighbors())) # line to filter not edge neighbours
   
    ax.scatter3D(box[cell_id].pos[0], box[cell_id].pos[1], box[cell_id].pos[2], color = "firebrick", s = 40)
    
    if(flag_draw_neighbors):
        for i in range(len(neighbors_cell_not_edge)): # plot neighbor points
            ax.scatter3D(box[neighbors_cell_not_edge[i]].pos[0], box[neighbors_cell_not_edge[i]].pos[1], box[neighbors_cell_not_edge[i]].pos[2], color = "green", s = 20) #draw cell neighbors (points around which the cell are constructed)
       
    if(flag_draw_normals):
        for i in range(len(neighbours_id)): 
            ax.quiver(box[cell_id].pos[0], box[cell_id].pos[1], box[cell_id].pos[2], box[cell_id].normals()[i][0], box[cell_id].normals()[i][1], box[cell_id].normals()[i][2], color = "cyan")

    
    #print(box_2[cell_id].pos[0])
    for i in range(number_of_cell_faces):
        color.append('#%06X' % randint(0, 0xFFFFFF)) # the %06X gives you zero-padded hex (always 6 chars long)

    color_iterator = iter(color)

    for j in range(number_of_cell_faces):
        b = list(box[cell_id].vertices()[i] for i in box[cell_id].face_vertices()[j])   
        x = []
        y = []
        z = []
        vertices = []
        
        for k in range(len(box[cell_id].face_vertices()[j])): # print the vertex coordinates of every face
            #print(f'{box[cell_id].face_vertices()[j][k]} {b[k]}')
            x.append(b[k][0])
            y.append(b[k][1])
            z.append(b[k][2])
            vertices = [list(zip(x, y, z))]
            
        poly = Poly3DCollection(vertices, alpha = 0.4, facecolor = next(color_iterator), edgecolors = "black", linewidths = 0.1) # try color instead of facecolor
        ax.add_collection3d(poly)
