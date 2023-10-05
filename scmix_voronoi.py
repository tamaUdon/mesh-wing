import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# 3D空間上にランダムな点を生成
points = np.random.rand(40, 3)

# 3D空間でのボロノイ図は直接サポートされていないため、ここでは2D表現にする
points_2d = points[:, :2]

# ボロノイ図を計算
vor = Voronoi(points_2d)

# 色の定義
complementary_colors_A = ['#FF0000', '#00FFFF']  # 赤とシアン
complementary_colors_B = ['#FF8080', '#80FFFF']  # 明るい赤と明るいシアン
colors = complementary_colors_A + complementary_colors_B

def assign_colors_to_regions(vor, colors):
    region_colors = []
    color_index = 0
    for region in vor.regions:
        if not -1 in region:
            region_colors.append(colors[color_index])
            color_index = (color_index + 1) % len(colors)
    return region_colors

region_colors = assign_colors_to_regions(vor, colors)

fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_points=True, show_vertices=False)

# 領域を色で塗りつぶす
for region, color in zip(vor.regions, region_colors):
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        ax.fill(*zip(*polygon), color=color)

plt.show()
