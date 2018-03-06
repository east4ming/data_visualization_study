import pygal

from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子, 并将结果保存在列表中
results = [die_1.roll()+die_2.roll() for i in range(1000)]
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(i) for i in range(2, max_result+1)]
# for i in range(2, max_result+1):
#     frequency = results.count(i)
#     frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling {} D{} dice {} times".format('two', 6, 1000)
hist.x_labels = map(str, range(2, max_result+1))
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
