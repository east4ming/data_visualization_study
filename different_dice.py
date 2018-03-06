from die import Die

import pygal

# 创建一个D6和D10
die_1 = Die()
die_2 = Die(10)

# 掷骰子多次, 并将结果存储在列表中
results = [die_1.roll()+die_2.roll() for i in range(50000)]
# for roll_num in range(50000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(i) for i in range(2, max_result)]
# for i in range(2, max_result+1):
#     frequency = results.count(i)
#     frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times"
hist.x_labels = map(str, range(2, max_result+1))
hist._x_title = "Result"
hist._y_title = "Frenquency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file('different_dice_visual.svg')
