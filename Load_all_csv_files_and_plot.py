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

# create a new dataframe from sensordataDF split by commas
sensordataDFclean = sensordataDF[0].str.split(",", expand=True)

# print the dataframe
print(sensordataDFclean)

# delete rows 6,7,8,9,10
#sensordataDFclean = sensordataDFclean.drop([5,6,7,8,9,10], axis=1)

# include rows 0,1,2,3,4,5
sensordataDFclean = sensordataDFclean[[0,1,2,3,4]]

#remove [ from column 1
sensordataDFclean[1] = sensordataDFclean[1].str.replace('[', '')

#remove ] from column 3
sensordataDFclean[3] = sensordataDFclean[3].str.replace(']', '')

#remove \n from column 4
sensordataDFclean[4] = sensordataDFclean[4].str.replace('\n', '')

#remove [ from column 4
sensordataDFclean[4] = sensordataDFclean[4].str.replace('[', '')

# rename the columns
sensordataDFclean.columns = ["sensor", "x", "y", "z", "time"]

# print the dataframe
print(sensordataDFclean)

print(sensordataDFclean.dtypes)

# delete any x,y,z or time rows with device in them
sensordataDFclean = sensordataDFclean[sensordataDFclean["x"] != "device"]
sensordataDFclean = sensordataDFclean[sensordataDFclean["y"] != "device"]
sensordataDFclean = sensordataDFclean[sensordataDFclean["z"] != "device"]
sensordataDFclean = sensordataDFclean[sensordataDFclean["time"] != "device"]

# itterate through the dataframe and convert the x,y,z and time columns to floats appending the rows to a new dataframe called sensordataDFcleanFloats

sensordataDFcleanFloats = pd.DataFrame()

count = 0
for index, row in sensordataDFclean.iterrows():
    try:
        sensordataDFcleanFloats = pd.concat([sensordataDFcleanFloats, pd.DataFrame({"sensor": str(row["sensor"]), "x": float(row["x"]), "y": float(row["y"]), "z": float(row["z"]), "time": float(row["time"])}, index=[0])])
    except:
        print("exception encountered")
        print(row["sensor"], row["x"], row["y"], row["z"], row["time"])
        print(count)
        count = count + 1
        continue

# print the max and min values of each column except for sensor
print(sensordataDFcleanFloats[["x", "y", "z", "time"]].max())
print(sensordataDFcleanFloats[["x", "y", "z", "time"]].min())

print(sensordataDFcleanFloats.shape)

#split the dataframe into 2 dataframes, one for each device
sensordataDFcleanFloatsDevice1 = sensordataDFcleanFloats[sensordataDFcleanFloats["sensor"] == "device_1"]
sensordataDFcleanFloatsDevice2 = sensordataDFcleanFloats[sensordataDFcleanFloats["sensor"] == "device_2"]

#plot sensordataDFcleanFloatsDevice1 as a scatter plot
import matplotlib.pyplot as plt

plt1 = plt
plt2 = plt

#plot sensordataDFcleanFloatsDevice1 and sensordataDFcleanFloatsDevice2 as a line plots on the same graph
plt.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["x"], label="x")
plt.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["y"], label="y")
plt.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["z"], label="z")
plt.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["x"], label="x")
plt.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["y"], label="y")
plt.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["z"], label="z")
plt.legend()
# save the plot as a .png file
plt.savefig("plotcombined.png")
plt.show()

#plot sensordataDFcleanFloatsDevice1 as a line plot
plt1.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["x"], label="x")
plt1.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["y"], label="y")
plt1.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["z"], label="z")
plt1.legend()
plt1.show()
# save the plot as a .png file
plt1.savefig("plotDevice1.png")

#plot sensordataDFcleanFloatsDevice2 as a line plot
plt2.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["x"], label="x")
plt2.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["y"], label="y")
plt2.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["z"], label="z")
plt2.legend()
plt2.show()

# save the plot as a .png file
plt2.savefig("plotDevice2.png")

#plot device 1 x,y,z as three seperate line plots
plt3 = plt
plt3.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["x"], label="x")
plt3.legend()
plt3.show()
plt3.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["y"], label="y")
plt3.legend()
plt3.show()
plt3.plot(sensordataDFcleanFloatsDevice1["time"], sensordataDFcleanFloatsDevice1["z"], label="z")
plt3.legend()
plt3.show()

#plot device 2 x,y,z as three seperate line plots
plt4 = plt
plt4.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["x"], label="x")
plt4.legend()
plt4.show()
plt4.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["y"], label="y")
plt4.legend()
plt4.show()
plt4.plot(sensordataDFcleanFloatsDevice2["time"], sensordataDFcleanFloatsDevice2["z"], label="z")
plt4.legend()
plt4.show()

