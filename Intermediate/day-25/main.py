'''with open("./Intermediate/day-25/weather_data.csv") as f:
    data = f.readlines()
    print(data)'''

'''import csv

with open("./Intermediate/day-25/weather_data.csv") as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        print(row)

        if row[1].isdigit():
            temperatures.append(int(row[1]))
    
    print(temperatures)'''

import pandas as pd

data = pd.read_csv("./Intermediate/day-25/weather_data.csv")
print(data.get("condition"))