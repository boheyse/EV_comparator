import pandas as pd
import numpy as np
import types

#website to find electricity rate data 
# https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a

file_path = "/Users/Heyseb1/Downloads/April_rates.csv"
data = pd.read_csv(file_path)

num_utilities = len(data.index)
print(num_utilities)

# typeService = data.iloc[0:num_utilities, 2]
# startDate = data.iloc[0:num_utilities, 3]
state = data.iloc[0:num_utilities, 0]
rate = data.iloc[0:num_utilities, 1]



Data = {'state':  state,
        'rate': rate,
        'distributedGen': distributedGen,
        'fixedCharge': fixedcharge,
        'energyRate': energyrate
        }

df = pd.DataFrame(Data, columns = ['state', 'rate'])

df = df[df.sector == "Residential"]
df.to_csv("/Users/Heyseb1/Desktop/Coding/EV_App/EV_comparator/data/Feb2019ElectricRates.csv")