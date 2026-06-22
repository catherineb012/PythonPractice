#Cleaning data

#Bad data is:
# - empty cells
# - data in wrong format
# - wrong data
# - duplicates

import pandas as pd

#Removing rows with empty cells

df = pd.read_csv('data2.csv')
print(df.to_string())
new_df = df.dropna() #removes all rows with any missing cells, but doesn't change the OG DataFrame, dropna() returns a new df
print(new_df.to_string()) 


#df.dropna(inplace = True) #to change the original df then use 'inplace = True'
#print(df.to_string())



#Replace Empty Values For Specified Columns

new_df = df.fillna({"Calories" : 130})
print(new_df.to_string())



#Replacing cells with Mean, Median, Mode

x = df["Calories"].mean() #selects the 'Calories' column from the table
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

y = df["Calories"].median()
new_df = df.fillna({"Calories" : y})
print(new_df)

#print(df["Calories"].mode()) returns 0 300.0
z = df["Calories"].mode()[0] #need [0] to select the first winner of the mode if there is a tie
new_df = df.fillna({"Calories": z})
print(new_df.to_string())

date = " '2020/12/22' "
new_df = df.fillna({"Date": date})
print(new_df.to_string())


print(df.isnull().sum()) #prints a list of the columns with the counts of blanks


df.fillna({"Date" : date,"Calories" : x}, inplace = True) #one single dictionary and replaces all missing values in the table
print(df.to_string())


