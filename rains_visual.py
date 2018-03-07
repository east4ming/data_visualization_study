import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, rains = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            index = ord('T')-ord('A')
            rain = row[index]
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rains.append(rain)

fig = plt.figure(figsize=(10, 6))

plt.scatter(dates, rains)

# 设置图形格式
title = "Daily PrecipitationIn - 2014-07\n {}".format(filename[:-9])
plt.title(title, fontsize=14)
fig.autofmt_xdate()
plt.ylabel('PrecipitationIn')
plt.yscale('linear')

plt.show()
