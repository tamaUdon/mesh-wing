# 目的: 三角形で半球をtilingする

import math
import matplotlib.pyplot as plt

def icosphere_subdivision(vertices, faces):
    def add_vertex(v):
        length = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
        vertices.append((v[0]/length, v[1]/length, v[2]/length))
        return len(vertices) - 1

    def get_middle_point(p1, p2):
        key = f"{min(p1, p2)}-{max(p1, p2)}"
        if key in middle_point_cache:
            return middle_point_cache[key]

        v1 = vertices[p1]
        v2 = vertices[p2]
        middle = ((v1[0]+v2[0])/2, (v1[1]+v2[1])/2, (v1[2]+v2[2])/2)

        index = add_vertex(middle)
        middle_point_cache[key] = index
        return index

    middle_point_cache = {}
    faces_subdivided = []

    for face in faces:
        v1 = face[0]
        v2 = face[1]
        v3 = face[2]
        a = get_middle_point(v1, v2)
        b = get_middle_point(v2, v3)
        c = get_middle_point(v3, v1)
        
        faces_subdivided.append([v1, a, c])
        faces_subdivided.append([v2, b, a])
        faces_subdivided.append([v3, c, b])
        faces_subdivided.append([a, b, c])

    return faces_subdivided

# 6頂点を起点とする。再起的に2分割し、頂点を追加していく (2分割で20面体, 12頂点となる)
vertices = [
    (-1,  0,  0),
    (1,  0,  0),
    (0, -1,  0),
    (0,  1,  0),
    (0,  0, -1),
    (0,  0,  1)
]

faces = [
    [0, 2, 4],
    [2, 1, 4],
    [1, 3, 4],
    [3, 0, 4],
    [0, 5, 2],
    [2, 5, 1],
    [1, 5, 3],
    [3, 5, 0],
]

subdivision_level = 2 # 20面体
for _ in range(subdivision_level):
    faces = icosphere_subdivision(vertices, faces)

# 半球のみを残す (y軸正方向の頂点のみ残す)  
faces = [face for face in faces if all(vertices[v][2] >= 0 for v in face)]

# Display the result
for face in faces:
    print(face)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for face in faces:
        x = [vertices[v][0] for v in face]
        y = [vertices[v][1] for v in face]
        z = [vertices[v][2] for v in face]
        ax.plot_trisurf(x, y, z)

    plt.show()
