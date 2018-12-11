### Date created
2018/12/10

### Project Title
BikeShare Analysis | Udacity Data Science Programming

### Description
This Python script is written for the python portion of the Intro to Data Science on Udacity and is used to explore data related to bike share systems for Chicago, New York City, and Washington. It imports data from a specified csv files of data and computes relevant statistics from said data. This project provides an interactive experience in the terminal to present these statistics.

### How to run the script
You can run the script using a Python integrated development environment (IDE) such as Spyder. To install Spyder, you will need to download the Anaconda installer. This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing Anaconda, you will find the Spyder IDE by opening Anaconda Navigator.

### Questions explored
The script answers the following questions about the bike share data:
•    What is the most popular month for start time?
•    What is the most popular day of week (Monday, Tuesday, etc.) for start time?
•    What is the most popular hour of day for start time?
•    What is the total trip duration and average trip duration?
•    What is the most popular start station and most popular end station?
•    What is the most popular trip?
•    What are the counts of each user type?
•    What are the counts of gender?
•    What are the earliest aka oldest rider, most recent aka youngest rider, and most common birth year?


### Files used
bikeshare.py
washington.csv
chicago.csv
new_york_city.csv

### Credits
Use sort_values to get max values:
•    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
•    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.idxmax.html#pandas.Series.idxmax
•    https://www.reddit.com/r/learnpython/comments/5j8h4x/pandas_groupby_to_get_max_occurrences_of_value/

Working with GroupBy in Pandas:
•    https://stackoverflow.com/questions/29836477/pandas-create-new-column-with-count-from-groupby
•    http://pandas.pydata.org/pandas-docs/stable/groupby.html

Iterating through Pandas Groupby values:
•    https://stackoverflow.com/questions/38387529/how-to-iterate-over-pandas-series-generated-from-groupby-size

Format Float Values:
•    https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

Read day of week, month, hour etc.:
•    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html
•    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.dayofweek.html
•    http://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.DatetimeIndex.weekday_name.html

Extracting data from pandas groupby:
•    https://stackoverflow.com/questions/35523635/extract-values-in-pandas-value-counts/35523820

General Python Pandas Documentation:
•    https://pandas.pydata.org/pandas-docs/stable/basics.html#basics-binop
•    https://pandas.pydata.org/pandas-docs/stable/dsintro.html#indexing-selection


