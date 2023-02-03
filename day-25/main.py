# # with open("weater_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weater_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     next(data, None)
# #     temperatures = []
# #     for row in data:
# #         temperatures.append(int(row[1]))
# #     print(temperatures)
#
import pandas
#
# data = pandas.read_csv("weater_data.csv")
# # temp_list = data["temp"].to_list()
# # sum_total = 0
# # for _ in temp_list:
# #     sum_total += _
# # print(sum_total / len(temp_list))
#
# # print(data["temp"].max())
# #
# # print(data.temp)
#
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# def cel_to_f(celsius):
#     return (celsius * 9 / 5) + 32
#
# print(cel_to_f(monday.temp))

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_list = data["Primary Fur Color"].to_list()
fur_colors = ["Gray", "Cinnamon", "Black"]
color_list = []

for color in fur_colors:
    color_list.append(fur_list.count(color))

fur_dict = {
    "Color": fur_colors,
    "Count": color_list
}

d_f = pandas.DataFrame(fur_dict)
d_f.to_csv("squirrel_count.csv")


