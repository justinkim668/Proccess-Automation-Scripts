import pandas as pd
#we will be using the pandas package for this
dates = pd.read_csv('<INSERT .CSV FILE PATH HERE>', converters = {'Dates': lambda x: str(x)})
#reads .csv file and puts values into pandas dataframe; reads values in 'Dates' column as string instead of int
dates['Dates'] = dates['Dates'].apply(lambda x: x.zfill(8))
#fills in leading zeros into the dates if the number of characters in a value is less than 8
re_dates = []
#initialize empty list re_dates to append reformatted dates to
for i in dates['Dates']:
    day = i[0:2]
    #month/day is the 1st and 2nd characters in i
    month = i[2:4]
    #month/day is the 3rd and 4th characters in i
    year = i[4:8]
    #year is the last 4 characters in i
    reformatted_dates = day+'/'+month+'/'+year
    #reformatted_dates takes the string variables day, month year and combines them to get DD/MM/YYYY date format
    re_dates.append(reformatted_dates)
    #appends valued of reformatted_dates to empty re_dates list
dates['reformatted_dates'] = re_dates
#create new column 'reformatted_dates' in dates dataframe where we add the values of the re_dates list to the column
dates.to_csv('<INSERT .CSV FILE PATH HERE>', index = False, header = True)
#save updated dataframe as .csv file
