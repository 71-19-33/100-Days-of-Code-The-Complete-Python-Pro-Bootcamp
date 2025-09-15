import pandas

#import csv into panda data structure
data_input = pandas.read_csv("2018_Squirrel_Data.csv")

#get fur color data
fur_color_data = data_input.value_counts("Primary Fur Color")

#get fur color names
fur_color_names = fur_color_data.index
gray = fur_color_names[0]
cinnamon = fur_color_names[1]
black = fur_color_names[2]

#get fur color counts
gray_count = fur_color_data.loc[gray]
cinnamon_count = fur_color_data.loc[cinnamon]
black_count = fur_color_data.loc[black]

#create new data dict
data_output_dict = {
    "Fur Color": [gray, cinnamon, black],
    "Count": [gray_count, cinnamon_count, black_count],
}

#create new data frame
data_output = pandas.DataFrame(data_output_dict)

#output to new csv
data_output.to_csv("squirrel_count.csv")
