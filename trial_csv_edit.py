# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv("data2.csv")

# updating the column value/data
df.loc[5, 'Name'] = 'SHIV CHANDRA'

# writing into the file
df.to_csv("data2.csv", index=False)

print(df)
