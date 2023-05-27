# import files and append all rows to a pandas dataframe

# list all .csv files in the current directory and write to a list called csv_files
import glob

csv_files = glob.glob("*.csv")
print(csv_files)

# import each line of the file one row at a time, if an exception is encountered, skip the row and continue

import pandas as pd

sensordataDF = pd.DataFrame()

for file in csv_files:
    openfile = open(file, "r")
    for line in openfile:
        try:
            sensordataDF = pd.concat([sensordataDF, pd.DataFrame({line}, index=[0])])
        except:
            print("exception encountered")
            continue

# print the dataframe
print(sensordataDF)

# delete the first 100 rows of the dataframe which are often corrupted
sensordataDF = sensordataDF.iloc[100:]

# remove 0,," from the start of each line
sensordataDF[0] = sensordataDF[0].str.replace('0,,"', '')

# remove " from the end of each line
sensordataDF[0] = sensordataDF[0].str.replace('"', '')

# print the dataframe
print(sensordataDF)

# create a new dataframe from sensordataDF split by commas
sensordataDFclean = sensordataDF[0].str.split(",", expand=True)

# print the dataframe
print(sensordataDFclean)

# delete rows 6,7,8,9,10
sensordataDFclean = sensordataDFclean.drop([5,6,7,8,9,10], axis=1)

#remove [ from column 1
sensordataDFclean[1] = sensordataDFclean[1].str.replace('[', '')

#remove ] from column 3
sensordataDFclean[3] = sensordataDFclean[3].str.replace(']', '')

#remove \n from column 4
sensordataDFclean[4] = sensordataDFclean[4].str.replace('\n', '')

# print the dataframe
print(sensordataDFclean)

# rename the columns
#sensordataDF.columns = ["sensor", "x", "y", "z", "time"]

# plot the data with column 4 as the time axis and columns 1,2,3 as the data
import matplotlib.pyplot as plt

plt.plot(sensordataDFclean[4], sensordataDFclean[1], label="x")
plt.plot(sensordataDFclean[4], sensordataDFclean[2], label="y")
plt.plot(sensordataDFclean[4], sensordataDFclean[3], label="z")
plt.legend()
plt.show()