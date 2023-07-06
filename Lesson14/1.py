import csv

afile = "SampleCSVFile_11kb.csv"

try:
    with open(afile, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"NO! {afile} No file for you!")