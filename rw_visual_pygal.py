import pygal

from random_walk import RandomWalk

# 创建一个RandomWalk实例, 并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
# plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers,
#             cmap=plt.cm.Blues)
# # plt.plot(rw.x_values, rw.y_values, linewidth=1)
#
# # 突出起点和终点
# plt.scatter(0, 0, c='green', s=100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
#
# # 隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
# plt.show()
hist = pygal.XY(stroke=False)
hist.title = 'Random Walk'
hist.add('Middle RW', zip(rw.x_values, rw.y_values), dots_size=1)
# for i in range(rw.num_points):
#     hist.add(None, [(rw.x_values[i], rw.y_values[i])], dots_size=1)
hist.add('Begin', (0, 0), dots_size=6)
hist.add('End', [(rw.x_values[-1], rw.y_values[-1])], dots_size=6)
hist.render_to_file('rw_visual_pygal.svg')
