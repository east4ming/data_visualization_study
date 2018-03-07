import csv
from datetime import datetime
import matplotlib.pyplot as plt

filenames = ['death_valley_2014.csv', 'sitka_weather_2014.csv']
city_info = {filenames[0]: {'dates': [], 'highs': [], 'lows': []},
             filenames[1]: {'dates': [], 'highs': [], 'lows': []}}
for filename in filenames:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[2])
            except ValueError:
                print(current_date, 'missing data')
            else:
                city_info[filename]['dates'].append(current_date)
                city_info[filename]['highs'].append(high)
                city_info[filename]['lows'].append(low)

fig = plt.figure(figsize=(10, 6))

for i in range(2):
    plt.subplot(121+i)
    plt.plot(city_info[filenames[i]]['dates'], city_info[filenames[i]]['highs'],
             c='red', alpha=0.5)
    plt.plot(city_info[filenames[i]]['dates'], city_info[filenames[i]]['lows'],
             c='blue', alpha=0.5)
    plt.fill_between(city_info[filenames[i]]['dates'],
                     city_info[filenames[i]]['highs'],
                     city_info[filenames[i]]['lows'],
                     facecolor='blue', alpha=0.1)

    # 设置图形格式
    title = "Daily high and low temperatures - 2014\n {}".format(filenames[i][:-9])
    plt.title(title, fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)')
    plt.ylim(20, 110)

plt.show()
