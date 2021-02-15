import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

# Read data using Pandas
df = pd.read_csv("Artworks.csv")

df.head()

df.describe()

"""Q1: Load the data and remove all rows that are missing a value for ANY of the following columns: 'Title', 'Artist', or 
'DateAcquired'. Use this cleaned data for the rest of the challenge. After removing these rows, how many rows remain?"""

# Drop rows with any missing value for the columns of Title, Artist, and DateAcquired
df_clean = df.dropna(subset = ["Title", "Artist", "DateAcquired"], how = "any")

# Check the shape of the cleaned dateaframe, the first entry is the number of rows.
df_clean.shape

print("there are {} rows remain".format(df_clean.shape[0]))
      
"""Q2: Of all pieces listed, what proportion belong to the Photography Department? Remember, you should be using the cleaned data you prepared in the last question."""
    
# Check the counts for each value of Department column.
df_clean.Department.value_counts()

# Calculate the percentage of artworks of Photography Department to the all artworks.
percent_photography = len(df_clean[df_clean["Department"] == "Photography"])/len(df_clean)

# what proportion belong to the Photography Department
print("the proportion belong to the Photography Department is {:.10f}".format(percent_photography))

"""Q3: Looking at the Title for each work of art, how many unique titles contain the string 'untitled' (NOT case-sensitive)?"""

# filter the Title columns contains 'untitled' and then list all unique titles
unique_titles = df_clean[df_clean["Title"].str.lower().str.contains("untitled")]["Title"].unique()

# Get the total number of unique titles
print("there are {} unique titles contain the string 'untitled'".format(len(unique_titles)))

"""Q4: MoMA tends more heavily toward printed works, rather than painted works, as evidenced by the value counts for each 
Department in the data set. What about the materials on which these prints and paintings appear? Looking at the Medium for 
each work of art, report the ratio of the number of works that contain the string 'paper' compared to those that contain the 
string 'canvas' (NOT case-sensitive)."""

# Check the values counts for each Department
df_clean.Department.value_counts()

# the ratio of the number of works that contain the string 'paper' compared to those that contain the \nstring 'canvas'
ratio_of_medium = np.sum(df_clean.Medium.str.lower().str.contains("paper"))/np.sum(df_clean.Medium.str.lower().str.contains("canvas"))

print("the ratio of the number of works that contain the string 'paper' compared to those that contain the string 'canvas' is {:.10f}".format(ratio_of_medium))

"""Q5: Of the works with a non-null, positive value for Duration (column 'Duration (sec.)'), what proportion of these durations 
are listed as being longer than 10 hours?"""

df_clean[df_clean["Duration (sec.)"].notnull()]["Duration (sec.)"]

# Calculate the proportion of works of duration longer than 10 hours to that of non-null, positive duration value
duration_ratio = np.sum(df_clean["Duration (sec.)"] > 10* 3600)/ np.sum(df_clean["Duration (sec.)"] > 0)

print("proportion of these durations are listed as being longer than 10 hours is {:.10f}".format(duration_ratio))

"""
Q6: For each year between 1960-1970 (inclusive), compute the number of unique artists whose work MoMA acquired that year. 
Perform a linear regression on these counts, where X is the year and y is the count of unique artists. Report the R^2 value for 
this fitted regression model.

"""

# convert the DateAcquired column to pandas datetime type
df_clean["DateAcquired"] = pd.to_datetime(df_clean["DateAcquired"], format = "%Y-%m-%d")

# filter the data with the acquired date between 1960 an d1970
df_lr = df_clean[df_clean["DateAcquired"].dt.year.between(1960, 1970)]

# Calculate one column for the year that the work is acquired
df_lr["year"] = df_lr["DateAcquired"].dt.year

# create a new dataframe for the unique artist that have been acquired for each year
df_artist = pd.DataFrame(df_lr.groupby("year")["Artist"].nunique())

# Set the column name
df_artist.columns = ["number"]

# reset index 
df_artist.reset_index(inplace = True)

# first fit the linear regression using numpy polyfit
coefficient, intercept = np.polyfit(df_artist["year"], df_artist["number"], deg = 1)

# draw the scatter plot and the fitted line
_ = plt.plot(df_artist["year"], df_artist["number"], marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('Year')
_ = plt.ylabel('Number of artists')

# Make theoretical line to plot
x = np.array([1960, 1970])
y = x * coefficient + intercept

# Add regression line to your plot
_ = plt.plot(x, y)

# calculate the r-squared for the iftted regression model
y_predict = np.empty(11)
for i, a in enumerate(df_artist["year"]):
    y_predict[i] = a * coefficient + intercept
score = r2_score(df_artist["number"], y_predict)

print("he R^2 value for this fitted regression model is {:.10f}".format(score))

# Then use Linear Regression model from sklearn to run the regression again

# Initaite the linear regression model
lr = LinearRegression()

# fit the moel and evaluate the r-squared
lr.fit(df_artist["year"].values.reshape(-1, 1), df_artist["number"].values)
lr.score(df_artist["year"].values.reshape(-1, 1), df_artist["number"].values)

"""Q7: The Golden Ratio (phi ~= 1.618) is popularly regarded for its aesthetic qualities, but how typically is it observed in 
canvas shapes in MoMA's collection? For all works in the department of Drawings & Prints whose Width (column 'Width (cm)') and 
Height (column 'Height (cm)') are greater than zero, compute each piece's aspect ratio as Width / Height. What proportion of 
these aspect ratios are within one percent of the Golden Ratio or the inverse of the Golden Ratio (which would denote a 
vertical Golden Rectangle)?
"""

phi = 1.618

# subset the artwork whoe department is Drawings & Prints
df_gr = df_clean[df_clean["Department"] == "Drawings & Prints"]

# sebset the data whose width and hegith are both above 0
df_gr = df_gr[(df_gr["Width (cm)"] > 0) & (df_gr["Height (cm)"] >0)]

# add one new column as the aspect ratio
df_gr["aspect_ratio"] = df_gr["Width (cm)"]/df_gr["Height (cm)"]

# calculate the proportion of these aspect ratios are within one percent of the Golden Ratio or the inverse of the Golden Ratio
prop_gr = np.sum((df_gr["aspect_ratio"].between(phi*0.99, phi*1.01))|(df_gr["aspect_ratio"].between(1/phi*0.99, 1/phi*1.01)))/len(df_gr)

print("the proportion of these aspect ratios are within one percent of the (inverse) Golden Ratio is {:.10f}".format(prop_gr))

"""
Q8: Does the number of MoMA's yearly acquisitions vary along with changes to the market? Compute the number of pieces acquired 
by MoMA for each year from 2000-2010 (inclusive), then compute the percent difference in yearly acquisitions. Next, using values 
from the link provided, obtain January's average closing price for the S&P 500 across those same years (2000-2010). Compute the 
year-to-year percent difference of those values, as well. Finally, compute and report the Pearson's correlation coefficient 
between the percent differences in yearly acquisitions and in the average January S&P 500 closing prices.

You can find the monthly average closing price for the S&P 500 at the following link: here. Note: Since your starting point is
2000, your percent differences will be defined for 2001-2010.
"""

# subset the data where the artwork is acquired from 2000-2010
df_2000 = df_clean[df_clean["DateAcquired"].dt.year.between(2000, 2010)]

# add one new column for the year of acquisition
df_2000["year"] = df_2000["DateAcquired"].dt.year

# calculate the count of artwork for each year
df_yearly = pd.DataFrame(df_2000.groupby("year")["Title"].count())

# calculate the percentage change. 
df_change = df_yearly.pct_change().dropna().rename(columns={"Title": "Number"})

# get the data from the Januray average of S&P for each year
data = {"year": [2000+i for i in range(11)], "SP": [1425.59, 1335.63, 1140.21, 895.84, 1132.52, 1181.41, 1278.73, 1424.16, 1378.76, 865.58, 1123.58]}
df_sp = pd.DataFrame.from_dict(data).set_index("year")

# calculate the percentage difference of S&P
df_sp = df_sp.pct_change().dropna()

# merge two dataframes of artwork and S&P
df_corr = pd.merge(df_change,df_sp, left_index=True, right_index=True)

# calculate the Person correlation
corr_value = df_corr.corr(method = "pearson").iloc[1,0]

print("Pearson's correlation coefficient between yearly acquisitions and S&P 500 closing prices is {:.10f}".format(corr_value))

