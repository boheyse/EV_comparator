import pandas as pd
import numpy as np
import types

#website to find vehicles data 
# https://www.fueleconomy.gov/feg/download.shtml

file_path = "/Users/Heyseb1/Downloads/vehicles.csv"
data = pd.read_csv(file_path)

num_vehicles = len(data.index)
print(num_vehicles)

gallons = data.iloc[0:num_vehicles, 0]
city_mpg = data.iloc[0:num_vehicles, 4]
avg_mpg = data.iloc[0:num_vehicles, 15]
highway_mpg = data.iloc[0:num_vehicles, 34]
make = data.iloc[0:num_vehicles, 46]
model = data.iloc[0:num_vehicles, 47]
year = data.iloc[0:num_vehicles, 63]


Data = {'gallons':  gallons,
        'city_mpg': city_mpg,
        'avg_mpg': avg_mpg,
        'highway_mpg': highway_mpg,
        'make': make,
        'model': model,
        'year': year
        }

df = pd.DataFrame(Data, columns = ['gallons','city_mpg', 'avg_mpg', 'highway_mpg', 'make', 'model', 'year'])
df.to_csv("/Users/Heyseb1/Desktop/Coding/EV_App/EV_comparator/data/June2019Vehicles.csv")