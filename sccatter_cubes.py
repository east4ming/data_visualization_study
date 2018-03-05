import matplotlib.pyplot as plt

input_values = list(range(1, 5001))
cubes = [x ** 3 for x in input_values]

plt.scatter(input_values, cubes, s=40, c=cubes, cmap='spring')

# 设置图表标题, 并给坐标轴加上标签
plt.title("Cubes Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubes of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
# plt.show()
plt.savefig('cubes_plog.png')
