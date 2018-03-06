import matplotlib.pyplot as plt

from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子, 并将结果保存在列表中
results = [die_1.roll()+die_2.roll() for i in range(1000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(i) for i in range(2, max_result+1)]

# 对结果进行可视化

plt.bar(list(range(2, max_result+1)), frequencies)
plt.title("Results of rolling {} D{} dice {} times".format('two', 6, 1000),
          fontsize=20)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)
plt.xticks(list(range(2, max_result+1)))
# legend
plt.legend(["D6 + D6"], loc=2)
plt.show()
