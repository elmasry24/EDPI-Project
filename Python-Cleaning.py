# modules we will use
import pandas as pd
import numpy as np
import seaborn as sp
import matplotlib.pyplot as plt

# To read data
data_file = pd.read_csv(r"F:\PROJECT\supply_chain_data.csv")   
#Look at the sample of data ex. 5 rows
print(data_file.head())

#Look at the missing of values
missing_data = data_file.isnull().sum()
print(missing_data)                                        #Data does not have nulls

#If data have nulls we will use the code to drop nulls
    ######    drop_null = data_file.dropna(axis=1)   #########

#Another way to fill in missing values
#instead of removing them completely
#is to replace them with other values ​​such as 0.

########    data_file.fillna(0)  ###########


#TO remove duplicates
# data_file.drop_duplicates(inplace=True)



