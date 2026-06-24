import pandas as pd

df = pd.read_csv("data.csv")

print(df.corr().to_string()) # corr() ignores non-numeric columns e.g., date

# Correlation varies from -1 to 1
# 1 is a perfect correlation, expected for two of the same columns
# -0.9 means that it is very likely that if one value is increased, the other will decrease
# 0.2 mean there is no clear relationship, if one value increases, we can't accurately predicted what the other will do
# -0.6 to 0.6 is a decent correlation


# As Duration and Calories has a correlation of 0.922721, we can conclude that the longer you work out the more calories you burn
# And it also works the other way around, if you burned a lot of calories you probably had a longer workout

# Duration and Maxpulse has a correlation of 0.009403 which suggests that we cannot predict the Maxpulse by looking at the Duration and v.v.





