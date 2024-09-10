import os


current_dir = os.path.dirname(os.path.realpath(__file__))
stl_file = os.path.join(current_dir,'Tet.stl')

print(stl_file)

def dist_2pts(node1,node2):
    x1,y1,z1 =node1
    x2,y2,z2 =node2
    x1 = float(x1.strip(','))
    y1 = float(y1.strip(','))
    z1 = float(z1.strip(','))
    x2 = float(x2.strip(','))
    y2 = float(y2.strip(','))
    z2 = float(z2.strip(','))
    dist = (((( x2- x1) ** 2) + ((y2 - y1) ** 2)+ ((z2 - z1) ** 2))** 0.5 )
    return dist
def read_stl_file( stl_file):
    tria_list =[]
    vertex_block = None
    with open(stl_file, 'r') as vertex_file:
        for line in vertex_file:
            line = line.strip()
            if line.startswith('outer loop'):
                vertex_block = True
                tria_vertex = []
            if vertex_block and line.startswith('vertex'):
                vertex = line.split (' ')
                tria_vertex.append(vertex[1:])
            elif vertex_block and line.startswith('endloop'):
                tria_list.append(tria_vertex)
                # print (f'{tria_vertex}')
                vertex_block =False
    return tria_list

tria_vertex_list = read_stl_file(stl_file)

def calc_tria_area(tria_list):
    tria_areas =[]
    for tria in tria_list:
        print(tria)
        n1,n2,n3 = tria
        # print (n1,n2,n3)
        a = dist_2pts(n1,n2)
        b= dist_2pts(n2,n3)
        c= dist_2pts(n3,n1)
        # print(a,b,c)
        tria_area = (a+b+c)/2
        # print(tria_area)
        tria_areas.append(tria_area)
    return sum(tria_areas)

area_value = calc_tria_area(tria_vertex_list)

print (f"Area of Given Trias = {area_value}")
