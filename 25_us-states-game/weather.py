## Classic
# with open("weather_data.csv", "r") as csvfile:
#     daily_forecast = [s.strip("\n") for s in csvfile.readlines()]
# print(daily_forecast)

## CSV module
# import csv
#
# with open("weather_data.csv") as csvfile:
#     daily_forecast = csv.reader(csvfile)
#     temperatures = []
#     for row in daily_forecast:
#         temperature = row[1]
#         if row[1] != "temp":
#             temperatures.append(int(temperature))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# daily_forecast_dict = daily_forecast.to_dict()
# daily_temperatures_list = daily_temperatures.tolist()

daily_temperatures = data["temp"]
daily_temperatures_avg = daily_temperatures.mean()

# print(daily_temperatures_avg)
# print(daily_temperatures.max())
# print(data.temp)
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp)
monday_temp_f = monday.temp[0]*(9/5)+32
print(monday_temp_f)
