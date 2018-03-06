import pygal

from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷几次骰子, 并将结果保存在列表中
results = [die_1.roll()+die_2.roll()+die_3.roll() for i in range(50000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(i) for i in range(3, max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling {} D{} dice {} times".format('three', 6, 50000)
hist.x_labels = map(str, range(3, max_result+1))
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_3_visual.svg')
