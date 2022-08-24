import pandas
Data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")



# Gray Squirrels Data
gray_counter = len(Data[Data["Primary Fur Color"]  == "Gray"])
gray_squirrels_data = Data[Data["Primary Fur Color"] == "Gray"].to_dict()
gray_squirrels_data = pandas.DataFrame(gray_squirrels_data)
gray_squirrels_data.to_csv("gray_squirrels.csv")
# Cinnamon Squirrels Data
cinnamon_counter = len(Data[Data["Primary Fur Color"] == "Cinnamon"])
cinnamon_squirrels_data = Data[Data["Primary Fur Color"] == "Cinnamon"].to_dict()
cinnamon_squirrels_data = pandas.DataFrame(cinnamon_squirrels_data)
cinnamon_squirrels_data.to_csv("cinnamon_squirrels.csv")
# Black Squirrels Data
black_counter = len(Data[Data["Primary Fur Color"] == "Black"])
Black_squirrels_data = Data[Data["Primary Fur Color"] == "Black"].to_dict()
Black_squirrels_data = pandas.DataFrame(Black_squirrels_data)
Black_squirrels_data.to_csv("black_squirrels.csv")

# Printing out the data about the squirrels
print(f"{gray_counter} gray squirrels  were founded in NY Central Park")
print(f"{cinnamon_counter} cinnamon squirrels  were founded in NY Central Park")
print(f"{black_counter} black squirrels  were founded in NY Central Park")

# Put all those data in just a file
data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_counter, cinnamon_counter, black_counter]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrels_in_Central_Park.csv")

