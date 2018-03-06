import pygal

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子, 并将结果保存在列表中
results = [die.roll() for i in range(1000)]
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# 分析结果
frequencies = [results.count(i) for i in range(1, die.num_sides+1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D{} {} times".format(6, 1000)
hist.x_labels = map(str, range(1, 7))
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
